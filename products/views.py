from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        brand = self.request.query_params.get("brand")
        search = self.request.query_params.get("search")

        if brand:
            queryset = queryset.filter(brand__name__icontains=brand)
        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset
