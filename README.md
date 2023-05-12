# GavelGen


![logo](https://user-images.githubusercontent.com/96174711/229123298-6ccd07ed-6b22-4db6-9c59-cac18835264b.png)





## Introduction
* GavelGen은 MZ 세대를 겨냥한 독특하고 재미있는 일상용품 경매 플랫폼입니다. 사용자들은 이 플랫폼에서 다양한 물건을 경매를 통해 구매하거나 판매할 수 있습니다.
* 해당 프로젝트의 서비스명은 'GavelGen'입니다. 'Gavel'은 경매에서 사용되는 작은 나무망치를 의미하며, 'Gen'은 Generation의 약자로써, MZ세대를 대상으로 한 경매 플랫폼임을 강조합니다.





## Features
* 회원가입, 로그인 및 로그아웃 기능
* 사용자 프로필 관리 (회원 정보 수정 및 탈퇴)
* 상품 CRUD 기능 (상품 등록, 조회, 수정 및 삭제)
* 댓글 CRUD 기능 (댓글 작성, 조회, 수정 및 삭제)
* 좋아요 CRUD 기능 (좋아요 추가, 조회, 삭제)
* 태그 CRUD 기능 (태그 추가, 조회, 수정 및 삭제)
* 고객신고 CRUD 기능 (신고 접수, 조회, 처리 및 삭제)
* 관리자 페이지 (회원 및 상품 관리)





## Technologies
* 프론트엔드: Django Templates, HTML, CSS
* 백엔드: Django Framework
* 데이터베이스: SQLite





## Getting Started
이 프로젝트를 시작하려면 다음 단계를 따르십시오.

1. 이 GitHub 저장소를 로컬 컴퓨터로 복제합니다.


2. 프로젝트의 루트 디렉토리로 이동합니다.


3. 터미널 또는 명령 프롬프트를 열고, 다음 명령을 실행하여 가상환경을 설정합니다.


* Windows
```
python -m venv venv
source venv\Scripts\activate
```


* macOS/Linux
```
python3 -m venv venv
source venv/bin/activate
```


4. 가상환경이 활성화된 상태에서, 다음 명령을 실행하여 프로젝트 종속성을 설치합니다.


```
pip install -r requirements.txt
```


5. 따로 첨부한 secrets.json 파일을 추가합니다. 해당 파일에는 필요한 시크릿 키를 설정합니다.


6. 데이터베이스 마이그레이션을 적용하기 위해 다음 명령을 실행합니다.


```
python manage.py migrate
```


7. 애플리케이션을 실행하기 위해 다음 명령을 실행합니다.


```
python manage.py runserver
```


8. 웹 브라우저를 열고 http://localhost:8080 주소로 접속하여 GavelGen을 이용할 수 있습니다.





## Contributing
기여를 원하시면 이 GitHub 저장소에 Pull Request를 보내주시기 바랍니다. 모든 기여는 감사하게 받아들이겠습니다.





## Contact
질문이나 건의사항이 있으면 아래 이메일로 연락주시기 바랍니다.


이메일: chosarah70@gmail.com