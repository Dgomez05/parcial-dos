


def calcular_bono(salariobase, cargo, nivel_desempeño):
    bono: int = 0

    if cargo.lower() == "directivo":
        if nivel_desempeño.lower() == "alto":
            bono = (salariobase * 0.20)
        elif nivel_desempeño.lower() == "medio":
            bonificacion = (salariobase * 0.10)
        elif nivel_desempeño.lower() == "bajo":
            bono = 0
    elif cargo.lower() == "operativo":
        if nivel_desempeño.lower() == "alto":
            bono = (salariobase * 0.15)
        elif nivel_desempeño.lower() == "medio":
            bono = (salariobase * 0.10)
        elif nivel_desempeño.lower() == "bajo":
            bono = 0
    return bono


def mostrar_resumen(salrariobase, cargo, nivel_desempeño):
    bono = calcular_bono(salrariobase, cargo, nivel_desempeño)
    total = (salrariobase + bono)
    print("----Resumen del pago----")
    print("Cargo: ", cargo)
    print("Nivel de desempeño: ", nivel_desempeño)
    print("Salario base: ", salrariobase)
    print("Bonificacion: ", bono)
    print("Total a recibir: ", total)
    print("-------------------------")


def main():
    try:
        salariobase = int(input("Salario base mensual: "))
        cargo = input("Cargo empleado: ")
        nivel_desempeño = input("Nivel de desempeño: ")
        mostrar_resumen(salariobase, cargo, nivel_desempeño)
    except ValueError:
        print("El valor introducido no es valido")

if __name__ == "__main__":
    main()





