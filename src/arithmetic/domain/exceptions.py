"""도메인 예외.

나눗셈에서 제수(divisor)가 0인 경우 Python 내장 ZeroDivisionError 대신
도메인 전용 예외를 둡니다.

이유:
- 메시지를 한글 등으로 통일해 호출부(콘솔·세션)에서 사용자에게 안내하기 쉽다.
- float 연산의 ``a / 0.0`` 도 ZeroDivisionError가 나지만, 정수 0과 동일 정책으로
  ``b == 0`` 선검사로 한 경로에서만 실패하게 할 수 있다.
"""


class DivisionByZeroError(ValueError):
    """제수가 0인 나눗셈을 수행하려 할 때 발생."""

    def __init__(self, message: str = "0으로 나눌 수 없습니다.") -> None:
        super().__init__(message)
