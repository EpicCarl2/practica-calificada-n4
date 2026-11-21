import os
import sys
from datetime import datetime

RUTA_PROYECTO = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
sys.path.append(RUTA_PROYECTO)

from FacturacionTaller.ModuloTaller import (
    ObtenerTarifaBase,
    CalcularDescuentoCliente,
    CalcularImpuestoIGV,
    CalcularTotalPagar,
    ConstruirRegistroPipe
)

from FacturacionTaller.ModuloArchivo import (
    GuardarAtencion,
    BuscarAtencion,
    ListarTodasLasAtenciones
)


def registrarAtencion():
    try:
        placa = input(
            "Ingrese la placa del vehículo: "
        ).strip()

        propietario = input(
            "Ingrese el nombre del propietario: "
        ).strip()

        print("\nTipos de servicio:")
        print("1. PREVENTIVO")
        print("2. CORRECTIVO")
        print("Cualquier otro texto se considera OTRO")

        tipoServicio = input(
            "Ingrese el tipo de servicio: "
        ).strip().upper()

        if tipoServicio == "1":
            tipoServicio = "PREVENTIVO"
        elif tipoServicio == "2":
            tipoServicio = "CORRECTIVO"

        esFrecuente = input(
            "¿El cliente es frecuente? (SI/NO): "
        ).strip().upper()

        if placa == "" or propietario == "":
            print("\nLa placa y el propietario son obligatorios.")
            return

        tarifaBase = ObtenerTarifaBase(tipoServicio)

        descuento = CalcularDescuentoCliente(
            tarifaBase,
            esFrecuente
        )

        tarifaConDescuento = tarifaBase - descuento
        igv = CalcularImpuestoIGV(tarifaConDescuento)

        totalPagar = CalcularTotalPagar(
            tarifaBase,
            descuento,
            igv
        )

        fecha = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        linea = ConstruirRegistroPipe(
            placa,
            propietario,
            tipoServicio,
            totalPagar,
            fecha
        )

        print("\n....FACTURACIÓN.........")
        print("Tarifa base: S/", format(tarifaBase, ".2f"))
        print("Descuento: S/", format(descuento, ".2f"))
        print("IGV: S/", format(igv, ".2f"))
        print("Total a pagar: S/", format(totalPagar, ".2f"))
        print("Fecha:", fecha)

        GuardarAtencion(linea)

    except Exception as error:
        print("Ocurrió un error al registrar:", error)


def mostrarMenu():
    print("\n.......TALLER MECÁNICO......")
    print("1. Registrar atención")
    print("2. Buscar atención por Placa")
    print("3. Reporte general de atenciones")
    print("4. Salir")


def main():
    while True:
        try:
            mostrarMenu()

            opcion = input(
                "\nSeleccione una opción: "
            ).strip()

            if opcion == "1":
                registrarAtencion()

            elif opcion == "2":
                placa = input(
                    "Ingrese la placa que desea buscar: "
                ).strip()

                BuscarAtencion(placa)

            elif opcion == "3":
                ListarTodasLasAtenciones()

            elif opcion == "4":
                print("\nPrograma finalizado.")
                break

            else:
                print("\nSeleccione una opción del 1 al 4.")

        except KeyboardInterrupt:
            print("\nOperación cancelada.")

        except Exception as error:
            print("\nOcurrió un error inesperado:", error)


if __name__ == "__main__":
    main()