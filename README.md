# Emosion Video (감정 비디오)
감정의 음악적 표현으로 정형화 - GPT CODEX 통합 비디오 감정 분석 프로젝트

## 프로젝트 개요
이 프로젝트는 OpenAI의 GPT CODEX를 활용하여 비디오에서 감정을 분석하고 음악적 표현으로 변환하는 시스템입니다.

## 주요 기능
- 🤖 **GPT CODEX 통합**: OpenAI Codex API를 통한 자동 코드 생성
- 🎥 **비디오 감정 분석**: 얼굴 표정에서 감정 추출
- 🎵 **음악적 표현**: 감정을 음악 요소로 변환
- 💻 **작업공간 설정**: C:\emosion 폴더에 자동 설정

## 설치 및 설정

### 1. 자동 설정 (권장)

#### Windows 사용자:
```batch
# setup_workspace.bat 실행
setup_workspace.bat
```

#### Linux/Mac 사용자:
```bash
# setup_workspace.sh 실행
chmod +x setup_workspace.sh
./setup_workspace.sh
```

### 2. 수동 설정

#### 1) 저장소 클론
```bash
# Windows의 경우 C:\emosion 폴더에 클론
git clone https://github.com/IdeasCosmos/emosion_vedio.git C:\emosion\emosion_vedio

# Linux/Mac의 경우 홈 디렉토리에 클론
git clone https://github.com/IdeasCosmos/emosion_vedio.git ~/emosion/emosion_vedio
```

#### 2) 의존성 설치
```bash
cd emosion_vedio
pip install -r requirements.txt
```

#### 3) 환경 설정
```bash
# 환경 파일 복사
cp config/.env.example config/.env

# config/.env 파일을 편집하여 OpenAI API 키 설정
# OPENAI_API_KEY=your_actual_api_key_here
```

## 사용법

### 1. GPT CODEX 통합 테스트
```python
from src.emosion.codex_integration import CodexIntegration

# CODEX 인스턴스 생성
codex = CodexIntegration()

# 작업공간 정보 확인
workspace_info = codex.get_workspace_info()
print(workspace_info)

# 코드 생성 테스트
code = codex.generate_code("비디오에서 프레임을 추출하는 함수")
print(code)
```

### 2. 감정 분석 코드 생성
```python
# 감정 분석을 위한 코드 자동 생성
video_path = "path/to/your/video.mp4"
emotion_code = codex.generate_emotion_analysis_code(video_path)
print(emotion_code)
```

## 프로젝트 구조
```
emosion_vedio/
├── config/              # 설정 파일
│   ├── config.json      # 메인 설정
│   └── .env.example     # 환경 변수 템플릿
├── src/emosion/         # 메인 소스 코드
│   ├── __init__.py
│   └── codex_integration.py  # GPT CODEX 통합 모듈
├── videos/              # 비디오 파일 (자동 생성)
│   └── output/          # 처리된 결과
├── logs/                # 로그 파일 (자동 생성)
├── temp/                # 임시 파일 (자동 생성)
├── requirements.txt     # Python 의존성
├── setup_workspace.bat  # Windows 설정 스크립트
├── setup_workspace.sh   # Linux/Mac 설정 스크립트
└── README.md           # 이 파일
```

## 설정 파일

### config/config.json
```json
{
  "openai": {
    "api_key": "YOUR_OPENAI_API_KEY_HERE",
    "model": "gpt-3.5-turbo",
    "codex_model": "code-davinci-002",
    "max_tokens": 2048,
    "temperature": 0.7
  },
  "workspace": {
    "local_path": "C:\\emosion",
    "project_name": "emosion_vedio",
    "git_remote": "https://github.com/IdeasCosmos/emosion_vedio.git"
  }
}
```

## 요구사항
- Python 3.7+
- OpenAI API 키
- OpenCV
- (선택사항) CUDA 지원 GPU (고성능 비디오 처리용)

## 라이센스
이 프로젝트는 MIT 라이센스 하에 배포됩니다.

## 기여하기
1. 포크하기
2. 기능 브랜치 생성 (`git checkout -b feature/amazing-feature`)
3. 커밋하기 (`git commit -m 'Add amazing feature'`)
4. 푸시하기 (`git push origin feature/amazing-feature`)
5. Pull Request 생성하기

## 문의
프로젝트에 대한 문의사항이나 버그 리포트는 Issues 탭을 이용해주세요.
