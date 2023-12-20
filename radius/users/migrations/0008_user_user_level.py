# Generated by Django 5.0 on 2023-12-20 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_created_at_alter_user_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_level',
            field=models.IntegerField(choices=[(1, 'Admin'), (2, 'Reseller'), (3, 'Isp'), (4, 'User')], default=4),
        ),
    ]
