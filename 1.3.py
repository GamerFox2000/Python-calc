import random
import requests
print("Bienvenido a Python Calc")
nombre = input("Introduzca su nombre por favor:\t")
if nombre == "oscar":
  def password():
    contraseña = input("Introduce la contraseña \n")
    contraseña=int(contraseña)
    if contraseña == 789632145:
      print("Hola de nuevo Óscar")
    else:
      print("Intentalo de nuevo")
      password()
  password()
else :
 print("Bienvenido", nombre)
def code():
  print("1 Calculadora")
  print("2 Juegos")
  print("3 Admin")
  print("4 Actualización")
  print("5 Apagar")
  print("6 creditos")
  print("Para más funciones pedirlas en el github(gamerfox2000/python-calc)")
  elegir = input("Elige \n")
  elegir = int(elegir)
  if elegir == 1:
   def suma(a, b):
    return a + b

   def resta(a, b):
    return a - b

   def multiplicacion(a, b):
    return a * b

   def division(a, b):
     if b != 0:
        return a / b
     else:
        return "Error: No se puede dividir entre cero"
   print("Seleccione la operación:")
   print("1. Suma")
   print("2. Resta")
   print("3. Multiplicación")
   print("4. División")

   opcion = input("Ingrese la opción (1/2/3/4): ")

   num1 = float(input("Ingrese el primer número: "))
   num2 = float(input("Ingrese el segundo número: "))
   if opcion == '1':
    print("La suma es:", suma(num1, num2))
    code()
   elif opcion == '2':
    print("La resta es:", resta(num1, num2))
    code()
   elif opcion == '3':
    print("La multiplicación es:", multiplicacion(num1, num2))
    code()
   elif opcion == '4':
    print("La división es:", division(num1, num2))
    code()
   else:
    code()

  elif elegir == 2:
    #esto es un menu para los juegos
   print("Elige un juego")
   print("1 adivinanzas")
   print("2 tres en raya")

   erjo = input("1 o 2 \n")
   erjo=int(erjo)
   if erjo == 2:
    def imprimir_tablero(tablero):
     for fila in tablero:
        print("|".join(fila))
        print("-" * 5)

    def verificar_ganador(tablero):
    # Verificar filas y columnas
      for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != ' ':
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != ' ':
            return tablero[0][i]
    # Verificar diagonales
        if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
            return tablero[0][0]
        if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
           return tablero[0][2]
        return None

    def jugar_tres_en_raya():
      tablero = [[' ' for _ in range(3)] for _ in range(3)]
      jugador_actual = 'X'
      jugadas_restantes = 9

      print("¡Bienvenido ",nombre ,"al juego de tres en raya!")

      while jugadas_restantes > 0:
        imprimir_tablero(tablero)
        fila = int(input(f"Turno del jugador {jugador_actual}. Ingrese el número de fila (0, 1, 2): "))
        columna = int(input(f"Ingrese el número de columna (0, 1, 2): "))

        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = jugador_actual
            jugadas_restantes -= 1

            ganador = verificar_ganador(tablero)
            if ganador:
                imprimir_tablero(tablero)
                print(f"¡Felicidades! ¡El jugador {ganador} ha ganado!")
                break

            jugador_actual = 'O' if jugador_actual == 'X' else 'X'
        else:
            print("Esa casilla ya está ocupada. Intenta de nuevo.")

      if jugadas_restantes == 0 and not ganador:
        imprimir_tablero(tablero)
        print("¡Es un empate!")

    # Ejecutar el juego
    jugar_tres_en_raya()

   if erjo == 1:
    def jugar_adivinanza():
      numero_secreto = random.randint(1, 100)
      intentos = 0

      print("¡Bienvenido", nombre ,"a Adivina el Número!")
      print("Estoy pensando en un número entre 1 y 100.")

      while True:
        intento = int(input("¿Cuál es tu adivinanza? "))

        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"¡Felicidades {nombre}! ¡Adivinaste el número en {intentos} intentos!")
            break
      volver_a_jugar = input("¿Quieres jugar de nuevo? (s/n): ")
      if volver_a_jugar.lower() == "s":
        jugar_adivinanza()
      else:
        print("¡Gracias por jugar!")
        code()

    jugar_adivinanza()

  elif (elegir == 3) and (nombre == "oscar"):
   print ("Zona para Administradores")
   print ("Acceso permitido")
   print ("Nada")
   print (code())
   code()
  elif (elegir == 3) and not (nombre == "oscar"):
   print ("Zona para Administradores")
   print ("Acceso prohibido")
   code()
  elif elegir == 4:
   print("actualizando")
   def descargar_archivo(url, nombre_archivo):
    try:
        # Realizar la solicitud GET a la URL para descargar el archivo
        respuesta = requests.get(url)
        # Verificar si la solicitud fue exitosa (código de estado 200)
        if respuesta.status_code == 200:
            # Escribir el contenido descargado en un archivo local
            with open(nombre_archivo, 'wb') as archivo:
                archivo.write(respuesta.content)
            print(f"El archivo {nombre_archivo} ha sido descargado exitosamente.")
        else:
            print("Error al descargar el archivo.")
    except Exception as e:
        print("Ocurrió un error:", e)

    # URL del archivo a descargar y nombre local del archivo
    url_archivo = "https://raw.githubusercontent.com/gamerfox2000/python-calc/main/1.3.py"
    nombre_local = "Python-calc-1.1.py"

    # Llamar a la función para descargar el archivo
    descargar_archivo(url_archivo, nombre_local)
   code()

  elif elegir == 5:
    print("Gracias por usar este codigo")

  elif elegir == 6:
    print("Calculadora, Juegos, Actualización, e Integración: Gamerfox2000")
    code()

  else:
   print ("Intentalo de nuevo")
   code()
code()
