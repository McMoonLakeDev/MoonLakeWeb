# Generated by Django 2.0 on 2018-04-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnlogs', '0009_auto_20180418_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='i18n',
            name='language',
            field=models.CharField(choices=[('zh-Hans', 'zh-Hans'), ('zh-Hant', 'zh-Hant'), ('en-US', 'en-US')], max_length=8),
        ),
    ]