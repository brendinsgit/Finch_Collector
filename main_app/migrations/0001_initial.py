# Generated by Django 4.2.5 on 2023-09-12 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=50)),
                ('origin', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
    ]
