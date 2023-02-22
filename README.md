# Sample Python Unittest

## Install required packages

```bash
pip install requests
```

## How to run test

```bash
python -m unittest  # to run all tests under the directory garage
python -m unittest discovery libs  # to run all tests under the directory garage/libs
python -m unittest discovery cars  # to run all tests under the directory garage/honda
python -m unittest cars/test_honda.py  # to run the test file cars/test_honda.py
python -m unittest cars.test_honda  # to run the test file cars/test_honda.py
```

