# Generated by Django 4.1.4 on 2023-01-05 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0003_rename_user_1_privateconversation_user1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='privateconversation',
            name='conversation_flag',
            field=models.BooleanField(default=False),
        ),
    ]
