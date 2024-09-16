from instituto.clase import estudiante_registrado_en_materia

# Pruebas de estudiantes y materias
print(estudiante_registrado_en_materia("Daniel", "Matematica"))  # True
print(estudiante_registrado_en_materia("Daniel", "Biologia"))    # False
print(estudiante_registrado_en_materia("Maria", "Fisica"))       # True
print(estudiante_registrado_en_materia("Pedro", "Matematica"))   # El estudiante Pedro no está registrado.
