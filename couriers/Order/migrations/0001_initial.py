# Generated by Django 3.1.7 on 2021-04-26 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField(verbose_name='order_number')),
                ('price', models.DecimalField(decimal_places=2, max_digits=300, verbose_name='price')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_category', to='Product.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_product', to='Product.product')),
            ],
            options={
                'verbose_name': 'Orders',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
