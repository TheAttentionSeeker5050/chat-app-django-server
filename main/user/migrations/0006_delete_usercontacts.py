# Generated by Django 4.1.4 on 2023-01-04 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_contactsblacklist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserContacts',
        ),
    ]
