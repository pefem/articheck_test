# Generated by Django 4.0.6 on 2022-08-01 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Content', models.CharField(max_length=500)),
            ],
        ),
    ]