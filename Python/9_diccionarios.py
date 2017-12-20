ALUMNO = {
    'nombre': 'David', 
    'edad': 21, 
    'clase': 'python'
}

print(ALUMNO['nombre'])
print(ALUMNO['edad'])
print(ALUMNO['clase']) 

print(ALUMNO)

ALUMNO['edad'] = 18
print(ALUMNO)

ALUMNO['sexo'] = 'maricon'
print(ALUMNO)

del ALUMNO ['clase']
print(ALUMNO)

ALUMNO.clear()
print(ALUMNO)

del ALUMNO
print(ALUMNO)