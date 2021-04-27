from django.db import models

class Order(models.Model):
    order_number = models.IntegerField(verbose_name='order_number')
    price = models.DecimalField(verbose_name='price', max_digits=300, decimal_places=2)
    category = models.ForeignKey('Product.category', models.CASCADE, 'order_category', null=True)
    product = models.ForeignKey('Product.product', models.CASCADE, 'order_product')
    user = models.ForeignKey('Profile.User', models.CASCADE, 'order_user', null=True)

    class Meta:
        verbose_name = 'Orders'
        verbose_name_plural = 'Orders'

