# Generated by Django 2.2.4 on 2020-06-26 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyFinData',
            fields=[
                ('companyName', models.CharField(max_length=200)),
                ('companyStockCode', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('companyTotalAssets', models.CharField(max_length=200)),
                ('companyTotalDebt', models.CharField(max_length=200)),
                ('comapnyTotalCapital', models.CharField(max_length=200)),
                ('companyTotalSales', models.CharField(max_length=200)),
                ('companyTotalBuzProfits', models.CharField(max_length=200)),
                ('companyTotalIncomeBeforeTax', models.CharField(max_length=200)),
                ('companyTotalNetIncome', models.CharField(max_length=200)),
            ],
        ),
    ]