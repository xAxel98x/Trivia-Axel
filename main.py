# Mi trivia - Carol García
import random
import time
MAGENTA = '\033[35m'
BLUE = '\033[34m'
RESET = '\033[39m'

iniciar_trivia = True
intentos = 0

print ("Bienvenido a mi trivia sobre geografía del Perú.\n")
print ("La trivia consiste en responder 03 preguntas y ver cuanto puntaje puedes recopilar.\n")

nombre = input(MAGENTA+"\nPrimero ingresa tu nombre: "+RESET)
time.sleep(1)
print("\nBonito nombre",nombre,"!")

time.sleep(2)
viaje = input(MAGENTA+"\nYa viajaste alguna vez? (si o no): "+RESET).lower()
#while viaje not in ("si", "no"):
  #viaje = input("Debes responder si o no. Ingresa nuevamente tu respuesta: ")
if viaje == "si":
  time.sleep(1)
  print("\nMuy bien", nombre,", ya que", viaje,"has viajado entonces esperamos que te vaya super bien!")
else:
  print("\nNo importa", nombre,"que", viaje, "hayas viajado. Pronto será tu oportunidad!")

time.sleep(3)
print("\nA continuación, responde las siguientes preguntas escribiendo la letra de la alternativa y presiona 'Enter' para enviar tu respuesta.\n")
time.sleep(4)
print("Recuerda que se sumarán 10 puntos por respuesta correcta y se restarán 2 puntos por las incorrectas.\n")

time.sleep(3)
while iniciar_trivia == True:
  intentos += 1
  puntaje = random.randint(0,10) 
  print(MAGENTA+"\nIntento número:"+RESET,intentos)
  input("Presiona Enter para continuar")

  print(MAGENTA+"\nQuisimos que comiences con:",puntaje, "puntos.\n"+RESET)
  
  time.sleep(2)
  # Pregunta 1
  print (BLUE+"Pregunta 1 ¿Cuál es la capital histórica de Perú?\n"+RESET)
  print ("a) Lima")
  print ("b) Arequipa")
  print ("c) Cusco")
  
  respuesta_1 = input(BLUE+"\nTu respuesta: "+RESET).lower()
  
  while respuesta_1 not in ("a", "b", "c"):
    respuesta_1 = input("Debes responder a, b, o c. Ingresa nuevamente tu respuesta: ").lower()
   
  if respuesta_1 == "a":
    print("\nIncorrecto", nombre, "\nCusco es la capital histórica del Perú\n")
    puntaje = puntaje - 2
  elif respuesta_1 == "b":
    print("\nIncorrecto", nombre, "\nCusco es la capital histórica del Perú\n")
    puntaje = puntaje - 2
  else:
    puntaje += 10
    print("\nCorrecto", nombre,"!\n")
  
  print (MAGENTA+nombre, "llevas",puntaje,"puntos"+RESET)
  
  time.sleep(2)
  #Pregunta 2
  print (BLUE+"\nPregunta 2 ¿Cuál es la ciudad conocida como la Eterna Primavera?\n"+RESET)
  print ("a) Lima")
  print ("b) Trujillo")
  print ("c) Chiclayo")
  
  respuesta_2 = input(BLUE+"\nTu respuesta: "+RESET).lower()
  
  while respuesta_2 not in ("a", "b", "c"):
    respuesta_2 = input("Debes responder a, b, o c. Ingresa nuevamente tu respuesta: ").lower()
  
  if respuesta_2 == "a":
    print("\nIncorrecto", nombre,"\nTrujillo es la ciudad de la eterna primavera.\n")
    puntaje -= 2
  elif respuesta_2 == "c":
    print("\nIncorrecto", nombre,"\nTrujillo es la ciudad de la eterna primavera.\n")
    puntaje = puntaje - 2
  else:
    puntaje += 10
    print("\nCorrecto", nombre,"!\n")
  
  print (MAGENTA+nombre, "llevas",puntaje,"puntos"+RESET)
  
  time.sleep(3)
  # Pregunta 3
  print (BLUE+"\nPregunta 3 ¿Las tres vertientes hidrográficas que emanan de los Andes peruanos son?.\n"+RESET)
  print ("a) Costa, Sierra,Selva")
  print ("b) Pacífico, Atlántico, Titicaca")
  print ("c) Litoral, montaña, sierra")
  
  respuesta_3 = input(BLUE+"\nTu respuesta: "+RESET).lower()
  
  while respuesta_3 not in ("a", "b", "c"):
    respuesta_3 = input("Debes responder a, b, o c. Ingresa nuevamente tu respuesta: ").lower()
  
  if respuesta_3 == "a":
    print("\nIncorrecto", nombre, ",\nla respuesta es la opción b.\n")
    puntaje = puntaje - 2
  elif respuesta_3 == "c":
    print("\nIncorrecto", nombre, ",\nla respuesta es la opción b.\n")
    puntaje = puntaje - 2
  else:
    puntaje += 10
    print("\nCorrecto", nombre, "!\n")
    
    print (MAGENTA+nombre, "llevas",puntaje,"puntos"+RESET)

    time.sleep(3)
  # Pregunta Secreta
  print ("\nPregunta Secreta: En caso respondas la siguiente pregunta, tu puntaje se multiplica por 10.\n")
  print (BLUE+"Escribe el nombre del río más largo del Perú:  "+RESET)
  
  respuesta_4 = input(BLUE+"\nTu respuesta: "+RESET).lower()
   
  if respuesta_4 == "Ucayali":
    print("Correcto", nombre,".Ganaste!")
    puntaje = puntaje*10
  else:
    puntaje = puntaje
    print("\nIncorrecto", nombre, ".\nLa respuesta es Ucayali.\n")

  time.sleep(4)
  #Resultados
  print (MAGENTA+"\nHora de tus resultados"+RESET)
  print(BLUE+"\nTu puntaje es de",puntaje, "puntos"+RESET)
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":  # != significa "distinto"
   print("\nEspero",nombre,"que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False
