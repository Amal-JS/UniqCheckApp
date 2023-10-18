# Generated by Django 4.2.4 on 2023-10-18 18:53

from django.db import migrations, models
import uniq_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True, validators=[uniq_app.models.CustomUser.username_check])),
                ('email', models.EmailField(max_length=254, unique=True, validators=[uniq_app.models.CustomUser.email_check])),
                ('phone', models.IntegerField(unique=True, validators=[uniq_app.models.CustomUser.phone_number_check])),
            ],
        ),
    ]
