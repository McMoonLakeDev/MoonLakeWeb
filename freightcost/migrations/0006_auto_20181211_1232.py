# Generated by Django 2.0.4 on 2018-12-11 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freightcost', '0005_auto_20181210_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skin',
            name='skin_img',
        ),
        migrations.AddField(
            model_name='skin',
            name='skin_path',
            field=models.TextField(default='default.png', verbose_name='皮肤路径'),
            preserve_default=False,
        ),
    ]
