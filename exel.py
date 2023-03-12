"""CALCULADORA DE SALDO  """
# Datos de entrada
acciones = ["Vender", "Vender", "Vender", "Vender", "Comprar", "Vender", "Vender", "Vender",
            "Comprar", "Vender", "Vender", "Vender", "Comprar ", "Vender", "Vender", "Comprar",]
importes = [
    102.41,
    4835.1,
    2700,
    2720,
    1500,
    1000,
    1110,
    3600,
    1658.08,
    150,
    150,
    1002.67,
    1000,
    856,
    3370.75,
    1489.75,
    1979.56,
    2786.4,
    390,
    620]

saldo = 0
saldos = []
for i in range(len(acciones)):
    if acciones[i] == "Sell":
        saldo += importes[i]
        saldos.append(saldo)
    elif acciones[i] == "Buy":
        saldo -= importes[i]
        saldos.append(saldo)

# Impresión de resultados
for i in range(len(acciones)):
    print(f"{acciones[i]}: {importes[i]}")
    print(f"Saldo: {saldos[i]}")
    print("--------------")
