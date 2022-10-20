import random
clientes = ["Alex","Bob","Carol","Dave","Flow","Katie","Nate"]
diccionario_descuentos = {cliente:random.randint(1,100) for cliente in clientes}
print(diccionario_descuentos)
#Resultado

{'Alex': 16, 'Bob': 26, 'Carol': 83, 'Dave': 21, 'Flow': 38, 'Katie': 47, 'Nate': 89}

