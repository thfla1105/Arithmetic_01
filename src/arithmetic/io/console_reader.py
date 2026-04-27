"""콘솔 입력만 담당. 연산 로직 없음."""


class ConsoleReader:
    def read_line(self, prompt: str = "") -> str:
        """프롬프트를 표시하고 한 줄 문자열을 읽는다."""
        return input(prompt)
