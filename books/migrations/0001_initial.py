# Generated by Django 5.0.6 on 2024-07-02 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0002_alter_customeraccount_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('after_balance', models.DecimalField(decimal_places=2, max_digits=12)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AddBalance', to='User.customeraccount')),
            ],
        ),
    ]
