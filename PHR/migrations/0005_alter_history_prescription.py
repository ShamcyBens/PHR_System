# Generated by Django 4.1.3 on 2023-06-29 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PHR', '0004_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='prescription',
            field=models.ImageField(blank=True, upload_to='prescrip/'),
        ),
    ]
