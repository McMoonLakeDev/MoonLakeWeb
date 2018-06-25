# Generated by Django 2.0 on 2018-04-20 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnlogs', '0011_auto_20180418_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='i18n',
            name='language',
            field=models.CharField(choices=[('en-US', 'English'), ('zh-Hans', '简体中文'), ('zh-Hant', '繁體中文')], default='zh-Hant', max_length=8),
        ),
    ]