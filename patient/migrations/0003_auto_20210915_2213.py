# Generated by Django 3.2.6 on 2021-09-15 16:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_rename_amount_add_detail_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_detail',
            name='disease',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='add_detail',
            name='got_discharge',
            field=models.BooleanField(default=False),
        ),
    ]
