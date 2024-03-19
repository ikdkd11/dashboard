import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import plotly.graph_objects as go
from PIL import Image
import streamlit as st

# 파일명과 해당 파일을 저장할 DataFrame 변수명 매핑
url1 = (
    "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/1stD.csv"
)
url2 = (
    "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/2ndD.csv"
    )
url3 = (
    "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/3rdD.csv"
    )
url4 = (
    "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/4thD.csv"
    )
url5 = (
    "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/5thD.csv"
)

df11 = pd.read_csv(url1)
df22 = pd.read_csv(url2)
df33 = pd.read_csv(url3)
df44 = pd.read_csv(url4)
df55 = pd.read_csv(url5)

df11_cleaned = df11.dropna()

# plotly를 사용하여 그래프 그리기
def create_graph(df11_cleaned):
    fig = go.Figure()

    # 기온 데이터 색상 (빨간색 계열)
    #temp_colors = ['rgb(255,0,0)', 'rgb(255,99,71)', 'rgb(255,69,0)', 'rgb(220,20,60)']
    # 노면온도 데이터 색상 (파란색 계열)
    road_temp_colors = [' rgb(204, 37, 41)', 'rgb(0, 158, 115)', 'rgb(255, 128, 0)', 'rgb(0, 114, 178)']

    #road_temp_colors = ['rgb(0,0,255)', 'rgb(30,144,255)', 'rgb(70,130,180)', 'rgb(100,149,237)']

    # 노면온도 데이터 추가
    for i in range(1, 5):
        fig.add_trace(go.Scatter(
            mode='lines',
            x=df11_cleaned.index,  # 인덱스를 x축 데이터로 사용
            y=df11_cleaned[f'노면온도({i}차)'],
            name=f'노면온도({i}차)',
            line=dict(color=road_temp_colors[i-1], width=2),
            connectgaps=True
        ))

    ##그래프에 도로 구간정보 주석으로 삽입
    # x=40 보성교에 1차 관측 주석 추가
    fig.add_annotation(
        x=40,  # 주석을 달고 싶은 x축 좌표 위치
        y=df11_cleaned.loc[df11_cleaned.index == 40, '노면온도(1차)'].values[0],  # 예시로 1차 노면온도 사용
        text='초당교(초당교차로)(1차)',  # 주석에 표시될 텍스트
        showarrow=True,  # 화살표 표시 여부
        arrowhead=3,  # 화살표 머리 스타일
        ax=90,  # 화살표의 x축 방향 길이 (음수 값 사용하여 왼쪽으로 이동)
        ay=-20,  # 화살표의 y축 방향 길이 (음수 값 사용하여 위로 이동)
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1,  # 화살표 크기
        bgcolor='rgba(0, 0, 0, 0.8)',  # 배경색
        font=dict(color='white', size=14)  # 글자색 및 크기 설정
    )
    # x=40 보성교에 2차 관측 주석 추가
    fig.add_annotation(
        x=40,  # 주석을 달고 싶은 x축 좌표 위치
        y=df11_cleaned.loc[df11_cleaned.index == 40, '노면온도(2차)'].values[0],  # 예시로 1차 노면온도 사용
        text='초당교(초당교차로)(2~4차)',  # 주석에 표시될 텍스트
        showarrow=True,  # 화살표 표시 여부
        arrowhead=3,  # 화살표 머리 스타일
        ax=-90,  # 화살표의 x축 방향 길이 (음수 값 사용하여 왼쪽으로 이동)
        ay=-35,  # 화살표의 y축 방향 길이 (음수 값 사용하여 위로 이동)
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1,  # 화살표 크기
        bgcolor='rgba(0, 0, 0, 0.8)',  # 배경색
        font=dict(color='white', size=14)  # 글자색 및 크기 설정
    )

    # 그래프 레이아웃 설정
    fig.update_layout(
        title=dict(
            text='위험구간1: [초당교] - 관측 회차 별 노면온도 시계열 비교',
            font=dict(size=20, color="black")  # 볼드 폰트로 변경
        ),
        xaxis=dict(title='방향 : 보성 > 광양'),
        yaxis=dict(title='온도(°C)'),
        hovermode="x"
    )
    return fig
grp11 = create_graph(df11_cleaned)

# NaN 값을 가진 행 제거

df22_cleaned = df22.dropna()

def create_graph(df22_cleaned):
    fig = go.Figure()
    # 기온 데이터 색상 (빨간색 계열)
    #temp_colors = ['rgb(255,0,0)', 'rgb(255,99,71)', 'rgb(255,69,0)', 'rgb(220,20,60)']
    # 노면온도 데이터 색상 (파란색 계열)
    road_temp_colors = [' rgb(204, 37, 41)', 'rgb(0, 158, 115)', 'rgb(255, 128, 0)', 'rgb(0, 114, 178)']

    # 노면온도 데이터 추가
    for i in range(1, 5):
        fig.add_trace(go.Scatter(
            mode='lines',
            x=df22_cleaned.index,  # 인덱스를 x축 데이터로 사용
            y=df22_cleaned[f'노면온도({i}차)'],
            name=f'노면온도({i}차)',
            line=dict(color=road_temp_colors[i-1], width=2),
            connectgaps=True
        ))

    ##그래프에 도로 구간정보 주석으로 삽입
    # x=86 신월2교고가 하부(남해고속도로 교차지점) 교차 위치에 1차 관측 주석 추가
    fig.add_annotation(
        x=87,  # 주석을 달고 싶은 x축 좌표 위치
        y=df22_cleaned.loc[df22_cleaned.index == 87, '노면온도(1차)'].values[0],  # 예시로 1차 노면온도 사용
        text='남해고속도로 교차점(1차)',  # 주석에 표시될 텍스트
        showarrow=True,  # 화살표 표시 여부
        arrowhead=3,  # 화살표 머리 스타일
        ax=-40,  # 화살표의 x축 방향 길이 (음수 값 사용하여 왼쪽으로 이동)
        ay=100,  # 화살표의 y축 방향 길이 (음수 값 사용하여 위로 이동)
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1,  # 화살표 크기
        bgcolor='rgba(0, 0, 0, 0.8)',  # 배경색
        font=dict(color='white', size=14)  # 글자색 및 크기 설정
    )
    # x=88 신월2교고가 하부(남해고속도로 교차지점) 교차 위치에 3차 관측 주석 추가
    fig.add_annotation(
        x=88,  # 주석을 달고 싶은 x축 좌표 위치
        y=df22_cleaned.loc[df22_cleaned.index == 88, '노면온도(3차)'].values[0],  # 예시로 1차 노면온도 사용
        text='남해고속도로 교차점(2차)',  # 주석에 표시될 텍스트
        showarrow=True,  # 화살표 표시 여부
        arrowhead=3,  # 화살표 머리 스타일
        ax=90,  # 화살표의 x축 방향 길이 (음수 값 사용하여 왼쪽으로 이동)
        ay=-20,  # 화살표의 y축 방향 길이 (음수 값 사용하여 위로 이동)
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1,  # 화살표 크기
        bgcolor='rgba(0, 0, 0, 0.8)',  # 배경색
        font=dict(color='white', size=14)  # 글자색 및 크기 설정
    )
    # x=70 신월2교고가 하부(남해고속도로 교차지점) 교차 위치에 2차 관측 주석 추가
    fig.add_annotation(
        x=70,  # 주석을 달고 싶은 x축 좌표 위치
        y=df22_cleaned.loc[df22_cleaned.index == 70, '노면온도(2차)'].values[0],  # 예시로 1차 노면온도 사용
        text='남해고속도로 교차점(3차)',  # 주석에 표시될 텍스트
        showarrow=True,  # 화살표 표시 여부
        arrowhead=3,  # 화살표 머리 스타일
        ax=-130,  # 화살표의 x축 방향 길이 (음수 값 사용하여 왼쪽으로 이동)
        ay=0,  # 화살표의 y축 방향 길이 (음수 값 사용하여 위로 이동)
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1,  # 화살표 크기
        bgcolor='rgba(0, 0, 0, 0.8)',  # 배경색
        font=dict(color='white', size=14)  # 글자색 및 크기 설정
    )

    # x=87 신월2교고가 하부(남해고속도로 교차지점) 교차 위치에 4차 관측 주석 추가
    fig.add_annotation(
        x=87,  # 주석을 달고 싶은 x축 좌표 위치
        y=df22_cleaned.loc[df22_cleaned.index == 87, '노면온도(4차)'].values[0],  # 예시로 1차 노면온도 사용
        text='남해고속도로 교차점(4차)',  # 주석에 표시될 텍스트
        showarrow=True,  # 화살표 표시 여부
        arrowhead=3,  # 화살표 머리 스타일
        ax=-25,  # 화살표의 x축 방향 길이 (음수 값 사용하여 왼쪽으로 이동)
        ay=80,  # 화살표의 y축 방향 길이 (음수 값 사용하여 위로 이동)
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1,  # 화살표 크기
        bgcolor='rgba(0, 0, 0, 0.8)',  # 배경색
        font=dict(color='white', size=14)  # 글자색 및 크기 설정
    )

    # 그래프 레이아웃 설정
    fig.update_layout(
        title=dict(
            text='위험구간2: [옥전교] - 관측 회차 별 노면온도 시계열 비교',
            font=dict(size=20, color="black")  # 볼드 폰트로 변경
        ),
        xaxis=dict(title='방향 : 보성 > 광양'),
        yaxis=dict(title='온도(°C)'),
        hovermode="x"
    )
    return fig
grp22 = create_graph(df22_cleaned)

##벌교대교

# NaN 값을 가진 행 제거
df33_cleaned = df33.dropna()
# plotly를 사용하여 그래프 그리기
def create_graph(df33):
    fig = go.Figure()

    # 기온 데이터 색상 (빨간색 계열)
    #temp_colors = ['rgb(255,0,0)', 'rgb(255,99,71)', 'rgb(255,69,0)', 'rgb(220,20,60)']
    # 노면온도 데이터 색상 (파란색 계열)
    road_temp_colors = [' rgb(204, 37, 41)', 'rgb(0, 158, 115)', 'rgb(255, 128, 0)', 'rgb(0, 114, 178)']

    #road_temp_colors = ['rgb(0,0,255)', 'rgb(30,144,255)', 'rgb(70,130,180)', 'rgb(100,149,237)']

    # 노면온도 데이터 추가
    for i in range(1, 5):
        fig.add_trace(go.Scatter(
            mode='lines',
            x=df33.index,  # 인덱스를 x축 데이터로 사용
            y=df33[f'노면온도({i}차)'],
            name=f'노면온도({i}차)',
            line=dict(color=road_temp_colors[i-1], width=2),
            connectgaps=True
        ))

    ##그래프에 도로 구간정보 주석으로 삽입
    # x=13 벌교대교 시작위치에 1차 관측 주석 추가
    fig.add_annotation(
        x=13,  # 주석을 달고 싶은 x축 좌표 위치
        y=df33.loc[df33.index == 13, '노면온도(1차)'].values[0],  # 예시로 1차 노면온도 사용
        text='벌교대교(1차)',  # 주석에 표시될 텍스트
        showarrow=True,  # 화살표 표시 여부
        arrowhead=3,  # 화살표 머리 스타일
        ax=-20,  # 화살표의 x축 방향 길이 (음수 값 사용하여 왼쪽으로 이동)
        ay=40,  # 화살표의 y축 방향 길이 (음수 값 사용하여 위로 이동)
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1,  # 화살표 크기
        bgcolor='rgba(0, 0, 0, 0.8)',  # 배경색
        font=dict(color='white', size=14)  # 글자색 및 크기 설정
    )

    # x=12 벌교대교 위치에 2차 관측 주석 추가
    fig.add_annotation(
        x=12,  # 주석을 달고 싶은 x축 좌표 위치
        y=df33.loc[df33.index == 12, '노면온도(2차)'].values[0],  # 예시로 1차 노면온도 사용
        text='벌교대교(2차)',  # 주석에 표시될 텍스트
        showarrow=True,  # 화살표 표시 여부
        arrowhead=3,  # 화살표 머리 스타일
        ax=20,  # 화살표의 x축 방향 길이 (음수 값 사용하여 왼쪽으로 이동)
        ay=-20,  # 화살표의 y축 방향 길이 (음수 값 사용하여 위로 이동)
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1,  # 화살표 크기
        bgcolor='rgba(0, 0, 0, 0.8)',  # 배경색
        font=dict(color='white', size=14)  # 글자색 및 크기 설정
    )

    # x=48 벌교대교 위치에 3차 관측 주석 추가
    fig.add_annotation(
        x=48,  # 주석을 달고 싶은 x축 좌표 위치
        y=df33.loc[df33.index == 48, '노면온도(3차)'].values[0],  # 예시로 1차 노면온도 사용
        text='벌교대교(3차)',  # 주석에 표시될 텍스트
        showarrow=True,  # 화살표 표시 여부
        arrowhead=3,  # 화살표 머리 스타일
        ax=40,  # 화살표의 x축 방향 길이 (음수 값 사용하여 왼쪽으로 이동)
        ay=-18,  # 화살표의 y축 방향 길이 (음수 값 사용하여 위로 이동)
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1,  # 화살표 크기
        bgcolor='rgba(0, 0, 0, 0.8)',  # 배경색
        font=dict(color='white', size=14)  # 글자색 및 크기 설정
    )

    # x=42 벌교대교 위치에 4차 관측 주석 추가
    fig.add_annotation(
        x=42,  # 주석을 달고 싶은 x축 좌표 위치
        y=df33.loc[df33.index == 42, '노면온도(4차)'].values[0],  # 예시로 1차 노면온도 사용
        text='벌교대교(4차)',  # 주석에 표시될 텍스트
        showarrow=True,  # 화살표 표시 여부
        arrowhead=3,  # 화살표 머리 스타일
        ax=50,  # 화살표의 x축 방향 길이 (음수 값 사용하여 왼쪽으로 이동)
        ay=1,  # 화살표의 y축 방향 길이 (음수 값 사용하여 위로 이동)
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1,  # 화살표 크기
        bgcolor='rgba(0, 0, 0, 0.8)',  # 배경색
        font=dict(color='white', size=14)  # 글자색 및 크기 설정
    )

    # x=252 장양육교 위치에 1차 관측 주석 추가
    fig.add_annotation(
        x=252,  # 주석을 달고 싶은 x축 좌표 위치
        y=df33.loc[df33.index == 252, '노면온도(1차)'].values[0],  # 예시로 1차 노면온도 사용
        text='장양육교(1차)',  # 주석에 표시될 텍스트
        showarrow=True,  # 화살표 표시 여부
        arrowhead=3,  # 화살표 머리 스타일
        ax=-50,  # 화살표의 x축 방향 길이 (음수 값 사용하여 왼쪽으로 이동)
        ay=5,  # 화살표의 y축 방향 길이 (음수 값 사용하여 위로 이동)
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1,  # 화살표 크기
        bgcolor='rgba(0, 0, 0, 0.8)',  # 배경색
        font=dict(color='white', size=14)  # 글자색 및 크기 설정
    )

    # x=230 장양육교 위치에 1차 관측 주석 추가
    fig.add_annotation(
        x=230,  # 주석을 달고 싶은 x축 좌표 위치
        y=df33.loc[df33.index == 230, '노면온도(2차)'].values[0],  # 예시로 1차 노면온도 사용
        text='장양육교(2차)',  # 주석에 표시될 텍스트
        showarrow=True,  # 화살표 표시 여부
        arrowhead=3,  # 화살표 머리 스타일
        ax=45,  # 화살표의 x축 방향 길이 (음수 값 사용하여 왼쪽으로 이동)
        ay=-5,  # 화살표의 y축 방향 길이 (음수 값 사용하여 위로 이동)
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1,  # 화살표 크기
        bgcolor='rgba(0, 0, 0, 0.8)',  # 배경색
        font=dict(color='white', size=14)  # 글자색 및 크기 설정
    )

    # x=260 장양육교 위치에 1차 관측 주석 추가
    fig.add_annotation(
        x=260,  # 주석을 달고 싶은 x축 좌표 위치
        y=df33.loc[df33.index == 260, '노면온도(3차)'].values[0],  # 예시로 1차 노면온도 사용
        text='장양육교(3차)',  # 주석에 표시될 텍스트
        showarrow=True,  # 화살표 표시 여부
        arrowhead=3,  # 화살표 머리 스타일
        ax=45,  # 화살표의 x축 방향 길이 (음수 값 사용하여 왼쪽으로 이동)
        ay=-5,  # 화살표의 y축 방향 길이 (음수 값 사용하여 위로 이동)
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1,  # 화살표 크기
        bgcolor='rgba(0, 0, 0, 0.8)',  # 배경색
        font=dict(color='white', size=14)  # 글자색 및 크기 설정
    )
    # x=252 장양육교 위치에 1차 관측 주석 추가
    fig.add_annotation(
        x=252,  # 주석을 달고 싶은 x축 좌표 위치
        y=df33.loc[df33.index == 252, '노면온도(1차)'].values[0],  # 예시로 1차 노면온도 사용
        text='장양육교(1차)',  # 주석에 표시될 텍스트
        showarrow=True,  # 화살표 표시 여부
        arrowhead=3,  # 화살표 머리 스타일
        ax=-50,  # 화살표의 x축 방향 길이 (음수 값 사용하여 왼쪽으로 이동)
        ay=5,  # 화살표의 y축 방향 길이 (음수 값 사용하여 위로 이동)
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1,  # 화살표 크기
        bgcolor='rgba(0, 0, 0, 0.8)',  # 배경색
        font=dict(color='white', size=14)  # 글자색 및 크기 설정
    )

    # x=230 장양육교 위치에 1차 관측 주석 추가
    fig.add_annotation(
        x=230,  # 주석을 달고 싶은 x축 좌표 위치
        y=df33.loc[df33.index == 230, '노면온도(2차)'].values[0],  # 예시로 1차 노면온도 사용
        text='장양육교(2차)',  # 주석에 표시될 텍스트
        showarrow=True,  # 화살표 표시 여부
        arrowhead=3,  # 화살표 머리 스타일
        ax=45,  # 화살표의 x축 방향 길이 (음수 값 사용하여 왼쪽으로 이동)
        ay=-5,  # 화살표의 y축 방향 길이 (음수 값 사용하여 위로 이동)
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1,  # 화살표 크기
        bgcolor='rgba(0, 0, 0, 0.8)',  # 배경색
        font=dict(color='white', size=14)  # 글자색 및 크기 설정
    )

    # x=260 장양육교 위치에 4차 관측 주석 추가
    fig.add_annotation(
        x=264,  # 주석을 달고 싶은 x축 좌표 위치
        y=df33.loc[df33.index == 264, '노면온도(4차)'].values[0],  # 예시로 1차 노면온도 사용
        text='장양육교(4차)',  # 주석에 표시될 텍스트
        showarrow=True,  # 화살표 표시 여부
        arrowhead=3,  # 화살표 머리 스타일
        ax=-55,  # 화살표의 x축 방향 길이 (음수 값 사용하여 왼쪽으로 이동)
        ay=-5,  # 화살표의 y축 방향 길이 (음수 값 사용하여 위로 이동)
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1,  # 화살표 크기
        bgcolor='rgba(0, 0, 0, 0.8)',  # 배경색
        font=dict(color='white', size=14)  # 글자색 및 크기 설정
    )
    fig.update_layout(
    title=dict(
        text='위험구간3: [벌교대교] - 관측 회차 별 노면온도 시계열 비교',
        font=dict(size=20, color="black")
    ),
    xaxis=dict(title='방향 : 보성 > 광양'),
    yaxis=dict(title='온도(°C)'),
    hovermode="x"
    )
    return fig
grp33 = create_graph(df33)
grp33.show()
