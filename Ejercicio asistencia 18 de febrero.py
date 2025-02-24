import pandas as pd
import numpy as np

class Dataset:
    def __init__(self, file_path=None, data=None, num_rows=1000):
        """
        Carga datos desde archivo o genera datos aleatorios
        :param file_path: Ruta de archivo CSV (opcional)
        :param num_rows: Número de filas para datos aleatorios
        """
        if file_path:
            self.df = pd.read_csv(file_path)
        else:
            # Generar datos aleatorios si no se proporciona archivo
            if data is None:
                data = {
                    'columna_numerica': np.random.normal(50, 15, num_rows),
                    'columna_categorica': np.random.choice(['A', 'B', 'C'], num_rows),
                    'valor': np.random.randint(0, 100, num_rows)
                }
            self.df = pd.DataFrame(data)
    
    def filtrar(self, condicion):
        """
        Filtra el DataFrame según una condición
        :param condicion: String con condición en sintaxis de pandas
        :return: DataFrame filtrado
        """
        return self.df.query(condicion)
    
    def get_data(self):
        """Devuelve el DataFrame completo"""
        return self.df

class Procesador:
    def __init__(self, dataset):
        """
        :param dataset: Objeto Dataset
        """
        self.df = dataset.get_data()
    
    def calcular_media(self, columna):
        """Calcula la media de una columna"""
        return self.df[columna].mean()
    
    def calcular_mediana(self, columna):
        """Calcula la mediana de una columna"""
        return self.df[columna].median()
    
    def calcular_suma(self, columna):
        """Calcula la suma de una columna"""
        return self.df[columna].sum()
    
    def generar_estadisticas(self, columna=None):
        """
        Genera estadísticas descriptivas
        :param columna: Columna específica (opcional)
        """
        if columna:
            return self.df[columna].describe()
        return self.df.describe()

# Ejemplo de uso
if __name__ == "__main__":
    # Crear dataset con datos aleatorios
    dataset = Dataset()
    
    # Filtrar datos
    filtrado = dataset.filtrar("valor > 50 & columna_categorica == 'A'")
    print("Datos filtrados:", filtrado.shape)
    
    # Procesar datos
    procesador = Procesador(dataset)
    print("Media de valores:", procesador.calcular_media('valor'))
    print("Suma de valores:", procesador.calcular_suma('valor'))
    print("\nEstadísticas descriptivas:")
    print(procesador.generar_estadisticas('valor'))