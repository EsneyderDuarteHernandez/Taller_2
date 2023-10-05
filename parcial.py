import time
import statistics
import random


class GenerarListaAleatoria:
    ''' Esta clase sirve para generar una lista con datos aleatorios'''
    
    def __init__(self, tamaño):     #Metodo de instancia
        self.tamaño = tamaño
                       #variable            [for variable in lista]  [condicional]
        listrand = [random.randint(1, self.tamaño + 1) for i in range (1, self.tamaño + 1)] #se genera una lista con numero aleatorio entre 1 y el tamaño de la lista
        if tamaño >= 10:
            print("Lista generada (primeros 10 elementos):")
            listaelem = []
            for i in range(0,10):
                listaelem.append(listrand[i])           #Recorre el ciclo for hasta 10 y le asgina los valores de los primeros 10 indices a listelem
            #print(listaelem)
            self.mostrar_lista(listaelem)
        else:
            self.mostrar_lista(listrand)
        
        

    def mostrar_lista(self,lista):
        self.lista = lista
        print(lista)


'''
if __name__== '__main__':
    gen = GenerarListaAleatoria(5)
               
    '''

class CompararSorted:
    pass


class BusquedaLineal:
    '''La busqueda lineal recorre la lista de principio a fin hasta encontrar el elemento.'''

class BusquedaBinaria:
    '''La busqueda binaria requiere que la lista este ordenada y encuentra el elemento dividiendo la lista en mitades.'''
    

class OrdenamientoBurbuja:
    '''El ordenamiento por burbuja compara los pares de elementos adyacentes y los intercambia si estan en orden incorrecto.'''

class OrdenamientoRapido:
    '''El ordenamiento rapido utiliza un elemento 'pivote' para dividir la lista y ordenarla de manera eficiente.
    '''
class SumarElem:
    pass

class CalcPromedio:
    pass

class CalcMediana():
    pass

class CalcVarianza:
    pass
class EncMinimo:
    pass

class EncMaximo:
    pass
class MostrarLong:
    pass
class Complists:
    pass
class Ayuda(BusquedaLineal, BusquedaBinaria, OrdenamientoBurbuja, OrdenamientoRapido): #Herencia multiple
    def __str__(self):
        bl = BusquedaLineal()  #Se asigna la clase para imprimir el doc de cada clase
        bb = BusquedaBinaria()
        ob = OrdenamientoBurbuja()
        otr = OrdenamientoRapido()
        
        return (f'Busqueda linal: {bl.__doc__}\nBusqueda Binaria: {bb.__doc__}\nOrdenamiento por burbuja: {ob.__doc__}\nOrdenamiento Rapido: {otr.__doc__}')
'''
if __name__ == '__main__':
    bl2= Ayuda()
    #print(bl2)
'''
class Submenu(GenerarListaAleatoria, OrdenamientoBurbuja,OrdenamientoRapido,CompararSorted,BusquedaLineal,BusquedaBinaria,SumarElem,CalcPromedio,CalcMediana,CalcVarianza,EncMinimo,EncMaximo,MostrarLong,Complists):
  
    @staticmethod
    def submenu():
        print("\nSubmenú:")
        option = ['a.','b.','c.','d.','e.','f.','g.','h.','i.','j.','k','l.','m.','n.','o.']
        title = ['Imprimir lista', 'Ordenar con burbuja','Ordenar rapido','Comparar con sorted()','Buscar elemento (Lineal)','Buscar elemento (binaria)','Sumar elementos','Calcular promedio','Calcular mediana','Calcular varianza','Encontrar el minimo','Encontrar el maximo','Mostrar longitud de la lista','Comparar con otra lista','Volver al menú principal']
        for i, j in zip(option, title):         #Crea un iterador que agregara elementos de dos o mas iterables
            print(i, j)
        subm = input("Seleccione una opcion: ")
        subm.lower()
        if subm == 'a':
            print("Imprimir lista: ")
            pass
           

            
         
        '''
if __name__ == '__main__':
    sm = Submenu.submenu()
    print(sm.submenu())
'''


while True:
    #Menu principal
    print("Menú principal:")
    print("1. Generar lista aleatoria")
    print("2. Ingresar lista manualmente")
    print("3. Usar lista previamente cargada")
    print("4. Crear lista desde rango")
    print("5. Ayuda")
    print("6. Salir")
    while True:             #Para controlar la opcion ingresada por el usuario
        try:
            opcion = int(input("\nSeleccione una opción: "))            
            if 0 < opcion <= 6:                             #Lo que puede causar el error
                break
            else:
                print("Opción Invalida. Intente de nuevo")
        except ValueError:
            print("La entrada debe ser un número válido. Intente de nuevo.")            #en caso de que se de el error

    if opcion == 1:
        print("Generar lista aleatoria")
        while True:                                                             #Para controlar el numero ingresado para el tamaño de la lista
            try:
                tamaño = int(input("Ingrese el tamaño de la lista: "))
                if (type(tamaño) is int()):
                    print("Número valido.")
                break
            except ValueError:
                print("La entrada debe ser un número válido. Intente de nuevo.")
        opcion1 = GenerarListaAleatoria(tamaño)
        sm1 = Submenu.submenu()
        print(sm1.submenu())

    elif opcion == 2:
        print ("Ingresar lista manualmente")
    elif opcion == 3:
        print("Usar lista previamente cargada ")
    elif opcion == 4:
        print("Crear lista desde rango")
    elif opcion == 5:
        print("Ayuda:")
        ayuda = Ayuda()
        print(ayuda)
    elif opcion == 6:
        print("¡Vuelva pronto!")
        break

