# Generated by Django 4.1 on 2022-08-15 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0009_alter_category_name_alter_expense_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='expense',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]