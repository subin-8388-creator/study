
import pandas as pd
import streamlit as st

# 1. 페이지 제목 설정
st.title("📊 공부 습관 대시보드")

# 2. 데이터 불러오기
# study.csv 파일에서 데이터를 읽어옵니다.
df = pd.read_csv("study.csv")

# 3. 요약 지표 표시 (한 줄로 배치)
# st.columns를 사용해 3개의 열을 나누어 배치합니다.
col1, col2, col3 = st.columns(3)

with col1:
    # 전체 학생 수 계산 및 표시
    total_students = len(df)
    st.metric(label="전체 학생 수", value=f"{total_students}명")

with col2:
    # 평균 점수 계산 및 표시 (소수점 1자리까지 표기)
    avg_score = df["점수"].mean()
    st.metric(label="평균 점수", value=f"{avg_score:.1f}점")

with col3:
    # 평균 공부시간 계산 및 표시 (소수점 1자리까지 표기)
    avg_study = df["공부시간"].mean()
    st.metric(label="평균 공부시간", value=f"{avg_study:.1f}시간")

st.divider()  # 구분선 추가

# 4. 슬라이더를 이용한 필터링 설정
# 데이터 내 공부시간의 최소값과 최대값을 구해 슬라이더 범위를 지정합니다.
min_hours = float(df["공부시간"].min())
max_hours = float(df["공부시간"].max())

# 사용자가 최소 공부시간을 선택할 수 있는 슬라이더 생성
selected_min_hours = st.slider(
    label="최소 공부시간 선택 (시간)",
    min_value=min_hours,
    max_value=max_hours,
    value=min_hours,  # 기본값은 최소값으로 설정
    step=0.5,
)

# 선택된 최소 공부시간 이상인 학생만 필터링합니다.
filtered_df = df[df["공부시간"] >= selected_min_hours]

# 필터링된 결과 수 안내
st.write(
    f"💡 선택한 조건({selected_min_hours}시간 이상)에 해당하는 학생: **{len(filtered_df)}명**"
)

# 5. 그래프 시각화
# st.scatter_chart: 공부시간과 점수 간의 관계를 보는 산점도
st.subheader("📌 공부시간 대 점수 산점도")
st.scatter_chart(data=filtered_df, x="공부시간", y="점수")

# st.bar_chart: 학생별 점수 비교 막대 그래프
st.subheader("📊 학생별 점수 막대 그래프")
st.bar_chart(data=filtered_df, x="학생ID", y="점수")