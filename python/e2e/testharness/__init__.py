"""Test harness for E2E tests."""

from typing import Any

from .context import DEFAULT_GITHUB_TOKEN, E2ETestContext, is_inprocess_transport
from .helper import get_final_assistant_message, get_next_event_of_type, wait_for_condition
from .proxy import CapiProxy

__all__ = [
    "CLI_PATH",
    "DEFAULT_GITHUB_TOKEN",
    "E2ETestContext",
    "CapiProxy",
    "get_final_assistant_message",
    "get_next_event_of_type",
    "wait_for_condition",
    "is_inprocess_transport",
]


def __getattr__(name: str) -> Any:
    """Forward ``CLI_PATH`` to its lazy definition in ``context`` (PEP 562)."""
    if name == "CLI_PATH":
        from . import context

        return context.CLI_PATH
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
