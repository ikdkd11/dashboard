import pandas as pd
import os
import geopandas as gpd
import glob
import plotly.express as px
import plotly.graph_objects as go
import folium
# import folium
import json
# import math
import tot2
import plotbox
import streamlit as st
from datetime import datetime
from PIL import Image
from folium.plugins import DualMap
from branca.colormap import LinearColormap
import mapp5

#github로부터 데이터 파일을 읽어오기 위한 raw url
url_bar = 'https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data_bar-main/0_data_bar/streamlit_data_bar/result_data_bar1.csv'

# 데이터 불러오기
data_bar = pd.read_csv(url_bar)

# 필요없는 열 제거
data_bar = data_bar.drop(['행정구역', '이름'], axis=1)

# 결측치 제거
data_bar = data_bar.dropna()

