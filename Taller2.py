import pickle                           #Modulo para serializar y deserializar
# Lista para almacenar los estudiantes
estudiantes = []

# Tupla de carreras disponibles
carreras_disponibles = (
    "Ingenieria civil",
    "Ingenieria en automatizacion y control",
    "Ingenieria de productividad y calidad",
    "Ingenieria agropecuaria",
    "Ingenieria en seguridad y salud en el trabajo",
    "Ingenieria informatica\n"
)

# Función de validación para verificar si el nombre contiene solo letras y espacios
def es_nombre_valido(nombre):
    for caracter in nombre:
        if not (caracter.isalpha() or caracter.isspace()):    #Si el caracter no es letra o espacio entonces retorne falso
            return False
    return True

# Función para registrar estudiantes
def registrar_estudiante():
    while True:
        nombre = input("Ingrese el nombre del estudiante: ")

        # Verificar si el nombre contiene solo letras y espacios
        if es_nombre_valido(nombre):
            break
        else:
            print("El nombre debe contener solo letras y espacios. Intente de nuevo.")

    # Mostrar las opciones de carreras disponibles
    print("\nCarreras disponibles:")
    for i, carrera in enumerate(carreras_disponibles, start=1):         #Accede a los elementos empezando con el indice en 1
        print(f"{i}. {carrera}")

    # Pedir al usuario que seleccione una carrera por número
    while True:
        try:
            opcion = int(input("Seleccione el número de la carrera del estudiante: "))
            if 1 <= opcion <= len(carreras_disponibles):                #numero ingresado debe estar entre 1 y el numero de carreras disponilbes
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Opción no válida. Intente de nuevo.")

    # Obtener la carrera seleccionada
    carrera = carreras_disponibles[opcion - 1]          #-1 ya que la lista esta desde indice 0


    # Obtener la nota del estudiante
    while True:
        try:
            nota = float(input("\nIngrese la nota del estudiante (de 0 a 5): "))
            if 0 <= nota <= 5:
                break
            else:
                print("La nota debe estar dentro del rango de 0 a 5. Intente de nuevo.")
        except ValueError:
            print("La entrada debe ser un número válido. Intente de nuevo.")

    # Utilizar un diccionario para representar al estudiante (nombre, carrera, nota)
    estudiante = {"nombre": nombre, "carrera": carrera, "nota": nota}

    estudiantes.append(estudiante)                              #Asigna el dato de estudiante a la lista estudiantes
    print("\nEstudiante registrado con éxito.")


# Función para consultar estudiantes de una carrera
def consultar_estudiantes_carrera():
    # Mostrar las opciones de carreras disponibles
    print("Carreras disponibles:")
    for i, carrera in enumerate(carreras_disponibles, start=1):     #Accede a los indices de la lista y los enumera, empezando en 1
        print(f"{i}. {carrera}")

    # Pedir al usuario que seleccione una carrera por número
    while True:
        try:
            opcion = int(input("Seleccione el número de la carrera a consultar: "))
            if 1 <= opcion <= len(carreras_disponibles):            #opcion debe estar entre 1 y el tamaño de carreras_disp
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Opción no válida. Intente de nuevo.")

    # Obtener la carrera seleccionada
    carrera_buscar = carreras_disponibles[opcion - 1]

    estudiantes_carrera = [estudiante for estudiante in estudiantes if estudiante["carrera"] == carrera_buscar]     
    if estudiantes_carrera:             #Busca 
        print("Estudiantes de la carrera", carrera_buscar + ":")
        for estudiante in estudiantes_carrera:
            print(f"Nombre: {estudiante['nombre']}, Nota: {estudiante['nota']}")
    else:
        print(f"No se encontraron estudiantes en la carrera {carrera_buscar}.")
# Función para calcular el promedio de notas
def calcular_promedio():

    if estudiantes:
        promedio = sum(estudiante["nota"] for estudiante in estudiantes) / len(estudiantes)
        print(f"El promedio de notas de todos los estudiantes es: {promedio:.2f}")
    else:
        print("No hay estudiantes registrados.")

# Función para ver estudiantes destacados
def ver_estudiantes_destacados():
    if estudiantes:
        estudiantes_destacados = [estudiante for estudiante in estudiantes if estudiante["nota"] >= 4.0]
        if estudiantes_destacados:
            print("Estudiantes destacados:")
            for estudiante in estudiantes_destacados:
                print(f"Nombre: {estudiante['nombre']}, Nota: {estudiante['nota']}")
        else:
            print("No hay estudiantes destacados.")
    else:
        print("No hay estudiantes registrados.")

#Funcion deserializar
def leer_archivo():
    try:
        with open ("archivo.pickle","rb") as f:     #abre archivo para lectura
            datos = pickle.load(f)                  #carga los datos que hay en archivo en datos
            #print(datos)
            return (datos)
    except (FileNotFoundError):                     #En caso de que aun no se haya creado el archivo llama la funcion serializacion para crearlo
        serializacion()

#Funcion para serializar
def serializacion():
    with open ("archivo.pickle","wb") as f:         #abre archivo para escritura
        datos = estudiantes
        pickle.dump(datos,f)                        #Carga lo que hay en datos en el archivo


lista_estudiantes1 = leer_archivo()             #llama la funcion leer archivo y los datos los asigna a estudiantes
while True:

        if (lista_estudiantes1):

            abrir = input("Ya existe una base de datos guardada. Desea abrir este archivo? (S/N): ")
            if (abrir.lower()=='s'):
                lista_estudiantes = leer_archivo()
                estudiantes.extend(lista_estudiantes)
                #print(estudiantes)
                print(f"\nSe ha cargado una base de datos con {len(estudiantes)} estudiantes")
                break
            elif abrir.lower() == 'n':
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida. (S/N): ")
        else:
            print("No se encontro una base de datos anterior. iniciando con una base de datos nueva")
            break


# Menú principal
while True:

    print("\nMenú:")
    print("1. Registrar estudiantes")
    print("2. Consultar estudiantes de una carrera")
    print("3. Calcular promedio")
    print("4. Ver estudiantes destacados")
    print("5. Salir")

    opcion = input("\nSeleccione una opción (1/2/3/4/5): ")

    if opcion == "1":
        registrar_estudiante()
    elif opcion == "2":
        consultar_estudiantes_carrera()
    elif opcion == "3":
        calcular_promedio()
    elif opcion == "4":
        ver_estudiantes_destacados()
    elif opcion == "5":
        while True:
            salir = input("Desea guarda los datos ingresados? (S/N): ")
            if salir.lower() == 's':
                serializacion()
                print("¡Datos guardados con exito!")
                break
            elif salir.lower() =='n':
                print("¡Hasta luego!")
                break

            else:
                print("Opción no válida. Por favor, digite una opción válida.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")