from typing import Union


def multiply(a: int, b: int) -> int:
    """Return a * b."""
    return a * b


def safe_divide(a: Union[int, float], b: Union[int, float]) -> float:
    """Divide a by b, raising ValueError on division by zero."""
    if b == 0:
        raise ValueError("division by zero")
    return a / b
