import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 기본 설정
st.set_page_config(
    page_title="정관장 에브리타임 밸런스 주간 성과 대시보드",
    page_icon="📊",
    layout="wide"
)

st.title("📊 마케팅 성과 대시보드")
st.markdown("""
<div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;'>
    <p style='color: gray; font-size: 1.1rem; margin: 0;'>정관장 에브리타임 밸런스 (2026년 3월 4주차)</p>
    <span style='background-color: #dc2626; color: white; padding: 5px 15px; border-radius: 8px; font-weight: bold;'>KGC 브랜드 전략실</span>
</div>
<hr>
""", unsafe_allow_html=True)

st.subheader("핵심 성과 지표 (KPI)")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="수도권 판매량 (편의점) 🏪", 
        value="+15%", 
        delta="15% 상승 (편의점 견인)"
    )

with col2:
    st.metric(
        label="지방 판매량 (대형마트) 🛒", 
        value="-2%", 
        delta="-2% 하락 (대형마트 부진)"
    )

with col3:
    st.metric(
        label="2030 구매 비중 🧑‍💼", 
        value="45%", 
        delta="사회초년생 중심",
        delta_color="off" # 색상 변화 없이 회색 표시
    )

with col4:
    st.metric(
        label="아웃도어 키워드 언급 ⛺", 
        value="+30%", 
        delta="30% 급증 (New TPO)"
    )

st.markdown("<br>", unsafe_allow_html=True)

col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.markdown("#### 구매 연령층 분포")
    # 도넛 차트 데이터
    df_age = pd.DataFrame({
        '연령대': ['20-30대 (사회초년생 등)', '40대', '50대 이상', '10대 이하'],
        '비중(%)': [45, 30, 20, 5]
    })
    
    # Plotly 도넛 차트 생성
    fig_age = px.pie(
        df_age, 
        values='비중(%)', 
        names='연령대', 
        hole=0.5, # 도넛 형태
        color_discrete_sequence=['#3b82f6', '#60a5fa', '#93c5fd', '#e5e7eb']
    )
    fig_age.update_traces(textposition='inside', textinfo='percent+label')
    fig_age.update_layout(margin=dict(t=20, b=20, l=20, r=20), showlegend=False)
    st.plotly_chart(fig_age, use_container_width=True)

with col_chart2:
    st.markdown("#### 고객 리뷰 감성 분석 (500건)")
    # 바 차트 데이터
    df_sentiment = pd.DataFrame({
        '리뷰 항목': ['맛/제형 (긍정)', '패키지/디자인 (긍정)', '가격 (부정/저항)', '사용성 (부정)'],
        '언급 비중(%)': [42, 38, 12, 8],
        '감성': ['긍정', '긍정', '부정', '부정']
    })
    
    # Plotly 바 차트 생성
    fig_sentiment = px.bar(
        df_sentiment, 
        x='리뷰 항목', 
        y='언급 비중(%)',
        color='감성',
        color_discrete_map={'긍정': '#10b981', '부정': '#f43f5e'}, # 초록, 빨강 색상 매핑
        text_auto=True
    )
    fig_sentiment.update_layout(margin=dict(t=20, b=20, l=20, r=20), showlegend=False)
    st.plotly_chart(fig_sentiment, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

col_review, col_action = st.columns([1, 2])

with col_review:
    st.subheader("주요 리뷰 키워드")
    
    st.success("""
    **👍 긍정적 반응**
    * "포장이 세련되어 선물용으로 좋다"
    * "기존보다 쓴맛이 덜해 먹기 편하다"
    """)
    
    st.error("""
    **👎 개선 필요**
    * "가격이 작년보다 오른 느낌이다" (저항감)
    * "박스 개봉이 가끔 뻑뻑하다" (사용성)
    """)

with col_action:
    st.subheader("Action Items (Next Steps)")
    
    st.info("""
    **1️⃣ 액티브 라이프 타겟 캠페인 (즉시)**
    * 테니스장, 등산로 인근 편의점 판촉 집중
    * 스포츠 앰배서더 콜라보레이션 검토
    """)
    
    st.info("""
    **2️⃣ 지방/대형마트 판촉 강화 (단기)**
    * 가족 단위 고객 타겟 대용량 기획세트 운영
    * 5월 가정의 달 대비 선물 VMD 사전 세팅
    """)
    
    st.info("""
    **3️⃣ 패키지 CX 개선 (중장기)**
    * 생산부서 협의를 통한 박스 개봉 뻑뻑함 이슈 원인 파악
    * 패키지 구조 및 금형 수정 검토
    """)
