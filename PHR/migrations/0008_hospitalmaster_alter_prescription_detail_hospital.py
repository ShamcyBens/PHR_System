# Generated by Django 4.1.3 on 2023-06-29 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PHR', '0007_prescription_detail_delete_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=50)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='prescription_detail',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PHR.hospitalmaster'),
        ),
    ]
