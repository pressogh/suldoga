# suldoga
### 한성대학교 멋쟁이사자처럼 4팀

## How to start
### Clone project
```git clone https://github.com/pressogh/suldoga.git```
### Virtualenv Setting
1. ```cd suldoga```
2. ```python -m venv venv```
3.
- #### Windows
```.\venv\Scripts\activate```
- #### Mac
```./venv/bin/activate```
### Install packages
```pip install -r requirements.txt```
### Get secrets
프로젝트 루트에 secrets.json파일을 만들고 개발 채널에 있는 env코드 복사 후, 만든 secrets.json폴더에 붙여넣으시면 됩니다.
1. 프로젝트 루트에 secrets.json파일 만들기
2. 개발 채널에 있는 env 코드 복사하기
3. 만든 secrets.json파일에 복사한 코드 붙여넣기
### Start server
```python manage.py runserver```

## Notice
- 반드시 자신의 브랜치인지 확인하고 Pull 부탁드립니다!
- 작업 완료하신 후 master에 Pull request 보내시면 코드 확인 후 승인해드리겠습니다.
