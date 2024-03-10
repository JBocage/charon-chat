# charon

## Install

### Locally
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install project as editable
pip install -e . # Also installs requirements

# IF YOU ARE A DEV:
# Install dev requirements
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

## Use

```bash
# Config first time you use:
charon setup

# Use the chat
charon chat
```