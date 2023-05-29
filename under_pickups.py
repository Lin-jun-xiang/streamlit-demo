import streamlit as st
import pandas as pd
import numpy as np


# 定義 page name
st.set_page_config(
        page_title="Streamlit Demo App",
)


# 標題
st.title('Uber pickups in NYC')


# 獲取一些數據
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


## Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
## Load 10,000 rows of data into the dataframe.
data = load_data(10000)
## Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')


# 檢查原始數據
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


# 繪製直方圖
st.subheader('Number of pickups by hour')

## 使用 NumPy 生成一個直方圖，該直方圖按小時劃分取件時間:
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)


# 在地圖上繪製數據
st.subheader('Map of all pickups')
st.map(data)

# 使用 Slider 過濾結果
hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

