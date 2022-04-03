# Generated by Django 4.0.3 on 2022-03-31 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название продукта')),
                ('cost', models.FloatField(verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]