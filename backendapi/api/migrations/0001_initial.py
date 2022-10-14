# Generated by Django 4.1.2 on 2022-10-11 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('sportId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('birthDate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('locationId', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=150)),
                ('tgChannel', models.CharField(max_length=50)),
                ('sportId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sport')),
            ],
        ),
    ]
