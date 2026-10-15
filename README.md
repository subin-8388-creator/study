# 📊 공부 습관 대시보드 (Study Habit Dashboard)

Streamlit과 Pandas를 활용하여 학생들의 공부 시간과 성적 데이터를 시각화하고 분석하는 간단한 웹 애플리케이션입니다.

---

## 📌 주요 기능

- **주요 지표 요약 (`st.metric`)**: 전체 학생 수, 평균 점수, 평균 공부 시간을 한눈에 확인합니다.
- **데이터 필터링 (`st.slider`)**: 슬라이더를 조정하여 원하는 '최소 공부 시간' 이상의 데이터를 실시간으로 걸러냅니다.
- **시각화 차트 (`st.scatter_chart`, `st.bar_chart`)**:
  - **산점도**: 공부 시간과 점수 사이의 연관성 분석
  - **막대 그래프**: 학생 ID별 점수 비교

---

## 📁 프로젝트 구조

```text
.
├── app.py              # Streamlit 메인 실행 파일
├── study.csv           # 학생 공부 습관 데이터셋
├── requirements.txt    # 의존성 패키지 목록
└── README.md           # 프로젝트 안내 문서
```

---

## 🚀 실행 방법

### 1. Repository 클론 및 이동
```bash
git clone https://github.com/사용자이름/저장소이름.git
cd 저장소이름
```

### 2. 가상환경 설정 및 실행 (권장)
```bash
# 가상환경 생성 (선택 사항)
python -m venv venv

# 가상환경 활성화 (Windows)
venv\Scripts\activate

# 가상환경 활성화 (Mac/Linux)
source venv/bin/activate
```

### 3. 필요 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. Streamlit 앱 실행
```bash
streamlit run app.py
```

---

## 📊 데이터셋 형식 (`study.csv`)

프로젝트 루트 폴더에 아래와 같은 형식의 `study.csv` 파일이 존재해야 합니다.

| 학생ID | 공부시간 | 스마트폰 | 점수 |
| :--- | :--- | :--- | :--- |
| S01 | 4.5 | 2.0 | 85 |
| S02 | 2.0 | 5.5 | 60 |
| S03 | 6.0 | 1.0 | 95 |

---

## 🛠️ 사용 기술

- **Language**: Python 3.x
- **Data Analysis**: Pandas
- **Web Interface & Visualization**: Streamlit
