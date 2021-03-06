# Generated by Django 3.1.7 on 2021-07-15 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('type', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='companydb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('phno', models.BigIntegerField()),
                ('address', models.CharField(max_length=500)),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.login')),
            ],
        ),
        migrations.CreateModel(
            name='appilcantdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=500)),
                ('phno', models.BigIntegerField()),
                ('gender', models.CharField(max_length=150)),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.login')),
            ],
        ),
    ]
