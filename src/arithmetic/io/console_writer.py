"""콘솔 출력만 담당. 계산 로직 없음."""


class ConsoleWriter:
    def write(self, text: str) -> None:
        """한 줄 출력 (개행 없음)."""
        print(text, end="", flush=True)

    def writeln(self, text: str) -> None:
        """한 줄 출력 후 개행."""
        print(text)
