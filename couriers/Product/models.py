from django.db import models

class product(models.Model):
    name = models.CharField('name', max_length=255)
    price = models.PositiveIntegerField('price')
    description = models.TextField('description')
    image = models.FileField('image', upload_to='product_images/')
    category = models.ForeignKey('Product.category', models.CASCADE, 'product_category', null=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'product'

    def __str__(self):
        return f'{self.name}'



class category (models.Model):
	name_category = models.CharField('name_category', max_length = 255)
	description = models.CharField('description', max_length = 300)

	def __str__(self):
		return self.name_category


