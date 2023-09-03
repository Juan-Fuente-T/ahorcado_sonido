# *** J U E G O  D E L  A H O R C A D O :: Version 0.2.0 ***

# © Copyleft Juan Fuente · 2023

"""
Esta aplicación multiplataforma (Windows, Linux, Mac) ofrece la posibilidad de
juagar al Ahorcado.

Mecánica y reglas del juego:
1. A partir de una Lista de Palabras el ordenador escoge una al azar.
2. De la palabra_escogida el ordenador escoge una letra al azar.
3. Se imprime la palabra a adivinar en forma de una cadena de guiones bajos donde
    solo se muestra(n) a modo de pista la(s) posicion(es) que ocupa la letra revelada.
4. El jugador debe ir proponiendo letras para completar la palabra.
    4a. Para cada letra que exista en la palabra el ordenador revela todas las
        posiciones en las que aparece.
    4b. Por cada error se va completando la figura del ahorcado.
5. El juego termina cuando el jugador acierta todas las letras faltantes antes que
    quede ahorcado o, cuando comete seis errores en cuyo caso queda ahorcado y pierde.
    

Novedades de la versión 0.2.0
-Incorporación de sonidos que acompañan al juego: Inicio, error en la introduccion de letras, fallos, derrota y victoria.
-Correccion de un bug con el numero de impresiones a la hora de mostrar las letras que se decubre el usuario 
"""
#IMPORTACIONES
import random #se importa random para generar numeros aleatorios
import pygame #se importa pygame para reproducir sonido en multiplataforma

#LISTA DE FUNCIONES

#FUNCIONES

#Funcion para 
def obtener_letras (lista_palabras):
    palabra_escondida=lista_palabras[random.randint(0, len(lista_palabras)-1)]
    letras_palabra = list(palabra_escondida)
    return letras_palabra, palabra_escondida


#LA FUNCION cambiar_letras TOMA LA LISTA letras_palabra Y LE HACE UNA COPIA A LA QUE LE CAMBIA CADA UNO DE SUS CARACTERES POR UN GUION BAJO.
def cambiar_letras (letras_palabra):
    letras_palabra_escondida = letras_palabra[:]
    for i in range(len(letras_palabra_escondida)):
        letras_palabra_escondida[i] = "_"
    return letras_palabra_escondida

print("El PASO 5 es hacer visible uno de esos caracteres transformados para usarlo como pista de cara al usuario. Se utiliza la función cambiar_letras.")
def descubrir_letra(letras_palabra, letras_palabra_escondida):
    indice_aleatorio = random.randint(0, len(letras_palabra_escondida)-1)
    letras_palabra_escondida[indice_aleatorio] = letras_palabra[indice_aleatorio]     
    return letras_palabra_escondida

"""def comprobar_letras(letras_palabra, letras_palabra_escondida, dibujo_ahorcado):
    print ("La funcion comprobar_letras realiza una copia de la lista de caracteres y los transforma en guiones bajos") 
    palabra_descubierta = False
    contador = 0
    while not palabra_descubierta:
        print()
        letra_elegida = input("Elige una letra: ") 
        for i in range(len(letras_palabra)):
            if letra_elegida == letras_palabra[i]:
            #if letra_elegida in letras_palabra:
                #indice = letras_palabra.index(letra_elegida)
                letras_palabra_escondida[i] = letra_elegida
                print()
                print("¡Muy bien! Letra incluida, continua.")
                print()
                print("La palabra es ", letras_palabra_escondida)
                if not "_" in letras_palabra_escondida:
                     palabra_descubierta = True
                     break
            
            else:
                print()
                print("¡Mala suerte!Letra no incluida.")
                print()
                contador += 1
                print(dibujo_ahorcado[contador])
                print()
                print("¡Cuidado! Te quedan", 6-contador, "fallos.")
                print()
                print("La palabra es ", letras_palabra_escondida)
        return palabra_descubierta"""

def mostrar_error(contador):
        print()
        print("¡Mala suerte!Letra no incluida.")
        print()
        if contador < 5:
            print(dibujo_ahorcado[contador+1])
            print()
        palabra_descubierta = False
        pygame.mixer.music.load("pacman-dies.mp3")  # cargar archivo de sonido de victoria
        pygame.mixer.music.play()  # reproducir el sonido
        # Esperar hasta que el sonido termine de reproducirse
        while pygame.mixer.music.get_busy():
            continue
        if contador < 5:
            print("¡Cuidado! Te quedan", 5-contador, "fallos.")
            print()
        print("La palabra es ", letras_palabra_escondida)
        if contador == 5:
            print()
            print("""                   GAME OVER""")
            print()
            print(dibujo_ahorcado[contador+1])
            print()
            pygame.mixer.music.load("derrota.mp3")  # cargar archivo de sonido de victoria
            pygame.mixer.music.play()  # reproducir el sonido
            # Esperar hasta que el sonido termine de reproducirse
            while pygame.mixer.music.get_busy():
                continue
            print("Lo siento, la palabra era", (palabra_escondida).upper())
            print()
            palabra_descubierta = True
            return palabra_descubierta
             
def examinar_letras():
    contador = 0
    palabra_descubierta = False
    letras_seleccionadas = []
    while not palabra_descubierta:
        print()
        letra_elegida = input("Elige una letra: ").lower() 
        if letra_elegida not in letras_seleccionadas:
            if letra_elegida in letras_palabra:
                if letra_elegida not in letras_palabra_escondida:
                    letras_seleccionadas.insert(0, letra_elegida)
                    palabra_descubierta = revelar_letra(letra_elegida)
                else:
                    print()
                    print("Esa letra ya estaba descubierta.")
                    pygame.mixer.music.load("mario-bros-die.mp3")  # cargar archivo de sonido de victoria
                    pygame.mixer.music.play()  # reproducir el sonido
                    # Esperar hasta que el sonido termine de reproducirse
                    while pygame.mixer.music.get_busy():
                        continue
            else:
                if len(letra_elegida) > 1 or not letra_elegida.isalpha():
                        print()
                        print("No has introducido una letra.")
                        pygame.mixer.music.load("mario-bros-die.mp3")  # cargar archivo de sonido de victoria
                        pygame.mixer.music.play()  # reproducir el sonido
                        # Esperar hasta que el sonido termine de reproducirse
                        while pygame.mixer.music.get_busy():
                            continue
                else:
                    palabra_descubierta = mostrar_error(contador)
                    contador += 1
                    letras_seleccionadas.insert(0, letra_elegida)
        else:
            print()
            print("Esa letra ya la habías elegido.")
            print()
            pygame.mixer.music.load("mario-bros-die.mp3")  # cargar archivo de sonido de victoria
            pygame.mixer.music.play()  # reproducir el sonido
            # Esperar hasta que el sonido termine de reproducirse
            while pygame.mixer.music.get_busy():
                continue
    return letra_elegida, contador, palabra_descubierta

def revelar_letra(letra_elegida):
    for i in range(len(letras_palabra)):
            if letra_elegida == letras_palabra[i]:
                letras_palabra_escondida[i] = letra_elegida
                print()
                print("¡Muy bien! Letra incluida, continua.")
                print()
                pygame.mixer.music.load("mario-bros-yes.mp3")  # cargar archivo de sonido de victoria
                pygame.mixer.music.play()  # reproducir el sonido
                # Esperar hasta que el sonido termine de reproducirse
                while pygame.mixer.music.get_busy():
                    continue
                print("La palabra es ", letras_palabra_escondida)
                print()
    if not "_" in letras_palabra_escondida:
        palabra_descubierta = True
        return palabra_descubierta 
                     
def mostrar_victoria(palabra_descubierta, palabra_escondida, contador):
    if palabra_descubierta and contador < 5:
        print(""" ¡¡¡VICTORIA!!!

               ¡HAS DESCUBIERTO LA PALABRA!! """)
        print()
        print("La palabra es", (palabra_escondida).upper())
        print()
        pygame.mixer.music.load("sfx-victory6.mp3")  # cargar archivo de sonido de victoria
        pygame.mixer.music.play()  # reproducir el sonido
        # Esperar hasta que el sonido termine de reproducirse
        while pygame.mixer.music.get_busy():
            continue
        palabra_descubierta = True
        return palabra_descubierta
        


def comprobar_nueva_partida(palabra_descubierta):
    if palabra_descubierta:
        comprobar_cierre = False #variable que controla el bucle, en false para iniciarlo
        #bucle para comprobar los meses en que quiere realizar el prestamo
        while not comprobar_cierre:
            nueva_partida = (input("¿Quieres jugar otra partida S/n Teclea s ó n: ")).lower() #input para solicitar una posible nueva operacion o salida del programa forzado a minusculas
            if nueva_partida == "n": #si la opcion elegida es no (n) se cierra el programa
                print()
                print("Espero que hayas disfrutado del ahorcado. Hasta pronto.") #impresion de despedida
                print()
                comprobar_cierre = True #se cambia el valor de la variable para salir del bucle
        
            elif nueva_partida != 's' and nueva_partida != 'n':
            #se necesita que el usuario introduzca solo "n" o "s", por lo tanto el siguiente mensaje se imprimirá mientras no lo sean            
                    print()
                    print("No has introducido una letra válida.") #impresion para solicitar posible nueva operacion si en la primera ocasion que se solicito no introdujo "n" o "s"
                    print()
                    comprobar_cierre = False #se cambia el valor de la variable para salir del bucle
            else:
                return nueva_partida #se devuelve el valor

      



#SE CREA UNA LISTA CON LOS GRAFICOS A MOSTRAR EN CASO DE ERROR DEL JUGADOR. PARA LOCALIZAR LA IMPReSION CORRESPONDIENTE SE UTILIZA contador COMO INDICE.

dibujo_ahorcado=["""
            _____
            |    |
            |    
            |   
            |    
            |   
            |
            |
        ----+--------
                 ""","""
            _____
            |    |
            |    O
            |   
            |    
            |   
            |
            |
        ----+--------
                 ""","""
            _____
            |    |
            |    O
            |    |
            |    |
            |   
            |
            |
        ----+--------
                 ""","""
            _____
            |    |
            |    O
            |   /|
            |    |
            |   
            |
            |
        ----+--------
                 ""","""
            _____
            |    |
            |    O
            |   /|\\
            |    |
            |   
            |
            |
        ----+--------
                 ""","""
            _____
            |    |
            |    O
            |   /|\\
            |    |
            |   / 
            |
            |
        ----+--------
                 ""","""
            _____
            |    |
            |    O
            |   /|\\
            |    |
            |   / \\
            |
            |
        ----+--------
                 """]
                          ## ////////////////////// ##
                          ## MOTOR DE LA APLICACION ##
                          ## ////////////////////// ##

#SE INICIA LA INTERFAZ GRAFICA, SE REALIZA LA IMPRESION DE BIENVENIDA Y SE MUESTRAN LAS INSTRUCCIONES
pygame.init()

print("""¡Bienvenido al juego del ahorcado! 

         Intenta adivinar la palabra oculta, 
    pero ten cuidado, ya que solo dispones de 6 fallos.
         Te muestro una letra como pista.    
         """)

#SE MUESTRA LA PALABRA ESCONDIDA CON UNO DE SUS CARACTERES DESCUBIERTOS COMO PISTA

lista_palabras  = ["turbio", "decidido","decision", "curandero", "cabeza", "cabra", "cable", "cadera","cafeina", "cajon", "calambre", "calamar", "calcio", "calculo", "calidad", "caliente", "caldero", "caluroso", "calzado", "camerino", "camaleon", "camarero", "camarote", "cambio", "camelia", "camion", "campamento", "campana", "campeonato", "canario", "canela", "camilla", "calabaza", "cantidad", "cancion", "cantautor", "cantimplora", "cantero", "serpiente", "capitan", "capital", "capucha", "caramelo", "caravana", "carbon", "carcajada", "cartero", "carton", "caseta", "casado", "campestre", "casino", "conquistador", "costilla", "castillo", "catapulta", "camisa", "catolico", "cautivador", "cautivo", "cavidad", "torpedo","cazador", "cazar", "cazuela", "cebadura", "cebolla", "cecina", "ceder", "cedula", "cegar", "celebracion", "cementerio", "cenizas", "centavo", "centro", "cepillo", "cerrado", "espacio", "cesped", "chaleco", "champu", "chicle", "chiflado", "chimpance", "paraguas", "espada", "hermano", "bisagra", "chispa", "chocolate", "desastre", "circulo", "ciruela", "bicicleta", "claroscuro", "martillo", "clima", "coagulo", "cobertizo", "cobra", "coccion","vacante", "elefante", "gorro", "saco","baloncesto", "barato", "barbilla", "barniz", "basura", "batalla", "bebida", "biblioteca", "bienestar", "billar", "blanco", "bloque", "bobina", "boda", "bodega", "bombilla", "botella", "sigilo","sargento","sangre","bravo","parrilla", "cerrar", "torre", "guitarra","rebanada", "receta", "rechazo", "recoger", "recto", "reducir", "reformar", "regalo", "regular", "reina", "relieve", "remolacha"]
#lista_palabras = ["turbio", "decidido"]

nueva_partida = "s"
while nueva_partida == "s":
    
    letras_palabra, palabra_escondida = obtener_letras(lista_palabras)

    letras_palabra_escondida = cambiar_letras(letras_palabra)

    letras_palabra_escondida = descubrir_letra(letras_palabra, letras_palabra_escondida)
    
    pygame.mixer.music.load("kart-start-mario.mp3")  # cargar archivo de sonido de victoria
    pygame.mixer.music.play()  # reproducir el sonido
    # Esperar hasta que el sonido termine de reproducirse
    while pygame.mixer.music.get_busy():
        continue

    print("La palabra es ", letras_palabra_escondida)

    letra_elegida, contador, palabra_descubierta  = examinar_letras()

    mostrar_victoria(palabra_descubierta, palabra_escondida, contador)
        
    nueva_partida = comprobar_nueva_partida(palabra_descubierta)

pygame.quit()

#SE SOLICITA UNA LETRA AL JUGADOR A TRAVÉS DE UN INPUT FORZADO A MINUSCULAS Y SE ASOCIA A UNA VARIABLE.DENTRO DE LA FUNCION comprobar_letras



# SE EVALUA SI LA LETRA DEL JUGADOR ESTA DENTRO DE LA PALABRA ESCONDIDA. ESTO DENTRO 
#DE LA FUNCION comprobar_letras QUE DEVUELVE LA VARIABLE palabra_descubierta (True O False). DENTRO DE LA FUNCION comprobar_letras().


#PASO 12: TANTO SI LA LETRA ESTA EN LA PALABRA SOMO SI NO LO ESTA SE LE COMUNICA AL JUGADOR Y SE MUESTRA UN PRINT CON ESAS O ESAS LETRAS DESCUBIERTAS.
#O EN CASO DE ERROR SE LE MUESTRA LA IMAGEN CORRESPONDIENTE E LA LISTA DE DIBUJOS DEL AHORCADO Y SE LE MUESTRA EL NUMERO DE ERRORES RESTANTES. SE ACTUALIZA EL CONTADOR.
#SI ES POSIBLE SE EMITE SONIDO DE ERROR. DENTRO DE LA FUNCION comprobar_letras().


#LA FUNCION comprobar_letras PIDE UNA LETRA AL USUARIO Y EVALUA SI ES ACERTADA. SI LO ES LA MUESTRA CAMBIANDOLA POR UNO DE LOS GUIONES BAJOS.


#PASO 13: SE COMPRUEBA SI QUEDA ALGUNA LETRA AUN POR DESCUBRIR. EN CASO CONTRARIO SE MUESTRA IMAGEN O SONIDO ESPECIAL.

# PASO 14: SE CONSULTA SI DESEA JUGAR UNA NUEVA PARTIDA. CON LA FUNCION comprobar_nueva_partida()


#FUNCION comprobar_nueva_partida(), CONSULTA AL USUARIO SI DESEA JUGAR DE NUEVO O SALIR DE LA APLICACION


            
