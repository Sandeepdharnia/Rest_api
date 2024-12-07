# Generated by Django 4.0.5 on 2024-12-04 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('added_date', models.DateField(auto_created=True)),
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('IT', 'IT'), ('Non IT', 'Non IT'), ('Mobiles Phone', 'Mobile Phone')], max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
