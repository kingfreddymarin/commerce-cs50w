# Generated by Django 4.1.2 on 2022-11-15 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_bid_listing_alter_listing_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='latestBidder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='latestBidder', to=settings.AUTH_USER_MODEL),
        ),
    ]