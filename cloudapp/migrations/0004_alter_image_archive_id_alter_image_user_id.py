# Generated by Django 5.0.3 on 2024-05-03 12:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloudapp', '0003_alter_customuser_design_id_alter_customuser_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='archive_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cloudapp.archive', verbose_name='Архив'),
        ),
        migrations.AlterField(
            model_name='image',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
