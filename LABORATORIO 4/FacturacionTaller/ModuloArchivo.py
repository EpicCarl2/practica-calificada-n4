import os

RUTA_ARCHIVO = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "atenciones.txt"
)


def GuardarAtencion(linea):
    try:
        archivo = open(
            RUTA_ARCHIVO,
            "a",
            encoding="utf-8"
        )
        archivo.write(linea + "\n")
        archivo.close()

        print("\nAtención registrada correctamente.")

    except Exception as error:
        print("No se pudo guardar la atención:", error)


def BuscarAtencion(placaBuscada):
    if not os.path.exists(RUTA_ARCHIVO):
        print("\nTodavía no existen registros.")
        return

    try:
        archivo = open(
            RUTA_ARCHIVO,
            "r",
            encoding="utf-8"
        )

        placaBuscada = str(placaBuscada).strip().upper()
        coincidencias = 0

        for linea in archivo:
            linea = linea.strip()

            if linea == "":
                continue

            campos = linea.split("|")

            if len(campos) == 5:
                placa = campos[0].strip().upper()

                if placa == placaBuscada:
                    coincidencias += 1

                    print("\nAtención encontrada:")
                    print("Placa:", campos[0])
                    print("Propietario:", campos[1])
                    print("Tipo de servicio:", campos[2])
                    print("Total: S/", campos[3])
                    print("Fecha:", campos[4])

        archivo.close()

        if coincidencias == 0:
            print("\nNo se encontró ninguna atención con esa placa.")

    except Exception as error:
        print("Ocurrió un error al buscar:", error)


def ListarTodasLasAtenciones():
    if not os.path.exists(RUTA_ARCHIVO):
        print("\nTodavía no existen registros.")
        return

    try:
        archivo = open(
            RUTA_ARCHIVO,
            "r",
            encoding="utf-8"
        )

        cantidad = 0
        totalRecaudado = 0.0

        print("\n....REPORTE GENERAL......")

        for linea in archivo:
            linea = linea.strip()

            if linea == "":
                continue

            campos = linea.split("|")

            if len(campos) == 5:
                cantidad += 1
                totalRecaudado += float(campos[3])

                print(
                    "Placa:", campos[0],
                    "| Propietario:", campos[1],
                    "| Servicio:", campos[2],
                    "| Total: S/", campos[3],
                    "| Fecha:", campos[4]
                )

        archivo.close()

        print("\nCantidad de atenciones:", cantidad)
        print(
            "Total recaudado: S/",
            format(totalRecaudado, ".2f")
        )

    except Exception as error:
        print("Ocurrió un error al generar el reporte:", error)