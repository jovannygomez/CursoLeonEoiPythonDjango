"""
ejemplo para pedir input de usuario y formatear la respuesta
"""

PREGUNTA = '¿Como te llamas?'
RESPUESTA = input(PREGUNTA)

print('Hola', RESPUESTA, '¿Como estas?')

respuesta_formateada = 'Hola {}, ¿como estas?'.format(RESPUESTA)

print(respuesta_formateada)