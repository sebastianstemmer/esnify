# Generated by Django 2.1.5 on 2019-01-16 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email_adr', models.EmailField(default=None, max_length=50)),
                ('since', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='StayAbroad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_amount', models.PositiveIntegerField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='stay_abroad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='memberapp.StayAbroad'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
