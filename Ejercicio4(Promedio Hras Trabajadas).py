print('Promedio de horas trabajadas en la semana')
horasTrabajadasPorDia=[]
horasTrabajadasPorDia.append(input('Horas trabajadas el Lunes: '))
horasTrabajadasPorDia.append(input('Horas trabajadas el Martes: '))
horasTrabajadasPorDia.append(input('Horas trabajadas el Miercoles: '))
horasTrabajadasPorDia.append(input('Horas trabajadas el Jueves: '))
horasTrabajadasPorDia.append(input('Horas trabajadas el Viernes: '))
horasTrabajadasPorDia.append(input('Horas trabajadas el Sabado: '))
horasTrabajadasPorDia.append(input('Horas trabajadas el Domingo: '))
#horasTrabajadasPorDia=[12,12,12,12,12,0,0]

print(horasTrabajadasPorDia)

sumaDeHoras = 0
for i in horasTrabajadasPorDia:
    sumaDeHoras = sumaDeHoras + i
    print("sumaDeHoras: ", sumaDeHoras)

print("sumaDeHoras FINAL: ", sumaDeHoras)

promedio = round(sumaDeHoras / 7, 1)
print("promedio: ", promedio, 'horas')