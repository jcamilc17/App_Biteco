import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from reportes.logic.logic_reportes import get_reporte_mensual, get_total_por_proveedor

@csrf_exempt
def reporte_mensual(request):
    if request.method == 'GET':
        empresa_id = request.GET.get('empresa_id', 1)
        mes = request.GET.get('mes', 3)
        anio = request.GET.get('anio', 2026)

        totales = get_total_por_proveedor(empresa_id, mes, anio)

        response = {
            'empresa_id': empresa_id,
            'mes': mes,
            'anio': anio,
            'total_por_proveedor': totales
        }
        return HttpResponse(json.dumps(response), content_type='application/json')

    return HttpResponse(
        json.dumps({'error': 'Método no permitido'}),
        content_type='application/json',
        status=405
    )