# Arithmetic_01

콘솔 기반 **사칙연산 연습** 프로젝트입니다. UI·DB 없이 Python 패키지로 도메인 로직과 콘솔 입출력을 분리했습니다.

## 한눈에 보기

| 항목 | 설명 |
|------|------|
| 언어·런타임 | Python 3.10 이상 |
| 패키지 위치 | `src/arithmetic` |
| 핵심 기능 | `add` / `subtract` / `multiply` / `divide`, 나눗셈 시 제수 0이면 `DivisionByZeroError` |
| 테스트 | `unittest`, `tests/test_operations.py` |
| 원격 저장소 | [github.com/thfla1105/Arithmetic_01](https://github.com/thfla1105/Arithmetic_01) |

## 디렉터리 구조

```
Arithmetic_01/
├── README.md                 # 본 파일
├── pyproject.toml
├── report/                   # 작업 보고서
├── prompting/                # 프롬프트·결과 정리 문서
├── src/arithmetic/           # 애플리케이션 패키지
│   ├── domain/               # 연산·예외 (순수 로직)
│   ├── io/                   # 콘솔 Reader/Writer
│   ├── main.py               # 데모 조립
│   └── __main__.py
└── tests/                    # 단위 테스트
```

## 실행

```powershell
cd c:\DEV\Arithmetic_01
py -3 -m pip install -e .
py -3 -m arithmetic
```

## 테스트

```powershell
py -3 -m unittest discover -s tests -p "test_*.py" -v
```

## 나눗셈 예외 처리

- `divide(a, b)`는 **`b == 0`**(정수 0·실수 0.0 포함)이면 연산을 하지 않고 **`DivisionByZeroError`**를 발생시킵니다.
- 이 예외는 **`ValueError`의 하위 클래스**이므로, 호출부에서 `ValueError`만 잡아도 함께 처리할 수 있습니다.
- 도메인에서 메시지와 실패 경로를 한곳에 모아, 콘솔·향후 세션 계층에서 사용자 안내를 통일하기 쉽게 했습니다.

## 문서

- **작업 보고서:** [report/Arithmetic_01_작업보고서.md](report/Arithmetic_01_작업보고서.md)
- **프롬프팅 정리:** [prompting/README.md](prompting/README.md)
