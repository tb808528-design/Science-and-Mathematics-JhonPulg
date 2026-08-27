TEOREMA DE JHON PULGARIN 
Tratado sobre la Discontinuidad Espacial y el Cero

Autor: Jhon Pulgarin
Villavicencio, Meta - Colombia
27 Agosto 2026

                                            Teorema de Jhon Pulgarín
                        Tratado sobre la Discontinuidad Espacial y el Cero Arquitectónico

1. Introducción y Contexto Histórico: Un Problema de Siglos
La contradicción entre el conteo abstracto y la realidad física no es una confusión moderna. Es un dilema
lógico con siglos de historia que afecta la forma en que los seres humanos organizamos el tiempo, el
espacio y la información. El origen principal de este conflicto radica en la dificultad histórica para aceptar
e integrar el concepto del 'cero' como una entidad física y no solo matemática.
El ejemplo más claro de esto se encuentra en nuestro calendario actual. El sistema cronológico pasa
directamente del año 1 antes de Cristo (a.C.) al año 1 después de Cristo (d.C.). Físicamente, el 'año cero'
nunca existió en la historia oficial. Esto genera que, al calcular el tiempo transcurrido entre el año 1 a.C. y
el año 1 d.C., la matemática pura dicte una distancia de 2 unidades, cuando en la línea de tiempo real
solo hay un cambio de era sin ningún año de por medio.

2. La Discrepancia Lógica: Matemáticos vs. Programadores
Este desfase histórico ha provocado un debate clásico en el mundo de la ciencia y la tecnología,
dividiendo la lógica en dos bandos bien definidos:
• El Enfoque Matemático Puro: Los matemáticos operan bajo una recta numérica continua donde el
cero es indispensable. Para la matemática abstracta, el cero representa el punto de origen o de equilibrio.
Al ignorar si el cero tiene una representación física real, sus cálculos siempre asumen un espacio
intermedio que incrementa artificialmente las distancias físicas.
• El Enfoque de la Programación e Ingeniería: Los desarrolladores de software y los ingenieros chocan
constantemente con esto mediante el famoso 'Error del Poste de Cerca' (Fencepost Error) o los
problemas de indexación base cero (donde las listas empiezan en 0 y no en 1). Un programador sabe que
una cosa es la cantidad de elementos intermedios y otra muy distinta es el índice de las posiciones,
requiriendo ajustes constantes en el código para que las aplicaciones no fallen al interactuar con el
mundo real.

3. El Caso de Estudio: El Dilema del Ascensor
La Teoría de Jhon Pulgarín nace de la observación directa de este fenómeno en la arquitectura cotidiana:
Una persona vive en la planta 2 y su plaza de garaje está en el sótano 1. ¿Cuántas plantas separan
su vivienda de su plaza?
Si se introduce este problema de forma lineal en una Inteligencia Artificial o un sistema matemático
teórico, el cálculo matemático estricto establece que la distancia es 3 (calculando 2 - (-1) = 3). Sin
embargo, en la vida real, los botones del ascensor de ese edificio muestran que al bajar del piso 2 se



                                    FORMULA OFICIAL

O = |indice(A) - indice(B)| - 1


Donde:
- O = Cantidad de cosas que hay EN MEDIO de A y B, sin contar a A ni a B.
- indice(A) = Posicion del primer elemento
- indice(B) = Posicion del segundo elemento
- | | = Valor absoluto
- -1 = Porque al restar índices cuentas un extremo, menos uno lo corrige todo

ESTA ES LA FORMULA QUE REEMPLAZA A TODAS LAS ANTERIORES.

3. ENUNCIADO FORMAL DEL TEOREMA

Dadas dos posiciones distintas A y B con indices
indice(A) e indice(B), el numero de elementos
estrictamente intermedios entre ellas es igual a:

O = |indice(A) - indice(B)| - 1

4. DEMOSTRACION (QED)

1. La distancia absoluta entre indices es:
   D = |indice(A) - indice(B)|

2. D incluye la distancia desde A hasta B inclusive.

3. Para contar SOLO el interior, debemos excluir
   los extremos A y B. Restamos 1.

4. Queda: O = D - 1 = |indice(A) - indice(B)| - 1

5. QED - Quod Erat Demonstrandum (como se queria demostrar)

Propiedades demostradas:
- Si A y B son consecutivos: O = 0
- Si A = B: O = -1 (intervalo vacio por definicion)
- O >= 0 para posiciones distintas no consecutivas
- Simetrico: O(A,B) = O(B,A) gracias al valor absoluto
- Funciona en cualquier orden

5. EJEMPLOS COMPLETOS

1. PROBLEMA DE ACENSOR P2 A S1:
Un ascensor está en el piso 2 y debe bajar hasta el S1 (Sótano 1). Se requiere saber cuántos pisos lo separan, sin contar el piso de origen ni el de destino.2. Datos:
Piso A (origen) = 2 → índice 2
Piso B (destino) = S1 → índice -1
 Fórmula y desarrollo:Primero hallamos la distancia total D:
D = |índice(A) - índice(B)|
D = |2 - (-1)|
D = |3|
D = 3 #Ahora hallamos los pisos intermedios O:
O = D - 1
O = 3 - 1
O = 2
  Respuesta: Lo separan 2 pisos intermedios, que son el Piso 1 y la Planta Baja.

2.PROBLEMA DE LOS POTES1. Enunciado del problema:
Hay 5 potes en fila numerados del 1 al 5. El pote 1 y el pote 5 son los extremos. Se requiere saber cuántos potes hay entre ellos, sin contar el origen ni el destino.2. Datos:
Pote A (origen) = 1 → índice 1
Pote B (destino) = 5 → índice 53. Fórmula y desarrollo:
D = |índice(A) - índice(B)|
D = |1 - 5|
D = |-4|
D = 4O = D - 1
O = 4 - 1
O = 34. Respuesta: Los separan 3 potes intermedios, que son el 2, 3 y 4.2. PROBLEMA DE LOS AÑOS 1 a.C. y 1 d.C.1. Enunciado del problema:
3. PROBLEMA DE LAS ERAS:Se quiere saber cuántos años completos hay entre el año 1 a.C. y el año 1 d.C., sin contar el año de origen ni el de destino.2. Datos:
Año A = 1 a.C. → índice -1
Año B = 1 d.C. → índice 13. Fórmula y desarrollo:
D = |índice(A) - índice(B)|
D = |-1 - 1|
D = |-2|
D = 2O = D - 1
O = 2 - 1
Respuesta: Los separan 1 año intermedio, que sería el año 0. Como en la historia no existe el año 0, en la realidad O = 0

(Script de los problemas en Python)
def intermedios(A, B):
    D = abs(A - B)
    O = D - 1
    return D, O

# 1. ASCENSOR: Piso 2 al S1
D1, O1 = intermedios(2, -1)
print(f"Ascensor 2 al S1 -> D={D1}, O={O1}")

# 2. POTES: Pote 1 al 5
D2, O2 = intermedios(1, 5)
print(f"Potes 1 al 5 -> D={D2}, O={O2}")

# 3. AÑOS: 1 a.C. (-1) al 1 d.C. (1)
D3, O3 = intermedios(-1, 1)
print(f"Años -1 al 1 -> D={D3}, O={O3} (año 0 no existe, real O=0)")

6. APLICACIONES DEL TEOREMA

1. Estructuras de datos y Arrays
2. Listas enlazadas y Listas y arrays
3. Teoria de intervalos abiertos y conjuntos
4. Conteo combinatorio y Analisis de secuencias
5. Programacion (soluciona Fencepost Error)
6. Organizacion de tiempo y espacio

7. CONCLUSION FINAL

Conclusión Final:
El Teorema de Pulgarin es altamente útil porque transforma un problema de conteo visual, que suele generar confusión y errores, en una fórmula matemática exacta y universal (O = D - 1). Su aplicabilidad es escalable, funciona igual para contar potes, como para calcular los niveles intermedios de un edificio de 100 pisos.Además, demuestra ser una herramienta fundamental y transversal, utilizada por ingenieros civiles, arquitectos y programadores como base lógica para optimizar cálculos estructurales y para programar sistemas automatizados como el recorrido de un ascensor.



Jhon Pulgarin - 2026
Villavicencio, Meta - Colombia
