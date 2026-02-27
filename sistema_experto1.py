
# FUNCION PARA CLASIFICAR GLUCOSA
def clasificar_glucosa(glucosa):
    # Regla 1: Azúcar baja
    if glucosa < 70:
        return "Baja"
    
    # Regla 2: Azúcar normal
    elif 70 <= glucosa <= 100:
        return "Normal"
    
    # Regla 3: Azúcar alta
    else:
        return "Alta"

# FUNCION PARA CLASIFICAR PRESION
def clasificar_presion(sistolica, diastolica):
    # Regla 1: Presión baja
    if sistolica < 90 or diastolica < 60:
        return "Baja"
    
    # Regla 2: Presión normal
    elif 90 <= sistolica <= 120 and 60 <= diastolica <= 80:
        return "Normal"
    
    # Regla 3: Presión alta
    else:
        return "Alta"

# FUNCION PARA GENERAR RECOMENDACION

def generar_recomendacion(glucosa_estado, presion_estado):
    
    # Si todo está normal
    if glucosa_estado == "Normal" and presion_estado == "Normal":
        return "Sus niveles están dentro de los rangos normales. Mantenga hábitos saludables."
    
    # Si algún valor está alto
    elif glucosa_estado == "Alta" or presion_estado == "Alta":
        return "Se recomienda mejorar la alimentación, hacer ejercicio y consultar a un profesional de salud."
    
    # Si algún valor está bajo
    elif glucosa_estado == "Baja" or presion_estado == "Baja":
        return "Se recomienda monitoreo y consultar a un profesional si presenta síntomas."
    
    # Caso general
    else:
        return "Se recomienda control periódico de sus niveles."



# PROGRAMA PRINCIPAL


print("=== SISTEMA EXPERTO DE SALUD BÁSICO ===")

# Entrada de datos
edad = int(input("Ingrese su edad: "))
nombre = str(input("Ingrese su nombre: "))
glucosa = float(input("Ingrese su nivel de glucosa (mg/dL): "))
sistolica = int(input("Ingrese su presión sistólica: "))
diastolica = int(input("Ingrese su presión diastólica: "))

# Motor de inferencia (aplicación de reglas)
estado_glucosa = clasificar_glucosa(glucosa)
estado_presion = clasificar_presion(sistolica, diastolica)

# Generación de recomendación
recomendacion = generar_recomendacion(estado_glucosa, estado_presion)

# Salida del sistema experto
print("\n=== RESULTADOS ===")
print("Edad:", edad)
print("Nombre:", nombre)
print("Clasificación de Glucosa:", estado_glucosa)
print("Clasificación de Presión Arterial:", estado_presion)
print("Recomendación:", recomendacion)