# 1. 설치

Rasa를 실행하기 위해서는 먼저 터미널 혹은 cmd를 통해서 패키지를 설치하여야 한다.  

![image](https://user-images.githubusercontent.com/43739827/103540852-bf59bb80-4edd-11eb-88b0-4b4fd243c820.png)
> Fig 1. Install Rasa Open Source using pip  

사용하고자 하는 Rasa 프로젝트가 존재하는 경우에는 패키지 설치 후에 파일을 불러와 사용하면 되지만, 만약 아무런 패키지도 존재하지 않는다면  
Rasa가 제공하는 가장 기초적인 모델을 커맨드를 통하여 불러올 수 있다.  
이 때 Rasa에서 사용되는 파일들은 자동적으로 생성되며 기초적인 nlu, core등을 training한 모델이 만들어진다.  

![image](https://user-images.githubusercontent.com/43739827/103540861-c1bc1580-4edd-11eb-91e8-84bebcabdf16.png)
> Fig 2. Create new project using command line  

![image](https://user-images.githubusercontent.com/43739827/103540879-ca145080-4edd-11eb-8e09-e1991812d64d.png)
> Fig 3. Rasa project file  

 후에 프로젝트에 사용할 데이터들이 전부 완성되고 나면 training을 통하여 model을 생성해주어야 하며 생성된 모델은 프로젝트 폴더 내부의  
 models 폴더에 자동으로 추가된다. Rasa를 실행할 때 가장 최근에 생성된 모델을 불러들이기 때문에 반드시 내부에 모델은 1개 이상이 존재해야 한다.  

![image](https://user-images.githubusercontent.com/43739827/103540867-c4b70600-4edd-11eb-8e91-69792efe8bf9.png)
> Fig 4. rasa train using command line

# 2. 실행 방법

Rasa를 실행하는 방법으로는 목적에 따라 크게 두 가지로 나뉜다.
1.	Rasa 명령어를 통해 action 서버와 model을 연결하여 사용자와 bot간의 대화
2.	커스텀 서버를 통해 Facebook messenger, telegram등과 같은 외부와 연결하여 챗봇 사용
해당 문서에서는 1을 중점으로 다루어 설명한다.

2-1. action server와 model 연결
 시작하기 앞서 여기서 설명하는 action 서버란 사용자의 task에 맞게 설계되어 있는 actions.py를 bot이 사용하도록 하는 것으로, 후에 서술할 domain에  
정의되어있는 utterance만을 사용한다면 action 서버를 사용하지 않아도 된다.  
만약 actions.py를 사용하는 프로젝트라면 터미널을 통해 해당 프로젝트의 디렉토리로 이동한 뒤 **rasa run actions** 를 입력하여 action 서버를 실행시킨다.  
후에 별도의 터미널을 실행하여 마찬가지로 해당 프로젝트의 디렉토리로 이동한 뒤 rasa shell을 입력하여 model을 불러온다.  
정상적으로 실행된다면 rasa shell을 입력한 터미널에서 사용자의 input을 받으며 bot의 output이 출력된다.

![image](https://user-images.githubusercontent.com/43739827/103650320-2c835480-4fa3-11eb-9c88-e98dc0932d61.png)
> Fig 5. Rasa run actions and rasa shell

2-2 외부 연결
 Rasa를 외부 인터페이스나 다른 서버에 연결시키기 위해서는 프로젝트 파일 내부의 credentials.yml 파일에서 token이나 proxy등을 일치시켜 사용해야한다.  
대부분 양 쪽의 포트가 일치해야 하기 때문에 이 때 action 서버를 사용하지 못하는 경우가 많으며, 이런 부분을 보완하기 위해 facebook messenger나  
telegram 등에서는 별도의 기능들이 존재한다.  

![image](https://user-images.githubusercontent.com/43739827/103650400-4d4baa00-4fa3-11eb-87c0-ad462de9fc35.png)
> Fig 6. Facebook messenger channel connect example

# 3. Training Data

# 4. Domain

# 5. Configuration

# 6. Actions
