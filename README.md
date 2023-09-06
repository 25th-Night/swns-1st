# 📣 소셜 네트워크 서비스 개발 프로젝트

<br>

## 🗒️ 프로젝트 개요
- Python, Django를 이용한 소셜 네트워크 서비스 애플리케이션 개발
- Django REST Framework, drf-spectacular를 이용한 백엔드 API 개발
- Docker를 이용한 컨테이너 형태로의 배포
- CICD pipeline 구축
- NCloud에서 로드밸런서를 활용한 클라우드 방식의 배포

<br>

## 📖 프로젝트 주요 기능

### 1️⃣ 유저

- 사용자 회원가입 시 프로필도 함께 생성
- 로그인 시 Token 발급 - JWT를 이용한 토큰 인증
- 사용자 본인을 제외한 전체 사용자 목록(USERNAME) 확인 가능
- 사용자는 본인의 프로필을 수정 가능
- 사용자는 회원 탈퇴 가능


### 2️⃣ 게시글
- 사용자는 게시글 작성 가능
- 사용자는 공개 설정된 전체 게시글 조회 가능
- 사용자는 본인의 게시물을 모아 볼 수 있음
- 사용자는 본인의 게시물을 수정 또는 삭제 가능


### 3️⃣ follow

- 사용자는 다른 사용자를 follow 혹은 unfollow 가능
- 사용자는 following (내가 follow한 사람들) 목록 확인 가능
- 사용자는 follower (나를 follow한 사람들) 목록 확인 가능
- 사용자는 follow한 사람들이 올린 게시물을 모아 볼 수 있음

<br>

## 🪓 주요 설치 패키지/모듈
|    종류    |       이름        |      버전      |
|:--------:|:---------------:|:------------:|
|    Language    |     python      |     3.11     |
|  Framework   | Django |    4.2.4     |
| Database |   PostgreSQL    |     13     |

<br>

## 📑 Check List

### 0️⃣0️⃣ DB & API설계

- [x]  DB 설계
- [x]  API 설계

### 0️⃣1️⃣ 초기 셋팅

- [x]  github 관련 설정
- [x]  가상환경 및 장고 설치
- [x]  프로젝트 및 주요 앱 생성
- [x]  `gunicorn` 설정
- [x]  `requirements.txt` 작성
- [x]  stage에 따른 설정 파일 분리
- [x]  환경변수 관련 디렉토리 및 파일 생성

### 0️⃣2️⃣ Docker 셋팅

- [x]  Dockerfile for Django - 작성
- [x]  관련 스크립트 파일 작성
- [x]  Django 프로젝트에서 psycopg2 사용 설정
- [x]  Dockerfile for nginx in ubuntu - 작성
- [x]  관련 스크립트 파일 작성
- [x]  docker-compose.yml for local 환경 - 작성
- [x]  local 환경에서 사용할 환경변수 파일 작성
- [x]  docker-compose.yml for test - 작성

### 0️⃣3️⃣ Terraform 셋팅

- [x]  디렉토리 및 파일 생성
- [x]  기본 모듈 : `network` 작성
- [x]  기본 모듈 : `server` 작성
- [x]  기본 모듈 : `loadBalancer` 작성
- [x]  서버 모듈 : `staging` 작성
- [x]  서버 모듈 : `prod` 작성
- [x]  배포 스크립트 작성
- [x]  SSH provider를 이용한 배포
- [x]  정상 생성 및 배포 확인

### 0️⃣4️⃣ CI/CD 셋팅

- [x]  github repository - Settings - Secrets and variables 설정
- [x]  github 환경 설정 - `branch protection rule`
- [x]  CI : feature 브랜치로 push 이벤트 발생 시
- [x]  CD : develop 브랜치로 PR이 완료 시 staging 서버로 배포
- [x]  CD : main 브랜치로 PR이 완료 시 prod 서버로 배포
- [x]  Django 앱 이미지 교체 (로컬/원격 환경 및 NCR)


<br>

## 📌 Notion
- [00. DB & API 설계](https://www.notion.so/browneyed/00-DB-API-2e7c2be0ed3b447cae64c1113a50f4ee?pvs=4)
- [01. 초기 셋팅](https://www.notion.so/browneyed/01-81b4ca5fab734a14b1e50bfe56b307ec?pvs=4)
- [02. Docker 셋팅](https://www.notion.so/browneyed/02-Docker-54acd08e87744d1bb7edf096ce365e19?pvs=4)
- [03. Terraform 셋팅](https://notion.so/1bc02cc29f784493be1a104edf900f9f)
- [04. CI/CD 셋팅](https://notion.so/d4c0eef1aa734e3ca7aa3b7f23836902)


<br>
<br>
<br>