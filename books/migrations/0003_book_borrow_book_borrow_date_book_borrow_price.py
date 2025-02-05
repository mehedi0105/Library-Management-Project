# Generated by Django 5.0.6 on 2024-07-02 16:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='borrow',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='borrow_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='book',
            name='borrow_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
