import pandas as pd

#! Funciones del programa
# La ruta se envia desde main para ejecutarse al utilizar las funciones
def cargaDatos(rutaArchivo):
    df = pd.read_csv(rutaArchivo)
    # Convertir las columnas a datetime para que pandas lo manipule mejor
    df["fecha_inicio"] = pd.to_datetime(df["fecha_inicio"]) 
    df["fecha_fin"] = pd.to_datetime(df["fecha_fin"])
    return df

def filtrarPorAnio(df, anio):
    # fecha_inicio se vuelve una serie de datos por año que se convertira después de cambiarlo a datetime
    # !en vez de 2016-12-31 queda simplemente 2016
    return df[df["fecha_inicio"].dt.year == anio]

def promedioTarifa(df):
    # mean() calcula el promedio de valores de un DataFrame o de series
    # se sacara el promedio de 2016 y de 2017
    return df["volumetrica"].mean()

def variacionPrecio(promedio_2016, promedio_2017):
    # calculo de la variacion ((vf - vi)/vi) * 100 donde vf es el promedio de 2017 y vi es el promedio de 2016
    return ((promedio_2017 - promedio_2016) / promedio_2016) * 100

def tarifaMaxima(df):
    # max() busca el valor maximo dentro de la lectura de la columna de datos
    return df["volumetrica"].max()

#! Metodo main
def main():
    #lectura de la ruta del archivo y carga de los datos del .csv
    rutaArchivo = "Tarifas por zonas 2016-2017.csv"
    df = cargaDatos(rutaArchivo)
    
    #filtros por año y conversion de dataframe a un año solamente
    df_2016 = filtrarPorAnio(df, 2016)
    df_2017 = filtrarPorAnio(df, 2017)
    
    #promedio de valores por año
    promedio_2016 = promedioTarifa(df_2016)
    promedio_2017 = promedioTarifa(df_2017)

    #promedio ambos años
    promedio_anios = ((promedio_2016 + promedio_2017) / 2)

    #variacion donde los valores de la formula son los promedios de 2016 y 2017
    variacion = variacionPrecio(promedio_2016, promedio_2017)

    #tarifas maximas por año
    maxTarifa_2016 = tarifaMaxima(df_2016)
    maxTarifa_2017 = tarifaMaxima(df_2017)
    
    print(f"Promedio del costo a la tarifa correspondiente a los años 2016 y 2017: {promedio_anios:.2f}")
    print(f"Promedio del costo de la tarifa de 2016: {promedio_2016:.2f}")
    print(f"Promedio del costo de la tarifa de 2017: {promedio_2017:.2f}")
    print(f"Variación del precio de gas a lo largo de los años: {variacion:.2f}%")
    print(f"Tarifa máxima 2016: {maxTarifa_2016:.2f}")
    print(f"Tarifa máxima 2017: {maxTarifa_2017:.2f}")

# TODO: Guardar la informacion que se esta imprimiendo en un archivo .txt


if __name__ == "__main__":
    main()
