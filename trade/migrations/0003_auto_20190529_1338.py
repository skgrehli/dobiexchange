# Generated by Django 2.2.1 on 2019-05-29 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_auto_20190529_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myorder',
            name='status',
            field=models.IntegerField(choices=[(0, 'uncompleted transactions'), (1, 'Partial transaction'), (2, 'Completed Transactions'), (3, 'Revoked')], default='Buy'),
        ),
    ]
