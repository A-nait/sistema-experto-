
from clips import Environment

# CREAR MOTOR DE INFERENCIA
env = Environment()

# DEFINIR BASE DE CONOCIMIENTOS (una por una)

# Templates
env.build("""
(deftemplate persona
    (slot nombre)
    (slot edad)
    (slot glucosa)
    (slot sistolica)
    (slot diastolica)
)
""")

env.build("""
(deftemplate clasificacion
    (slot tipo)
    (slot valor)
)
""")

# REGLAS PARA GLUCOSA

env.build("""
(defrule glucosa-baja
    (persona (glucosa ?g))
    (test (< ?g 70))
    =>
    (assert (clasificacion (tipo glucosa) (valor Baja)))
)
""")

env.build("""
(defrule glucosa-normal
    (persona (glucosa ?g))
    (test (and (>= ?g 70) (<= ?g 100)))
    =>
    (assert (clasificacion (tipo glucosa) (valor Normal)))
)
""")

env.build("""
(defrule glucosa-alta
    (persona (glucosa ?g))
    (test (> ?g 100))
    =>
    (assert (clasificacion (tipo glucosa) (valor Alta)))
)
""")

# REGLAS PARA PRESION

env.build("""
(defrule presion-baja
    (persona (sistolica ?s) (diastolica ?d))
    (test (or (< ?s 90) (< ?d 60)))
    =>
    (assert (clasificacion (tipo presion) (valor Baja)))
)
""")

env.build("""
(defrule presion-normal
    (persona (sistolica ?s) (diastolica ?d))
    (test (and (>= ?s 90) (<= ?s 120)
               (>= ?d 60) (<= ?d 80)))
    =>
    (assert (clasificacion (tipo presion) (valor Normal)))
)
""")

env.build("""
(defrule presion-alta
    (persona (sistolica ?s) (diastolica ?d))
    (test (or (> ?s 120) (> ?d 80)))
    =>
    (assert (clasificacion (tipo presion) (valor Alta)))
)
""")

# REGLAS DE RECOMENDACION

env.build("""
(defrule recomendacion-normal
    (clasificacion (tipo glucosa) (valor Normal))
    (clasificacion (tipo presion) (valor Normal))
    =>
    (printout t "Recomendacion: Mantenga habitos saludables." crlf)
)
""")

env.build("""
(defrule recomendacion-alta
    (or
        (clasificacion (tipo glucosa) (valor Alta))
        (clasificacion (tipo presion) (valor Alta))
    )
    =>
    (printout t "Recomendacion: Mejore alimentacion, haga ejercicio y consulte profesional." crlf)
)
""")

env.build("""
(defrule recomendacion-baja
    (or
        (clasificacion (tipo glucosa) (valor Baja))
        (clasificacion (tipo presion) (valor Baja))
    )
    =>
    (printout t "Recomendacion: Monitoreo y consulte profesional si presenta sintomas." crlf)
)
""")

# Reiniciar entorno
env.reset()

# INTERFAZ

print("=== SISTEMA EXPERTO DE SALUD ===")

nombre = input("Nombre: ")
edad = int(input("Edad: "))
glucosa = float(input("Glucosa (mg/dL): "))
sistolica = int(input("Presión sistólica: "))
diastolica = int(input("Presión diastólica: "))

# Insertar hecho en memoria
env.assert_string(f"""
(persona
    (nombre "{nombre}")
    (edad {edad})
    (glucosa {glucosa})
    (sistolica {sistolica})
    (diastolica {diastolica})
)
""")

# Ejecutar motor de inferencia
env.run()

# MOSTRAR RESULTADOS
print("\n=== RESULTADOS ===")

for fact in env.facts():
    if fact.template.name == "clasificacion":
        print(f"{fact['tipo'].capitalize()}: {fact['valor']}")