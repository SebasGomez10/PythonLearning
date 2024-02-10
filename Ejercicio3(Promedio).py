print('promedio de los tres examenes del primer periodo')
a = float(input('que nota saco en el primer examen del primer periodo'))
b = float(input('que nota saco en el segundo examen del primer periodo'))
c = float(input('que nota saco en el tercer examen del primer periodo'))
promedioPrimerPeriodo = (a + b + c)/3
print('el promedio de los examenes del primer periodo fue:') 
print(promedioPrimerPeriodo)

print('promedio de los tres examenes del segundo periodo')
d = float(input('que nota saco en el primer examen del segundo periodo'))
e = float(input('que nota saco en el segundo examen del segundo periodo'))
f = float(input('que nota saco en el tercer examen del segundo periodo'))
promedioSegundoPeriodo = (d + e + f)/3
print('el promedio de los examenes del segundo periodo fue:') 
print(promedioSegundoPeriodo)

print('la nota final fue')
notaFinal =  (promedioPrimerPeriodo + promedioSegundoPeriodo) / 2
print(notaFinal)