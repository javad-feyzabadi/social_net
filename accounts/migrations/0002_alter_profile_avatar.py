# Generated by Django 3.2 on 2023-01-11 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='profile_avatars/'),
        ),
    ]
