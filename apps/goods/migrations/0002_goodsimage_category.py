# Generated by Django 2.1 on 2018-08-22 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsimage',
            name='category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsCategory', verbose_name='类别'),
            preserve_default=False,
        ),
    ]
