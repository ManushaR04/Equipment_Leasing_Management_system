# Generated by Django 4.0.7 on 2023-06-03 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=20)),
                ('Username', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
    ]
