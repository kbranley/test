# Project

Repository configuration files: `requirements.txt`, `pyproject.toml`, and `.pre-commit-config.yaml` are included.

Setup:

```powershell
& 'c:/Users/kbran/.copilot/ide/.venv/Scripts/python.exe' -m pip install -r requirements.txt
pre-commit install
```

Run tests:

```powershell
& 'c:/Users/kbran/.copilot/ide/.venv/Scripts/python.exe' -m pytest
```

Example package:

This repo includes a minimal package `project` with a sample function and tests:

```python
from project import add
print(add(2,3))  # 5
```
