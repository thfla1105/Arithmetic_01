# Arithmetic_01 작업 보고서

## 1. 개요

| 항목 | 내용 |
|------|------|
| 프로젝트명 | Arithmetic_01 |
| 목적 | 콘솔 기반 사칙연산 연습용 애플리케이션의 기반 구조 및 도메인 로직 구축 |
| 저장소 | `https://github.com/thfla1105/Arithmetic_01` |
| 기술 | Python 3.10+, 표준 라이브러리 중심(`unittest`), 패키지 레이아웃 `src/` |

## 2. 수행 작업 요약

### 2.1 버전 관리·원격 저장소

- 로컬 디렉터리 `c:\DEV\Arithmetic_01`를 Git으로 관리하고 `main` 브랜치를 사용함.
- GitHub 저장소 `Arithmetic_01`와 `origin` 연동 후 초기 상태(원격의 `README.md`)와 로컬 빈 `prompting` 폴더를 맞추기 위해 `prompting/.gitkeep` 추가 및 푸시함.
- 이후 소스·문서 추가분을 지속적으로 커밋·푸시함.

### 2.2 프로젝트 구조 설계

- **조건:** 순수 콘솔, UI·DB 없음, 사칙연산, 단일 책임 원칙(SRP), 확장 가능한 디렉터리 구조.
- **결과:** `src/arithmetic` 하위에 `domain`(연산·예외), `io`(콘솔 입출력), `main`(조립)으로 분리하는 방향을 채택하고 실제 코드에 반영함.

### 2.3 사칙연산 도메인 구현

- **함수:** `add`, `subtract`, `multiply`, `divide` (`domain/operations.py`).
- **예외:** `b == 0`인 나눗셈은 `DivisionByZeroError`로 처리 (`domain/exceptions.py`). `ValueError` 하위 클래스로 통합 예외 처리 가능.
- **클래스:** `Operation` 추상 및 `AddOperation` 등 구체 클래스가 위 함수에 위임 (`domain/operation.py`).
- **콘솔:** `ConsoleReader` / `ConsoleWriter`로 입출력 분리 (`io/`).
- **진입점:** `python -m arithmetic` → `main.py` 데모.
- **테스트:** `tests/test_operations.py`에서 함수·클래스·0 나눗셈·예외 타입 검증(10건).

### 2.4 빌드·실행

- `pyproject.toml`으로 패키지 메타데이터 및 `src` 레이아웃 정의.
- 로컬 개발 시 `pip install -e .` 후 모듈 실행 및 단위 테스트 수행.

## 3. 디렉터리 구조(현재)

```
Arithmetic_01/
├── README.md
├── pyproject.toml
├── .gitignore
├── report/                 # 본 보고서 등
├── prompting/              # 프롬프트·대화 정리 문서
├── src/
│   └── arithmetic/
│       ├── __init__.py
│       ├── __main__.py
│       ├── main.py
│       ├── domain/
│       │   ├── exceptions.py
│       │   ├── operations.py
│       │   └── operation.py
│       └── io/
│           ├── console_reader.py
│           └── console_writer.py
└── tests/
    └── test_operations.py
```

(`prompting/.gitkeep` 및 기존 프롬프팅 마크다운 파일 포함.)

## 4. 산출물

| 산출물 | 위치 |
|--------|------|
| 작업 보고서 | `report/Arithmetic_01_작업보고서.md` |
| 프롬프팅 정리·목차 | `prompting/README.md`, `prompting/Arithmetic_프로젝트_프롬프팅_정리.md` |
| Git/GitHub 대화 기록 | `prompting/Arithmetic_Git_GitHub_프롬프팅_기록.md` |
| 구현 코드 | `src/arithmetic/**` |
| 단위 테스트 | `tests/test_operations.py` |

## 5. 향후 과제(제안)

- `service` 계층: `ProblemGenerator`, `QuizSession` 등 출제·채점 루프.
- 설정: `config.py`로 난이도·문항 수 분리.
- `tests` 확장: 경계값·부동소수점 정책 등.

## 6. 결론

콘솔 전용·DB/UI 없이 사칙연산 도메인을 SRP에 맞게 모듈화했고, 0으로 나누기 예외와 단위 테스트로 동작을 고정했습니다. 보고·프롬프팅 문서를 `report`·`prompting`에 두어 추적 가능하도록 정리했습니다.
