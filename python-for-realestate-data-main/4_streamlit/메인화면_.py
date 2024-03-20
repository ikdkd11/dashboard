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

st.set_page_config(
    page_title="결빙관측 대시보드",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.header('2번국도(보성(초당교차로)~광양(마룡교)) 결빙관측 관측회차 별 노면온도 시계열 그래프') 
vis_trade_rent1 = tot2.grp2
trade_count1 = tot2.grp4
trade_mean1 = tot2.grp3            
trade_mean_map1 = tot2.grp1
mmap1 = mapp5.map61
tab1, tab2, tab3, tab4 = st.tabs(["1차 관측", "2차 관측", "3차 관측", "4차 관측"])
with tab1:
# 첫 번째 차트
    st.plotly_chart(trade_mean_map1, use_container_width=True)
    st.plotly_chart(mmap1, use_container_width=True)
with tab2:
# 두 번째 차트
    st.plotly_chart(vis_trade_rent1, use_container_width=True)
with tab3:
# 세 번째 차트
    st.plotly_chart(trade_mean1, use_container_width=True)
with tab4:
# 네 번째 차트
    st.plotly_chart(trade_count1, use_container_width=True)

#5
#st_folium(mmap1, width=1000)
#col1, col2 = st.columns([1,1])
#col1.plotly_chart(trade_mean_map1, use_container_width = True) 
#col2.plotly_chart(vis_trade_rent1, use_container_width = True)


#col1, col2 = st.columns([1,1])
#col1.plotly_chart(trade_mean1, use_container_width = True)
#col2.plotly_chart(trade_count1, use_container_width = True)


