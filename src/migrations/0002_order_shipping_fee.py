# Generated by Django 2.2.4 on 2019-11-16 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_fee',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
