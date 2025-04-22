from django.http import JsonResponse
from .models import Institution


def institution_data(request, pk):
    try:
        instituition = Institution.objects.get(pk=pk)
        return JsonResponse({
            'address': instituition.address or '',
            'number': instituition.number or '',
            'phone': instituition.phone or '',
            'contact': instituition.contact or '',
            'neighborhood': instituition.neighborhood.id if instituition.neighborhood else None,
        })
    except Institution.DoesNotExist:
        return JsonResponse({'error': 'Institution not found'}, status=404)


def institution_by_type(request, type_id):
    try:
        institutions = Institution.objects.filter(typesInstitution_id=type_id)
        data = [
            {'id': inst.id, 'name': inst.name}
            for inst in institutions
        ]
        return JsonResponse({'result': data})

    except Institution.DoesNotExist:
        return JsonResponse({'error': 'Institutions not found'}, status=404)
