from reportes.models import ConsumoCloud

def get_reporte_mensual(empresa_id, mes, anio):
    consumos = ConsumoCloud.objects.using('monitoring').filter(
        empresa_id=empresa_id,
        mes=mes,
        anio=anio
    )
    return consumos

def get_total_por_proveedor(empresa_id, mes, anio):
    consumos = get_reporte_mensual(empresa_id, mes, anio)
    totales = {}
    for c in consumos:
        proveedor = c.proveedor
        if proveedor not in totales:
            totales[proveedor] = 0
        totales[proveedor] += float(c.costo)
    return totales