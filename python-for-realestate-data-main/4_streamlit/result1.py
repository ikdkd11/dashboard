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

# 평균 계산을 위한 그룹화
grouped = data_bar.groupby(['차수', '종류'])['변화량'].mean().reset_index()

# 전체 평균 계산
overall_mean = data_bar.groupby('종류')['변화량'].mean().reset_index()
overall_mean['차수'] = '전체'  # 새로운 열 '차수'에 '전체'로 설정

# 두 data_barFrame 병합
combined = pd.concat([grouped, overall_mean], ignore_index=True)

# 막대 그래프 생성
def create_graph(combined):
    fig = px.bar(combined, x='차수', y='변화량', color='종류', barmode='group',
                title='차수별 종류에 따른 변화량 평균', text=combined['변화량'].round(1).astype(str))

    # 레이아웃 조정
    fig.update_layout(
        xaxis_tickangle=0,
        xaxis_title_font=dict(size=20),
        yaxis_title_font=dict(size=20),
        xaxis_tickfont=dict(size=23),
        yaxis_tickfont=dict(size=23),
        xaxis_title='관측 회차',  # x축 제목 변경
        yaxis_title='노면온도 감소량'  # y축 제목 변경
    )

    # 텍스트 글꼴 크기 조정
    fig.update_traces(textfont_size=20, textangle=0, textposition="outside", cliponaxis=False)
    return fig

    # 그래프 출력
bar1 = create_graph(combined)
    fig.show()