# archivo principal
# Sistema de facturación

from paquete.entradas import leer_numero, List, menu
from paquete.salidas import encabezado, linea
from paquete.procesos import calcular_monto

def main() -> None:
  #pass Pass para que diga paso, no tengo nada para agregar ahorita
  tipos_pizzas: List[str] = ['Volver al menu','Americana', 'Primavera', "Freddy's", 'RompePocetas', 'Gocha']
  precios_unidades: List[float] = [3.5, 2.5, 10, 15, 5]
  formas_pago: List[str] = ['Binance', 'Zelle', 'Zinli', 'Paypal']
  menu_list: List[str] = ['Salir del menu', 'Ver tipos de pizza', 'Ver metodos de pago']
  opcion: int = 0
  
  def menu_pizzas() -> None:
    while True:
      encabezado('Pizzas', 48)
      for i, item in enumerate(tipos_pizzas):
        print(f' {i}.- {item}')
      linea(48)
      opcion_pizza = leer_numero('selecciona una pizza', int)
      if opcion_pizza == 0:
            print('Volviendo al menú principal...')
            break
      elif opcion_pizza > 0 and opcion_pizza < len(tipos_pizzas):
            precio = precios_unidades[opcion_pizza]
            linea(48)
            print(f'Pizza seleccionada: {tipos_pizzas[opcion_pizza]} tiene un precio de {precio}$')
            cantidad = leer_numero('que cantidad de pizzas quiere', float)
            total = calcular_monto(cantidad, precio)
            total_bs = convert_bs_usd(total)
            print(f'Monto total a pagar {total} $ o {total_bs} bs')
            return pagos()
      else:
            print('La opción no existe')
    
  def pagos() -> None:
    while True:
      encabezado('Metodos de pago', 48)
      for i, item in enumerate(formas_pago):
        print(f' {i}.- {item}')
      
  
  def convert_bs_usd(USD: float) -> float:
    VES: float = 231.05
    return USD * VES
  
  while True:
    encabezado("Fazber's Freddy Pizza", 48)
    try:
      menu(menu_list)
      linea(48)
      opcion = leer_numero('Selecciona una opcion', int)
      
      match opcion:
        case 0:
          print('Gracias por visitarnos')
          break
        case 1:
          menu_pizzas()
        case 2:
          pagos()
        case _: # El guion bajo representa el caso por defecto
          print("El valor es otro")
        
    except ValueError:
      print(ValueError)
  
  
if __name__ == '__main__':
  main()