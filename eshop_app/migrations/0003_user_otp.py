# Generated by Django 5.1.1 on 2024-10-01 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_app', '0002_contact_remove_user_message_remove_user_subject_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
