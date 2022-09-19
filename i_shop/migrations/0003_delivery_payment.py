# Generated by Django 4.1 on 2022-09-19 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('i_shop', '0002_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=250)),
                ('cost', models.FloatField()),
            ],
            options={
                'verbose_name': 'Тип доставки',
                'verbose_name_plural': 'Типы доставки',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Тип оплаты',
                'verbose_name_plural': 'Типы оплаты',
            },
        ),
    ]
