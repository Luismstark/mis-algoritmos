

"""
CREARE UN PROGRMA QUE GESTIONE MI DINERO
lo llamare billetera
tendre las opciones de agregar saldo, pagar, y retirar.
y tambien me notificara cuanto de saldo tengo
"""

# variables globales definidos
global saldo
global historial
saldo = 0
historial = []



#funcion para pregunta el saldo total
def saldototal():
    if saldo <= 0: #si el saldo es 0 te preguntara si quieres recargar
       print(f"TU SALDO ES: {saldo} SI DESEA RECARGAR\n 1: agregarsaldo()\n 2: No")
       res = int(input())
       if res == 1:# respuesta 1 para  agregar saldo
            agregarsaldo()
       else:
           inicio()
    else:# si hay saldo  te mostrara cuanto hay
        print(f"TU SALDO Es: {saldo}")
        inicio()

# funcion para retirar saldo
def retirar():
    global saldo
    if saldo <= 0:# sil esl saldo esta 0 no podras retirar
        print("----------\nSALDO INSUFICIENTE PARA RETIRAR----------")
        inicio()
    else:  # sil hay saldo podras retirar pero...
        monto = int(input("MONTO A RETIRAR:"))
        if saldo >= monto: #si el monto que deseas retirar es mayos al saldo no podras
           saldo -= monto
           historial.append(monto)
           mensaje("retiro",monto)
           saldototal()
        else: # si es menor o igual al saldo actual podras retirar
            print(f"tu saldo solo es de:  {saldo}")
            inicio()


#funcion para agregar saldo

def agregarsaldo():
    global saldo
    monto = int(input("Monto a recargar: "))
    saldo += monto # el monto es la cantidad que se agrego y se suma al saldo total
    historial.append(monto)
    mensaje("recarga",monto)
    inicio()


# funcion que permite pagos
def pagar():
    global saldo
    monto = (int(input("-------MONTO A PAGAR-------")))
    saldo -= monto # se resta al saldo total el monto que pagaste
    historial.append(monto)
    mensaje("pago",monto)
    inicio()

# funcion para ver tu istorial de movimientos
def histoiales():
    resultado = historial
    print(f"-------------------------------------------------------\n HISTORIAL DE CUENTA\n {resultado}")
    inicio()

# funcion de mensajes que te inica si agreagste, retiraste o pagaste
def mensaje(sms,monto):
    if sms == "recarga":
        print(f"____RECARGASTE ${monto}______")
    elif sms == "pago":
         print(f"____pagaste ${monto}______")
    elif sms == "retiro":
        print(f"____RETIRASTE ${monto}______")


# esta funcion inicializa todo el programa
def inicio():
     print("--------MY BILLETERA----------\n1: saldo()\n2:retirar()\n3:pagar()\n4:agregarsaldo()\n5:historial()\n")
     opcion = int(input())#ingresa el numero de opcion de la ue quieres realizar
     if opcion == 1:
        saldototal()
     elif opcion ==2:
         retirar()
     elif opcion ==3:
         pagar()
     elif opcion == 5:
         histoiales()
     else:
        agregarsaldo()

inicio()



