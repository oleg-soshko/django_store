# Generated by Django 4.1 on 2022-08-20 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('i_shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='image', upload_to='category/'),
            preserve_default=False,
        ),
    ]