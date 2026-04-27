import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from the project root (two levels up from this file)
_root = Path(__file__).parent.parent.parent
load_dotenv(_root / ".env")


def get_api_key() -> str:
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not key or key.startswith("sk-ant-..."):
        raise EnvironmentError(
            "ANTHROPIC_API_KEY is not set.\n"
            "Copy .env.example to .env and add your key from "
            "https://console.anthropic.com/settings/keys"
        )
    return key


MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6")
