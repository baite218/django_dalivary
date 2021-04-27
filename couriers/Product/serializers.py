from rest_framework import serializers

from Product.models import product, category


class ProductSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = self.context.get('request').user

        product = Product.objects.create(user=user, **validated_data)
        return product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = category
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user

        category = category.objects.create(user=user, **validated_data)
        return category
