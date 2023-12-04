import pandas as pd
import streamlit as st
import joblib
import warnings

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

warnings.filterwarnings("ignore")

modelo = joblib.load("modelo_ml.pkl")

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

df = pd.read_csv('atributos_csv\category.csv')

# Crear una lista desplegable con los valores de 'category'
cat = st.selectbox(
    'Selecciona una Categoria',
    df['category'])

st.write('Has seleccionado:', cat)

category = df[df['category'] == cat]['category_int'].values[0]

# st.write(category)
# ---------------------------------------------------------------
# eleccion de estado

df = pd.read_csv('atributos_csv\estados.csv')

# Crear un conjunto de botones de opción con los valores de 'state'
sta = st.sidebar.radio(
    'Selecciona un Estado',
    df['state'])

# st.write('Has seleccionado:', sta)

state = df[df['state'] == sta]['state_int'].values[0]

# st.write(state)
# ---------------------------------------------------------------
# eleccion de servicio 0

df = pd.read_csv('atributos_csv\Service0.csv')

# Crear una lista desplegable con los valores de 'servicio'
Ser0 = st.selectbox(
    'Servicio 1 a ofrecer',
    df['Service0'])

st.write('Has seleccionado:', Ser0)

Service0 = df[df['Service0'] == Ser0]['Service0_int'].values[0]

# st.write(Service0)
# ---------------------------------------------------------------
# eleccion de servicio 1

df = pd.read_csv('atributos_csv\Service1.csv')

# Crear una lista desplegable con los valores de 'servicio'
Ser1 = st.selectbox(
    'Servicio 2 a ofrecer',
    df['Service1'])

st.write('Has seleccionado:', Ser1)

Service1 = df[df['Service1'] == Ser1]['Service1_int'].values[0]

# st.write(Service1)
# ---------------------------------------------------------------
# eleccion de servicio 2

df = pd.read_csv('atributos_csv\Service2.csv')

# Crear una lista desplegable con los valores de 'servicio'
Ser2 = st.selectbox(
    'Servicio 3 a ofrecer',
    df['Service2'])

st.write('Has seleccionado:', Ser2)

Service2 = df[df['Service2'] == Ser2]['Service2_int'].values[0]

# st.write(Service2)
# ---------------------------------------------------------------
# eleccion de Accecibilidad

df = pd.read_csv('atributos_csv\Accessibilidad.csv')

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

df = pd.read_csv('atributos_csv\Offerings0.csv')

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

df = pd.read_csv('atributos_csv\Offerings1.csv')

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

df = pd.read_csv('atributos_csv\Offerings2.csv')

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

df = pd.read_csv('atributos_csv\Amenities0.csv')

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

df = pd.read_csv('atributos_csv\Atmosphere0.csv')

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

df = pd.read_csv('atributos_csv\Crowd0.csv')

# Crear una lista desplegable con los valores de 'Enfoques'
Cro = st.selectbox(
    'Seleccione un Público',
    df['Crowd0'])

st.write('Has seleccionado:', Cro)

Crowd0 = df[df['Crowd0']
            == Cro]['Crowd0_int'].values[0]

# st.write(Crowd0)


# Supongamos que tienes el siguiente DataFrame
x_prueba = pd.DataFrame(columns=('rating', 'category_int', 'state_int', 'Service0_int', 'Service1_int', 'Service2_int', 'Accessibility0_int', 'Offerings0_int',
                                 'Offerings1_int', 'Offerings2_int', 'Amenities0_int', 'Atmosphere0_int', 'Crowd0_int', 'class1'))

# Supongamos que tienes los siguientes datos
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
data_details = pd.read_csv('category_details.csv')
data_details = data_details[(data_details['category_det'] == cat) & (
    data_details['state'] == sta)]

# Crear una lista desplegable con los valores de 'name_y'
nombre = st.selectbox(
    'Selecciona un Restaurante de Referencia',
    data_details['name_y'])

st.write('Has seleccionado:', nombre)

caracteristicas = data_details.loc[data_details['name_y']
                                   == nombre, 'features'].values[0]


st.markdown(" El Restaurant de Referencia: " + nombre + ", esta ubicado en el Estado de " + sta +
            " y es de la categoría de " + cat + " el mismo es de clase Premiun y cuenta con las siguientes caracteristicas: " + caracteristicas)
# ---------------------------------------------------------------
# se carga los datasets que se va a utilizar para dos dataframes distintos

category1 = cat + ' - ' + sta + ' - ' + nombre
print(category1)

data = pd.read_csv('category_features.csv')
data_det = pd.read_csv('category_details.csv')

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

result_df = resultado.merge(data_det, on='category', how='left')
result_df = result_df[['name_y', 'state', 'features']][1:6]

st.markdown(" A demas, sugerimos que se observen con atencion los casos de exitos garantizados similares a las caracteristicas que has escogido: ")
st.dataframe(result_df)
