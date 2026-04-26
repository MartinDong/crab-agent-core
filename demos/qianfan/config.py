import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = PROJECT_ROOT / ".env"
load_dotenv(dotenv_path=ENV_PATH)


class LLMConfig:
    r"""
    \u7edf\u4e00\u7ba1\u7406 .env \u4e2d\u7684 LLM \u670d\u52a1\u914d\u7f6e
    \u652f\u6301 OpenAI \u517c\u5bb9 API \u548c\u767e\u5ea6\u5343\u5e06\u4e24\u79cd\u914d\u7f6e
    """

    # OpenAI \u517c\u5bb9 API \u914d\u7f6e
    _k1 = "OPENAI_API_KEY"
    _b1 = "OPENAI_API_BASE"
    _m1 = "OPENAI_MODEL_NAME"
    OPENAI_API_KEY = os.getenv(_k1, "").strip()
    OPENAI_API_BASE = os.getenv(_b1, "https://api.openai.com/v1").strip()
    OPENAI_MODEL_NAME = os.getenv(_m1, "gpt-4o-mini").strip()

    # \u767e\u5ea6\u5343\u5e06\u914d\u7f6e
    _k2 = "QIANFAN_API_KEY"
    _b2 = "QIANFAN_API_BASE"
    _m2 = "QIANFAN_MODEL_NAME"
    QIANFAN_API_KEY = os.getenv(_k2, "").strip()
    QIANFAN_API_BASE = os.getenv(_b2, "https://qianfan.baidubce.com/v2").strip()
    QIANFAN_MODEL_NAME = os.getenv(_m2, "deepseek-v3").strip()

    @classmethod
    def _is_valid_key(cls, key: str) -> bool:
        if not key:
            return False
        # \u6392\u9664\u660e\u663e\u7684\u5360\u4f4d\u7b26
        placeholders = ("***", "your-api-key", "sk-xxx", "bce-v3/AK/SK")
        if key in placeholders:
            return False
        # \u77ed\u5b57\u7b26\u4e32\u4e2d\u542b *** \u89c6\u4e3a\u5360\u4f4d\u7b26
        if "***" in key and len(key) < 20:
            return False
        return True

    @classmethod
    def get_active_config(cls):
        # \u4f18\u5148\u68c0\u67e5 OpenAI \u517c\u5bb9 API
        if cls._is_valid_key(cls.OPENAI_API_KEY):
            return {
                "api_key": cls.OPENAI_API_KEY,
                "base_url": cls.OPENAI_API_BASE,
                "model": cls.OPENAI_MODEL_NAME,
                "provider": "openai-compatible",
            }
        # \u5176\u6b21\u68c0\u67e5\u767e\u5ea6\u5343\u5e06
        if cls._is_valid_key(cls.QIANFAN_API_KEY):
            return {
                "api_key": cls.QIANFAN_API_KEY,
                "base_url": cls.QIANFAN_API_BASE,
                "model": cls.QIANFAN_MODEL_NAME,
                "provider": "qianfan",
            }
        raise ValueError(
            f"\n\u9519\u8bef: \u5728 {ENV_PATH} \u4e2d\u672a\u627e\u5230\u6709\u6548\u7684 API Key \u914d\u7f6e\u3002\n"
            f"\n\u8bf7\u5728 .env \u6587\u4ef6\u4e2d\u914d\u7f6e\u4ee5\u4e0b\u73af\u5883\u53d8\u91cf\u4e4b\u4e00:\n"
            f"  1) OpenAI \u517c\u5bb9 API:\n"
            f"     OPENAI_API_KEY=sk-xxx\n"
            f"     OPENAI_API_BASE=https://api.openai.com/v1\n"
            f"     OPENAI_MODEL_NAME=gpt-4o-mini\n"
            f"\n  2) \u767e\u5ea6\u5343\u5e06:\n"
            f"     QIANFAN_API_KEY=bce-v3/...\n"
            f"     QIANFAN_API_BASE=https://qianfan.baidubce.com/v2\n"
            f"     QIANFAN_MODEL_NAME=deepseek-v3\n"
        )

    @classmethod
    def print_config(cls):
        try:
            cfg = cls.get_active_config()
            key = cfg["api_key"]
            preview = key[:12] + "..." if len(key) > 15 else key
            print(f"  \u670d\u52a1\u63d0\u4f9b\u5546: {cfg['provider']}")
            print(f"  API \u5730\u5740:   {cfg['base_url']}")
            print(f"  \u6a21\u578b:       {cfg['model']}")
            print(f"  API Key:    {preview}")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    print(f"\u5df2\u52a0\u8f7d .env: {ENV_PATH}")
    print("\u5f53\u524d\u914d\u7f6e:")
    LLMConfig.print_config()
