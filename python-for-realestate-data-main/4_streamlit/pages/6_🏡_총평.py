import pandas as pd
import os
import geopandas as gpd
import glob
import plotly.express as px
import plotly.graph_objects as go
import folium
import json
import math
import plotbox
import streamlit as st
from datetime import datetime
from PIL import Image
import requests
from io import BytesIO
import tot3
import mapp4
import tta

st.header('위험구간 분류')
st.text('위험구간: 노면온도가 2~3초 이내에 섭씨 1도 이상 급락하는 구간')    
st.subheader('위험구간 중 90%가 고각이나 터널 출입구에 나타남')
st.write('교각의 경우: 육상 교량에서 노면온도 감소 효과가 수상 교량에서보다 더욱 크고 기상 조건에 영향을 덜 받는 특성을 확인함')
