import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="나의 포트폴리오", page_icon="👋", layout="wide")

# 헤더 섹션
st.title("안녕하세요! 데이터 분석가 OOO입니다. 👋")
st.write("파이썬과 데이터를 활용해 가치 있는 인사이트를 도출하는 것을 좋아합니다.")

st.divider() # 구분선

# 프로젝트 섹션
st.header("💡 주요 프로젝트")
col1, col2 = st.columns(2) # 화면을 두 개의 열로 나눔

with col1:
    st.subheader("1. 캐글 데이터 분석")
    st.write("- 머신러닝 모델을 활용한 예측")
    st.write("- 성과: 상위 랭킹 달성")

with col2:
    st.subheader("2. 시계열 데이터 대시보드")
    st.write("- 금융 데이터 수집 및 분석")
    st.write("- 향후 트레이딩 봇 연동 예정")