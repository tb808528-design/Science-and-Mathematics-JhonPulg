#( Q ) = calor (Joules)
#( m ) = masa (kg)
#( c ) = calor específico (J/kg·°C)
#( \Delta T ) = cambio de temperatura (°C)


# Cálculo del calor sensible en Python con inputs (por ahora en español)
# Fórmula: Q = m * c * ΔT

def calcular_calor(masa, calor_especifico, temp_inicial, temp_final):
    """
    Calcula el calor sensible usando Q = m * c * ΔT.
    
    Parámetros:
        masa (float): masa en kilogramos (kg)
        calor_especifico (float): calor específico en J/(kg·°C)
        temp_inicial (float): temperatura inicial en °C
        temp_final (float): temperatura final en °C
    
    Retorna:
        float: calor en Joules (J)
    """
    # Validaciones de entrada
    if masa <= 0:
        raise ValueError("La masa debe ser mayor que cero.")
    if calor_especifico <= 0:
        raise ValueError("El calor específico debe ser mayor que cero.")
    
    delta_t = temp_final - temp_inicial
    calor = masa * calor_especifico * delta_t
    return calor


# Ejemplo de uso
try:
    m = float(input("Ingrese la masa (kg): "))
    c = float(input("Ingrese el calor específico (J/kg·°C): "))
    t1 = float(input("Ingrese la temperatura inicial (°C): "))
    t2 = float(input("Ingrese la temperatura final (°C): "))

    q = calcular_calor(m, c, t1, t2)

    print(f"El calor transferido es: {q:.2f} Joules")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
