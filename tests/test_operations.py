"""도메인 사칙연산 함수 및 연산 클래스 단위 테스트."""

from __future__ import annotations

import unittest

from arithmetic.domain.exceptions import DivisionByZeroError
from arithmetic.domain.operation import (
    AddOperation,
    DivideOperation,
    MultiplyOperation,
    SubtractOperation,
)
from arithmetic.domain.operations import add, divide, multiply, subtract


class TestOperations(unittest.TestCase):
    def test_add_integers(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(10, 3), 7)

    def test_multiply(self) -> None:
        self.assertEqual(multiply(4, 5), 20)

    def test_divide_integer_result(self) -> None:
        self.assertEqual(divide(6, 3), 2.0)

    def test_divide_float(self) -> None:
        self.assertAlmostEqual(divide(1, 2), 0.5)

    def test_divide_by_zero_raises(self) -> None:
        with self.assertRaises(DivisionByZeroError) as ctx:
            divide(1, 0)
        self.assertIn("0", str(ctx.exception))

    def test_divide_by_zero_float_zero(self) -> None:
        with self.assertRaises(DivisionByZeroError):
            divide(1.0, 0.0)

    def test_division_by_zero_is_value_error_subclass(self) -> None:
        self.assertTrue(issubclass(DivisionByZeroError, ValueError))


class TestOperationClasses(unittest.TestCase):
    def test_classes_delegate_to_functions(self) -> None:
        self.assertEqual(AddOperation().evaluate(2, 3), add(2, 3))
        self.assertEqual(SubtractOperation().evaluate(10, 3), subtract(10, 3))
        self.assertEqual(MultiplyOperation().evaluate(4, 5), multiply(4, 5))
        self.assertEqual(DivideOperation().evaluate(6, 3), divide(6, 3))

    def test_divide_operation_zero(self) -> None:
        with self.assertRaises(DivisionByZeroError):
            DivideOperation().evaluate(5, 0)


if __name__ == "__main__":
    unittest.main()
