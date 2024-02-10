# Descripcion del programa
print('Programa que calcula pago neto de un trabajador')

# Pedir usuario que ingrese los parametros
print('Porfavor ingrese los siguentes datos:')

nHorasTrabajadas = 0
while nHorasTrabajadas <= 0:
    nHorasTrabajadas = float(input('Cuantas horas trabajó: '))
    if nHorasTrabajadas <= 0:
        print('La cantidad de horas ingresadas no son validas')


tarifaHoraria = 0
while tarifaHoraria <= 0:
    tarifaHoraria = float(input('Cuanto le pagan por hora: '))
    if tarifaHoraria <= 0:
        print('La tarifa ingresada no es validas')


tasaImpuestos = -1
while tasaImpuestos < 0 or tasaImpuestos >= 50:
    tasaImpuestos = float(input('Cuanto paga de impuestos(porcentaje): '))
    if tasaImpuestos < 0 or tasaImpuestos >= 50:
        print('La tasa ingresada no es valida')

# Ejecutar calculo
def calcularPagoNeto(nHoras, tarifaHora, tasaImpuesto):
    pagoBruto = nHoras * tarifaHora
    cantImpuesto = pagoBruto * (tasaImpuesto/100)
    resultado = pagoBruto - cantImpuesto
    return resultado

pagoNeto = calcularPagoNeto(nHorasTrabajadas, tarifaHoraria, tasaImpuestos)
# Muestra el resultado
print('El pago neto es: ')
print(pagoNeto)