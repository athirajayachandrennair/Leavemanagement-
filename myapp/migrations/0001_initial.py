# Generated by Django 3.1.12 on 2021-12-26 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
