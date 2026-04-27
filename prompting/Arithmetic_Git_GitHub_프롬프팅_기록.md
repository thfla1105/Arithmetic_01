# Arithmetic Git/GitHub 프롬프팅 및 결과 기록

이 문서는 Arithmetic_01 저장소와 관련해 진행한 프롬프트 요약과 그에 대한 결과를 보관합니다.

---

## 1. Git 초기화·main·첫 커밋 안내 (Windows)

**요청 요약:** Git 초기화, main 브랜치 확인, 첫 커밋, 커밋 메시지 예시를 Windows 기준으로 단계별 안내.

**결과 요약:**

- `cd c:\DEV\Arithmetic_01` 후 `git init -b main` 권장 (처음부터 `main` 사용).
- 첫 커밋 전에는 `git branch`에 브랜치가 안 보일 수 있음 → `git config --global init.defaultBranch main` 또는 첫 커밋 후 `git status`에서 `On branch main` 확인.
- 첫 커밋: `git add .` → `git status` → `git commit -m "..."`.
- 참고: 일부 환경에서는 터미널에 Git이 PATH에 없으면 명령이 실패할 수 있음 → [Git for Windows](https://git-scm.com/download/win) 설치 및 PATH 확인.

---

## 2. 첫 커밋 메시지 (Conventional Commits, 예시 3개)

**조건:** Conventional Commit 형식, 변경 내용 명확, 한 줄 요약 + 상세 본문, 예시 3개.

**제공한 예시:**

### 예시 1

```
chore: Arithmetic 프로젝트 초기 가져오기

- 연산 연습용 소스 및 디렉터리 구조를 저장소에 추가함
- 빌드/실행에 필요한 설정 파일을 포함함
- 이후 기능 추가는 별도 커밋으로 분리할 예정
```

### 예시 2

```
feat: 사칙연산 연습 앱의 최초 버전 추가

- 덧셈·뺄셈·곱셈·나눗셈 문제 생성 및 채점 흐름 구현
- 난이도 또는 범위 설정이 있다면 여기에 한 줄로 명시
- 테스트 또는 샘플 데이터가 포함된 경우 그 사실을 적음
```

### 예시 3

```
docs: README 및 개발 환경 안내 추가

- 프로젝트 목적과 로컬 실행 방법을 README에 정리함
- 의존성 설치·실행 명령을 Windows 기준으로 기술함
- 소스 트리 개요나 폴더 역할이 있다면 간단히 나열
```

---

## 3. GitHub 저장소 연결 및 push (명령만)

**요청 요약:** Repository `Arithmetic_01`, `main`, Author 이소림, Reviewer 박철수, description에 Author/Reviewer 포함, 명령어만 단계별.

**제공한 명령 흐름 (플레이스홀더 버전):**

```powershell
cd c:\DEV\Arithmetic_01
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/Arithmetic_01.git
gh repo edit YOUR_GITHUB_USERNAME/Arithmetic_01 --description "Author: 이소림 | Reviewer: 박철수"
git push -u origin main
```

- `origin`이 이미 있으면: `git remote set-url origin https://github.com/...`
- 커밋 작성자: `git config user.name "이소림"`, `git config user.email "..."`.
- `gh` 없으면 GitHub 웹에서 Description 수동 입력.

---

## 4. 원격 저장소에 프로젝트 전체 push

**요청:** `https://github.com/thfla1105/Arithmetic_01.git`에 프로젝트 전체 업로드.

**실행 결과 요약:**

- 로컬 `.git`에 이미 `origin`이 `https://github.com/thfla1105/Arithmetic_01.git`로 설정되어 있었음.
- 로컬은 커밋이 없었고, 추적 가능한 파일도 없었음(빈 `prompting` 폴더만 존재 — Git은 빈 디렉터리를 추적하지 않음).
- 원격 `origin/main`에는 GitHub 초기 커밋만 존재(`README.md` 한 파일).
- `git fetch origin` 후 `git reset --hard origin/main`으로 로컬 작업 트리를 원격과 일치시킴.
- 빈 `prompting`을 저장소에 남기기 위해 `prompting/.gitkeep` 추가.
- 커밋 메시지: `chore: track prompting directory` (본문: prompting 폴더 보존 목적).
- `git push -u origin main` 성공 (`5afbf38..e053dfc`).

**당시 저장소 트리:** `README.md`, `prompting/.gitkeep`

---

## 5. 본 문서 저장 및 Git 반영 (이번 작업)

**요청:** 현재까지의 프롬프팅과 결과를 `prompting` 폴더에 저장하고 Git에 올리기.

**산출물:** 이 파일 — `prompting/Arithmetic_Git_GitHub_프롬프팅_기록.md`
