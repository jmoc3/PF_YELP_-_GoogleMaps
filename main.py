import pandas as pd
import streamlit as st
import joblib
import warnings
import matplotlib.pyplot as plt

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

warnings.filterwarnings("ignore")

modelo = joblib.load("./modelo/modelo_ml.pkl")

# clase 'Regular' por defualt
class1 = 0

st.title('Predicción de Probabilidad de Éxito de un Nuevo Restaurant')
st.markdown('***')
# ---------------------------------------------------------------
# eleccion de categoria

# Recupere todos los datos de la tabla en un DataFrame de pandas
df = pd.read_csv('./modelo/atributos_csv/category.csv')

# Crear una lista desplegable con los valores de 'category'
cat = st.sidebar.selectbox(
    'Selecciona una Categoria',
    df['category'])

category = df[df['category'] == cat]['category_int'].values[0]

# st.write(category)
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
# eleccion de estado

# Recupere todos los datos de la tabla en un DataFrame de pandas
df = pd.read_csv('./modelo/atributos_csv/estados.csv')

# Crear un conjunto de botones de opción con los valores de 'state'
sta = st.sidebar.radio(
    'Selecciona un Estado',
    df['state'])

# st.write('Has seleccionado:', sta)

state = df[df['state'] == sta]['state_int'].values[0]

# st.write(state)
# ---------------------------------------------------------------
# data de estados
df_states = pd.read_csv('./modelo/atributos_csv/data_states.csv')

try:
    num_rest = df_states[(df_states['category'] == cat) & (
        df_states['state'] == sta)].groupby('state').size().values[0]
except:
    num_rest = 0
# ---------------------------------------------------------------
# ---------------------------------------------------------------
st.write('## Para Restaurante de Categoría', cat, 'en el Estado de', sta)
st.write('## Existen:', num_rest, 'locales')
st.markdown('***')
# ---------------------------------------------------------------
# Gráficos

col11, col21 = st.columns(2)
with col11:
    # grafico de cantidad de restaurantes de categoria por estado
    cant_por_estado = df_states[df_states['category'] == cat][[
        'state']].groupby('state').size().sort_values(ascending=False)

    plt.figure()
    color = 'white'
    plt.bar(cant_por_estado.index, cant_por_estado.values)
    plt.xlabel('Estado', color=color)
    plt.ylabel('Número de restaurantes', color=color)
    plt.title('Número de restaurantes por estado', color=color)
    plt.tick_params(colors=color)
    plt.xticks(rotation=90, color=color)
    st.pyplot(plt, transparent=True)

with col21:
    # grafico de clases
    class_por_estado = df_states[(df_states['state'] == sta) & (df_states['category'] == cat)][[
        'class']].groupby('class').size().sort_values(ascending=False)
    plt.figure()
    color = 'white'
    labels = [f'{index} ({value})' for index, value in zip(
        class_por_estado.index, class_por_estado.values)]
    plt.pie(class_por_estado.values, labels=labels,
            autopct='%1.1f%%', textprops={'fontsize': 10, 'color': 'white'})
    plt.title('% Clases de Restaurantes para Estado y Categoría',
              fontsize=(10), color=color)
    st.pyplot(plt, transparent=True)

# grafico de restaurantes por categoria
cate_por_estado = df_states[df_states['state'] == sta][['category']].groupby(
    'category').size().sort_values(ascending=False).head(20)

plt.figure(figsize=(10, 4))
color = 'white'
plt.bar(cate_por_estado.index, cate_por_estado.values)
plt.xlabel('Categoría', color=color)
plt.ylabel('Número de restaurantes', color=color)
plt.title('Número de restaurantes por categoría', color=color)
plt.tick_params(colors=color)
plt.xticks(rotation=90)
st.pyplot(plt, transparent=True)


# ---------------------------------------------------------------
st.markdown('### Selección de Servicios:')
# eleccion de servicio 0

# Recupere todos los datos de la tabla en un DataFrame de pandas
df1 = pd.read_csv('./modelo/atributos_csv/Service0.csv')

# ---------------------------------------------------------------
# eleccion de servicio 1

# Recupere todos los datos de la tabla en un DataFrame de pandas
df2 = pd.read_csv('./modelo/atributos_csv/Service1.csv')

# ---------------------------------------------------------------
# eleccion de servicio 2

# Recupere todos los datos de la tabla en un DataFrame de pandas
df3 = pd.read_csv('./modelo/atributos_csv/Service2.csv')

# Divide la pantalla en tres columnas
col1, col2, col3 = st.columns(3)

# Agrega una lista desplegable en cada columna
# Crear una lista desplegable con los valores de 'servicio 1'
with col1:
    Ser0 = st.selectbox(
        'Servicio 1',
        df1['Service0'])

    # st.write('Has seleccionado:', Ser0)

    Service0 = df1[df1['Service0'] == Ser0]['Service0_int'].values[0]

    # st.write(Service0)

# Crear una lista desplegable con los valores de 'servicio 2'
with col2:
    Ser1 = st.selectbox(
        'Servicio 2',
        df2['Service1'])

    # st.write('Has seleccionado:', Ser1)

    Service1 = df2[df2['Service1'] == Ser1]['Service1_int'].values[0]

    # st.write(Service1)

# Crear una lista desplegable con los valores de 'servicio 3'
with col3:
    Ser2 = st.selectbox(
        'Servicio 3',
        df3['Service2'])

    # st.write('Has seleccionado:', Ser2)

    Service2 = df3[df3['Service2'] == Ser2]['Service2_int'].values[0]
    # st.write(Service2)

# ---------------------------------------------------------------
st.markdown('### Selección de Acceso Preferencial:')
# eleccion de Accecibilidad

# Recupere todos los datos de la tabla en un DataFrame de pandas
df = pd.read_csv('./modelo/atributos_csv/Accessibilidad.csv')

# Crear una lista desplegable con los valores de 'Accecibilidad'
Acc = st.selectbox(
    'Seleccione una opción',
    df['Accessibility0'])

# st.write('Has seleccionado:', Acc)

Accessibility0 = df[df['Accessibility0']
                    == Acc]['Accessibility0_int'].values[0]

# st.write(Accessibility0)
# ---------------------------------------------------------------
st.markdown('### Selección de Ofrecimientos:')
# eleccion de Ofertas

# Recupere todos los datos de la tabla en un DataFrame de pandas
df4 = pd.read_csv('./modelo/atributos_csv/Offerings0.csv')
# ---------------------------------------------------------------
# eleccion de Ofertas

# Recupere todos los datos de la tabla en un DataFrame de pandas
df5 = pd.read_csv('./modelo/atributos_csv/Offerings1.csv')
# ---------------------------------------------------------------
# eleccion de Ofertas

# Recupere todos los datos de la tabla en un DataFrame de pandas
df6 = pd.read_csv('./modelo/atributos_csv/Offerings2.csv')

# Crear una lista desplegable con los valores de 'Ofertas'

# Divide la pantalla en tres columnas
col4, col5, col6 = st.columns(3)

# Agrega una lista desplegable en cada columna
# Crear una lista desplegable con los valores de 'Ofertas'
with col4:
    Off0 = st.selectbox(
        'Oferta 1',
        df4['Offerings0'])

    # st.write('Has seleccionado:', Off0)

    Offerings0 = df4[df4['Offerings0']
                     == Off0]['Offerings0_int'].values[0]

    # st.write(Offerings0)

# Crear una lista desplegable con los valores de 'Ofertas'
with col5:

    Off1 = st.selectbox(
        'Oferta 2',
        df5['Offerings1'])

    # st.write('Has seleccionado:', Off1)

    Offerings1 = df5[df5['Offerings1']
                     == Off1]['Offerings1_int'].values[0]

    # st.write(Offerings1)

# Crear una lista desplegable con los valores de 'servicio 3'
with col6:
    Off2 = st.selectbox(
        'Oferta 3',
        df6['Offerings2'])

    # st.write('Has seleccionado:', Off2)

    Offerings2 = df6[df6['Offerings2']
                     == Off2]['Offerings2_int'].values[0]

    # st.write(Offerings2)
# ---------------------------------------------------------------
st.markdown('### Selección de Amenidad, Tipo de Atmosfera y Tipo de Público:')
# eleccion de Amenidades

# Recupere todos los datos de la tabla en un DataFrame de pandas
df7 = pd.read_csv('./modelo/atributos_csv/Amenities0.csv')
# ---------------------------------------------------------------
# eleccion de Atmosfera
# Recupere todos los datos de la tabla en un DataFrame de pandas
df8 = pd.read_csv('./modelo/atributos_csv/Atmosphere0.csv')
# ---------------------------------------------------------------
# eleccion de Enfoque

# Recupere todos los datos de la tabla en un DataFrame de pandas
df9 = pd.read_csv('./modelo/atributos_csv/Crowd0.csv')

# Divide la pantalla en tres columnas
col7, col8, col9 = st.columns(3)

# Agrega una lista desplegable en cada columna
# Crear una lista desplegable con los valores de 'Amenidades'
with col7:
    Ame = st.selectbox(
        'Amenidad',
        df7['Amenities0'])

    # st.write('Has seleccionado:', Ame)

    Amenities0 = df7[df7['Amenities0']
                     == Ame]['Amenities0_int'].values[0]

# st.write(Amenities0)

# Crear una lista desplegable con los valores de 'Atmosferas'
with col8:
    Atm = st.selectbox(
        'Atmósfera',
        df8['Atmosphere0'])

    # st.write('Has seleccionado:', Atm)

    Atmosphere0 = df8[df8['Atmosphere0']
                      == Atm]['Atmosphere0_int'].values[0]

    # st.write(Atmosphere0)

# Crear una lista desplegable con los valores de 'Enfoques'
with col9:
    Cro = st.selectbox(
        'Público',
        df9['Crowd0'])

    # st.write('Has seleccionado:', Cro)

    Crowd0 = df9[df9['Crowd0']
                 == Cro]['Crowd0_int'].values[0]

    # st.write(Crowd0)


# sistema de clasificacion con árbol de decisión para determinar que clase es el restaurant
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

# Recupere todos los datos de la tabla en un DataFrame de pandas
data_details = pd.read_csv('./modelo/category_details.csv')

data_details = data_details[(data_details['category_det'] == cat) & (
    data_details['state'] == sta)]

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


try:
    caracteristicas = data_details.loc[data_details['name_y']
                                       == nombre, 'features'].values[0]

    st.markdown(" El Restaurant de Referencia: " + nombre + ", esta ubicado en el Estado de " + sta +
                " y es de la categoría de " + cat + " el mismo es de clase Premiun y cuenta con las siguientes caracteristicas: " + caracteristicas)

    # sistema de recomendacion por similitud de coseno
    category1 = cat + ' - ' + sta + ' - ' + nombre

    # se carga los datasets que se va a utilizar para dos dataframes distintos

    # Recupere todos los datos de la tabla en un DataFrame de pandas
    data = pd.read_csv('./modelo/category_features.csv')

    # Recupere todos los datos de la tabla en un DataFrame de pandas
    data_det = pd.read_csv('./modelo/category_details.csv')

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
        result_df = result_df[[
            'name_y', 'category_det', 'state', 'features']][1:6]

        try:
            st.markdown(
                " A demas, sugerimos que se observen con atencion los casos de exitos garantizados similares a las caracteristicas que has escogido: ")
            st.dataframe(result_df)

        except Exception as e:
            st.write('Lo siento, este para el estado de' + sta +
                     'no existe restaurante de categoria ' + cat, str(e))

except:
    st.write('No existen Restaurantes con características similares.')
# ---------------------------------------------------------------
