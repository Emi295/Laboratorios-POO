from .estudiante import devolver_materias

# Función para verificar si un estudiante está registrado en una materia
def estudiante_registrado_en_materia(nombre_estudiante, materia):
    try:
        materias = devolver_materias(nombre_estudiante)
        return materia in materias
    except ValueError as e:
        print(e)
        return False