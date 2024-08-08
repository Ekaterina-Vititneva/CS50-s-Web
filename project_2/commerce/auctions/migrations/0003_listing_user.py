# Generated by Django 5.0.7 on 2024-08-08 12:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listing_alter_user_id_comment_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
