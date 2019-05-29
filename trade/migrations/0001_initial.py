# Generated by Django 2.2.1 on 2019-05-29 12:38

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('BUY', 'Buy'), ('SELL', 'Sell')], default='Buy', max_length=5)),
                ('price', models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20)),
                ('number', models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20)),
                ('market', models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20)),
            ],
        ),
    ]
