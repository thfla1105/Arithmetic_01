# Arithmetic 프로젝트 프롬프팅 정리

Git/GitHub 전용 대화는 [Arithmetic_Git_GitHub_프롬프팅_기록.md](./Arithmetic_Git_GitHub_프롬프팅_기록.md)에 두고, 여기서는 **애플리케이션 설계·구현·문서화** 관련 프롬프트를 정리합니다.

---

## 1. 기본 폴더 구조 설계

**요청 요약 (조건)**

- 순수 콘솔, UI·DB 없음, 사칙연산, SRP, 확장 가능한 구조.
- 출력: 폴더 구조, 파일 역할, 클래스 책임.

**결과 요약**

- `src/arithmetic/` 아래 `domain` / `service`(향후) / `io` / `main` 분리안 제시.
- 연산은 `Operation` 추상과 구체 클래스, 출제·세션은 서비스 계층으로 확장하는 방향.

**반영 현황**

- `domain`, `io`, `main` 구현 완료. `service`는 보고서의 향후 과제로 남김.

---

## 2. 사칙연산 기능 구현

**요청 요약 (조건)**

- `add`, `subtract`, `multiply`, `divide`, 0으로 나누기 예외 처리, 입출력 명확, 순수 로직, 단위 테스트.
- 출력: 구현 코드, 테스트 코드, 예외 처리 설명.
- **제안한 구조대로** 구현.

**결과 요약**

| 구분 | 경로 |
|------|------|
| 순수 함수 | `src/arithmetic/domain/operations.py` |
| 예외 | `src/arithmetic/domain/exceptions.py` (`DivisionByZeroError`) |
| 연산 클래스 | `src/arithmetic/domain/operation.py` |
| 콘솔 I/O | `src/arithmetic/io/console_reader.py`, `console_writer.py` |
| 데모 진입 | `src/arithmetic/main.py`, `__main__.py` |
| 테스트 | `tests/test_operations.py` |

예외: `divide`에서 `b == 0`이면 `DivisionByZeroError` ( `ValueError` 하위). README·모듈 docstring에 설명.

---

## 3. 보고서·프롬프팅 정리·README·Git 반영

**요청 요약**

- `report` 폴더에 보고서 작성.
- 지금까지의 prompting을 `prompting` 폴더에 정리 (본 파일 및 `prompting/README.md`).
- 작업 후 프로젝트 요약을 README에 반영하고 Git에 업로드.

**산출물**

- `report/Arithmetic_01_작업보고서.md`
- `prompting/README.md`, 본 문서(`Arithmetic_프로젝트_프롬프팅_정리.md`)
- 루트 `README.md` 갱신
- 커밋·`origin/main` 푸시

---

## 4. 기타 (Git/GitHub 계열)

저장소 생성, `main`, Author/Reviewer·description, 원격 URL, 프롬프팅 내용 저장 등은 **Git/GitHub 기록 문서**에 상세 기재되어 있습니다.
