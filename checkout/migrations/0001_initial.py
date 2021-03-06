# Generated by Django 3.2.9 on 2021-12-23 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=256)),
                ('phone_number', models.CharField(max_length=20)),
                ('street_address1', models.CharField(max_length=128)),
                ('street_address2', models.CharField(blank=True, max_length=128, null=True)),
                ('city_town', models.CharField(max_length=128)),
                ('county_state', models.CharField(blank=True, max_length=64, null=True)),
                ('postcode_zip', models.CharField(max_length=12)),
                ('country', models.CharField(max_length=40)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('total_order', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('delivery_charge', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('line_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.order')),
            ],
        ),
    ]
