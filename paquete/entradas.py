# Que es un paradigma?
# Son reglas a seguir para programar, o mejor dicho un conjunto de reglas
# Python es multiparadigma

'''
tipos de programacion
- estructurada
- POO programacion orientado a objetos
- Funcional
'''

# Funciondes de entradas de datos
from typing import Any

def leer_numero(msj: str, fun: Any) -> Any:
  numero: Any
  while True:
    try:
      numero = fun(input(msj + ': '))
      return numero
    except ValueError:
      print(ValueError)