import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from reportes.logic.logic_reportes import get_reporte_mensual, get_total_por_proveedor
from django.core import serializers

@csrf_exempt
def reporte_mensual(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        empresa_id = body.get('empresa_id')
        mes = body.get('mes')
        anio = body.get('anio')

        consumos = get_reporte_mensual(empresa_id, mes, anio)
        totales = get_total_por_proveedor(empresa_id, mes, anio)

        consumos_dto = serializers.serialize('json', consumos)

        response = {
            'empresa_id': empresa_id,
            'mes': mes,
            'anio': anio,
            'total_por_proveedor': totales,
            'detalle': json.loads(consumos_dto)
        }
        return HttpResponse(json.dumps(response), content_type='application/json')

    return HttpResponse(
        json.dumps({'error': 'Método no permitido'}),
        content_type='application/json',
        status=405
    )