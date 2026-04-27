"""연산 단일 책임 클래스. 구현은 :mod:`arithmetic.domain.operations`에 위임."""

from __future__ import annotations

from abc import ABC, abstractmethod

from . import operations


class Operation(ABC):
    """한 종류의 이항 연산."""

    @abstractmethod
    def evaluate(self, left: float | int, right: float | int) -> float | int:
        """두 피연산자의 결과를 반환."""


class AddOperation(Operation):
    def evaluate(self, left: float | int, right: float | int) -> float | int:
        return operations.add(left, right)


class SubtractOperation(Operation):
    def evaluate(self, left: float | int, right: float | int) -> float | int:
        return operations.subtract(left, right)


class MultiplyOperation(Operation):
    def evaluate(self, left: float | int, right: float | int) -> float | int:
        return operations.multiply(left, right)


class DivideOperation(Operation):
    def evaluate(self, left: float | int, right: float | int) -> float:
        return operations.divide(left, right)
