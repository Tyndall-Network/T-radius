# Generated by Django 5.0 on 2023-12-20 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nas',
            name='manufacturer',
            field=models.CharField(default='MikroTik', max_length=16),
        ),
        migrations.AlterField(
            model_name='nas',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
