# Generated by Django 3.0.5 on 2022-02-01 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
