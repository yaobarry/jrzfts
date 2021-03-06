# Generated by Django 2.0.6 on 2018-06-19 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardBin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardbin', models.CharField(max_length=10)),
                ('cardnolen', models.IntegerField()),
                ('cardtype', models.BooleanField()),
                ('status', models.BooleanField()),
                ('bankname', models.CharField(max_length=100)),
                ('bankabbname', models.CharField(max_length=10)),
                ('associations', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['cardbin'],
            },
        ),
        migrations.CreateModel(
            name='PayList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.BigIntegerField()),
                ('payname', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
            ],
            options={
                'ordering': ['pid'],
            },
        ),
        migrations.CreateModel(
            name='SubPayList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.BigIntegerField()),
                ('subpayname', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
            ],
            options={
                'ordering': ['sid'],
            },
        ),
    ]
