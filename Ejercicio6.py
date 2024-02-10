ventasDelDia = [4000,15000,500,100,1000,1500,1500,30000,50000,2000,5000,3500]

print(ventasDelDia)

ventaMayor = float('-inf')
for numero in ventasDelDia:
    if numero>ventaMayor:
        ventaMayor = numero
print("La venta mayor fue: ", ventaMayor)

ventaMenor = float('inf')
for numero in ventasDelDia:
    if numero<ventaMenor:
        ventaMenor = numero
print("La venta menor fue: ", ventaMenor)