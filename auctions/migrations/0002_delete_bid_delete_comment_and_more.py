# Generated by Django 4.1.2 on 2022-11-10 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bid',
        ),
        migrations.DeleteModel(
            name='comment',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='activeListing',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='description',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='image',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='price',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='title',
        ),
    ]
