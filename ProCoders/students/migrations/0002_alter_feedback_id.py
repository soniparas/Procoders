# Generated by Django 4.1.3 on 2022-11-14 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
