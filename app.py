import streamlit as st
import pandas as pd

# 페이지 기본 설정
st.set_page_config(page_title="나의 포트폴리오", page_icon="👋", layout="wide")

# 헤더 섹션
st.title("안녕하세요! 데이터 분석가 OOO입니다. 👋")
st.write("파이썬과 데이터를 활용해 가치 있는 인사이트를 도출하는 것을 좋아합니다.")

st.divider() # 구분선

# --- 📊 데이터 분석 역량 보여주기 ---
st.header("📊 프로젝트 성과 시각화")

# 1. 파이썬 Pandas로 표(DataFrame) 만들기
st.subheader("✅ 주요 프로젝트 성과 요약 (표)")

# 실제 프로젝트 결과를 데이터프레임으로 정의
project_summary_data = {
    'Project Name': ['캐글 타이타닉 생존 예측', '주택 가격 회귀 분석', '이커머스 고객 세그먼테이션'],
    'Score (Metric)': [0.912, 'RMSE 0.125', 'Silhouette Score 0.65'],
    'Rank (Top %)' : ['1.2%', '5.0%', '8.3%'],
    'Status': ['Completed', 'Completed', 'In Progress']
}
df = pd.DataFrame(project_summary_data) # 딕셔너리를 판다스 데이터프레임으로 변환

# 스트림릿에서 인터랙티브한 표 보여주기 (정렬, 검색 가능)
# use_container_width=True: 화면 너비에 맞게 표 확장
st.dataframe(df, use_container_width=True)


st.divider() # 구분선


# 2. 스트림릿 자체 그래프로 시각화하기 (막대 그래프)
st.subheader("📈 학습 및 분석 활동 시간 (그래프)")

# 그래프를 위한 간단한 데이터프레임 만들기 (월별 학습 시간 예시)
# index가 x축, data가 y축이 됩니다.
learning_hours_data = pd.DataFrame({
    'Hours': [20, 35, 30, 45, 50, 40]
}, index=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']) # x축 라벨 설정

# 스트림릿 막대 그래프 그리기 (매우 쉬움!)
st.bar_chart(learning_hours_data)
st.write("* 월별 데이터 분석 학습 및 프로젝트 수행 시간*")