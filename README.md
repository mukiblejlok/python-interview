# Python-Interview

## Prerequisites

1. Create Virtual Environment
    ```
    python3 -m venv venv
    ```
2. Install requirements from `pyproject.toml` file
    ```
    pip install .[dev]
    ```

## Solving the questions

Questions are located in  `/questions` folder.
There are six of them.
Follow the guide on top of each file. 
In each one you should create a working function/class that solves the problem stated in question.
There is always an empty function/class definition provided to start with.

## Testing the answers

After solving the questions you can test your answers with pytest
```
pytest tests -v
```
