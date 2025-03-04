import pandas as pd

class Datos: 
    # Dataset que contiene los datos del archivo .csv
    datos : pd.DataFrame = None # Se inicializa en None pues se define el valor hasta que se carguen los datos

    def cargarDatos(self, rutaArchivo):
        # Carga de datos del archivo .csv
        Df = pd.read_csv(rutaArchivo)
        
        # TODO: Descomentar esta fracción de código
        # Convertir la primera columan en una fecha para que pandas lo manipule mejor
        # Df["Mes/Anio"] = pd.to_datetime(Df["Mes/Anio"], format="%Y/%m")

        return Df

    def __init__(self, rutaArchivo):
        self.datos = self.cargarDatos(rutaArchivo)
    
    def valorMaximo(self):
        return self.datos["Indice"].max()
    
    def valorMinimo(self):
        return self.datos["Indice"].min()
    
    def promedio(self):
        return self.datos["Indice"].mean()
    
    def desviacionEstandar(self):
        return self.datos["Indice"].std()

    # TODO: Descomentar esta función
    def filtrarPorAnio(self, anio):
        pass
        #return self.datos[self.datos["Mes/Anio"].dt.year == anio]

def main():
    #lectura de la ruta del archivo y carga de los datos del .csv
    rutaArchivo = "./Fuentes/INPCMensualAnualizadoHasta2024.csv"
    dfPersonalizado = Datos(rutaArchivo)

    # TODO: Incluir el filtrado por año

    # Imprimir en la consola los resultados
    print(f"Valor máximo en el índice: {dfPersonalizado.valorMaximo()}")
    print(f"Valor mínimo en el índice: {dfPersonalizado.valorMinimo()}")
    print(f"Promedio del índice en general: {dfPersonalizado.promedio()}")
    print(f"Desviación estándar del índice: {dfPersonalizado.desviacionEstandar()}")

    with open("resultados.txt", "r") as f:
        f.write(f"Valor máximo en el índice: {dfPersonalizado.valorMaximo()}\n")
        f.write(f"Valor mínimo en el índice: {dfPersonalizado.valorMinimo()}\n")
        f.write(f"Promedio del índice en general: {dfPersonalizado.promedio()}\n")
        f.write(f"Desviación estándar del índice: {dfPersonalizado.desviacionEstandar()}\n")
    

if (__name__ == "__main__"):
    main()
