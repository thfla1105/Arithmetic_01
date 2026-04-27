"""진입점: 입출력 어댑터와 도메인 함수를 연결한다."""

from arithmetic.domain.exceptions import DivisionByZeroError
from arithmetic.domain.operations import add, divide, multiply, subtract
from arithmetic.io.console_reader import ConsoleReader
from arithmetic.io.console_writer import ConsoleWriter


def main() -> None:
    writer = ConsoleWriter()
    reader = ConsoleReader()

    writer.writeln("=== Arithmetic 데모 (콘솔) ===")
    a, b = 10, 3
    writer.writeln(f"피연산자: a={a}, b={b}")
    writer.writeln(f"add(a, b) = {add(a, b)}")
    writer.writeln(f"subtract(a, b) = {subtract(a, b)}")
    writer.writeln(f"multiply(a, b) = {multiply(a, b)}")
    writer.writeln(f"divide(a, b) = {divide(a, b)}")

    writer.writeln("")
    writer.writeln("나눗셈 예외 데모: divide(1, 0)")
    try:
        divide(1, 0)
    except DivisionByZeroError as exc:
        writer.writeln(f"  처리 결과: {exc!s}")

    writer.writeln("")
    writer.writeln("직접 두 정수를 입력하면 덧셈 결과를 보여줍니다. (종료: 빈 줄)")
    raw = reader.read_line("첫 번째 수: ").strip()
    if raw:
        try:
            x = int(raw, 10)
            raw2 = reader.read_line("두 번째 수: ").strip()
            y = int(raw2, 10)
            writer.writeln(f"add({x}, {y}) = {add(x, y)}")
        except ValueError:
            writer.writeln("정수 형식이 아닙니다.")


if __name__ == "__main__":
    main()
