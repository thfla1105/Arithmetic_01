"""순수 사칙연산 함수. 부수 효과 없음."""

from __future__ import annotations

from arithmetic.domain.exceptions import DivisionByZeroError


def add(a: float | int, b: float | int) -> float | int:
    """덧셈. 정수끼리면 int, 그 외에는 연산 결과에 따름."""
    return a + b


def subtract(a: float | int, b: float | int) -> float | int:
    """뺄셈."""
    return a - b


def multiply(a: float | int, b: float | int) -> float | int:
    """곱셈."""
    return a * b


def divide(a: float | int, b: float | int) -> float:
    """나눗셈 (실수 나눗셈). ``b == 0`` 이면 :class:`DivisionByZeroError`."""
    if b == 0:
        raise DivisionByZeroError()
    return a / b
