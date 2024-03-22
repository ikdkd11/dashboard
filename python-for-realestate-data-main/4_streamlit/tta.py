import pandas as pd

# CSV 파일을 읽어들입니다.
url1 = 'https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/plot11.csv'
url2 = "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/plot2.csv"
data1 = pd.read_csv(url1)
data2 = pd.read_csv(url2)
# '차수'열에서 숫자만 추출합니다.
data1['차수'] = data1['차수'].str.extract('(\d+)').astype(int)
data2['차수'] = data2['차수'].str.extract('(\d+)').astype(int)
# '구분'별과 '차수'별로 그룹화하여 '온도'의 평균을 계산합니다.
average_temperatures1 = data1.groupby(['구분', '차수'])['온도'].mean().unstack()
average_temperatures2 = data2.groupby(['구분', '차수'])['온도'].mean().unstack()
# 구분 순서를 지정하고, 소수 첫째 자리까지 나오게 조정합니다.
custom_order = ['구간 전체', '진입 전', '급락구간']

average_temperatures1 = average_temperatures1.reindex(custom_order).round(1)
average_temperatures2 = average_temperatures2.reindex(custom_order).round(1)

average_temperatures1.columns = ['1차 관측', '2차 관측', '3차 관측', '4차 관측']
average_temperatures2.columns = ['1차 관측', '2차 관측', '3차 관측', '4차 관측']
