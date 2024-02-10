ventasDelDia = [4000,15000,500,100,1000,1500,1500,30000,50000,2000,5000,3500]

sumaDeVentas = 0
for valorDeVenta in ventasDelDia:
    sumaDeVentas = sumaDeVentas + valorDeVenta
    print('suma de ventas: ', sumaDeVentas)

print("suma de ventas en total: ", sumaDeVentas)

gananciaDelDia = sumaDeVentas * 0.2
print("Ganancia de dia: ", gananciaDelDia ) 