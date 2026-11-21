def ObtenerTarifaBase(tipoServicio):
    tipo = str(tipoServicio).strip().upper()

    if tipo == "PREVENTIVO":
        return 180.00
    elif tipo == "CORRECTIVO":
        return 320.00
    else:
        return 120.00


def CalcularDescuentoCliente(tarifaBase, esFrecuente):
    frecuencia = str(esFrecuente).strip().upper()

    if frecuencia == "SI":
        return tarifaBase * 0.15
    else:
        return 0.00


def CalcularImpuestoIGV(tarifaBaseConDescuento):
    return tarifaBaseConDescuento * 0.18


def CalcularTotalPagar(tarifaBase, descuento, igv):
    return tarifaBase - descuento + igv


def ConstruirRegistroPipe(
    placa,
    propietario,
    tipoServicio,
    totalAPagar,
    fecha
):
    registro = (
        str(placa).strip() + "|" +
        str(propietario).strip() + "|" +
        str(tipoServicio).strip().upper() + "|" +
        format(totalAPagar, ".2f") + "|" +
        str(fecha)
    )

    return registro