# Generated by Django 2.0.5 on 2018-05-15 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freightcost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='img',
            field=models.ImageField(upload_to='freightcost/static/media/img', verbose_name='发票图片'),
        ),
    ]
