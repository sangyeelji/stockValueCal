# Generated by Django 2.2.4 on 2020-06-20 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=200)),
                ('stockCode', models.CharField(max_length=200)),
                ('companyBuz', models.TextField()),
                ('companyCEO', models.CharField(max_length=200)),
            ],
        ),
    ]