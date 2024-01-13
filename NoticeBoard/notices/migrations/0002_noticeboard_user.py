# Generated by Django 5.0.1 on 2024-01-13 06:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('notices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticeboard',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='notices_uploaded', to='accounts.user'),
        ),
    ]
