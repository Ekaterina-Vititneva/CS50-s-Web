# Generated by Django 5.1 on 2024-09-15 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_rename_last_modifed_by_listing_last_modified_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, choices=[('Electronics', 'Electronics'), ('Fashion', 'Fashion'), ('Home', 'Home'), ('Toys', 'Toys'), ('Books', 'Books'), ('Sports', 'Sports'), ('Health', 'Health'), ('Beauty', 'Beauty'), ('Jewelry', 'Jewelry'), ('Garden', 'Garden'), ('Music', 'Music')], max_length=64),
        ),
    ]