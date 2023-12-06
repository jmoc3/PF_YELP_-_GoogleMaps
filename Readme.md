# <h1 align="center">**`YELP & GOOGLE MAPS - REVIEWS AND RECOMMENDATIONS`**</h1>

<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Yelp_Logo.svg/2560px-Yelp_Logo.svg.png"  height="100">&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Google_Maps_Logo_2020.svg/512px-Google_Maps_Logo_2020.svg.png"  height="100">
</div>

* * *

**Proyecto Grupal de** &nbsp;&nbsp;<img src="https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png"  height="30">  
**Fecha de realización:** desde **el 21-nov-23** al **08-dic-2023**  
**Integrantes:** Daniel Suarez, Francisco Delas, José Miguel Orejarena, Eduardo Bursese

## Introducción

Los integrantes arriba mencionados, forman parte de una consultora que brinda el servicio de asesoramiento a grupos de inversores que desean expandirse o iniciar nuevas inversiones.
Este proyecto, recoge los datos existentes en Google Maps y Yelp respecto de los negocios tales como restaurantes, hoteles y servicios entre otros, y realiza una recopilación y análisis para asesorar a un cliente externo respecto a su decisión de invertir en estos mercados. 

## Objetivos

**Generales:** Realizar un reporte final que desemboque en un sistema de cálculo de posibilidad de éxito respecto al emplazamiento de nuevos locales.

**Específicos:**      
1) Confeccionar un dashboard en base a los KPIs seleccionados.
2) Hacer uso de los servicios cloud de Google para mayor eficiencia de  los procesos internos.
3) Disponibilizar de manera diversa la extracción de los datos. 


## Product Owner

- El Product Owner es nuestro cliente, el cual es integrante de un conglomerado de empresas de restaurantes y afines, con la idea de expansión en el mercado gastronómico.

* * *
## Stack de desarrollo
<div align='center'>
    <img src="https://static-00.iconduck.com/assets.00/google-cloud-icon-2048x1646-7admxejz.png"  height="70">&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="https://k21academy.com/wp-content/uploads/2021/02/Google-Cloud-Storage-logo-1.png"  height="70">&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="https://assets-global.website-files.com/5abc6c4b0a243a2dc939ee6e/5fdb995550a781d7c0c4ec5f_google-bigquery-logo-1.svg"  height="70">&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="https://codelabs.developers.google.com/static/codelabs/cloud-starting-cloudfunctions/img/3b93ba3023ef58a5.png"  height="70">&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="https://www.svgrepo.com/show/354012/looker-icon.svg"  height="70">&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="https://www.ancoris.com/hubfs/Google%20Cloud%20Logos/Cloud%20Composer.png"  height="70">
</div>

<div align='center'>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png"  height="70">&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Pandas_mark.svg/1200px-Pandas_mark.svg.png"  height="70">&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/1280px-NumPy_logo_2020.svg.png"  height="70">&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/2560px-Scikit_learn_logo_small.svg.png"  height="70">&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="https://lh3.googleusercontent.com/-kTfFzkEzgx4/WAo2rS97EUI/AAAAAAAAAQs/6pDmnPbfJLUxSHsqpaE9OrEdcPhIegGaQCMYCGAYYCw/s400/g256x256.png"  height="70">&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="https://cdn.icon-icons.com/icons2/3041/PNG/512/trello_logo_icon_189227.png"  height="70">
</div>

* * *
## Alcance del proyecto

- Basaremos el desarrollo para la ***zona sur*** de **EEUU** siendo la misma la solicitada por nuestro cliente, incluyendo los condados de: California, Arizona, Nuevo Mexico, Texas, Louisiana, Oklahoma, Arkansas, Mississipi, Alabama, Georgia, Florida, Tennessee, Carolina del Sur y del Norte.
- El rubro de interés del cliente es el de **restaurantes**.
- El período de tiempo considerado es a partir del año **2016** hasta la fecha. 

* * *

## KPIs planteados

1. **Índice de Satisfacción del Cliente (CSI - Customer Satisfaction Index):** Obtener un rating promedio mayor al de la media de los últimos 3 meses de la misma categoría en el Estado correspondiente.
2. **Mayor concurrencia:** Obtener una concurrencia promedio MAYOR al de la media de los últimos 3 meses de la misma categoría y en el estado correspondiente.
3. **Sin reseñas de 0 estrellas:** Alcanzar no obtener ninguna reseña de 0 (cero) estrellas en los primeros 3 meses.

## Flujo de trabajo

1. Reuniones ***'Pre-daily'*** donde se habla de los avances individuales.
2. Daily con 🌟Facundo🌟.
3. Reuniones ***'Post-daily'*** para distribuir temas individuales en base a lo completado y a las actividades faltantes.
4. Trabajo individual donde cada quien con su propia gestion del tiempo desarrolla sus respectivos deberes.

* * *
## Modelo Entidad-Relación

![Modelo_ER](./img//PF2_Modelo_ER.jpg)

## Diccionario de datos

#### Tablas:
La tabla 'maestro-diponible' es la final, unificada y depurada donde basamos principalmente los datos mostrados y analizados por el dashboard y el modelo de ML, la cual se armó en base a la tabla dimensional 'sitios' y de la tabla de hecho 'reviews', y cuenta con las siguientes columnas:


- **state:** contiene el estado donde se encuentra el restaurant, ejemplo 'Georgia'.
- **mane_y:** indica el nombre del restaurant, ejemplo 'Krispy Kreme'.
- **category:** tiene las categorias que es catalogada dentro del rubro comida. Puede tener mas de una categoría, ejemplo 'Donut shop'.
- **gmap_id:** es el id de Google Maps para la locación del establecimiento, ejemplo '0x88fba15053b7f129:0x89110fa293e93a76'.
- **latitude y longitude:** contiene las coordenadas goegráficas del lugar, ejemplo '32.1346497 y 81.2432264'.
- **time:** tiene los datos temporales de los reviews (ejemplo: 2019-09-29T16:03:26.972000).
- **rating:** contiene la calificación otorgada por el usuario. Los valores van de 1 al 5.
- **sentiment:** indica el análisis de sentimiento luego de haber ejecutado la librería "textblob" a la columna 'text' de la tabla 'maestro-reviews-sitios' la cual es una tabla temporal intermediaria de trabajo, los valores son 0=negativo, 1=neutral y 2= positivo.
- **resp:** tiene el valor 0 si el establecimiento no dio respuesta al review del usuario, y 1 si respondió al mismo.
- **avg_rating:** contiene un valor decimal de un dígito y señala el promedio de las calificaciones, el rango de valores van de 1.0 a 5.0, ejemplo '4.7'.
- **num_of_reviews:** indica la cantidad de reviews que ha recibido el local por parte de usuarios desde su apertura, ejemplo '2455'.
- **Service0, Service1 y Service2:** indican los servicos extras que el usuario puede encontrar en el lugar de comidas, ejemplo 'Curbside pickup, In-store pickup, In-store shopping'. Puede contener celdas con 'No' indicando que no se dispone de información al respecto.
- **Accessibility0:** indica si el establecimiento tiene algún facility que ayude a la accesibilidad dentro del establecimiento, ejemplo 'Wheelchair accessible entrance'. Puede contener celdas con 'No' indicando que no se dispone de información al respecto.
- **Offerings0, Offerings1, Offerings2:** contiene el detalle de disponibilidad de servicios extras, ejemplo 'Coffe, Wi-Fi, Organic products'. Puede contener celdas con 'No' indicando que no se dispone de información al respecto.
- **Amenities0:** tiene la información respecto a la existencia de comodidades extras, ejemplo 'Public restroom'. Puede contener celdas con 'No' indicando que no se dispone de información al respecto.
- **Atmosphere0:** señala el tipo de ambiente que es de esperarse en el restaurant, ejemplo 'Casual'. Puede contener celdas con 'No' indicando que no se dispone de información al respecto.
- **Crowd0:** tiene el tipo de personas que lo frecuentan, ejemplo 'Family friendly'. Puede contener celdas con 'No' indicando que no se dispone de información al respecto.

## Pipeline

El flujo que siguen los datos es el indicado por el siguiente esquema:

![pipeline](./img/PF2_pipeline.png)

## Carga Incremental Automatizada - Funciones

- El archivo `'ETL_PFH_Carga_de_archivos_a_Storage.ipynb'` realiza la carga autómatica incremental ante el ingreso de un nuevo dataset. En caso de existir la tabla debido a una carga previa 
tan solo concatena los nuevos datos, y en caso de no existir la tabla la crea.

- Los siguientes códigos completan las operaciones de ETL y EDA respectivamente:
    - `EDA_y_ML_PFH_1_1_modelos_de_arbol_y_random forest.ipynb`
    - `ETL_PFH_metadata-sitios_Google.ipynb`
    - `ETL_PFH_reviews-estados_Google_validacion.ipynb`
    - `ETL_PFH_unificado_maestro-disponible.ipynb`
