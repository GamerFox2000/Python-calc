# -*- coding: utf-8 -*-
"""Copia de Tecno.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-YcFEiSMyRR7XnWAEYWcvZC1k3pfGlrr
"""

import random as r
import time as t
from IPython.display import clear_output

print("Iniciando MSDOS 6.0")
t.sleep(4)
clear_output()
print("Cargando [_____]")
t.sleep(2)
clear_output()
print("Cargando [-____]")
t.sleep(2)
clear_output()
print("Cargando [--___]")
t. sleep(2)
clear_output()
print ("Cargando [---__]")
t. sleep(2)
clear_output ()
print("Cargando [----_]")
t. sleep(2)
clear_output()
print("Cargando [-----]")
t.sleep(1)
clear_output()
print ("Listo")
t. sleep(3)
clear_output ()
t. sleep(0.1)
print("CARGANDO FIRST BOOT")
t.sleep(2)
clear_output()
nombre = input("¿como te llamas?")
if nombre == "deb":
  cmd()
else:
  etaso = input(f"hola {nombre} que tal estas?")
listamal = ["mejorate", "que mal", "recuperate"]
listabien = ["que bien", "perfecto"]
if etaso == "Mal":
  print(r.choice(listamal))
  t.sleep(10)
elif etaso == "Bien":
  print(r.choice(listabien))
  t.sleep(5)
else:
  print("no se que responder")
  t.sleep(5)
clear_output()
t.sleep(0.1)
if input("Quieres jugar?") == "Si":
  print("Adivina el numero de entre 1 a 100")
  def juego():
    numint = r.randint(1,100)
    def guess():
      guessnum = input("")
      guessing = int(guessnum)
      if guessing == numint:
        print("¡Ganaste!")
      elif guessing >= numint:
        print("Muy alto")
        guess()
      elif guessing <= numint:
        print("Muy bajo")
        guess()
      else:
        guess()
    guess()
    jdn = input("Quieres jugar de nuevo?")
    if jdn == "Si":
      juego()
    else:
      print("Espero que te haya gustado")
  juego()
else:
  print("Vale")
t.sleep(2)
clear_output()
print("Iniciando MSDOS 6.0")
t.sleep(4)
clear_output()
print("Cargando [_____]")
t.sleep(2)
clear_output()
print("Cargando [-____]")
t.sleep(2)
clear_output()
print("Cargando [--___]")
t.sleep(2)
clear_output()
print("Cargando [---__]")
t.sleep(2)
clear_output()
print("Cargando [----_]")
t.sleep(2)
clear_output()
print("Cargando [-----]")
t.sleep(1)
clear_output()
print("Listo")
t.sleep(3)
clear_output()
t.sleep(0.1)
dosstart = (f"C:/users/{nombre}/")
hide = ("off")
def cmd():
  dos = input(dosstart)
  if dos == "Dir":
    if nombre == "dev":
      print(" ")
      print(" ")
      print(" BOOM.EXE           EXE !")
      print(" DOCUMENTS          DIR")
      print(" DOWNLOADS          DIR")
      print(" PHOTO              DIR")
      print(" TELNET             CMD")
      print(" VIDEO              DIR")
      print(" ")
      print(" ")
    else:
      print(" ")
      print(" ")
      print(" DOCUMENTS   DIR")
      print(" DOWNLOADS   DIR")
      print(" PHOTO       DIR")
      print(" VIDEO       DIR")
      print(" ")
      print(" ")
    cmd()
  elif dos == "WIN":
    clear_output()
    print("Booting Windows")
    t.sleep(2)
    clear_output()
    print("Loading Graphical User Interface")
    t.sleep(2)
    clear_output()
    print("Graphical User Interface Error")
    print("Going back to MSDOS")
    t.sleep(1)
    clear_output()
    cmd()
  elif dos == "Documents":
    def docu():
      dosdoc = input(f"C/users/{nombre}/documents:")
      if dosdoc == "Cd":
        cmd()
      elif dosdoc == "Dir":
        print(" ")
        print("EMPTY")
        print(" ")
        docu()
      else:
        print("WRONG COMMAND OR FILE")
        docu()
    docu()
  elif dos == "Downloads" :
    def down():
      dosdow = input(f"C/users/{nombre}/downloads:")
      if dosdow =="Cd":
        cmd()
      elif dosdow == "Dir":
        print(" ")
        print("EBAY.EXE     EXE")
        print("NETFLIX.EXE  EXE")
        print(" ")
        down()
      elif dosdow == "Netflix.exe":
        print("⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️")
        print("⬛️⬛️⬛️⬛️🟥⬛️⬛️⬛️⬛️⬛️🟥⬛️⬛️⬛️⬛️")
        print("⬛️⬛️⬛️⬛️🟥🟥⬛️⬛️⬛️⬛️🟥⬛️⬛️⬛️⬛️")
        print("⬛️⬛️⬛️⬛️🟥🟥⬛️⬛️⬛️⬛️🟥⬛️⬛️⬛️⬛️")
        print("⬛️⬛️⬛️⬛️🟥⬛️🟥⬛️⬛️⬛️🟥⬛️⬛️⬛️⬛️")
        print("⬛️⬛️⬛️⬛️🟥⬛️🟥⬛️⬛️⬛️🟥⬛️⬛️⬛️⬛️")
        print("⬛️⬛️⬛️⬛️🟥⬛️⬛️🟥⬛️⬛️🟥⬛️⬛️⬛️⬛️")
        print("⬛️⬛️⬛️⬛️🟥⬛️⬛️🟥⬛️⬛️🟥⬛️⬛️⬛️⬛️")
        print("⬛️⬛️⬛️⬛️🟥⬛️⬛️⬛️🟥⬛️🟥⬛️⬛️⬛️⬛️")
        print("⬛️⬛️⬛️⬛️🟥⬛️⬛️⬛️🟥⬛️🟥⬛️⬛️⬛️⬛️")
        print("⬛️⬛️⬛️⬛️🟥⬛️⬛️⬛️⬛️🟥🟥⬛️⬛️⬛️⬛️")
        print("⬛️⬛️⬛️⬛️🟥⬛️⬛️⬛️⬛️🟥🟥⬛️⬛️⬛️⬛️")
        print("⬛️⬛️⬛️⬛️🟥⬛️⬛️⬛️⬛️⬛️🟥⬛️⬛️⬛️⬛️")
        print("⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️")
        print(" ")
        print("INICIANDO")
        t.sleep(4)
        clear_output()
        print("ERROR AL CONECTARSE")
        down()
      elif dosdow == "Ebay.exe":
        print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
        print("⬜️⬜️⬜️⬜️⬜️🟦⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
        print("⬜️⬜️⬜️⬜️⬜️🟦⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
        print("⬜️🟥🟥🟥⬜️🟦⬜️⬜️⬜️🟨🟨🟨⬜️⬜️⬜️⬜️⬜️")
        print("⬜️🟥⬜️🟥⬜️🟦🟦🟦⬜️⬜️⬜️🟨⬜️🟩⬜️🟩⬜️")
        print("⬜️🟥🟥🟥⬜️🟦⬜️🟦⬜️🟨🟨🟨⬜️🟩⬜️🟩⬜️")
        print("⬜️🟥⬜️⬜️⬜️🟦⬜️🟦⬜️🟨⬜️🟨⬜️🟩🟩🟩⬜️")
        print("⬜️🟥🟥🟥⬜️🟦🟦🟦⬜️🟨🟨🟨⬜️⬜️🟩⬜️⬜️")
        print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟩⬜️⬜️")
        print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
        print("")
        print("INICIANDO")
        t.sleep(4)
        clear_output()
        print("          INICIO         ")
        print("                         ")
        print("Comprar ahora:    Ch     ")
        print("Subasta:          Su     ")
        ebay = input("Elige")
        clear_output()
        if ebay == "Ch":
          print("     COMPRAR AHORA     ")
          print("                       ")
          print("    NO HAY PRODUCTOS   ")
          down()
        elif ebay == "Su":
          print("        SUBASTA        ")
          print("                       ")
          print("    NO HAY PRODUCTOS   ")
          down()
        else:
          down()
        down()
      else:
        print("WRONG COMMAND OR FILE")
        down()
    down()
  elif dos == "Photo" :
    def phot():
      dospho = input(f"C/users/{nombre}/photos:")
      if dospho =="Cd":
        cmd()
      elif dospho == "Dir":
        print(" ")
        print("EMPTY")
        print(" ")
        phot()
      else:
        print("WRONG COMMAND OR FILE")
        phot()
    phot()
  elif dos == "Video" :
    def vide():
      dosvid = input(f"C/users/{nombre}/video:")
      if dosvid =="Cd":
        cmd()
      elif dosvid == "Dir":
        print(" ")
        print("EMPTY")
        print(" ")
        vide()
      else:
        print("WRONG COMMAND OR FILE")
        vide()
    vide()
  elif dos == "Clr":
    clear_output()
    t.sleep(0.1)
    cmd()
  elif dos == "Boom":
    def boom():
      print("Loop")
      boom()
    boom()
  elif dos == "Pwr":
    clear_output()
  elif dos == "Telnet":
    clear_output()
    t.sleep(0.1)
    def telnetbucle():
      telnet = input("Telnet:")
      if telnet == "Star wars":
        clear_output()
        t.sleep(0.1)
        print("                                          ")
        print("                                          ")
        print("                                          ")
        print("                                          ")
        print("                                          ")
        print("                                          ")
        print("                                          ")
        print("                 loading                  ")
        t.sleep(3)
        clear_output()
        print("                                          ")
        print("                                          ")
        print("           \\\            //               ")
        print("            \\\          //                ")
        print("             o _________o                 ")
        print("                 20th                     ")
        print("                century                   ")
        print("                studios                   ")
        t.sleep(2)
        clear_output()
        print("                                          ")
        print("                                          ")
        print("                                          ")
        print("                  STAR                    ")
        print("                  WARS                    ")
        print("                                          ")
        print("                                          ")
        print("                                          ")
        t.sleep(2)
        clear_output()
        print("CONECTION ERROR")
        t.sleep(1)
        clear_output()
        i = 0
        while i <= 10:
          print(".")
          t.sleep(0.5)
          clear_output()
          print(". .")
          t.sleep(0.5)
          clear_output()
          print(". . .")
          t.sleep(0.5)
          clear_output()
          t.sleep(0.1)
          i = i + 1
        print("CONECTION LOST")
        telnetbucle()
      elif telnet == "Pwr":
        cmd()
      else:
        print("WRONG COMMAND")
        telnetbucle()
    telnetbucle()
  else:
    print(" ")
    print("WRONG COMMAND OR FILE")
    print(" ")
    cmd()
cmd()