"""
GPT CODEX 통합 모듈
OpenAI의 Codex API를 사용하여 감정 기반 비디오 처리 코드를 생성합니다.
"""

import json
import os
import logging
from typing import Dict, Any, Optional
try:
    import openai
except ImportError:
    openai = None
    print("OpenAI 패키지가 설치되지 않았습니다. 'pip install openai'를 실행해주세요.")


class CodexIntegration:
    """GPT CODEX API 통합 클래스"""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        CODEX 통합 초기화
        
        Args:
            config_path: 설정 파일 경로 (기본값: config/config.json)
        """
        self.logger = self._setup_logging()
        self.config = self._load_config(config_path)
        self._setup_openai()
    
    def _load_config(self, config_path: Optional[str] = None) -> Dict[str, Any]:
        """설정 파일 로드"""
        if config_path is None:
            config_path = os.path.join("config", "config.json")
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            self.logger.error(f"설정 파일을 찾을 수 없습니다: {config_path}")
            return self._get_default_config()
        except json.JSONDecodeError:
            self.logger.error(f"설정 파일 형식이 올바르지 않습니다: {config_path}")
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """기본 설정 반환"""
        return {
            "openai": {
                "api_key": "YOUR_OPENAI_API_KEY_HERE",
                "model": "gpt-3.5-turbo",
                "codex_model": "code-davinci-002",
                "max_tokens": 2048,
                "temperature": 0.7
            }
        }
    
    def _setup_openai(self):
        """OpenAI API 설정"""
        if openai is None:
            self.logger.error("OpenAI 패키지가 필요합니다.")
            return
        
        api_key = os.getenv('OPENAI_API_KEY') or self.config.get('openai', {}).get('api_key')
        if api_key and api_key != "YOUR_OPENAI_API_KEY_HERE":
            openai.api_key = api_key
        else:
            self.logger.warning("OpenAI API 키가 설정되지 않았습니다.")
    
    def _setup_logging(self) -> logging.Logger:
        """로깅 설정"""
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def generate_code(self, prompt: str, language: str = "python") -> Optional[str]:
        """
        CODEX를 사용하여 코드 생성
        
        Args:
            prompt: 코드 생성을 위한 프롬프트
            language: 프로그래밍 언어 (기본값: python)
        
        Returns:
            생성된 코드 문자열 또는 None
        """
        if openai is None or not hasattr(openai, 'api_key') or not openai.api_key:
            self.logger.error("OpenAI API가 설정되지 않았습니다.")
            return None
        
        try:
            openai_config = self.config.get('openai', {})
            model = openai_config.get('codex_model', 'code-davinci-002')
            
            # CODEX용 프롬프트 포맷팅
            formatted_prompt = f"# {language} 코드 생성\n# 요청: {prompt}\n\n"
            
            response = openai.Completion.create(
                engine=model,
                prompt=formatted_prompt,
                max_tokens=openai_config.get('max_tokens', 2048),
                temperature=openai_config.get('temperature', 0.7),
                stop=["# 끝", "# END"]
            )
            
            generated_code = response.choices[0].text.strip()
            self.logger.info(f"코드가 성공적으로 생성되었습니다. 길이: {len(generated_code)} 문자")
            return generated_code
            
        except Exception as e:
            self.logger.error(f"코드 생성 중 오류 발생: {str(e)}")
            return None
    
    def generate_emotion_analysis_code(self, video_path: str) -> Optional[str]:
        """
        감정 분석을 위한 비디오 처리 코드 생성
        
        Args:
            video_path: 분석할 비디오 파일 경로
        
        Returns:
            감정 분석 코드 또는 None
        """
        prompt = f"""
비디오 파일 '{video_path}'에서 감정을 분석하는 Python 코드를 작성해주세요.
다음 기능을 포함해야 합니다:
1. 비디오에서 프레임 추출
2. 얼굴 감지
3. 감정 분석 (행복, 슬픔, 분노, 놀람, 두려움, 혐오, 중립)
4. 결과를 JSON 형태로 저장

OpenCV와 face_recognition 라이브러리를 사용하세요.
        """
        
        return self.generate_code(prompt, "python")
    
    def get_workspace_info(self) -> Dict[str, str]:
        """작업공간 정보 반환"""
        workspace_config = self.config.get('workspace', {})
        return {
            'local_path': workspace_config.get('local_path', 'C:\\emosion'),
            'project_name': workspace_config.get('project_name', 'emosion_vedio'),
            'git_remote': workspace_config.get('git_remote', ''),
        }


def main():
    """메인 함수 - 기본 테스트"""
    codex = CodexIntegration()
    
    # 작업공간 정보 출력
    workspace_info = codex.get_workspace_info()
    print("작업공간 정보:")
    for key, value in workspace_info.items():
        print(f"  {key}: {value}")
    
    # 간단한 코드 생성 테스트
    test_prompt = "비디오 파일을 로드하고 기본 정보를 출력하는 함수 작성"
    generated_code = codex.generate_code(test_prompt)
    
    if generated_code:
        print("\n생성된 코드:")
        print("=" * 50)
        print(generated_code)
        print("=" * 50)
    else:
        print("코드 생성에 실패했습니다.")


if __name__ == "__main__":
    main()