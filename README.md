# Portfolio Management

Este proyecto permite gestionar un portafolio de acciones y calcular tanto la ganancia como el rendimiento anualizado entre dos fechas específicas. La funcionalidad principal está basada en las clases `Stock` y `Portfolio`.

## Requisitos

Asegúrate de tener Python instalado en tu sistema.

## Estructura del Código

- **Stock**: Representa una acción específica e incluye los precios históricos en diferentes fechas.
- **Portfolio**: Representa el portafolio de inversiones y permite agregar acciones, calcular la ganancia en un rango de fechas y obtener el rendimiento anualizado.

## Configuración de un Portafolio

1. **Crear un diccionario de precios para cada acción.**
   - Usa un diccionario donde las claves son fechas (`datetime`) y los valores son los precios de la acción en esas fechas.
   
   ```python
   from datetime import datetime

   # Ejemplo de precios para la acción AAPL
   aapl_prices = {
       datetime(2023, 1, 1): 150,
       datetime(2024, 1, 1): 180
   }
   ```

2. **Crear instancias de la clase `Stock`.**
   - Pasa el símbolo de la acción y el diccionario de precios al crear cada acción.

   ```python
   aapl = Stock("AAPL", aapl_prices)
   ```

3. **Crear una instancia de `Portfolio` y agregar acciones.**
   - Usa `add_stock` para agregar cada acción al portafolio junto con la cantidad de acciones que se posee.

   ```python
   portfolio = Portfolio()
   portfolio.add_stock(aapl, 10)  # 10 acciones de AAPL
   ```

## Cálculo de Ganancia y Rendimiento Anualizado

- **Calcular la ganancia entre dos fechas**: Utiliza el método `profit` del portafolio con las fechas de inicio y final.

  ```python
  start_date = datetime(2023, 1, 1)
  end_date = datetime(2024, 1, 1)
  ganancia = portfolio.profit(start_date, end_date)
  print("Ganancia:", ganancia)
  ```

- **Calcular el rendimiento anualizado**: Usa el método `annualized_return` para obtener el rendimiento en términos anuales.

  ```python
  rendimiento_anualizado = portfolio.annualized_return(start_date, end_date)
  print("Rendimiento Anualizado:", rendimiento_anualizado)
  ```

## Ejemplo Completo

Aquí está un ejemplo completo con dos acciones y el cálculo de ganancia y rendimiento anualizado:

```python
from datetime import datetime

# Datos de precios
aapl_prices = {datetime(2023, 1, 1): 150, datetime(2024, 1, 1): 180}
msft_prices = {datetime(2023, 1, 1): 250, datetime(2024, 1, 1): 300}

# Crear acciones
aapl = Stock("AAPL", aapl_prices)
msft = Stock("MSFT", msft_prices)

# Crear portafolio y agregar acciones
portfolio = Portfolio()
portfolio.add_stock(aapl, 10)  # 10 acciones de AAPL
portfolio.add_stock(msft, 5)   # 5 acciones de MSFT

# Calcular ganancia y rendimiento anualizado
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 1, 1)
print("Ganancia:", portfolio.profit(start_date, end_date))
print("Rendimiento Anualizado:", portfolio.annualized_return(start_date, end_date))
```

## Notas

- El método `price` en `Stock` busca el precio de una acción en una fecha específica.
- `profit` calcula la diferencia en el valor total del portafolio entre las dos fechas dadas.
- `annualized_return` convierte la ganancia total en un rendimiento anualizado ajustado al periodo de tiempo indicado.
