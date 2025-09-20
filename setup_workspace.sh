#!/bin/bash

echo "=========================================="
echo "Emosion Video 프로젝트 설정 스크립트 (Linux/Mac)"
echo "=========================================="
echo

# 작업 디렉토리 생성 (Linux/Mac의 경우 홈 디렉토리에)
WORKSPACE_DIR="$HOME/emosion"
echo "1. $WORKSPACE_DIR 디렉토리 생성 중..."
if [ ! -d "$WORKSPACE_DIR" ]; then
    mkdir -p "$WORKSPACE_DIR"
    echo "✓ $WORKSPACE_DIR 디렉토리가 생성되었습니다."
else
    echo "✓ $WORKSPACE_DIR 디렉토리가 이미 존재합니다."
fi

# Git 저장소 클론
echo
echo "2. Git 저장소 클론 중..."
cd "$WORKSPACE_DIR"
if [ ! -d "emosion_vedio" ]; then
    git clone https://github.com/IdeasCosmos/emosion_vedio.git
    echo "✓ 저장소가 성공적으로 클론되었습니다."
else
    echo "✓ 저장소가 이미 존재합니다. 업데이트 중..."
    cd emosion_vedio
    git pull origin main
    cd ..
fi

# 필요한 디렉토리 생성
echo
echo "3. 프로젝트 디렉토리 구조 생성 중..."
cd "$WORKSPACE_DIR/emosion_vedio"
mkdir -p videos/output logs temp
echo "✓ 디렉토리 구조가 생성되었습니다."

# 환경 파일 복사
echo
echo "4. 환경 설정 파일 준비 중..."
if [ -f "config/.env.example" ]; then
    if [ ! -f "config/.env" ]; then
        cp "config/.env.example" "config/.env"
        echo "✓ .env 파일이 생성되었습니다. config/.env 파일을 편집하여 API 키를 설정해주세요."
    else
        echo "✓ .env 파일이 이미 존재합니다."
    fi
fi

echo
echo "=========================================="
echo "설정 완료!"
echo "=========================================="
echo
echo "다음 단계:"
echo "1. config/.env 파일을 열어 OpenAI API 키를 설정하세요"
echo "2. 프로젝트 작업을 시작하세요"
echo
echo "작업 디렉토리: $WORKSPACE_DIR/emosion_vedio"
echo