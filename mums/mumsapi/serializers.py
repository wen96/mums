from rest_framework import serializers

from mumsapi.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Product


class CartSerializer(serializers.Serializer):
    cart = serializers.JSONField(required=True)
