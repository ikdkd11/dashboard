import folium
import pandas as pd
import branca.colormap as cm
import pandas as pd
import plotly.graph_objects as go

# 데이터 불러오기
url = "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/1_1.csv"
df = pd.read_csv(url)

# 평균 위도와 경도 계산
avg_lat = df["위도"].mean()
avg_lon = df["경도"].mean()

# Plotly Graph Objects를 사용한 시각화
def create_graph(df):
    fig = go.Figure(go.Scattermapbox(
        lat=df["위도"],
        lon=df["경도"],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=15,
            color=df["노면온도"],
            colorscale="Plasma",
            cmin=df["노면온도"].min(),
            cmax=df["노면온도"].max(),
            showscale=True,
        ),
        text=df["노면온도"],
    ))

    fig.update_layout(
        mapbox=dict(
            style="open-street-map",
            center=dict(lat=avg_lat, lon=avg_lon),
            zoom=15,
        ),
        showlegend=False,
    )
    return fig
map11 = create_graph(df)
