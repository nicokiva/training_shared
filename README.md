# training-shared

Shared constants package used by all training projects. Currently contains the `EventType` enum that defines all valid event names for the inter-project event queue.

## Install

```bash
pip install git+https://github.com/nicokiva/training_shared.git
```

Or pin a specific commit:

```bash
pip install git+https://github.com/nicokiva/training_shared.git@<commit-sha>
```

## Usage

```python
from training_shared.events import EventType

print(list(EventType))  # see all available events

publish_event(EventType.RUN_GLOBAL)
```

Because `EventType` inherits from `str`, each value is also a plain string — you can pass it directly wherever a string is expected (e.g. a SQLite INSERT).

## Available events

| Constant | Value | Description |
|---|---|---|
| `EventType.RUN_GLOBAL` | `"run:global"` | Full history analysis |
| `EventType.RUN_MONTHLY` | `"run:monthly"` | Monthly balance |
| `EventType.RUN_NEW_ROUTINE` | `"run:new-routine"` | New routine evaluation |
| `EventType.RUN_WEEKLY` | `"run:weekly"` | Weekly comparison |

## How to add a new event

1. Edit `training_shared/events.py` and add a new member to the `EventType` class:
   ```python
   RUN_FORTNIGHTLY = "run:fortnightly"
   ```
2. Commit and push to GitHub.
3. Reinstall the package in every consuming project:
   ```bash
   pip install --force-reinstall git+https://github.com/nicokiva/training_shared.git
   ```
4. Handle the new event type in `routine-analyzer`'s `analyze.py`.
