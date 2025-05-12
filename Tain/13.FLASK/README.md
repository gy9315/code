# flask

## D0423

### 학습내용
Flask의 기본 라우팅 구조를 학습하며, route 데코레이터, HTML 파일 렌더링, 환경변수 설정, 서버 실행 방법 등을 실습함.

### 개인 복습/실습
- Flask 애플리케이션을 my_app.py에 구성하고 `@app.route()`로 URL 라우팅 실습
- index.html을 templates 폴더 내 구성하여 render_template 연동 실습
- os.getenv, .env 파일 등을 활용한 환경 설정 실습
- URL에 따른 분기, GET 요청 파라미터 출력, 문자열 반환 등 다양한 형태의 출력 확인
- 'Blueprint 없이 단일 app.py에서 모든 기능 구성 시 어떤 단점이 있는가?'에 대해 질문하며 구조화 필요성 인지

### 회고
기본 구조가 단순한 만큼 빠르게 결과를 볼 수 있었고, HTML과 Python을 연동하며 백엔드의 흐름이 실제로 어떻게 전달되는지를 명확히 느낄 수 있었다.

## D0424

### 학습내용
HTML 기반 폼 처리 및 입력값 전달 실습을 진행하며, form 태그, input 처리 방식, GET/POST 메서드 차이 등을 익힘.

### 개인 복습/실습
- 다양한 형태의 input (text, password, radio, checkbox 등)을 활용한 HTML 폼 실습
- ex_input_form.html에서 form 태그의 action, method 구조를 직접 설계
- Flask에서 request.form으로 전달된 값을 추출하고 조건문을 통해 분기 처리 실험
- 사용자 입력값을 받아 다른 템플릿에서 결과 출력 구조 구현
- 입력값 검증 없이 단순 전달 시 발생하는 보안 위험 및 예외 처리 고민 시작

### 회고
단순한 입력에서 시작한 폼 처리도 다양한 input 조합에 따라 코드 흐름이 복잡해짐을 체감했고, 사용자 경험과 서버 안정성 모두 고려해야 함을 알게 되었다.

## D0425

### 학습내용
Flask 프로젝트 구조를 분리하고 Blueprint 구조를 활용한 뷰 설계 및 사용자 인증 흐름을 구성함. HTML 렌더링부터 DB 연동 고려까지 기초 뼈대를 구현함.

### 개인 복습/실습
- Webserver/views 디렉토리 구조로 view 함수 분리, Blueprint 등록 실습
- index.html, login.html, user_page.html 등 템플릿을 연결하고 render 흐름 정리
- 사용자 입력 기반 조건 분기와 redirect 처리 흐름 구현
- Flask 객체를 app.py → blueprint → HTML로 전달하는 전체 흐름을 실습함
- 'Blueprint가 왜 필요한가?', 'route마다 views.py로 나누는 기준은?' 등의 구조화 질문을 반복하며 MVC 개념과의 연결 이해

### 회고
작은 기능이 늘어나면서 점점 구조가 복잡해지고, 이를 해결하기 위한 분리 전략(blueprint)이 왜 필요한지 직접적으로 느낄 수 있었다.
