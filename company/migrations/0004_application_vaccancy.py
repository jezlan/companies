# Generated by Django 3.1.7 on 2021-07-28 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20210724_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='vaccancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noofvaccany', models.IntegerField()),
                ('jobdetail', models.CharField(max_length=450)),
                ('date', models.DateField(default='2020-01-01')),
                ('qualification', models.CharField(max_length=250)),
                ('salary', models.BigIntegerField()),
                ('Experiance', models.IntegerField()),
                ('status', models.CharField(max_length=250)),
                ('cmp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.companydb')),
            ],
        ),
        migrations.CreateModel(
            name='application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=250)),
                ('aid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.appilcantdb')),
                ('vid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.vaccancy')),
            ],
        ),
    ]
