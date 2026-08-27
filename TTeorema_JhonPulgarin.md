# Teorema de Jhon Pulgarin - Discontinuidad Espacial

**Teorema que resuelve el Fencepost Error mediante la fórmula O = |A-B| - 1**

---

### 1. INTRODUCCIÓN HISTÓRICA

Desde la antigüedad, el conteo de intervalos ha generado confusión. El calendario gregoriano es el ejemplo perfecto: no existe el año 0, se pasa del año 1 a.C. al 1 d.C. Esto demuestra que entre dos puntos discretos siempre hay un desfase que debe calcularse.

### 2. CASO DE ESTUDIO: EL ASCENSOR

Caso real: Ascensor del Parqueadero 2 (P2) al Sótano 1 (S1).
Distancia total = |P2 - S1|. Si P2 = -2 y S1 = -1, la distancia es 1, pero ¿cuántos pisos intermedios hay? 0.
Esto prueba la necesidad del teorema.

### 3. ENUNCIADO DEL TEOREMA

Para dos puntos discretos A y B en un espacio ordenado:

**D = |A - B| : Distancia Total**
**O = D - 1 : Puntos Intermedios / Objetos**

Donde O son los espacios vacíos o intermedios entre A y B.

### 4. DEMOSTRACIÓN FORMAL (QED)

1.  Sean A, B pertenecientes a Z, con A < B.
2.  El número de enteros en el intervalo cerrado [A, B] es |A-B| + 1.
3.  El número de enteros en el intervalo abierto (A, B) es (|A-B| + 1) - 2.
4.  Simplificando: O = |A-B| - 1. QED.

### 5. EJEMPLOS PRÁCTICOS

## 1. Problema del Ascensor (Piso 2 a S1)

### Enunciado del problema
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

### 6. SCRIPT EN PYTHON

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
