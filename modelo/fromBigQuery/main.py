import pandas as pd
import streamlit as st
import joblib
import warnings

from google.cloud import bigquery

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

from google.cloud import bigquery
import os

warnings.filterwarnings("ignore")

# lee archivo de credenciales de servicio
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "pf-henry-405314-70013f74b521.json"

# definir proyecto y dataset de BigQuery
project_id = "pf-henry-405314"
dataset_id = "Modelo_ML"

# Crea cliente de BigQuery

client = bigquery.Client(project=project_id)

modelo = joblib.load("modelo_ml.pkl")

# clase 'Regular' por defualt
class1 = 0

st.title('Predicción de Probabilidad de Éxito de un Nuevo Restaurant')
st.markdown('***')
# ---------------------------------------------------------------

st.sidebar.markdown('## Cuántas Estrellas? Dónde? ')

# eleccion de estrellas

options = {'⭐': 1,
           '⭐⭐': 2,
           '⭐⭐⭐': 3,
           '⭐⭐⭐⭐': 4,
           '⭐⭐⭐⭐⭐': 5}

selected_option = st.sidebar.radio(
    "¿Cuántas estrellas quieres para tu restaurante?",
    list(options.keys())
)

rating = options[selected_option]

# st.write(f"Has seleccionado: {rating} {selected_option}")

# st.write(rating)
# ---------------------------------------------------------------
# eleccion de categoria

# nombre de la tabla en BigQuery
table_id = "category"

# Crea referencia a la tabla en BigQuery
table_ref = client.dataset(dataset_id).table(table_id)

# Solicitud de API: buscar la tabla
table = client.get_table(table_ref)

# Recupere todos los datos de la tabla en un DataFrame de pandas
df = client.list_rows(table).to_dataframe()

# Crear una lista desplegable con los valores de 'category'
cat = st.selectbox(
    'Selecciona una Categoria',
    df['category'])

st.write('Has seleccionado:', cat)

category = df[df['category'] == cat]['category_int'].values[0]

# st.write(category)
# ---------------------------------------------------------------
# eleccion de estado

# nombre de la tabla en BigQuery
table_id = "estados"

# Crea referencia a la tabla en BigQuery
table_ref = client.dataset(dataset_id).table(table_id)

# Solicitud de API: buscar la tabla
table = client.get_table(table_ref)

# Recupere todos los datos de la tabla en un DataFrame de pandas
df = client.list_rows(table).to_dataframe()

# Crear un conjunto de botones de opción con los valores de 'state'
sta = st.sidebar.radio(
    'Selecciona un Estado',
    df['state'])

# st.write('Has seleccionado:', sta)

state = df[df['state'] == sta]['state_int'].values[0]

# st.write(state)
# ---------------------------------------------------------------
# eleccion de servicio 0

# nombre de la tabla en BigQuery
table_id = "Service0"

# Crea referencia a la tabla en BigQuery
table_ref = client.dataset(dataset_id).table(table_id)

# Solicitud de API: buscar la tabla
table = client.get_table(table_ref)

# Recupere todos los datos de la tabla en un DataFrame de pandas
df = client.list_rows(table).to_dataframe()

# Crear una lista desplegable con los valores de 'servicio'
Ser0 = st.selectbox(
    'Servicio 1 a ofrecer',
    df['Service0'])

st.write('Has seleccionado:', Ser0)

Service0 = df[df['Service0'] == Ser0]['Service0_int'].values[0]

# st.write(Service0)
# ---------------------------------------------------------------
# eleccion de servicio 1

# nombre de la tabla en BigQuery
table_id = "Service1"

# Crea referencia a la tabla en BigQuery
table_ref = client.dataset(dataset_id).table(table_id)

# Solicitud de API: buscar la tabla
table = client.get_table(table_ref)

# Recupere todos los datos de la tabla en un DataFrame de pandas
df = client.list_rows(table).to_dataframe()

# Crear una lista desplegable con los valores de 'servicio'
Ser1 = st.selectbox(
    'Servicio 2 a ofrecer',
    df['Service1'])

st.write('Has seleccionado:', Ser1)

Service1 = df[df['Service1'] == Ser1]['Service1_int'].values[0]

# st.write(Service1)
# ---------------------------------------------------------------
# eleccion de servicio 2

# nombre de la tabla en BigQuery
table_id = "Service2"

# Crea referencia a la tabla en BigQuery
table_ref = client.dataset(dataset_id).table(table_id)

# Solicitud de API: buscar la tabla
table = client.get_table(table_ref)

# Recupere todos los datos de la tabla en un DataFrame de pandas
df = client.list_rows(table).to_dataframe()

# Crear una lista desplegable con los valores de 'servicio'
Ser2 = st.selectbox(
    'Servicio 3 a ofrecer',
    df['Service2'])

st.write('Has seleccionado:', Ser2)

Service2 = df[df['Service2'] == Ser2]['Service2_int'].values[0]

# st.write(Service2)
# ---------------------------------------------------------------
# eleccion de Accecibilidad

# nombre de la tabla en BigQuery
table_id = "Accesibilidad"

# Crea referencia a la tabla en BigQuery
table_ref = client.dataset(dataset_id).table(table_id)

# Solicitud de API: buscar la tabla
table = client.get_table(table_ref)

# Recupere todos los datos de la tabla en un DataFrame de pandas
df = client.list_rows(table).to_dataframe()

# Crear una lista desplegable con los valores de 'Accecibilidad'
Acc = st.selectbox(
    'Seleccione una opción',
    df['Accessibility0'])

st.write('Has seleccionado:', Acc)

Accessibility0 = df[df['Accessibility0']
                    == Acc]['Accessibility0_int'].values[0]

# st.write(Accessibility0)
# ---------------------------------------------------------------
# eleccion de Ofertas

# nombre de la tabla en BigQuery
table_id = "Offerings0"

# Crea referencia a la tabla en BigQuery
table_ref = client.dataset(dataset_id).table(table_id)

# Solicitud de API: buscar la tabla
table = client.get_table(table_ref)

# Recupere todos los datos de la tabla en un DataFrame de pandas
df = client.list_rows(table).to_dataframe()

# Crear una lista desplegable con los valores de 'Ofertas'
Off0 = st.selectbox(
    'Seleccione una Oferta 1',
    df['Offerings0'])

st.write('Has seleccionado:', Off0)

Offerings0 = df[df['Offerings0']
                == Off0]['Offerings0_int'].values[0]

# st.write(Offerings0)
# ---------------------------------------------------------------
# eleccion de Ofertas

# nombre de la tabla en BigQuery
table_id = "Offerings1"

# Crea referencia a la tabla en BigQuery
table_ref = client.dataset(dataset_id).table(table_id)

# Solicitud de API: buscar la tabla
table = client.get_table(table_ref)

# Recupere todos los datos de la tabla en un DataFrame de pandas
df = client.list_rows(table).to_dataframe()

# Crear una lista desplegable con los valores de 'Ofertas'
Off1 = st.selectbox(
    'Seleccione una Oferta 2',
    df['Offerings1'])

st.write('Has seleccionado:', Off1)

Offerings1 = df[df['Offerings1']
                == Off1]['Offerings1_int'].values[0]

# st.write(Offerings1)
# ---------------------------------------------------------------
# eleccion de Ofertas

# nombre de la tabla en BigQuery
table_id = "Offerings2"

# Crea referencia a la tabla en BigQuery
table_ref = client.dataset(dataset_id).table(table_id)

# Solicitud de API: buscar la tabla
table = client.get_table(table_ref)

# Recupere todos los datos de la tabla en un DataFrame de pandas
df = client.list_rows(table).to_dataframe()

# Crear una lista desplegable con los valores de 'Ofertas'
Off2 = st.selectbox(
    'Seleccione una Oferta 3',
    df['Offerings2'])

st.write('Has seleccionado:', Off2)

Offerings2 = df[df['Offerings2']
                == Off2]['Offerings2_int'].values[0]

# st.write(Offerings2)
# ---------------------------------------------------------------
# eleccion de Amenidades

# nombre de la tabla en BigQuery
table_id = "Amenities0"

# Crea referencia a la tabla en BigQuery
table_ref = client.dataset(dataset_id).table(table_id)

# Solicitud de API: buscar la tabla
table = client.get_table(table_ref)

# Recupere todos los datos de la tabla en un DataFrame de pandas
df = client.list_rows(table).to_dataframe()

# Crear una lista desplegable con los valores de 'Amenidades'
Ame = st.selectbox(
    'Seleccione una Amenidad',
    df['Amenities0'])

st.write('Has seleccionado:', Ame)

Amenities0 = df[df['Amenities0']
                == Ame]['Amenities0_int'].values[0]

# st.write(Amenities0)
# ---------------------------------------------------------------
# eleccion de Atmosfera

# nombre de la tabla en BigQuery
table_id = "Atmosphere0"

# Crea referencia a la tabla en BigQuery
table_ref = client.dataset(dataset_id).table(table_id)

# Solicitud de API: buscar la tabla
table = client.get_table(table_ref)

# Recupere todos los datos de la tabla en un DataFrame de pandas
df = client.list_rows(table).to_dataframe()

# Crear una lista desplegable con los valores de 'Atmosferas'
Atm = st.selectbox(
    'Seleccione una Atmósfera',
    df['Atmosphere0'])

st.write('Has seleccionado:', Atm)

Atmosphere0 = df[df['Atmosphere0']
                 == Atm]['Atmosphere0_int'].values[0]

# st.write(Atmosphere0)
# ---------------------------------------------------------------
# eleccion de Enfoque

# nombre de la tabla en BigQuery
table_id = "Crowd0"

# Crea referencia a la tabla en BigQuery
table_ref = client.dataset(dataset_id).table(table_id)

# Solicitud de API: buscar la tabla
table = client.get_table(table_ref)

# Recupere todos los datos de la tabla en un DataFrame de pandas
df = client.list_rows(table).to_dataframe()

# Crear una lista desplegable con los valores de 'Enfoques'
Cro = st.selectbox(
    'Seleccione un Público',
    df['Crowd0'])

st.write('Has seleccionado:', Cro)

Crowd0 = df[df['Crowd0']
            == Cro]['Crowd0_int'].values[0]

# st.write(Crowd0)

# sitema de clasificacion con árbol de decisión para determinar que clase es el restaurant
# tienes el siguiente DataFrame
x_prueba = pd.DataFrame(columns=('rating', 'category_int', 'state_int', 'Service0_int', 'Service1_int', 'Service2_int', 'Accessibility0_int', 'Offerings0_int',
                                 'Offerings1_int', 'Offerings2_int', 'Amenities0_int', 'Atmosphere0_int', 'Crowd0_int', 'class1'))

# tienes los siguientes datos
datos = (rating, category, state, Service0, Service1, Service2, Accessibility0, Offerings0, Offerings1, Offerings2, Amenities0,
         Atmosphere0, Crowd0, class1)

x_prueba.loc[0] = datos
y_pred = modelo.predict(x_prueba.drop(['class1'], axis=1))

if y_pred[0] == 1:
    st.markdown("# El restaurante será de 'Clase Premium'")
elif y_pred[0] == 0:
    st.markdown("# El restaurante será 'Regular'")

y_proba = modelo.predict_proba(x_prueba.drop(['class1'], axis=1))
st.markdown("## Con una probabilidad de Acierto de: " +
            str(round(y_proba[0][y_pred][0] * 100, 2))+"%")
st.markdown('***')
# ---------------------------------------------------------------
st.markdown('### A continuacion te invitamos a explorar los casos de exitos de acuardo a la categoria y el estado que has escogido, puedes elegir cualquier opcion para ver sus atributos mas llamativos.')

# eleccion de Restaurant de Referencia

# nombre de la tabla en BigQuery
table_id = "category_details"

# Crea referencia a la tabla en BigQuery
table_ref = client.dataset(dataset_id).table(table_id)

# Solicitud de API: buscar la tabla
table = client.get_table(table_ref)

# Recupere todos los datos de la tabla en un DataFrame de pandas
data_details = client.list_rows(table).to_dataframe()

data_details = data_details[(data_details['category_det'] == cat) & (
    data_details['state'] == sta)]

try:
    nombre = st.selectbox(
        'Selecciona un Restaurante de Referencia',
        data_details['name_y'])
    st.write('Has seleccionado:', nombre)

    if not data_details[data_details['name_y'] == nombre].empty:
        caracteristicas = data_details.loc[data_details['name_y']
                                           == nombre, 'features'].values[0]
    else:
        st.write('Para el estado de ' + sta +
                 ' no existen lugares de categoria ' + cat + ', que sean de "Clase Premium", lo sentimos.')
        caracteristicas = None
except Exception:
    st.write('Ha ocurrido un error al obtener las características.')

caracteristicas = data_details.loc[data_details['name_y']
                                   == nombre, 'features'].values[0]

st.markdown(" El Restaurant de Referencia: " + nombre + ", esta ubicado en el Estado de " + sta +
            " y es de la categoría de " + cat + " el mismo es de clase Premiun y cuenta con las siguientes caracteristicas: " + caracteristicas)

# ---------------------------------------------------------------
# sistema de recomendacion por similitud de coseno
category1 = cat + ' - ' + sta + ' - ' + nombre

# se carga los datasets que se va a utilizar para dos dataframes distintos

# nombre de la tabla en BigQuery
table_id = "category_features"

# Crea referencia a la tabla en BigQuery
table_ref = client.dataset(dataset_id).table(table_id)

# Solicitud de API: buscar la tabla
table = client.get_table(table_ref)

# Recupere todos los datos de la tabla en un DataFrame de pandas
data = client.list_rows(table).to_dataframe()

# nombre de la tabla en BigQuery
table_id = "category_details"

# Crea referencia a la tabla en BigQuery
table_ref = client.dataset(dataset_id).table(table_id)

# Solicitud de API: buscar la tabla
table = client.get_table(table_ref)

# Recupere todos los datos de la tabla en un DataFrame de pandas
data_det = client.list_rows(table).to_dataframe()

# crear una matriz de características de los juegos
tfidv = TfidfVectorizer(min_df=2, max_df=0.7,
                        token_pattern=r'\b[a-zA-Z0-9]\w+\b')
data_vector = tfidv.fit_transform(data['features'])

data_vector_df = pd.DataFrame(data_vector.toarray(
), index=data['category'], columns=tfidv.get_feature_names_out())

# calcular la similitud coseno entre los juegos en la matriz de características
vector_similitud_coseno = cosine_similarity(data_vector_df.values)

cos_sim_df = pd.DataFrame(vector_similitud_coseno,
                          index=data_vector_df.index, columns=data_vector_df.index)

rest_simil = cos_sim_df.loc[category1]
simil_ordenada = rest_simil.sort_values(ascending=False)
resultado = simil_ordenada.head(6).reset_index()

if not resultado.empty:
    result_df = resultado.merge(data_det, on='category', how='left')
    result_df = result_df[['name_y', 'category_det', 'state', 'features']][1:6]

    try:
        st.markdown(
            " A demas, sugerimos que se observen con atencion los casos de exitos garantizados similares a las caracteristicas que has escogido: ")
        st.dataframe(result_df)

    except Exception as e:
        st.write('Lo siento, este para el estado de' + sta +
                 'no existe restaurante de categoria ' + cat, str(e))

else:
    st.write('No se encontraron resultados.')
