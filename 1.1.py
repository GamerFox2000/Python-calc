import random
import requests
print("Bienvenido a Python Calc")
nombre = input("Introduzca su nombre:\t")
if nombre == "oscar":
 print("Hola de nuevo Óscar")
else :
 print("Bienvenido", nombre)
print("1 Calculadora")
print("2 Juegos")
print("3 Admin")
print("4 Actualización")
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
  elif opcion == '2':
    print("La resta es:", resta(num1, num2))
  elif opcion == '3':
    print("La multiplicación es:", multiplicacion(num1, num2))
  elif opcion == '4':
    print("La división es:", division(num1, num2))
  else:
    print("Rerun code please")

elif elegir == 2:
  #esto es un menu para los juegos
  print("Elige un juego")
  print("1 adivinanzas")

  erjo = input("\n")
  erjo=int(erjo)
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
            print(f"¡Felicidades ",nombre "! ¡Adivinaste el número en {intentos} intentos!")
            break
      volver_a_jugar = input("¿Quieres jugar de nuevo? (s/n): ")
      if volver_a_jugar.lower() == "s":
        jugar_adivinanza()
      else:
        print("¡Gracias por jugar!")

    jugar_adivinanza()

elif (elegir == 3) and (nombre == "oscar"):
  print ("Admin")
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
    url_archivo = "https://raw.githubusercontent.com/gamerfox2000/python-calc/main/1.1.py"
    nombre_local = "Python-calc-1.1.py"

    # Llamar a la función para descargar el archivo
    descargar_archivo(url_archivo, nombre_local)

else:
  print ("Rerun code please")
