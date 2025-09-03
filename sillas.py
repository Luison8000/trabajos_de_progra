
def calcular_monto(tipo_silla, cantidad):
    precios = {
        "basica": 700,
        "elegante": 900,
        "lujo": 1500
    }
    if tipo_silla in precios:
        return precios[tipo_silla] * cantidad
    else:
        return -1 

def determinar_descuento(monto, tipo_cliente):
    if tipo_cliente == "si":
        return monto * 0.20
    elif tipo_cliente == "no":
        if monto >= 20000:
            return monto * 0.15
        elif 10000 <= monto < 20000:
            return monto * 0.10
    return 0

def main():
    print("Bienvenido a la tienda de sillas")
    tipo_silla = input("ingrese el tipo de silla: ").lower()
    cantidad = int(input("ingrese la cantidad de sillas: "))
    tipo_cliente = input("es cliente frecuente? ").lower()

    monto = calcular_monto(tipo_silla, cantidad)

    if monto == -1:
        print("es silla no existe 😖")
        return

    descuento = determinar_descuento(monto, tipo_cliente)
    monto_final = monto - descuento

    print(f"monto sin descuento: ${monto:.2f}")
    print(f"descuento aplicado: ${descuento:.2f}")
    print(f"monto final a pagar: ${monto_final:.2f}")

main()

