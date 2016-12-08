from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from mumsapi.models import Product
from mumsapi.serializers import ProductSerializer
from mumsapi.services import CartSvc


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CalculateCartPrice(APIView):
    def post(self, request):
        return Response({'price': CartSvc.calculcate_cart_price(request.data['cart'])})
