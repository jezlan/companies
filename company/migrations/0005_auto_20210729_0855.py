# Generated by Django 3.1.7 on 2021-07-29 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_application_vaccancy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='aid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.appilcantdb'),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='aid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.appilcantdb'),
        ),
    ]