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
### 🗄️ 1st. 초기 셋팅

- [x]  github 관련 설정
- [x]  가상환경 및 장고 설치
- [x]  프로젝트 및 주요 앱 생성
- [x]  `gunicorn` 설정
- [x]  `requirements.txt` 작성
- [x]  stage에 따른 설정 파일 분리
- [x]  환경변수 관련 디렉토리 및 파일 생성



<br>
<br>
<br>