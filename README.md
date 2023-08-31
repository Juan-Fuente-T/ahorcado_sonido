# ahorcado_sonido

# Juego del Ahorcado

Este es un juego del ahorcado desarrollado en python. El juego presenta gráficos sencillos de pixel art y efectos de sonido para brindar una experiencia divertida y nostálgica.

## Capturas de pantalla
![CapturaAhorcado1](https://github.com/Juan-Fuente-T/ahorcado_sonido/assets/127140423/a9976a1b-84d9-41af-86d0-69550db7fe5d)

![CapturaAhorcado2](https://github.com/Juan-Fuente-T/ahorcado_sonido/assets/127140423/daf7038e-4b92-4946-944f-9fa2490ff954)

![CapturaAhorcado3](https://github.com/Juan-Fuente-T/ahorcado_sonido/assets/127140423/53290b0b-f89f-4f3a-8cab-a129e9e5d495)




## Instalación

1. Clona este repositorio en tu máquina local:
git clone https://github.com/tu-usuario/ahorcado_sonido.git

2.Activa tus altavoces. 

3.Abre el archivo con ti IDE favorido, por ejemplo VSCode y haz correr el programa. Si lo haces con VSCode puedes hacerlo con Ctrl + F5. 

## Características

- Gráficos sencillos de pixel art que le dan un toque retro al juego y te ayudan a saber cuantos fallos te restan.
- Efectos de sonido para una experiencia más inmersiva.
- Muchas palabras para adivinar.

## Mecánica y reglas del juego:
1. A partir de una Lista de Palabras el ordenador escoge una al azar.
2. De la palabra_escogida el ordenador escoge una letra al azar.
3. Se imprime la palabra a adivinar en forma de una cadena de guiones bajos donde
    solo se muestra uno de los caracteres a modo de pista, pudiendo ese mismo caracter repetirse aunque no se haya mostrado más que una vez.
4. El jugador debe ir proponiendo letras para completar la palabra.
    4a. Para cada letra que exista en la palabra el ordenador revela todas las
        posiciones en las que aparece.
    4b. Por cada error se va completando la figura del ahorcado.
5. El juego termina cuando el jugador acierta todas las letras faltantes antes que
    quede ahorcado o, cuando comete seis errores en cuyo caso queda ahorcado y pierde.
   

## Contribución

¡Todas las contribuciones son bienvenidas! Si deseas mejorar este juego del ahorcado, puedes seguir los siguientes pasos:

1. Haz un fork de este repositorio.
2. Crea una rama nueva para tu contribución:
git checkout -b feature/nueva-funcionalidad

3. Realiza los cambios y mejoras en tu rama.
4. Realiza commits descriptivos de tus cambios:
git commit -m "Agrega nueva funcionalidad"

5. Haz push de tu rama a tu repositorio remoto:
git push origin feature/nueva-funcionalidad

6. Abre un pull request en este repositorio para que podamos revisar tus cambios.

## Licencia

Este proyecto está bajo la Licencia © Copyleft Juan Fuente · 2023. 
