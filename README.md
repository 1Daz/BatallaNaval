# Batalla Naval (Consola - Un Jugador vs. Computadora)

Este proyecto implementa una versión simplificada del clásico juego de estrategia "Batalla Naval" para un solo jugador contra la computadora. El juego se ejecuta en la consola y ofrece una experiencia interactiva basada en texto.

## Descripción del Problema

El desafío principal consiste en trasladar la experiencia física del juego a un entorno digital interactivo mediante programación en Python.

## Funcionalidades

* **Tablero visual:** Representación del tablero de juego en la consola, utilizando los siguientes símbolos:
    * `(~)` Agua
    * `(X)` Impacto
    * `(*)` Hundido
* **Barcos de la computadora:** La computadora genera aleatoriamente una colección de barcos de tamaños 1, 2 y 3 celdas, cuya longitud total está entre 6 y 9 celdas.
* **Entrada de coordenadas por el usuario:** El jugador introduce las coordenadas (fila y columna) para intentar impactar los barcos de la computadora.
* **Retroalimentación:** El juego proporciona mensajes al usuario sobre sus intentos:
    * "¡Agua!" para disparos fallidos.
    * "¡Impacto!" cuando se golpea una parte de un barco.
    * "¡Hundiste un barco!" cuando un barco completo es hundido.
* **Victoria:** El jugador gana cuando todos los barcos de la computadora han sido hundidos. El juego muestra el número de intentos realizados al ganar.
* **Tablero revelado (para pruebas):** Una función opcional para mostrar la ubicación de los barcos de la computadora en el tablero, marcados con su tamaño ('1', '2', '3').

## Lenguaje Utilizado

* Python

## Justificación del Lenguaje

* **Sintaxis clara y legible:** Facilita el aprendizaje y la implementación para principiantes.
* **Facilidad para implementar estructuras de datos:** Las listas son ideales para representar el tablero.
* **Módulo `random`:** Útil para la generación aleatoria de la ubicación de los barcos.
* **Rapidez de desarrollo:** Permite crear un prototipo funcional rápidamente.

## Alcance del Proyecto

* Juego funcional en consola.
* Múltiples tipos de barcos (de 1, 2 y 3 celdas).
* Tablero de tamaño fijo (5x5).
* Turnos ilimitados hasta ganar.
* Generación aleatoria de la configuración de los barcos dentro de un rango de tamaño total.

## Cómo Ejecutar el Juego

1.  Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [https://www.python.org/downloads/](https://www.python.org/downloads/).
2.  Guarda los archivos del proyecto en la estructura de carpetas mencionada.
3.  Abre una terminal o símbolo del sistema.
4.  Navega hasta la carpeta `batalla_naval` (la que contiene `main.py`).
5.  Ejecuta el juego con el comando:
    ```bash
    python main.py
    ```

## Créditos

Este juego fue desarrollado como un proyecto de aprendizaje de programación en Python por Alejandra Barreto, Juan Sebastián Taborda y Jhofran Daza.

---
