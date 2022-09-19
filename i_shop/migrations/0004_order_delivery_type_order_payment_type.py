# Generated by Django 4.1 on 2022-09-19 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('i_shop', '0003_delivery_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='i_shop.delivery', verbose_name='Тип доставки'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='i_shop.payment', verbose_name='Тип оплаты'),
        ),
    ]
