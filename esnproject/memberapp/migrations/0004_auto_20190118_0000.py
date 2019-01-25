# Generated by Django 2.1.5 on 2019-01-17 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memberapp', '0003_auto_20190116_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='beispiel',
            field=models.CharField(default='beispieltext', max_length=32),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]