# Diccionario de estudiantes y sus materias
estudiantes_materias = {
    "Daniel": ["Matematica", "Computacion"],
    "Maria": ["Matematica", "Fisica"],
}

# Función para devolver las materias de un estudiante
def devolver_materias(nombre_estudiante):
    if nombre_estudiante in estudiantes_materias:
        return estudiantes_materias[nombre_estudiante]
    else:
        raise ValueError(f"El estudiante {nombre_estudiante} no está registrado.")