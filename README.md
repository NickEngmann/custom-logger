# custom-logger
Custom Logger


How to:

```
# your_project.py
from custom_logger import get_logger

log_file = '/path/to/your/log/file.log'
repo_url = 'https://your.repo.url'

logger = get_logger(log_file, repo_url)

# Use the logger
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.error('This is an error message')
```
