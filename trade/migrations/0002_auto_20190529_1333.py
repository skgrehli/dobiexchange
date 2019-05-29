# Generated by Django 2.2.1 on 2019-05-29 13:33

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market', models.CharField(max_length=5)),
                ('price_decimal_limit', models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20)),
                ('number_decimal_limit', models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20)),
                ('min', models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20)),
                ('max', models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20)),
                ('buy_rate', models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20)),
                ('sell_rate', models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='market',
            field=models.CharField(max_length=5),
        ),
        migrations.CreateModel(
            name='MyOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.CharField(choices=[('BUY', 'Buy'), ('SELL', 'Sell')], max_length=5)),
                ('number', models.IntegerField()),
                ('numberdeal', models.IntegerField()),
                ('numberover', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[(0, 'uncompleted transactions'), (1, 'Partial transaction'), (2, 'Completed Transactions'), (3, 'Revoked')], default='Buy', max_length=5)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.Order')),
            ],
        ),
    ]