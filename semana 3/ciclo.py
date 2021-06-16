class For:
    def __init__(self):
        pass

    def usoFor(self):
        # ciclo repettivo de incrementos o decrementos se ejecuta por verdadero
        nombre="DANIEL"
        datos = ["Daniel",50,True]
        # pos   0   1   2
        numeros=(2,5,6,4,1)
        listaNotas=(2.5, 8.5, 10, 6.5)
        docente = {'nombre': 'Daniel', 'edad': 50, 'fac': 'faci'}
        lisaAlumnos = [{"nombre":"Erick","final":70},{"nombre":"Yady","final":60},{"nombre":"Danny","final":90}]
        # range([inicio=0],limite,[inc/dec=1]). Genera un rango de valores desde un valor inicial a unv alor final
        #se ejecuta desde inicio hasta el limite
        #for con range() o for con colecciones
        j=0
        while j<5:
            print('while',j)
            j=j+1

        for i in range(5): #rango(0,1,2,3,4)
            print('for',i,end=" ")
        print()
        for i in range(1,5): # rango(1,2,3,4)
            print('for',i,end=" ")
        print()
        for i in range(2,10,2): # rango(/2,4,6,8)
            print('for',i,end=" ")
        print()
        for i in range(12,3,-3): # rango(12,9,6)
            print('for',i,end=" ")
        
        lon = len(nombre)
        for pos in range(lon):
            if pos%2 == 0 and pos !=0:
               print(pos,nombre[pos])

        #for elem in nombre:
         #   print(elem,end=" ")

        #for notas in listaNotas:
         #   print(notas, end=" ")
          #  print("saliendo del for ")

    #print(listaNotas)
    #for notas in listaNotas:
     #   acum=0
      #  for nota in notas:
       #     acum=acum+notas
        #print(acum/len(notas),end=" ")

        print("\nDiccionario de alumnos")
        print(lisaAlumnos)
        for alumnos in listaNotas:
            print(alumnos)
            for clave,valor in alumnos.items():
                print(clave,":",valor,end=" ")
            print()



bucle = For()
bucle.usoFor()
 
