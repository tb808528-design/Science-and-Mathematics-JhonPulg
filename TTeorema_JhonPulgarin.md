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

**Ejemplo 1: Ascensor P2 a S1**
A=-2, B=-1 -> D=1, O=0. No hay pisos intermedios.

**Ejemplo 2: Potes**
5 potes en fila. A=1, B=5 -> D=4, O=3. Hay 3 espacios entre potes.

**Ejemplo 3: Años**
Del año -1 al 1. A=-1, B=1 -> D=2, O=1. El año 0 no existe, el único intermedio teórico es 0, por eso O real = 0.

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
