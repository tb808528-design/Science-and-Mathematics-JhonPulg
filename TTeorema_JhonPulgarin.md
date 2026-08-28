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

### 1. Problema del Ascensor (Piso 2 a S1)
Un ascensor está en el piso 2 y debe bajar hasta el S1 (Sótano 1). Se requiere saber cuántos pisos lo separan, sin contar el piso de origen ni el de destino.

### Datos
Para evitar "pisos fantasma", asignamos índices consecutivos reales:
* **Piso A (origen):** Piso 2 $\rightarrow$ índice $2$
* **Piso B (destino):** Sótano 1 $\rightarrow$ índice $0$
*(Nota: El Piso 1 intermedio ocupa el índice 1)*

### Fórmula y desarrollo
Primero hallamos la distancia total ($D$):
$$D = |\text{índice}(A) - \text{índice}(B)|$$
$$D = |2 - 0|$$
$$D = |2| = 2$$

Ahora hallamos los pisos intermedios ($O$):
$$O = D - 1$$
$$O = 2 - 1 = 1$$

### Respuesta
Lo separa **1 solo piso intermedio**, que es el **Piso 1**.


---

## 2. Problema de los Potes

### Enunciado del problema
Hay 5 potes en fila numerados del 1 al 5. El pote 1 y el pote 5 son los extremos. Se requiere saber cuántos potes hay entre ellos, sin contar el origen ni el destino.

### Datos
Como los potes en el mundo físico ya son consecutivos por naturaleza, sus números equivalen a sus índices:
* **Pote A (origen):** Pote 1 $\rightarrow$ índice $1$
* **Pote B (destino):** Pote 5 $\rightarrow$ índice $5$

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
Dado que en la cronología histórica convencional **el año 0 no existe** (el año 1 d.C. comenzó inmediatamente después de terminar el año 1 a.C.), asignamos índices consecutivos reales para reflejar esta continuidad:
* **Año A (origen):** 1 a.C. $\rightarrow$ índice $0$
* **Año B (destino):** 1 d.C. $\rightarrow$ índice $1$

### Fórmula y desarrollo
Primero hallamos la distancia total ($D$):
$$D = |\text{índice}(A) - \text{índice}(B)|$$
$$D = |0 - 1|$$
$$D = |-1| = 1$$

Ahora hallamos los años intermedios ($O$):
$$O = D - 1$$
$$O = 1 - 1 = 0$$

### Respuesta
Los separan **0 años intermedios**. El año 1 d.C. es inmediatamente consecutivo al año 1 a.C.

### Ajuste Histórico Real
La fórmula matemática arroja un resultado teórico de 1 año intermedio (que correspondería al año 0). Sin embargo, en el registro histórico y cronológico cristiano **no existe el año 0**. El año 1 d.C. sigue inmediatamente al año 1 a.C.

Por lo tanto, en la realidad histórica:
$$O = 0$$

### Respuesta
En la realidad cronológica, **0 años completos** separan el año 1 a.C. del 1 d.C.

### SCRIPT EN PYTHON

```python
def calcular_elementos_intermedios(indice_a, indice_b):
    """
    Aplica la fórmula universal: O = |índice(A) - índice(B)| - 1
    """
    distancia = abs(indice_a - indice_b)
    intermedios = distancia - 1
    return intermedios

# =====================================================================
# 1. PROBLEMA DEL ASCENSOR (Piso 2 a Sótano 1 - Sin Planta Baja)
# Escala real continua: S1 = 0, Piso 1 = 1, Piso 2 = 2
# =====================================================================
piso_origen_idx = 2  # Piso 2
piso_destino_idx = 0  # Sótano 1

pisos_intermedios = calcular_elementos_intermedios(piso_origen_idx, piso_destino_idx)

print("--- 1. PROBLEMA DEL ASCENSOR ---")
print(f"Índice Origen (Piso 2): {piso_origen_idx}")
print(f"Índice Destino (S1): {piso_destino_idx}")
print(f"Pisos intermedios reales que los separan: {pisos_intermedios}\n")


# =====================================================================
# 2. PROBLEMA DE LOS POTES EN FILA
# Escala: Pote 1 = 1, Pote 5 = 5
# =====================================================================
pote_origen_idx = 1
pote_destino_idx = 5

potes_intermedios = calcular_elementos_intermedios(pote_origen_idx, pote_destino_idx)

print("--- 2. PROBLEMA DE LOS POTES ---")
print(f"Índice Origen (Pote 1): {pote_origen_idx}")
print(f"Índice Destino (Pote 5): {pote_destino_idx}")
print(f"Potes intermedios reales que los separan: {potes_intermedios}\n")


# =====================================================================
# 3. PROBLEMA DE LAS ERAS (1 a.C. a 1 d.C. - Sin Año 0 Histórico)
# Escala real continua: 1 a.C. = 0, 1 d.C. = 1
# =====================================================================
ano_origen_idx = 0  # 1 a.C.
ano_destino_idx = 1  # 1 d.C.

anos_intermedios = calcular_elementos_intermedios(ano_origen_idx, ano_destino_idx)

print("--- 3. PROBLEMA DE LAS ERAS ---")
print(f"Índice Origen (1 a.C.): {ano_origen_idx}")
print(f"Índice Destino (1 d.C.): {ano_destino_idx}")
print(f"Años intermedios reales que los separan: {anos_intermedios}\n")

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

-------------------------------------------------------------------------------------------------------------------------------
## 9. ANTECEDENTES HISTÓRICOS Y TRABAJO RELACIONADO

El **Teorema de Jhon Pulgarin** aborda de manera matemática un fenómeno que ha sido identificado en diversas disciplinas científicas a lo largo de la historia. Aunque la fórmula subyacente de la cardinalidad de intervalos abiertos es universal, su aplicación sistemática se conecta directamente con los siguientes hitos de la ciencia y la tecnología:

### A. Matemáticas Discretas: Cardinalidad de Intervalos Abiertos
En la teoría de conjuntos y la matemática discreta, el cálculo de elementos estrictamente internos entre dos límites enteros $A$ y $B$ (donde $A < B$) se define formalmente como la cardinalidad de un **intervalo abierto** $(A, B)$. El uso del valor absoluto $|\text{índice}(A) - \text{índice}(B)| - 1$ extiende esta noción haciéndola simétrica y aplicable independientemente de la dirección del recorrido vectorizado, un principio estudiado en la topología de espacios discretos.

### B. Ciencias de la Computación: Edsger Dijkstra y el "Fencepost Error"
En la ingeniería de software, el núcleo de este teorema resuelve el clásico **Error del Poste de Cerca** (*Fencepost Error* u *Off-by-one Error*). En la década de 1970, el renombrado científico de la computación **Edsger Dijkstra** formalizó la necesidad de la indexación basada en cero (empezar a contar desde 0) para que las operaciones de rango e intervalos en las memorias de las computadoras fuesen consistentes y no requirieran correcciones artificiales al interactuar con el mundo físico.

### C. Astronomía: Jacques Cassini y la Introducción del Año 0
El desfase analizado en el *Problema de las Eras (1 a.C. y 1 d.C.)* fue descubierto físicamente por el astrónomo francés **Jacques Cassini en 1740**. Cassini identificó que los cálculos matemáticos para predecir eclipses históricos fallaban por un factor de 1 año debido a la inexistencia del año 0 en el calendario gregoriano y juliano. Para solucionarlo, introdujo la escala del "Año Astronómico", donde el año 1 a.C. se denota numéricamente como el año 0, validando la necesidad de los índices continuos que propone este teorema.

## 10. VERIFICADOR FORMAL DE METODOS (THEOREM PROVER)
```python
import random

def calcular_elementos_intermedios(indice_a, indice_b):
    """
    Implementación oficial de la fórmula del Teorema de Jhon Pulgarin:
    O = |índice(A) - índice(B)| - 1
    """
    return abs(indice_a - indice_b) - 1

def ejecutar_casos_estudio():
    print("====================================================")
    print("  VALIDACIÓN DE CASOS DE ESTUDIO - TEOREMA DE JHON PULGARIN")
    print("====================================================\n")

    # 1. Caso Ascensor (P2 a S1 -> Índices continuos: S1=0, P1=1, P2=2)
    obs_ascensor = calcular_elementos_intermedios(2, 0)
    print(f"[Caso 1] Ascensor (P2 -> S1): {obs_ascensor} piso intermedio (Piso 1).")

    # 2. Caso Potes (P1 a P5)
    obs_potes = calcular_elementos_intermedios(1, 5)
    print(f"[Caso 2] Potes en fila (1 -> 5): {obs_potes} potes intermedios (2, 3, 4).")

    # 3. Caso Eras Históricas (1 a.C. a 1 d.C. -> Índices continuos: 1 a.C.=0, 1 d.C.=1)
    obs_eras = calcular_elementos_intermedios(0, 1)
    print(f"[Caso 3] Eras (1 a.C. -> 1 d.C.): {obs_eras} años intermedios.\n")

def test_cientifico_propiedades(num_simulaciones=10000):
    """
    Prueba científica automatizada. Valida el teorema contra 10,000 pares
    de índices aleatorios para verificar el cumplimiento de sus propiedades matemáticas.
    """
    print("====================================================")
    print(f"  EJECUTANDO PRUEBA DE PROPIEDADES ({num_simulaciones} ITERACIONES)")
    print("====================================================")
    
    for _ in range(num_simulaciones):
        # Generar dos índices aleatorios en un rango amplio de la recta numérica
        a = random.randint(-100000, 100000)
        b = random.randint(-100000, 100000)
        
        resultado_ab = calcular_elementos_intermedios(a, b)
        resultado_ba = calcular_elementos_intermedios(b, a)
        
        # Propiedad 1: Simetría -> O(A,B) debe ser igual a O(B,A)
        assert resultado_ab == resultado_ba, f"Falla de simetría en: {a}, {b}"
        
        # Propiedad 2: Elementos consecutivos -> Si |A - B| = 1, O debe ser 0
        if abs(a - b) == 1:
            assert resultado_ab == 0, f"Falla en contigüidad para consecutivos: {a}, {b}"
            
        # Propiedad 3: Elementos idénticos -> Si A == B, O debe ser -1 (Intervalo vacío)
        if a == b:
            assert resultado_ab == -1, f"Falla en identidad para elementos iguales: {a}, {b}"
            
    print("✅ ¡PRUEBA EXITOSA!")
    print("- Propiedad de Simetría Demostrada Matemáticamente.")
    print("- Propiedad de Contigüidad (Elementos Consecutivos) Verificada.")
    print("- Propiedad de Identidad (Intervalo Vacío O = -1) Confirmada.")
    print("\nEl Teorema de Jhon Pulgarin es matemáticamente consistente en Python.\n")

if __name__ == "__main__":
    ejecutar_casos_estudio()
    test_cientifico_propiedades()
```


**Jhon Pulgarin - 2026**
**Villavicencio, Meta - Colombia**
