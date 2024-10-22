# Generated by Django 5.1.1 on 2024-09-29 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='message',
        ),
        migrations.RemoveField(
            model_name='user',
            name='subject',
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='default_password', max_length=500),
        ),
    ]