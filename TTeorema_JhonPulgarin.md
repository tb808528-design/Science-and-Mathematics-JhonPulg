# Teorema de Jhon Pulgarin - Discontinuidad Espacial

**Tratado sobre la Discontinuidad Espacial y el Cero Arquitectónico**

---

### 1. INTRODUCCIÓN HISTÓRICA

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


### 2. CASO DE ESTUDIO: EL ASCENSOR
El Caso de Estudio: El Dilema del Ascensor caso por que Jhon Pulgarin hallo el problema con 0
La Teoría de Jhon Pulgarín nace de la observación directa de este fenómeno en la arquitectura cotidiana:
Una persona vive en la planta 2 y su plaza de garaje está en el sótano 1. ¿Cuántas plantas separan
su vivienda de su plaza?
Si se introduce este problema de forma lineal en una Inteligencia Artificial o un sistema matemático
teórico, el cálculo matemático estricto establece que la distancia es 3 (calculando 2 - (-1) = 3). Sin
embargo, en la vida real, los botones del ascensor de ese edificio muestran que al bajar del piso 2 al sotana 1 son 
solo 2 botones
                     FORMULA OFICIAL

O = |indice(A) - indice(B)| - 1


Donde:
- O = Cantidad de cosas que hay EN MEDIO de A y B, sin contar a A ni a B.
- indice(A) = Posicion del primer elemento
- indice(B) = Posicion del segundo elemento
- | | = Valor absoluto
- -1 = Porque al restar índices cuentas un extremo, menos uno lo corrige todo

### 3. ENUNCIADO DEL TEOREMA

Dadas dos posiciones distintas A y B con indices
indice(A) e indice(B), el numero de elementos
estrictamente intermedios entre ellas es igual a:

O = |indice(A) - indice(B)| - 1

Donde O son los espacios vacíos o intermedios entre A y B.

### 4. DEMOSTRACIÓN FORMAL (QED)

1. La distancia absoluta entre indices es:
   D = |indice(A) - indice(B)|

2. D incluye la distancia desde A hasta B inclusive.

3. Para contar SOLO el interior, debemos excluir
   los extremos A y B. Restamos 1.

4. Queda: O = D - 1 = |indice(A) - indice(B)| - 1



### 5. QED - Quod Erat Demonstrandum (como se queria demostrar)
Propiedades demostradas:
- Si A y B son consecutivos: O = 0
- Si A = B: O = -1 (intervalo vacio por definicion)
- O >= 0 para posiciones distintas no consecutivas
- Simetrico: O(A,B) = O(B,A) gracias al valor absoluto
- Funciona en cualquier orden.

## 6. EJEMPLOS COMPLETOS

### Problema del Ascensor (Piso 2 a S1)
Un ascensor está en el piso 2 y debe bajar hasta el S1 (Sótano 1). Se requiere saber cuántos pisos lo separan, sin contar el piso de origen ni el de destino.

### Datos
* **Piso A (origen):** 2 → índice $2$
* **Piso B (destino):** S1 → índice $-1$

### Fórmula y desarrollo
Primero hallamos la distancia total ($D$):
$$D = |\text{índice}(A) - \text{índice}(B)|$$
$$D = |2 - (-1)|$$
$$D = |3| = 3$$

Ahora hallamos los pisos intermedios ($O$):
$$O = D - 1$$
$$O = 3 - 1 = 2$$

### Respuesta
Lo separan **2 pisos intermedios**, que son el **Piso 1** y la **Planta Baja**.

---

## 2. Problema de los Potes

### Enunciado del problema
Hay 5 potes en fila numerados del 1 al 5. El pote 1 y el pote 5 son los extremos. Se requiere saber cuántos potes hay entre ellos, sin contar el origen ni el destino.

### Datos
* **Pote A (origen):** 1 → índice $1$
* **Pote B (destino):** 5 → índice $5$

### Fórmula y desarrollo
Primero hallamos la distancia total ($D$):
$$D = |\text{índice}(A) - \text{índice}(B)|$$
$$D = |1 - 5|$$
$$D = |-4| = 4$$

Ahora hallamos los potes intermedios ($O$):
$$O = D - 1$$
$$O = 4 - 1 = 3$$

### Respuesta
Los separan **3 potes intermedios**, que son el **2, 3 y 4**.

---

## 3. Problema de las Eras (1 a.C. y 1 d.C.)

### Enunciado del problema
Se quiere saber cuántos años completos hay entre el año 1 a.C. y el año 1 d.C., sin contar el año de origen ni el de destino.

### Datos
* **Año A (origen):** 1 a.C. → índice $-1$
* **Año B (destino):** 1 d.C. → índice $1$

### Fórmula y desarrollo
Primero hallamos la distancia total teórica ($D$):
$$D = |\text{índice}(A) - \text{índice}(B)|$$
$$D = |-1 - 1|$$
$$D = |-2| = 2$$

Ahora hallamos los años intermedios aplicando la fórmula estándar ($O$):
$$O = D - 1$$
$$O = 2 - 1 = 1$$

### Ajuste Histórico Real
La fórmula matemática arroja un resultado teórico de 1 año intermedio (que correspondería al año 0). Sin embargo, en el registro histórico y cronológico cristiano **no existe el año 0**. El año 1 d.C. sigue inmediatamente al año 1 a.C.

Por lo tanto, en la realidad histórica:
$$O = 0$$

### Respuesta
En la realidad cronológica, **0 años completos** separan el año 1 a.C. del 1 d.C.

### SCRIPT EN PYTHON

```python
def intermedios(A, B):
    D = abs(A - B)
    O = D - 1
    return D, O

# Ejemplo Ascensor
D1, O1 = intermedios(-2, -1)
print(f"P2 a S1 -> D={D1}, O={O1}")

# Ejemplo Potes
D2, O2 = intermedios(1, 5)
print(f"Potes 1 a 5 -> D={D2}, O={O2}")

# Ejemplo Años
D3, O3 = intermedios(-1, 1)
print(f"Años -1 a 1 -> D={D3}, O={O3} (año 0 no existe, real O=0)")
```
### 7. APLICACIONES DEL TEOREMA

1.  Estructuras de datos y Arrays
2.  Listas enlazadas
3.  Teoria de intervalos abiertos y conjuntos
4.  Conteo combinatorio y Analisis de secuencias
5.  Programacion (soluciona Fencepost Error)
6.  Organizacion de tiempo y espacio
7.  Ingenieria Civil y Arquitectura

### 8. CONCLUSION FINAL

El Teorema de Pulgarin es altamente util porque transforma un problema de conteo visual, que suele generar confusion y errores, en una formula matematica exacta y universal (O = D - 1). Su aplicabilidad es escalable, funciona igual para contar potes, como para calcular los niveles intermedios de un edificio de 100 pisos.

Ademas, demuestra ser una herramienta fundamental y transversal, utilizada por ingenieros civiles, arquitectos y programadores como base logica para optimizar calculos estructurales y para programar sistemas automatizados como el recorrido de un ascensor.

---
**Jhon Pulgarin - 2026**
**Villavicencio, Meta - Colombia**
