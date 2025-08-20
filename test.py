import streamlit as st

st.set_page_config(page_title="퀴즈 앱", page_icon="❓", layout="centered")

st.title("📝 간단한 객관식 퀴즈")

# 퀴즈 데이터
quiz = [
    {
        "question": "1. 대한민국의 수도는 어디일까요?",
        "options": ["서울", "부산", "인천", "대구"],
        "answer": "서울"
    },
    {
        "question": "2. 파이썬의 창시자는 누구일까요?",
        "options": ["리누스 토르발스", "귀도 반 로섬", "빌 게이츠", "제프 베조스"],
        "answer": "귀도 반 로섬"
    },
    {
        "question": "3. 지구에서 가장 큰 대륙은?",
        "options": ["아시아", "아프리카", "유럽", "남아메리카"],
        "answer": "아시아"
    }
]

# 점수 저장
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_q" not in st.session_state:
    st.session_state.current_q = 0

# 현재 문제 불러오기
q = quiz[st.session_state.current_q]
st.subheader(q["question"])
choice = st.radio("정답을 선택하세요:", q["options"])

if st.button("제출"):
    if choice == q["answer"]:
        st.success("✅ 정답입니다!")
        st.session_state.score += 1
    else:
        st.error(f"❌ 오답입니다! 정답은 {q['answer']} 입니다.")

    st.session_state.current_q += 1

    if st.session_state.current_q >= len(quiz):
        st.balloons()
        st.success(f"🎉 모든 문제 완료! 최종 점수: {st.session_state.score}/{len(quiz)}")
        # 초기화 버튼
        if st.button("다시 시작"):
            st.session_state.score = 0
            st.session_state.current_q = 0

