# 📣 소셜 네트워크 서비스 개발 프로젝트

<br>

## 🗒️ 프로젝트 개요
- Python, Django를 이용한 소셜 네트워크 서비스 애플리케이션 개발
- Django REST Framework, drf-spectacular를 이용한 백엔드 API 개발
- Docker를 이용한 컨테이너 형태로의 배포
- GitHub Actions를 이용한 CICD pipeline 구축
- Terraform을 이용한 IaC 구현
- NCloud에서 로드밸런서를 활용한 클라우드 방식의 배포

<br>

## 📖 프로젝트 주요 기능

### 0️⃣ 권한

- 모든 사용자는 데이터 종류에 상관없이 전체 데이터에 대한 조회 가능
- 단일 데이터에 대해서는 본인이 생성한 것에 대해서만 접근 및 변경 요청 가능 

### 1️⃣ 유저

- JWT를 이용한 토큰 인증
- 사용자는 전체 유저 정보 조회 가능
- 사용자는 조건에 따른 유저 정보 검색 가능

### 2️⃣ 프로필

- 사용자는 전체 프로필 조회 가능
- 사용자는 본인의 프로필 생성 및 수정 가능
- 사용자는 조건에 따른 프로필 검색 가능

### 3️⃣ 게시글
- 사용자는 게시글 작성 및 게시 여부 설정 가능
- 사용자는 전체 게시글 조회 가능
- 사용자는 본인의 게시물을 모아 볼 수 있음
- 사용자는 본인의 게시물을 수정 또는 삭제 가능
- 사용자는 조건에 따른 게시글 검색 가능

### 4️⃣ follow

- 사용자는 다른 사용자를 follow 혹은 unfollow 가능
- 사용자는 following (내가 follow한 사람들) 목록 확인 가능
- 사용자는 follower (나를 follow한 사람들) 목록 확인 가능
- 사용자는 follow한 사람들이 올린 게시물을 모아 볼 수 있음

<br>

## 🏤 Infra

### 🖥 GitHub Repository

**코드 및 버전 관리**

- 작업 환경 별 Branch 분리

| Branch | 용도                       | Merge to         |
|-------|--------------------------|------------------|
| `feat`  | 기능 개발 및 테스트              | `develop` branch |
| `develop` | 정상 동작 확인 및 버그 수정         |  `main` branch   |
| `main`  | 서비스 배포                   | -                |

<br>

### 🚥 GitHub Actions

**지속적 통합 (CI) 및 지속적 배포 (CD)를 구축**

**1️⃣ CI**

| 분류    | 설명                                                                      |
|-------|:------------------------------------------------------------------------|
| 조건    | `feature` 브랜치로 push되었을 때                                                  |
| 진행    | - 테스트 진행 <br> - 테스트 정상 완료 시 NCR로 이미지 `push` <br> - 원격 리포지토리에 해당 branch 생성 |
| 확인 대상 | - 모든 파일과 디렉토리 <br> - 단, `infra` 및 `script` 디렉토리 및 그 하위 파일과 디렉토리은 제외         |

**2️⃣ CD to staging**

| 분류    | 설명                                                                                                                                                |
|-------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| 조건    | - `feature` 브랜치에서 `develop` 브랜치로의 `Pull Request`가 완료되어 코드가 `merge` 되었을 때                                                                          |
| 진행    | - `staging` stage의 `django` 서버로 배포 <br> - 배포는 NCR Image를 통한 컨테이너 형태로 진행                                                                            |
| 확인 대상 | - 모든 파일과 디렉토리 <br> - 단, `docker` , `infra` , `script` 디렉토리 및 그 하위 파일과 디렉토리를 제외 <br> - .github/workflows 내 자기 자신(CD_dev.yaml)을 제외한 다른 워크플로우 파일 제외  |

**3️⃣ CD to production**

| 분류    | 설명                                                                                                                                          |
|-------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| 조건    | - `develop` 브랜치에서 `main` 브랜치로의 `Pull Request`가 완료되어 코드가 `merge` 되었을 때                                                                               |
| 진행    | - `prod` stage의 `django` 서버로 배포 <br> - 배포는 NCR Image를 통한 컨테이너 형태로 진행                                                                            |
| 확인 대상 | - 모든 파일과 디렉토리 <br> - 단, `docker` , `infra` , `script` 디렉토리 및 그 하위 파일과 디렉토리를 제외 <br> - .github/workflows 내 자기 자신(CD_main.yaml)을 제외한 다른 워크플로우 파일 제외 |

<br>

### ⛵ Docker
**컨테이너화된 애플리케이션 이미지를 생성 및 관리**

- 배포 시, 이미지 버전 관리를 위하여 `TIMESTAMP` Ver. 과 `latest` Ver. 를 동시에 생성
- 생성된 이미지는 클라우드 환경(NCloud Container Registry)에 Push
- 배포 시 `Latest` Ver. 이미지를 사용하며, 롤백 혹은 로그 확인 시 `TIMESTAMP` Ver. 이미지를 사용

<br> 

### 💻 Terraform

**클라우드 환경에서 인프라를 코드로 관리 및 프로비저닝**

**Shared Module**
- `Network` : VPC, Subnet 리소스 생성
- `Server` : Access Group, Network Interface, Init Script, Server 및 관련 리소스 생성
- `LoadBalancer` : Target Group, LoadBalancer 및 관련 리소스 생성

**Child Module**
- `Staging` : `develop` 브랜치 에서 관리되는 코드를 사용하여 `스테이징` 환경의 클라우드 리소스를 배포
- `Prod` :  `main` 브랜치 에서 관리되는 코드를 사용하여 `프로덕션` 환경의 클라우드 리소스를 배포

<br>

### ⛅ NCloud

**클라우드 리소스를 활용하여 애플리케이션 서비스를 SaaS 형태로 제공**


<br>

## 🪓 주요 설치 패키지/모듈

|   종류    |               이름                |   버전   |
|:---------:|:---------------------------------:|:--------:|
| Language  |            **python**             |   3.11   |
| Framework |            **Django**             |  4.2.4   |
| Database  |          **PostgreSQL**           |    13    |
|  Library  |           **gunicorn**            |  21.2.0  |
|  Library  |        **psycopg2-binary**        |  2.9.7   |
|  Library  |      **djangorestframework**      |  3.14.0  |
|  Library  | **djangorestframework-simplejwt** |  5.3.0   |
|  Library  |         **django-filter**         |   23.2   |
|  Library  |         **django-taggit**         |  4.0.0   |
|  Library  |        **drf-spectacular**        |  0.26.4  |
|  Library  |    **drf-spectacular-sidecar**    | 2023.9.1 |
|  Library  |             **boto3**             | 1.28.44  |
|  Library  |        **django-storages**        |   1.14   |
|  Library  |            **Pillow**             |  10.0.0  |

<br> 

## 📋 Database Schema

### 💾 User

| Column Name      | Data Type               | Constraint                                                       |
|------------------|-------------------------|------------------------------------------------------------------|
| **id**           | INTEGER                 | PRIMARY KEY                                                      |
| **email**        | VARCHAR(max_length=100) | UNIQUE , NOT NUL                                                 |
| **fullname**     | VARCHAR(max_length=30)  | NOT NULL                                                         |
| **phone**        | VARCHAR(max_length=30)  | UNIQUE,  NOT NULL                                                |
| **password**     | VARCHAR(max_length=100) |                                                                  |
| **is_admin**     | BOOLEAN                 | NOT NULL, DEFAULT : False                                        |
| **is_superuser** | BOOLEAN                 | NOT NULL, DEFAULT : False                                        |
| **is_active**    | BOOLEAN                 | NOT NULL, DEFAULT : True                                         |
| **last_login**   | DATETIME                | NULL                                                             |
| **created_at**   | DATETIME                | DEFAULT CURRENT_TIMESTAMP, NOT NULL                              |
| **updated_at**   | DATETIME                | DEFAULT CURRENT_TIMESTAMP, ON UPDATE CURRENT_TIMESTAMP, NOT NULL |

### 💾 Profile

| Column Name    | Data Type               | Constraint                                                       |
|----------------|-------------------------|------------------------------------------------------------------|
| **id**         | INTEGER                 | PRIMARY KEY                                                      |
| **user**       | INTEGER                 | FOREIGN KEY REFERENCES Users(user_id), NOT NULL                  |
| **nickname**   | VARCHAR(max_length=30)  | UNIQUE, NOT NULL                                                 |
| **birthday**   | DATE                    | NOT NULL                                                         |
| **image_url**  | VARCHAR(max_length=255) | NULL                                                             |
| **is_public**  | BOOLEAN                 | NOT NULL, DEFAULT : False                                        |
| **is_active**  | BOOLEAN                 | NOT NULL, DEFAULT : True                                         |
| **created_at** | DATETIME                | DEFAULT CURRENT_TIMESTAMP, NOT NULL                              |
| **updated_at** | DATETIME                | DEFAULT CURRENT_TIMESTAMP, ON UPDATE CURRENT_TIMESTAMP, NOT NULL |

### 💾 Post

| Column Name    | Data Type               | Constraint                                                       |
|----------------|-------------------------|------------------------------------------------------------------|
| **id**         | INTEGER                 | PRIMARY KEY                                                      |
| **title**      | VARCHAR(max_length=250) | NOT NULL                                                         |                                                                  |
| **slug**       | VARCHAR(max_length=250) | UNIQUE, NOT NULL                                                 |
| **author**     | INTEGER                 | FOREIGN KEY REFERENCES Users(user_id), NOT NULL                  |
| **body**       | TEXT                    | NOT NULL                                                         |
| **status**     | INTEGER                 | NOT NULL, DEFAULT : 0                                            |
| **publish**    | DATETIME                | DEFAULT CURRENT_TIMESTAMP,NOT NULL                               |
| **created_at** | DATETIME                | DEFAULT CURRENT_TIMESTAMP, NOT NULL                              |
| **updated_at** | DATETIME                | DEFAULT CURRENT_TIMESTAMP, ON UPDATE CURRENT_TIMESTAMP, NOT NULL |

### 💾 Follow

| Column Name    | Data Type | Constraint                                      |
|----------------|-----------|-------------------------------------------------|
| **id**         | INTEGER   | PRIMARY KEY                                     |
| **user_from**  | INTEGER   | FOREIGN KEY REFERENCES Users(user_id), NOT NULL |
| **user_to**    | INTEGER   | FOREIGN KEY REFERENCES Users(user_id), NOT NULL |
| **created_at** | DATETIME  | DEFAULT CURRENT_TIMESTAMP, NOT NULL             |

### 💾 Content_type

| Column Name   | Data Type                | Constraint  |
|---------------|--------------------------|-------------|
| **id**        | INTEGER                  | PRIMARY KEY |
| **app_label** | VARCHAR (max_length=100) | NOT NULL    |
| **model**     | VARCHAR (max_length=100) | NOT NULL    |

### 💾 Tag

| Column Name | Data Type                | Constraint  |
|-------------|--------------------------|-------------|
| **id**      | INTEGER                  | PRIMARY KEY |
| **name**    | VARCHAR (max_length=100) | NOT NULL    |
| **slug**    | VARCHAR (max_length=100) | NOT NULL    |

### 💾 Taggeditem

| Column Name         | Data Type | Constraint                                                     |
|---------------------|-----------|----------------------------------------------------------------|
| **id**              | INTEGER   | PRIMARY KEY                                                    |
| **object_id**       | INTEGER   |                                                                |
| **content_type_id** | INTEGER   | FOREIGN KEY REFERENCES Content_type(content_type_id), NOT NULL |
| **tag_id**          | INTEGER   | FOREIGN KEY REFERENCES Tag(tag_id), NOT NULL                   |

<br>

## 📅 ERD

![image](https://github.com/likelion-backend-6th/TrackProject_1_ChoiSeonWoo/assets/104040502/9d266776-e2c1-4777-b169-8cd39a62b265)

<br>

## API 명세서
> 하단 Notion 링크를 통해 접속하여 확인 가능

![API_docs](https://github.com/likelion-backend-6th/TrackProject_1_ChoiSeonWoo/assets/104040502/7af078df-6aca-486d-b0e0-7eefd17fa2b7)


<br>

## 배포 URL

### [🚧 `staging` Server URL](http://be-lb-staging-19480782-5e27276c4a42.kr.lb.naverncp.com/)

> [📜 `OpenAPI` URL](http://be-lb-staging-19480782-5e27276c4a42.kr.lb.naverncp.com/api/docs/)

### [🏳‍🌈 `production` Server URL](http://be-lb-prod-19480757-e92e545ff666.kr.lb.naverncp.com)

> [📜 `OpenAPI` URL](http://be-lb-prod-19480757-e92e545ff666.kr.lb.naverncp.com/api/docs/)



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

### 0️⃣5️⃣ Model

- [x]  Profile 모델 생성
- [x]  Follow 모델 생성
- [x]  Post 모델 생성
- [x]  Admin site에 모델 등록
- [x]  로컬 환경에서 docker-compose로 테스트
- [x]  Post 모델에 대한 테스트 코드 작성

### 0️⃣6️⃣ User

- [x]  패키지 설치 및 셋팅 - DRF, DRF Spectacular 외
- [x]  회원가입 기능 구현
- [x]  회원가입 테스트
- [x]  로그인 기능 구현
- [x]  로그인 테스트
- [x]  유저 C/U/D 기능 구현
- [x]  유저 C/U/D 기능 테스트
- [x]  프로필 C/R/U/D 기능 구현
- [x]  프로필 C/R/U/D 기능 테스트
- [x]  팔로우 기능 구현
- [x]  팔로우 기능 테스트

### 0️⃣7️⃣ Post

- [x]  권한 확인 클래스 리팩토링
- [x]  게시글 C/R/U/D 기능 구현
- [x]  게시글 관련 테스트
- [x]  내가 작성한 게시글 모아보기 기능 구현
- [x]  해당 기능 테스트
- [x]  내가 팔로우한 유저의 게시글 모아보기 기능 구현
- [x]  해당 기능 테스트

### 0️⃣8️⃣ OpenAPI

- [x]  drf-spectacular 관련 라이브러리 설치
- [x]  OpenAPI Swagger 생성
- [x]  각 앱별 drf-spectacular 추가 설정

### 0️⃣9️⃣ Image

- [x]  NCloud Object Storage 생성
- [x]  `boto3` 라이브러리 설치 및 `Object Storage` 설정
- [x]  프로필 이미지 업로드 기능 추가
- [x]  프로필 이미지 기능 테스트
- [x]  AWS S3 버킷 생성
- [x]  `django-storages` 라이브러리 설치 및 `S3` 설정
- [x]  정적 파일 정상 서빙 확인
- [x]  Terraform 코드 수정





<br>

## 📌 Notion
- [00. (📺 PLAN) DB & API 설계](https://www.notion.so/browneyed/00-DB-API-2e7c2be0ed3b447cae64c1113a50f4ee?pvs=4)
- [01. (🏗 SETTING) 초기 셋팅](https://www.notion.so/browneyed/01-81b4ca5fab734a14b1e50bfe56b307ec?pvs=4)
- [02. (🏰 INFRA) Docker 셋팅](https://www.notion.so/browneyed/02-Docker-54acd08e87744d1bb7edf096ce365e19?pvs=4)
- [03. (🏰 INFRA) Terraform 셋팅](https://notion.so/1bc02cc29f784493be1a104edf900f9f)
- [04. (🏗 SETTING) CI/CD 셋팅](https://notion.so/d4c0eef1aa734e3ca7aa3b7f23836902)
- [05. (👑 FEATURE) Model](https://notion.so/06deff565c354917afc045f67113a1c4)
- [06. (👑 FEATURE) User](https://notion.so/37b6c92d79074e2b8284a809fb3e6cd8)
- [07. (❓❗ Q&A) Github Actions](https://notion.so/fd8c3a72303e4502bbe99aa52b7483e9)
- [08. (🐞 BUG) Docker & CI/CD](https://notion.so/9a2d41b6042b466f90af5fe3589786a5)
- [09. (🐞 BUG) Model](https://notion.so/fe769e41e06e43ce9e90348c67c81187)
- [10. (👑 FEATURE) Post](https://notion.so/d3ec4bc1f1654d0797794085918721ef)
- [11. (👑 FEATURE) OpenAPI](https://notion.so/820a1c6a6da34d9d89495378a0531799)
- [12. (👑 IMAGE) OpenAPI](https://notion.so/2d88d0e5590d46368c817d08c3967b20)


<br>

## 🚧 2차에서 작업 예정 목록

**우선순위 기준으로 작성**

- [ ] 생성/그외 목적의 Serializer 분리
- [ ] API 명세서 추가 작성 (Request, Response)
- [ ] 데이터 유효성 검증 추가 및 테스트 코드 개선
- [ ] 쿼리 속도 개선
- [ ] API Endpoint 개선
- [ ] 코드 리팩토링
- [ ] Infra Architecture Diagram 작성
- [ ] 댓글, 좋아요 기능 추가



<br>
<br>
