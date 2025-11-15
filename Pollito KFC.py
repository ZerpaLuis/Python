PrePollo= 12
iva=0.16
nomCliente=input("ingresé su nombre:")
EdadCliente=float(input("ingresé su edad:"))
Cantidad_Pollos=float(input("ingresé la cantidad de pollos a comprar:"))
Precio_total=PrePollo*Cantidad_Pollos
Porcentaje_Descuento=0
if EdadCliente >=65:
    if 5<=Cantidad_Pollos<=10:
        Porcentaje_Descuento=0.12
    else:
        Porcentaje_Descuento=0.00
elif EdadCliente >=18:
    if Cantidad_Pollos>=20:
        Porcentaje_Descuento=0.10
    elif Cantidad_Pollos>=10:
        Porcentaje_Descuento=0.05
else:
    Porcentaje_Descuento=0.02
Total_Descuento=Precio_total-(Precio_total*Porcentaje_Descuento)
Total_Pagar=Total_Descuento+(Total_Descuento*iva)
print(f"Toral al pagar{Total_Pagar:.2f}")     

#APRENDAN A COPIARSE
# SEAN UN POCO MAS PILAS
# INSERTAR EMOJI DE DECEPCIÓN ACA
