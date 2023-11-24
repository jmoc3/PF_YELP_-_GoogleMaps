![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

## **PROYECTO GRUPAL Nº1**

- - -

## <h1 align="center">**`YELP & GOOGLE MAPS - REVIEWS AND RECOMMENDATIONS`**</h1>

<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Yelp_Logo.svg/2560px-Yelp_Logo.svg.png"  height="100">
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Google_Maps_Logo_2020.svg/512px-Google_Maps_Logo_2020.svg.png"  height="100">


### **Fecha de realización: desde el 21-nov-23 al 08-dic-2023**

### **Integrantes: Daniel Suarez, Francisco Delas, José Miguel Orejarena, Eduardo Bursese**

<span style="color: green; font-size: 20px; font-weight: bold;">Introducción</span>


    Los integrantes arriba mencionados, forman parte de una consultora que brinda el servicio de asesoramiento a grupos de inversores que desean expandirse o iniciar nuevas inversiones.
    Este proyecto, recoge los datos existentes en Google Maps y Yelp respecto de los negocios tales como restaurantes, hoteles y servicios entre otros, y realiza una recopilación y análisis para asesorar a un cliente externo respecto a su decisión de invertir en estos mercados. 

<span style="color: green; font-size: 20px; font-weight: bold;">Objetivos</span>


    Generales: realizar un reporte final que desemboque en un sistema de cálculo de posibilidad de éxito respecto al emplazamiento de nuevos locales.

    Específicos:    1- Confeccionar un dashboard en base a los KPIs seleccionados.
                    2- Hacer uso de los servicios cloud de Google para mayor eficiencia de  los procesos internos.
                    3- Disponibilizar de manera diversa la extracción de los datos. 

<span style="color: green; font-size: 20px; font-weight: bold;">Product Owner</span>


    El Product Owner es nuestro cliente, el cual es integrante de un conglomerado de empresas de restaurantes y afines, con la idea de expansión en el mercado gastronómico.

<span style="color: green; font-size: 20px; font-weight: bold;">Stack de desarrollo</span>

<div style="display: flex; justify-content: space-between;">
    <p align="left">
<img src="https://1000logos.net/wp-content/uploads/2020/05/Logo-Google-Cloud.jpg"  height="50">
    <p align="left">
<img src="https://k21academy.com/wp-content/uploads/2021/02/Google-Cloud-Storage-logo-1.png"  height="50">
    <p align="left">
<img src="https://assets-global.website-files.com/5abc6c4b0a243a2dc939ee6e/5fdb995550a781d7c0c4ec5f_google-bigquery-logo-1.svg"  height="50">
    <p align="left">
<img src="https://codelabs.developers.google.com/static/codelabs/cloud-starting-cloudfunctions/img/3b93ba3023ef58a5.png"  height="50">
    <p align="left">
<img src="https://www.svgrepo.com/show/354012/looker-icon.svg"  height="50">
    <p align="left">
<img src="https://www.ancoris.com/hubfs/Google%20Cloud%20Logos/Cloud%20Composer.png"  height="50">
</div>


<div style="display: flex; justify-content: space-between;">
    <p align="left">
<img src="https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-512.png"  height="50">
    <p align="left">
<img src="https://miro.medium.com/v2/resize:fit:1358/0*RWkQ0Fziw792xa0S"  height="50">
    <p align="left">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/1280px-NumPy_logo_2020.svg.png"  height="50">
    <p align="left">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/2560px-Scikit_learn_logo_small.svg.png"  height="50">
    <p align="left">
<img src="https://uploads-ssl.webflow.com/5f538c6ee630c3802820713d/5f9a91075f221be3ca31d5be_EN34oyc8fn1PfJnetkCjdlUrx03roolJKijsPQH5lqFciESiSTXrv1ZalHMmWaWPawqKrq2e6A%3Ds220-w220-h140.jpeg"  height="50">
    <p align="left">
<img src="https://logos-world.net/wp-content/uploads/2021/02/Trello-Logo.png"  height="50">
</div>


<span style="color: green; font-size: 20px; font-weight: bold;">Alcance del proyecto</span>


    Basaremos el desarrollo para la zona sur de EEUU siendo la misma la solicitada por nuestro cliente, incluyendo los condados de: California, Arizona, Nuevo Mexico, Texas, Louisiana, Oklahoma, Arkansas, Mississipi, Alabama, Georgia, Florida, Tennessee, Carolina del Sur y del Norte.
    El rubro de interés del cliente es el de restaurantes.
    El período de tiempo considerado es a partir del año 2016 hasta la fecha. 


<span style="color: red; font-size: 20px;">EDA: remitirse al archivo 'EDA_detail.ipynb'.</span>

<span style="color: green; font-size: 20px; font-weight: bold;">KPIs preliminares</span>

<span style="color: orange; font-size: 15px;">1-Índice de Satisfacción del Cliente (CSI - Customer Satisfaction Index):</span>

    Cálculo:
        CSI = AVG(avg_rating) GROUP BY state, year(time)
    
    Indicadores Relacionados:
        ● Correlación entre la Satisfacción del Cliente y el Número de Checkins.
        ● Evolución Temporal del CSI por Estado y Categoría.
        ● Correlación entre la Satisfacción del Cliente y la Densidad de Restaurantes.
    
    Fundamento: El CSI proporciona una medida detallada de la satisfacción del cliente en cada estado y año. La correlación con otras métricas permite entender cómo factores adicionales afectan la experiencia del cliente.

<span style="color: orange; font-size: 15px;">2-Densidad de Restaurantes por cada 1000 Habitantes:</span>

    Cálculo:
        Densidad = (Cantidad de Restaurantes / Población) * 1000
    
    Indicadores Relacionados:
        ● Cantidad de Restaurantes por Estado.
        ● Densidad de Restaurantes de Comida Especíﬁca en Comparación con la Media Nacional.
        ● Tendencia Temporal de la Densidad de Restaurantes.
        
    Fundamento: La densidad de restaurantes ajustada a la población permite identiﬁcar áreas con saturación de restaurantes o, por el contrario, con oportunidades para inversión.

<span style="color: orange; font-size: 15px;">3-Promedio de Checkins por Estado en Relación con Población y Poder Adquisitivo:</span>

    Cálculo:
        Promedio de Checkins = SUM(Checkins) / (Población * Poder Adquisitivo) GROUP BY state
    
    Indicadores Relacionados:
        ● Correlación entre el Promedio de Checkins y el Índice de Satisfacción del Cliente.
        ● Comparación del Promedio de Checkins entre Estados.
        ● Evolución Temporal del Promedio de Checkins.
    
    Fundamento: El promedio de checkins ajustado a la población y poder adquisitivo permite entender la interacción de los clientes en relación con la capacidad de gasto y tamaño de la población.

<span style="color: orange; font-size: 15px;">4-Cantidad de Reseñas Positivas por Categoría y Estado:</span>

    Cálculo:
        ● Reseñas Positivas = SUM("Cool" + "Funny" + "Useful") GROUP BY state, category
    
    Indicadores Relacionados:
        ● Correlación entre Reseñas Positivas y la Satisfacción del Cliente.
        ● Comparación de Reseñas Positivas entre Estados.
        ● Tendencia Temporal de Reseñas Positivas.
        ● Fundamento: La cantidad de reseñas positivas proporciona insights sobre la        percepción positiva del restaurante, contribuyendo al atractivo general y al potencial de éxito.

<span style="color: orange; font-size: 15px;">5-Correlación entre Características del Restaurante y la Satisfacción del Cliente:</span>

    Cálculo:
        ● CORREL(attribute, avg_rating)

    Indicadores Relacionados:
        ● Correlación entre Características del Restaurante y la Densidad de Restaurantes.
        ● Evolución Temporal de la Correlación entre Atributos y Satisfacción del Cliente.
        ● Comparación de Correlaciones entre Estados.
        ● Fundamento: Identiﬁcar la correlación entre características especíﬁcas del restaurante y la satisfacción del cliente proporciona información valiosa para la toma de decisiones estratégicas.

<span style="color: orange; font-size: 15px;">6-Avance de Puntaje Promedio de Reseña por Categoría y Año:</span>

    Cálculo:
        ● Avance de Puntaje Promedio = AVG(avg_rating) GROUP BY state, category, year(time)

    Indicadores Relacionados:
        ● Correlación entre el Avance de Puntaje Promedio y el Índice de Satisfacción del Cliente.
        ● Comparación del Avance de Puntaje Promedio entre Categorías.
        ● Tendencia Temporal del Avance de Puntaje Promedio.
    
    Fundamento: Seguir la evolución del puntaje promedio por categoría y año permite identiﬁcar tendencias y anticipar cambios en las preferencias del cliente, permitiendo adaptar estrategias de inversión.

<span style="color: green; font-size: 20px; font-weight: bold;">Flujo de trabajo</span>

a) Reuniones 'pre daily' donde se habla los avances individuales.

b) Daily con Facundo.

c) Reuniones 'post daily' para distribuir temas individuales en base a lo completado y a lo por hacer.

d) Trabajo individual.

<span style="color: red; font-size: 15px; font-style: italic;">(Para Spring #2 y #3)</span>



<span style="color: red; font-size: 15px; font-style: italic;">
Modelo Entidad-Relación. Diccionario.

Pipeline. Automatizado.Pipeline data warehouse.

Entregables.

Reporte final.</span>
