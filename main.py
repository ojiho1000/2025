import streamlit as st

# MBTI 데이터
mbti_jobs = {
    "INTJ": ["전략기획가", "데이터 분석가", "연구원"],
    "ENFP": ["마케터", "작가", "스타트업 창업가"],
    "ISTP": ["엔지니어", "정비사", "수사관"],
    "ESFJ": ["교사", "간호사", "인사 담당자"],
}

st.title("MBTI 기반 직업 추천기")
st.write("당신의 MBTI를 입력하면 어울리는 직업을 추천해드립니다!")

# 사용자 입력
user_mbti = st.selectbox("MBTI를 선택하세요:", list(mbti_jobs.keys()))

if st.button("추천 받기"):
    jobs = mbti_jobs.get(user_mbti, [])
    if jobs:
        st.subheader(f"{user_mbti} 유형에 어울리는 직업:")
        for job in jobs:
            st.write(f"- {job}")
    else:
        st.write("아직 데이터가 없어요 😢")
