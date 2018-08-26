from random import choice

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status, mixins
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from user.models import UserProfile, VerifyCode
from user.serializers import SmsSerializer, UserRegSerializer
from utils.yunpian_sms import YunPian

User = get_user_model()


class CustomBackend(ModelBackend):
    '''
    自定义用户验证
    '''

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            print('===登陆信息====', username, password)
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            print('====user====', user)
            if user.check_password(password):
                print('=====password=====pass')
                return user
        except Exception as e:
            print(e)
            return None


class SmsCodeViewset(CreateModelMixin, viewsets.GenericViewSet):
    '''发送短信验证码视图'''

    serializer_class = SmsSerializer

    def generate_code(self):
        """
        生成四位数字的验证码
        :return:
        """
        nums = "1234567890"
        random_str = ''
        for i in range(4):
            random_str += choice(nums)

        return random_str

    def create(self, request, *args, **kwargs):
        print('======注册请求=======', request.data)
        ser = self.get_serializer(data=request.data)
        # 验证不通过抛异常
        ser.is_valid(raise_exception=True)
        print('=====验证通过手机号码=======', ser)
        # 验证通过获取手机号码
        mobile = ser.validated_data['mobile']

        # ============发送短信验证码 start=================
        code = self.generate_code()
        result = YunPian.send_sms(code, mobile)
        print('=======验证码发送=======', result)
        if result["code"] != 0:
            return Response({
                "mobile": result["msg"]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({
                "mobile": mobile
            }, status=status.HTTP_201_CREATED)

        # ============发送短信验证码 end=================


class UserViewset(CreateModelMixin, viewsets.GenericViewSet):
    '''
    用户注册登录
    '''
    serializer_class = UserRegSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        print('=====创建用户======', user)
        payload = jwt_payload_handler(user)
        # 添加token 和name 让用户注册完毕后就登陆
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()
