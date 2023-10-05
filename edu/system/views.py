from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView


class UserLessonsView(APIView):
    def get(self, request, user_id):
        products = Product.objects.filter(productaccess__user_id=user_id)
        serialized_products = ProductSerializer(products, many=True)
        return Response({'Список уроков по продуктам, к которым у указанного пользователя есть доступ': serialized_products.data})

class UserProductLessonsView(APIView):
    def get(self, request, user_id, product_id):
        user = get_object_or_404(User, id=user_id)
        product = get_object_or_404(Product, id=product_id)

        if not ProductAccess.objects.filter(product=product, user=user).exists():
            return Response({'error': 'User does not have access to this product'})

        serialized_product = ProductSerializer(product)

        return Response({'Список уроков, доступных указанному пользователю в указанном продукте': serialized_product.data})

class ProductsWithAccessCountView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductWithAccessCountSerializer(products, many=True)
        return Response({'Список продуктов с количеством пользователей, занимающихся на продукте и процент '
                         'приобретения продукта': serializer.data})
