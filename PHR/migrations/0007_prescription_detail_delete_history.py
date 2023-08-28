# Generated by Django 4.1.3 on 2023-06-29 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PHR', '0006_alter_history_prescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescrip_no', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('document', models.FileField(blank=True, upload_to='prescrip/')),
                ('hospital', models.CharField(max_length=50)),
                ('doctor', models.CharField(max_length=50)),
                ('doc_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PHR.documentcategorymaster')),
                ('purpose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PHR.purposemaster')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='History',
        ),
    ]
