import anthropic
from src.core.config import get_api_key, MODEL


def make_client() -> anthropic.Anthropic:
    return anthropic.Anthropic(api_key=get_api_key())


def chat(
    messages: list[dict],
    system: str = "",
    tools: list[dict] | None = None,
    cache_system: bool = True,
) -> anthropic.types.Message:
    """
    Single call to Claude with optional prompt caching on the system prompt.

    cache_system=True marks the system prompt as ephemeral so it is cached
    across calls within the same session, reducing cost and latency significantly.
    """
    client = make_client()

    system_block = (
        [{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}]
        if system and cache_system
        else system or ""
    )

    kwargs: dict = dict(model=MODEL, max_tokens=8096, system=system_block, messages=messages)
    if tools:
        kwargs["tools"] = tools

    return client.messages.create(**kwargs)
