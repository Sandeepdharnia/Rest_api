# Generated by Django 4.0.5 on 2024-12-06 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]