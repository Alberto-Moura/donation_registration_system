from django.http import JsonResponse
from .models import Product


def product_data(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        return JsonResponse({
            'acronym': product.acronym.acronym if product.acronym else None,
            'category': product.category.name if product.category else None,
        })
    except product.DoesNotExist:
        return JsonResponse({'error': 'product not found'}, status=404)
