# Generated by Django 4.2.7 on 2023-11-16 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pod_name', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('item', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('uuid', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'testmenu',
            },
        ),
    ]