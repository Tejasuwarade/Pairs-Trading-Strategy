# Generated by Django 3.1.3 on 2020-11-17 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorname', models.CharField(max_length=50)),
                ('patientname', models.CharField(max_length=50)),
                ('doctoremail', models.EmailField(max_length=254)),
                ('patientemail', models.EmailField(max_length=254)),
                ('appointmentdate', models.DateField()),
                ('appointmenttime', models.TextField()),
                ('symptoms', models.CharField(max_length=150)),
                ('prescription', models.CharField(max_length=200)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=150)),
                ('phonenumber', models.CharField(max_length=10)),
                ('birthdate', models.DateField()),
                ('bloodgroup', models.CharField(max_length=5)),
                ('specialization', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('gender', models.CharField(max_length=10)),
                ('phonenumber', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('bloodgroup', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=150)),
                ('phonenumber', models.CharField(max_length=10)),
                ('birthdate', models.DateField()),
                ('bloodgroup', models.CharField(max_length=5)),
            ],
        ),
    ]
