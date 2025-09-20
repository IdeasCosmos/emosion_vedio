@echo off
echo ==========================================
echo Emosion Video 프로젝트 설정 스크립트
echo ==========================================
echo.

REM 작업 디렉토리 생성
echo 1. C:\emosion 디렉토리 생성 중...
if not exist "C:\emosion" (
    mkdir "C:\emosion"
    echo ✓ C:\emosion 디렉토리가 생성되었습니다.
) else (
    echo ✓ C:\emosion 디렉토리가 이미 존재합니다.
)

REM Git 저장소 클론
echo.
echo 2. Git 저장소 클론 중...
cd /d "C:\emosion"
if not exist "emosion_vedio" (
    git clone https://github.com/IdeasCosmos/emosion_vedio.git
    echo ✓ 저장소가 성공적으로 클론되었습니다.
) else (
    echo ✓ 저장소가 이미 존재합니다. 업데이트 중...
    cd emosion_vedio
    git pull origin main
    cd ..
)

REM 필요한 디렉토리 생성
echo.
echo 3. 프로젝트 디렉토리 구조 생성 중...
cd "C:\emosion\emosion_vedio"
if not exist "videos" mkdir "videos"
if not exist "videos\output" mkdir "videos\output"
if not exist "logs" mkdir "logs"
if not exist "temp" mkdir "temp"
echo ✓ 디렉토리 구조가 생성되었습니다.

REM 환경 파일 복사
echo.
echo 4. 환경 설정 파일 준비 중...
if exist "config\.env.example" (
    if not exist "config\.env" (
        copy "config\.env.example" "config\.env"
        echo ✓ .env 파일이 생성되었습니다. config\.env 파일을 편집하여 API 키를 설정해주세요.
    ) else (
        echo ✓ .env 파일이 이미 존재합니다.
    )
)

echo.
echo ==========================================
echo 설정 완료!
echo ==========================================
echo.
echo 다음 단계:
echo 1. config\.env 파일을 열어 OpenAI API 키를 설정하세요
echo 2. 프로젝트 작업을 시작하세요
echo.
echo 작업 디렉토리: C:\emosion\emosion_vedio
echo.
pause