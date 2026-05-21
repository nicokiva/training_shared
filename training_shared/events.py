"""
Event type constants for the training project event queue.

Both publishers (pdf2xls-generator) and consumers (routine-analyzer) import
from here so event names are never hardcoded as plain strings in either project.

Adding a new event:
    1. Add a constant here.
    2. Publisher: call publish_event(EventType.YOUR_EVENT).
    3. Consumer: handle it in the events switch (analyze.py or equivalent).
"""

from enum import Enum


class EventType(str, Enum):
    """
    All valid event types that can be published to events.db.

    Inheriting from str means each value IS a string, so you can pass
    EventType.RUN_GLOBAL directly wherever a str is expected (e.g. SQLite INSERT).
    """
    # Semantic event: emitted by pdf2xls-generator after a full upload cycle.
    # routine-analyzer reacts by running monthly + global + new-routine automatically.
    ROUTINE_UPLOADED = "routine:uploaded"

    # Manual modes: used when running analyze.py directly from the CLI (--mode flag).
    RUN_GLOBAL      = "run:global"
    RUN_MONTHLY     = "run:monthly"
    RUN_NEW_ROUTINE = "run:new-routine"
    RUN_WEEKLY      = "run:weekly"
