def convertidorVol(medida, valor):
    valorInicial=float(input("Ingrese el valor: "))
    total = valorInicial * valor 
    total = round(total, 2) 
    print("Usted tiene: ", total, medida)

menuPrincipal="""
Bienvenido al conversor de medidas
    
1 - Volumen
2 - Longitud
3 - Peso y Masa
4 - Temperatura
5 - Energía

Elige una opcion: """

opcionPrincipal=int(input(menuPrincipal))

#------------------------------------------------------------------------

if opcionPrincipal==1:
    menuVol1="""
    Elija el Volumen que tiene

    1 - Metro cúbicos
    2 - Litros
    3 - Mililitros
    4 - Galón Estadounidenses

    Elige una opcion: """
    
    datoVol1 = int(input(menuVol1))
    
    if datoVol1 == 1:
        menuVol2="""
        Elija el Volumen al que desea convertir

        1 - Litros
        2 - Mililitros
        3 - Galón Estadounidenses

        Elige una opcion: """
    
        datoVol2 = int(input(menuVol2))
        
        if datoVol2 == 1:
            convertidorVol("Litro",1000)
        elif datoVol2 == 2:
            convertidorVol("Mililitro",1e+6)
        elif datoVol2 == 3:
            convertidorVol("Galón Estadounidenses",264.172)
    
    if datoVol1 == 2:
        menuVol2="""
        Elija el Volumen al que desea convertir

        1 - Metrocubicos
        2 - Mililitros
        3 - Galón Estadounidenses

        Elige una opcion: """
    
        datoVol2 = int(input(menuVol2))
            
        if datoVol2 == 1:
            convertidorVol("Metrocubicos",0.001)
        elif datoVol2 == 2:
            convertidorVol("Mililitros",1000)
        elif datoVol2 == 3:
            convertidorVol("Galón Estadounidenses",0.264172)
            
    if datoVol1 == 3:
        menuVol2="""
        Elija el Volumen al que desea convertir

        1 - Metrocubicos
        2 - Litros
        3 - Galón Estadounidenses

        Elige una opcion: """
    
        datoVol2 = int(input(menuVol2))
            
        if datoVol2 == 1:
            convertidorVol("Metrocubicos",1e-6)
        elif datoVol2 == 2:
            convertidorVol("Litros",0.001)
        elif datoVol2 == 3:
            convertidorVol("Galón Estadounidenses",0.000264172)
            
    if datoVol1 == 4:
        menuVol2="""
        Elija el Volumen al que desea convertir

        1 - Metrocubicos
        2 - Litros
        3 - Mililitros

        Elige una opcion: """
    
        datoVol2 = int(input(menuVol2))
            
        if datoVol2 == 1:
            convertidorVol("Metrocubicos",0.00378541)
        elif datoVol2 == 2:
            convertidorVol("Litros",3.78541)
        elif datoVol2 == 3:
            convertidorVol("Mililitros",3785.40999993543)
            
#------------------------------------------------------------------------

elif opcionPrincipal==2:
    menuLong1="""
    Elija la Longitud que desea convertir

    1 - Kilómetros
    2 - Metros
    3 - Centimetros
    4 - Milimetros

    Elige una opcion: """
    
    datoLong1 = int(input(menuLong1))
    
    if datoLong1 == 1:
        menuLong2="""
        Elija la Longitud que desea convertir

        1 - Metros
        2 - Centimetros
        3 - Milimetros

        Elige una opcion: """
    
        datoLong2 = int(input(menuLong2))
        
        if datoLong2 == 1:
            convertidorVol("Metros",1000)
        elif datoLong2 == 2:
            convertidorVol("Centimetros",100000)
        elif datoLong2 == 3:
            convertidorVol("Milimetros",1e+6)
    
    if datoLong1 == 2:
        menuLong2="""
        Elija la Longitud que desea convertir

        1 - Kilometros
        2 - Centimetros
        3 - Milimetros

        Elige una opcion: """
    
        datoLong2 = int(input(menuLong2))
        
        if datoLong2 == 1:
            convertidorVol("Kiloetros",0.001)
        elif datoLong2 == 2:
            convertidorVol("Centimetros",100)
        elif datoLong2 == 3:
            convertidorVol("Milimetros",1000)
    
    if datoLong1 == 3:
        menuLong2="""
        Elija la Longitud que desea convertir

        1 - Kilometros
        2 - Metros
        3 - Milimetros

        Elige una opcion: """
    
        datoLong2 = int(input(menuLong2))
        
        if datoLong2 == 1:
            convertidorVol("Kiloetros",1e-5)
        elif datoLong2 == 2:
            convertidorVol("Metros",0.01)
        elif datoLong2 == 3:
            convertidorVol("Milimetros",10)
            
    if datoLong1 == 4:
        menuLong2="""
        Elija la Longitud que desea convertir

        1 - Kilometros
        2 - Metros
        3 - Centimetros

        Elige una opcion: """
    
        datoLong2 = int(input(menuLong2))
        
        if datoLong2 == 1:
            convertidorVol("Kiloetros",1e-6)
        elif datoLong2 == 2:
            convertidorVol("Metros",0.001)
        elif datoLong2 == 3:
            convertidorVol("Centimetros",0.1)
    
#------------------------------------------------------------------------
    
elif opcionPrincipal==3:
    menuPes1="""
    Elija el Peso o Masa que desea convertir

    1 - Toneladas
    2 - Kilogramos
    3 - Gramos
    4 - Miligramos

    Elige una opcion: """
    
    datoPes1 = int(input(menuPes1))
    
    if datoPes1 == 1:
        menuPes2="""
        Elija el Peso o Masa que desea convertir

        1 - Kilogramo
        2 - Gramo
        3 - Miligramo

        Elige una opcion: """
    
        datoPes2 = int(input(menuPes2))
        
        if datoPes2 == 1:
            convertidorVol("Kilogramos",1000)
        elif datoPes2 == 2:
            convertidorVol("Gramos",1e+6)
        elif datoPes2 == 3:
            convertidorVol("Miligramos",1e+9)
    
    if datoPes1 == 2:
        menuPes2="""
        Elija el Peso o Masa que desea convertir

        1 - Toneladas
        2 - Gramo
        3 - Miligramo

        Elige una opcion: """
    
        datoPes2 = int(input(menuPes2))
        
        if datoPes2 == 1:
            convertidorVol("Toneladas",0.001)
        elif datoPes2 == 2:
            convertidorVol("Gramos",1000)
        elif datoPes2 == 3:
            convertidorVol("Miligramos",1e+6)
            
    if datoPes1 == 3:
        menuPes2="""
        Elija el Peso o Masa que desea convertir

        1 - Toneladas
        2 - Kilogramos
        3 - Miligramo

        Elige una opcion: """
    
        datoPes2 = int(input(menuPes2))
        
        if datoPes2 == 1:
            convertidorVol("Toneladas",1e-6)
        elif datoPes2 == 2:
            convertidorVol("Kilogramos",0.001)
        elif datoPes2 == 3:
            convertidorVol("Miligramos",1000)
            
    if datoPes1 == 4:
        menuPes2="""
        Elija el Peso o Masa que desea convertir

        1 - Toneladas
        2 - Kilogramos
        3 - Gramo

        Elige una opcion: """
    
        datoPes2 = int(input(menuPes2))
        
        if datoPes2 == 1:
            convertidorVol("Toneladas",1e-9)
        elif datoPes2 == 2:
            convertidorVol("Kilogramos",1e-6)
        elif datoPes2 == 3:
            convertidorVol("Gramos",0.001)
            
#------------------------------------------------------------------------
    
elif opcionPrincipal==4:
    menuTemp= """
    Elija la Temperatura que desea convertir

    1 - Grados Celsius
    2 - Grados Fahrenheit
    3 - Kelvin

    Elige una opcion: """
    
    menuTemp = int(input(menuTemp))
    
#----------------------------------------------------------------------
    
elif opcionPrincipal==5:
    menuVol="""
    Elija la Energía que desea convertir

    1 - Julio
    2 - Kilojulio
    3 - Caloria gramo
    4 - Kilocaloria

    Elige una opcion: """
    
    menuVol = int(input(menuVol))
