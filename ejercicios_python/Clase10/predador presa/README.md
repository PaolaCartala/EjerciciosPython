# Ejercicio: Predador Presa

[![Gitter](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)](https://www.python.org/)

## Probando el modelo completo
Descargar los archivos de esta carpeta y correr el archivo mundo.py que tiene una instancia de Mundo que corre varias veces el mundo con una pausa de tiempo.

## Clases del modelo inicial
El modelo inicial tiene definidas la clase Animal de la que heredan dos nuevas clases: León y Antílope. También tiene definida una clase Tablero. Todas estas clases se integran en una clase Mundo.

## Descripción
Los modelos de depredación y competencia forman parte de la batería de herramientas clásicas del ecólogo. Vito Volterra en Italia y Alfred Lotka en Estados Unidos fueron los precursores en este tema y crearon modelos que, con diversas modificaciones y mejoras, seguimos usando hoy en día. El modelo de Volterra para depredación comienza suponiendo la existencia de dos poblaciones de animales, una de las cuales (el depredador) se alimenta de la otra (la presa). Se supone que las dos poblaciones están formadas por individuos idénticos, mezclados en el espacio.

La gran mayoría de los modelos usualmente estudiados tienen solamente en cuenta la dinámica temporal, desatendiendo la dinámica espacial. Con la excusa de implementar una versión espacio-temporal de este modelo, proponemos un ejercicio guiado que usa fuertemente programación orientada a objetos.

La idea es recrear un mundo que imaginaremos como un valle rodeado de montañas en el que existen depredadores (que llamaremos Leones) y presas (que llamaremos Antílopes). Este valle será bidimensional, y lo representaremos por medio de una grilla rectangular que llamaremos tablero.

El modelo inicial con el que trabajaremos tiene definidas 4 etapas que determinan un ciclo:

* Etapa de movimiento: en esta etapa cada animal se desplaza a alguna posición vecina desocupada (si es que existe, sino permanece en el lugar). La decisión de a cuál desplazarse será responsabilidad del animal, que, sabiendo las disponibles, elegirá una al azar.

* Etapa de alimentación: en esta etapa los animales se alimentan. Los antílopes comerán pasto en su lugar, mientras que los leones buscarán un antílope en las posiciones vecinas y, de existir, se lo comerán. Esta acción de un león se verá reflejada en el tablero con su desplazamiento a la posición del antílope, el cual ya no será más parte de nuestro mundo.

* Etapa de reproducción: cada animal buscará en sus posiciones vecinas alguien de su misma especie. Si lo encuentra y además hay una posición vacía en el tablero se incluirá un nuevo animal (de la misma especie) en el tablero. Nuevamente la elección de la pareja y del lugar del nuevo animal serán aleatorias. Este modelo inicial no prevee el atributo sexo, ni un límite entre la cantidad reproducciones en las que puede participar un animal por etapa.

* Cierre de ciclo: en la última etapa de un ciclo todos los animales "envejecen" en 1 unidad, aquellos que se reprodujeron y siguen en edad reproductiva vuelven a ser fértiles. Si alguno alcanzó la edad máxima de su especie se considera que ya puede retirárselo del mundo (es decir, se muere). Sucede lo mismo si, al pasar una etapa, alcanza el límite de etapas sin alimentarse, en cuyo caso muere de hambre.

## Contribuciones

Este repositorio está abierto a contribuciones, no dudes en hacerlo!

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)