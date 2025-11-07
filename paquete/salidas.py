'''
Funciones de salida de Datos
'''

def linea(largo: int) -> None:
  print('═' * largo)
  
def encabezado(titulo: str, largo: int) -> None:
  linea(largo)
  print(titulo.upper().center(largo))
  linea(largo)