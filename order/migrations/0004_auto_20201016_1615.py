# Generated by Django 3.0.7 on 2020-10-16 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20201015_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketlist',
            name='deliveryType',
            field=models.IntegerField(choices=[(1, 'Delivery'), (2, 'Pick up')], default=1, verbose_name='DeliveryType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basketlist',
            name='paymentType',
            field=models.IntegerField(choices=[(1, 'Card'), (2, 'Cash')], default=1, verbose_name='PaymnetType'),
        ),
    ]