import streamlit as st
import pandas as pd
from PIL import Image
import requests
from io import BytesIO

# --- 기본 설정 ---
st.set_page_config(page_title="saub03's Portfolio", page_icon="👋", layout="wide")

# --- 💡 헤더 섹션 (image_5.png의 최상단) ---
header_col1, header_col2 = st.columns([1, 4]) # 사진과 인사말 비율 (1:4)

with header_col1:
    # (1) 사진: 깃허브 프로필 사진 URL 사용 (둥글게 처리하는 것은 CSS가 필요하므로 일단은 기본으로 띄웁니다.)
    github_profile_img_url = "https://github.com/saub03.png"
    
    # URL에서 이미지를 다운로드하여 PIL Image 개체로 변환
    try:
        response = requests.get(github_profile_img_url)
        img = Image.open(BytesIO(response.content))
        # Streamlit st.image로 이미지 띄우기
        st.image(img, use_container_width=True, caption="@saub03")
    except Exception as e:
        # 이미지를 가져오지 못할 경우 더미 텍스트를 띄웁니다.
        st.error(f"프로필 이미지를 불러오지 못했습니다. {e}")
        st.text("사진 (더미)")

with header_col2:
    # (2) 인사말: 마크다운을 활용해 와이어프레임대로 구성
    st.title("안녕하세요! 데이터 분석을 공부하는 **김희우**입니다.")
    st.markdown("---") # 구분선
    st.markdown("##### **앙상블 모델 최적화** 및 **딥러닝 모델링**에 관심이 많습니다.")
    st.markdown("##### 최근에는 **XGBoost**와 같은 부스팅 기법을 공부하고 있습니다.")
    
    st.write("") # 소개글과 버튼 사이에 약간의 여백 주기
    
    # 컨택
    # header_col2 내부에서 다시 열을 나누어 버튼을 가로로 나란히 배치합니다.
    btn_col1, btn_col2, btn_col3 = st.columns([1.5, 2, 2]) # 3번째 열은 여백
    
    with btn_col1:
        st.markdown("**E-mail:**")
        st.code("devsaub03@gmail.com", language="text")
    with btn_col2:
        st.markdown("**Github:**")
        st.code("https://github.com/saub03", language="text")
    st.divider() # 전체 너비 구분선

# --- 💡 중간 섹션 (image_5.png의 중간) ---
mid_col1, mid_col2 = st.columns(2) # 2개의 열로 화면 분할 (학력 vs 자격증/어학 능력)

with mid_col1:
    # (3) 학력
    st.header("학력")
    st.markdown("---")
    # 학력 더미 데이터
    st.markdown("- **광운대학교** 정보융합학부 데이터사이언스학과, 2023 ~")
    # st.markdown("- **[고등학교 이름]**, [날짜]")

with mid_col2:
    # (4) 자격증 및 어학 능력 (와이어프레임의 세로선은 columns로 구현)
    st.header("자격증 및 어학 능력")
    st.markdown("---")
    # 자격증/어학 능력 더미 데이터
    st.markdown("- **데이터 분석 준전문가 (ADsP)**, 2026 ")
    st.markdown("- **SQL 개발자 (SQLd)**, 2026(취득 예정)")
    st.markdown("- **한국사능력검정시험 1급**, 2026")
    st.markdown("- **TOEIC**: 835점, 2025")

st.divider() # 전체 너비 구분선

# (5) 프로젝트 섹션 타이틀
st.header("프로젝트")
st.markdown("---") # 타이틀 아래 구분선


# --- 💡 첫 번째 프로젝트 (데이터 사이언스 스터디) ---
st.subheader("데이터 사이언스 스터디(데이터 분석 기술 스택!)")
# 링크는 마크다운으로 깔끔하게 한 줄로 처리
st.markdown("- [스터디 진행 깃허브 저장소](https://github.com/saub03/Data-Science-Deep-Dive)") 

# [핵심] 프로젝트 설명 아래에 이미지 추가
# caption: 이미지 아래에 나올 설명, use_container_width=True: 화면 너비에 맞게 자동 조절
# (💡 팁: 실제 이미지가 있다면 "path/to/image1.png" 처럼 파일 경로를 적으세요.)
# st.image("study.png", caption="스터디 결과물 대시보드 스크린샷", use_container_width=True)
st.image("study.png", caption="스터디 결과물 대시보드 스크린샷", width=400)

st.divider() # 프로젝트 간 구분선


# --- 💡 두 번째 프로젝트 (EDA 파이썬 스크립트) ---
st.subheader("탐색적 자료분석(EDA) 간편화를 위한 파이썬 스크립트")
st.markdown("- [easyEDA 깃허브 저장소(업로드 안함)](https://github.com/saub03/EDA_Script_Repo_Link_Here)")

# 두 번째 프로젝트 이미지 추가
st.image("easyEDA.png", caption="자동 생성된 EDA 리포트 예시", width=400)

st.divider() # 프로젝트 간 구분선


# --- 💡 세 번째 프로젝트 (주식 포트폴리오) ---
st.subheader("주식 포트폴리오 관리")
st.markdown("- [MyStocks 깃허브 저장소](https://github.com/saub03/MyStocks)")

# 세 번째 프로젝트 이미지 추가
st.image("stock.png", caption="롤링을 이용한 상관관계 분석", width=400)

st.divider() # 전체 너비 구분선

# (6) 기술 스택
# --- 💡 기술 스택 및 학습 기록 섹션 ---
st.header("Skills & Knowledge")
st.markdown("데이터 분석 및 모델링을 위해 학습한 내용입니다.")

# 3개의 탭으로 깔끔하게 분류
tab1, tab2, tab3 = st.tabs(["💻 기술 스택", "📚 수강 전공 과목", "📖 학습 및 연구 자료"])

with tab1:
    st.markdown("""
    #### ** Languages & Frameworks**
    - **Python**: `Pandas`, `Numpy`, `Pytorch`, `Matplotlib`, `Seaborn`, `Scipy`, `scikit-learn`, `statsmodels`, `XGBoost`, `CatBoost`, `LightGBM`
    - **SQL**: 데이터 추출 및 정제, 쿼리 최적화
    - **Java**: 객체지향 프로그래밍 기초 역량
    - **R**: 기초 통계 분석 및 시각화 (학습 중)
    
    #### ** Domain Knowledge**
    
    ##### **1. 앙상블 및 부스팅 메커니즘 (Ensemble & Boosting)**
    - **원리의 심층 이해**: `XGBoost`, `LightGBM`, `CatBoost` 등 부스팅 알고리즘의 작동 원리 및 잔차 학습 메커니즘 이해
    - **Hyperparameter 최적화**: 파라미터 간 상관관계 분석을 통한 과적합 방지 및 모델 성능 극대화
    - **정형 데이터 분석**: Kaggle 'Predict Customer Churn' 프로젝트 등 태뷸러 데이터 분석 및 인사이트 도출 경험
    
    ##### **2. 딥러닝 (Deep Learning)**
    - **기초 원리 구현**: `Numpy`만을 활용해 **신경망, 오차역전파법(Backpropagation), CNN**을 직접 구현하며 딥러닝 핵심 원리 습득
    - **프레임워크 활용**: `PyTorch`를 이용한 딥러닝 모델 설계 및 학습 자동화
    
    ##### **3. 알고리즘 트레이딩 파이프라인 (python-binance)**
    - **시계열 분석**: 시계열 모델링을 통한 가격 예측 알고리즘 설계 및 검증
    - **엔드투엔드 파이프라인**: 데이터 로딩부터 예측, 실행까지 이어지는 일련의 데이터 파이프라인 설계 및 구축 능력을 보유
    """)

with tab2:
    st.markdown("#### **주요 전공 교과목**")
    st.markdown("수학과 프로그래밍의 탄탄한 기초를 다지고, 최신 오픈소스 및 AI 기술을 학습하고 있습니다.")
    
    with st.expander("1학년 1학기 (1-1)"):
        st.markdown("""
        - **프로그래밍기초**: `C`언어 학습으로 프로그래밍 기초 학습
        - **대학수학연습1**: 미적분학 1
        - **통계학개론**: 기초 통계학
        """)
        
    with st.expander("1학년 2학기 (1-2)"):
        st.markdown("""
        - **이산수학**: 컴퓨터 과학을 위한 수학적 논리
        - **대학수학연습2**: 미적분학 2
        - **고급C프로그래밍**: `C++` 프로그래밍 기초 학습
        - **벡터해석학및연습**: 다변수 미적분 및 벡터 공간 이해
        - **인공지능과컴퓨팅사고**: `Python` 프로그래밍 기초 및 컴퓨팅 사고력
        """)
        
    with st.expander("2학년 1학기 (2-1)"):
        st.markdown("""
        - **데이터베이스**: 데이터베이스 시스템 및 설계 이해
        - **AI수학**: *Mathematics for Machine Learning* 교재 기반 선형대수, 통계, 최적화 내용 학습
        - **객체지향프로그래밍**: `Java` 언어 학습 및 객체지향 프로그래밍
        - **오픈소스소프트웨어**: `Git`, `GitHub`, `Linux OS`, `Docker`, `Huggingface` 등 실무 환경 툴체인 습득
        - **블록체인의이해**: 블록체인 알고리즘 및 구조 이해
        """)

with tab3:
    st.markdown("#### **Self-Study & References**")
    st.markdown("정규 교육과정 외에 개인 학습이나 스터디를 진행하면서 공부한 자료들입니다.")
    
    st.markdown("""
    ##### **전문 서적 및 교재**
    - **데이터 분석 준전문가 (ADsP) 수험서**
        - 데이터 기획, 데이터 분석, 통계 분석의 전반적인 파이프라인 및 이론 지식 습득
    - **Dive into Deep Learning (D2L)** - (학습중)
        - 주요 딥러닝 모델 이론과 구축 (CNN, RNN, LSTM, Attention & Transformer 등)
    - **밑바닥부터 시작하는 딥러닝 시리즈** (1, 2권 학습)
        - numpy로 주요 딥러닝 모델을 직접 구현해보면서 내부적인 동작 방식 이해
    - **파이썬 라이브러리를 활용한 데이터 분석**
        - 데이터 분석에 활용되는 파이썬 라이브러리와 활용 방안
    - **Do it! 5일 만에 끝내는 깃&깃허브 입문**
        - 협업을 위한 git과 github 기능 탐색
    - **선형대수와 통계학으로 배우는 머신러닝 with 파이썬**
        - 전통적 머신러닝 기법의 수학적 원리 이해
    - **머신러닝 딥러닝 문제해결 전략**
        - 실제 데이터 분석 워크플로우 이해
    - **XGBoost와 사이킷런을 활용한 그레이디언트 부스팅**
        - XGBoost 1.x 버전을 기준으로 나온 책의 코드를 3.x 버전에 맞게 수정하고 발전한 알고리즘을 체감함
    - **데이터베이스 개론과 실습**
        - 전공 수업 이외에 데이터 베이스에 대해 더 깊게 공부
    - **개발자를 위한 실전 선형대수학**
        - 전공 수업만으로 부족했던 선형대수학 내용 학습
        
    ##### **스터디 및 커뮤니티 활동**
    - **데이터 사이언스 스터디 리딩**
        - 스터디 그룹을 직접 조직하고 리딩
        - 주차별 발제 자료 제작, 과제 부여 및 머신러닝/딥러닝 핵심 개념 설명
        
    ##### **참고한 논문과 웹사이트**
    - **[XGBoost: A Scalable Tree Boosting System (2016)](https://arxiv.org/pdf/1603.02754)**
        - 트리 부스팅 시스템의 확장성과 수학적 최적화 원리 파악
    - **[Attention Is All You Need (2017)](https://arxiv.org/pdf/1706.03762)**
        - 트랜스포머 아키텍처와 Self-Attention 메커니즘 원리 학습
    """)