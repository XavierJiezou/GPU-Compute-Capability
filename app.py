import streamlit as st
from script.db import DB
import json


@st.cache()
def run_query(word, limit=5):
    db_name = 'data/cuda-gpus.db'
    table_name = 'GPUS'
    columns = {'ID': 'TEXT', 'CC': 'REAL'}
    res = DB(db_name).select_gpus(table_name, columns, word)
    return res[:limit]


def run_query_left():
    word = st.session_state.lid
    st.session_state.lcc = run_query(word)


def run_query_right():
    word = st.session_state.rid
    st.session_state.rcc = run_query(word)


def comparision():
    left_column, right_column = st.columns(2)

    with left_column:
        st.text_input('GPU Name 1', key='lid', on_change=run_query_left)
        if 'lcc' not in st.session_state:
            pass
        else:
            data = {'GPU': [], 'Compute Capability': []}
            for item in st.session_state.lcc:
                data['GPU'].append(item[0])
                data['Compute Capability'].append(item[1])
            st.table(data)

    with right_column:
        st.text_input('GPU Name 2', key='rid', on_change=run_query_right)
        if 'rcc' not in st.session_state:
            pass
        else:
            data = {'GPU': [], 'Compute Capability': []}
            for item in st.session_state.rcc:
                data['GPU'].append(item[0])
                data['Compute Capability'].append(item[1])
            st.table(data)


@st.cache
def load_json():
    with open('data/cuda-gpus.json') as fp:
        data = json.load(fp)
    return data


def table():
    data = load_json()
    for i in data:
        for j in data[i]:
            with st.expander(f'{i}/{j}'):
                st.table(data[i][j])


def json_preview():
    with st.expander('Json preivew'):
        data = load_json()
        with open('data/cuda-gpus.json', 'rb') as fp:
            st.download_button('Download', fp, 'cuda-gpus.json')
        st.write(data)


def app():
    st.set_page_config(
        page_title='GPU-Compute-Capability',
        page_icon=':rocket:',
        layout='centered',
        initial_sidebar_state='auto',
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': 'https://www.extremelycoolapp.com/bug',
            'About': 'An application for querying the computing power of each gpu released by NVIDIA.'
        }
    )

    st.title('GPU-Compute-Capability')

    st.header('Comparision')

    comparision()

    st.header('Table')

    table()

    st.header('Json')

    json_preview()


if __name__ == '__main__':
    app()
