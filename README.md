# Python scraps

A collection of Python snippets meant to be copy/pasted into codebases rather than installed separately.

## fragile_db

Shuts down the whole app on any DB connection error.

## logging

Snippets for configuring loggers across projects. Includes sentry logger.

- `settings_init.py` — put this into root settings module after star `settings_base.py` import
- `settings_base.py` — put this into default settings file which is imported by `settings_init.py` at project launch

Loggers should be initialized per module like this:

```
import logging

logger = logging.getLogger(__name__)
```