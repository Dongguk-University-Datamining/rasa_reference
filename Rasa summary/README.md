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

 Rasa가 사용자의 input을 이해하고 정의되어있는 output을 출력하기 위해서는 반드시 training data가 필요하다. 세 가지의 범주가 존재하며 각각  
1) NLU, 2) Story, 3) Rule이라 불린다. Rasa 2.0 버전부터 세 가지 전부 yaml 형식을 따르며, 프로젝트 파일 내부에서 data 폴더 내에 위치한다.  

3-1. NLU
 NLU는 사용자의 input을 사전에 저장하고 training한 뒤, 실행되었을 때 사용자의 문장을 이해하고 정의되어있는 output을 예측하도록 하는 역할을 한다.  
NLU에는 사용자의 의도를 예측할 수 있는 1) intent와 메시지에 포함되어 있는 2) entity, 동일한 entity value를 정의하여 문장의 사용 범위를  
다양하게 할 수 있는 3) synonym이 포함된다.

3-1-1. Intent
 Rasa가 사용자의 input을 이해하기 위해서는 이 intent의 존재가 중요하다. intent를 추가하기 위해서는 intent 이름과 이에 해당하는 example들이 요구되며,  
정의되는 intent 이름은 하나의 범주에 속하기 때문에 포함되는 example들은 전부 같은 의도를 지니고 있어야 한다.

![image](https://user-images.githubusercontent.com/43739827/103650662-bc290300-4fa3-11eb-930d-feba4e13d8c2.png)
> Fig 7. Intent  

생성한 intent는 반드시 domain에서 명시해주어야 하며, 하나의 intent에는 최소 2개 이상의 example이 존재해야 bot이 해당 intent를 인식할 수 있다.  

![image](https://user-images.githubusercontent.com/43739827/103650695-ce0aa600-4fa3-11eb-9117-dc3c0640e983.png)
> Fig 8. Domain defines intent  

3-1-2. Entity
 Entity는 사용자의 input으로부터 추출하는 키워드이다. 예를 들어 문장에서 전화 번호나 특정 장소, 제품의 이름등이 해당된다.  
이 entity는 actions.py에서 조건문을 정의하는데에 사용되거나 story에서 entity value를 통해 story flow를 따라가도록 특정하는데에 사용된다.  

![image](https://user-images.githubusercontent.com/43739827/103650761-e4186680-4fa3-11eb-9410-de6f5b6ae0eb.png)
> Fig 9. Entity example  

Entity format에는 두 가지가 존재한다.
1.	[<entity value>](entity name)
2.	[<entity value>]{entity : entity name}
1과 2는 기능상 동일하게 작동을 한다. 그럼에도 양식이 나뉘게 된 이유는 2를 사용하여 entity의 role과 group을 지정해 줄 수 있기 때문이다.  
예를 들어 비행기 예약에 대한 챗봇을 만든다면 사용자의 문장에서는 출발지와 도착지에 대한 정보가 필요하게 된다.  
이 때 role을 사용하여 출발지와 도착지를 지정해 두 개의 city entity가 구분되는 다른 역할을 수행하도록 할 수 있다.

![image](https://user-images.githubusercontent.com/43739827/103650864-0316f880-4fa4-11eb-97d6-2c3a5809bd47.png)
> Fig 10. Entity role  

 group은 entity들을 하나의 집합으로 취급하여 다른 entity들과 구분되도록 하기 위하여 사용된다. 예를 들어 피자 주문에 관한 챗봇을 만든다면 사용자가  
2판 이상을 주문했을 때 각각의 사이즈나 토핑이 다를 수 있다. 이런 경우 group을 사용하여 entity들을 각각의 집합으로 나눌 수 있다.  

![image](https://user-images.githubusercontent.com/43739827/103650935-1924b900-4fa4-11eb-9654-387e22b6c3bd.png)
> Fig 11. Entity group  

그러나 만약 Rasa의 프로젝트가 특정 분야의 챗봇을 설계하는 것이 아니라면 이러한 format은 가독성을 저하시키기 때문에 1번을 사용하는 것이 낫다.  
Entity를 사용하기 위해서는 intent와 마찬가지로 domain에 반드시 명시해주어야 하며, intent와 마찬가지로 최소 2개 이상의 example이 존재해야 bot이 해당 entity를 인식할 수 있다.

![image](https://user-images.githubusercontent.com/43739827/103650971-2cd01f80-4fa4-11eb-9438-7be61adb7036.png)  
> Fig 12. Domain defines entity  

![image](https://user-images.githubusercontent.com/43739827/103650973-2e99e300-4fa4-11eb-857f-6417f60a53bb.png)  
> Fig 13. training fail error  

3-1-3. Synonym  

 Synonym은 entity value와 뜻이 같은 단어들을 의미하며 문장에서 사용된 entity value 대신에 synonym으로 대체하여 같은 의미의 다른 문장을 사용할 수 있도록 한다.  
예를 들어 잔고를 확인할 수 있는 챗봇이있다고 하자. account라는 entity에서 entity value로 credit을 사용하여 문장을 생성했으나,  
사용자가 “credit” 대신 “credit account”나 “credit card account”라는 단어를 사용할 수 있다. 이러한 경우를대비해 “credit”의 synonym으로 위의 값들을 정의해주면  
bot이 세 단어가 같은 의미임을 인지하고 개발자가 설정해 둔 flow를 따라가게 된다. synonym을 정의해주지 않으면 각 단어는 언어적으로는 같은 의미도 bot은 다른 의미의 단어로 이해하게 된다.  

![image](https://user-images.githubusercontent.com/43739827/103651077-5e48eb00-4fa4-11eb-8f67-b9103a8e4120.png)
> Fig 14. Synonym example  

 Synonym을 정의할 때 주의해야 할 점은 3-2-2에서 언급했던 Entity format에 따라 정의하는 방식이 달라진다는 것이다.  
위의 [Fig 14]는 1번 유형에서 사용되는 Synonym이며 2번 유형처럼 {}안에서 entity가 선언되었을 경우 어떠한 value의 synonym인지 지정해주어야 한다.  
만약 하나의 nlu파일에서 두 개의 entity format이 같이 사용되어 synonym의 정의도 두 가지 format으로 사용되었다면 중복이 되어 training시에 에러가 발생한다.  

![image](https://user-images.githubusercontent.com/43739827/103651167-7fa9d700-4fa4-11eb-90f2-9b7dfe0f9b4a.png)
> Fig 15. Synonym example 2  

Synonym은 intent, entity와 다르게 별도로 Domain에 정의해줄 필요는 없다.

3-2. Story
 Story는 사용자와 bot의 대화 flow를 관리하는 training data이다. 또한 transformer architecture를 사용하여 정의된 story flow가 아니더라도  
대화가 끊기지 않도록 모델을 training하는 역할을 한다.  
Story의 경우 정해진 format을 준수해야 하며 intent, action, entity들이 포함된다.

![image](https://user-images.githubusercontent.com/43739827/103651275-b122a280-4fa4-11eb-9d80-e4fbcb06577c.png)
> Fig 16. Story format  

[Fig 16]의 format을 반드시 준수해야 하며 특히 특정 entity value를 사용하기 위해서는 “entities” 아래에 선언하는 것과 하나의 story는 마지막에 action이 와야함을 인지해야 한다.  

3-2-1. Checkpoint and OR Statement  

Checkpoint는 특정 story에서 또 다른 특정 story로 연결하는 일종의 표지판이다. 매우 긴 길이의 story를 구상하고 있을 때 이러한 checkpoint는  
story example을 모듈화하여 생성할 수 있다는 장점이 있으며 또한 일반적인 story와 다르게 가장 처음에 오는 event로 action이나 response가 나타날 수 있다.  
그러나 checkpoint의 양이 많아지면 training이 느려지고 bot이 story example을 인식하기 어렵다는 큰 단점이 존재한다.

![image](https://user-images.githubusercontent.com/43739827/103651377-d6171580-4fa4-11eb-8634-562625ba3860.png)
> Fig 17. Checkpoints  

Story example의 가장 마지막에 있는 checkpoint는 다른 story example에서 가장 맨 앞에 있는 이름이 같은 checkpoint와 이어진다.  
OR Statement는 여러 개의 intent를 하나로 묶어 내부에 선언된 intent 중 하나만 사용되어도 flow가 진행되게끔 한다.  
예를 들어 story example에서 hello intent가 입력되고 그에 대한 action으로 utter_hello가 출력된 후에 stop_dialog나 confused intent가 입력되었을 때  
flow가 진행되게끔 하고 싶다면, 두 개의 story example을 생성할 필요 없이 “or:”를 사용하고 그 안에 두 개의 intent를 정의해주면 원하는 기능을 수행할 수 있다.

![image](https://user-images.githubusercontent.com/43739827/103651681-53428a80-4fa5-11eb-8288-d6faa9103fde.png)
> Fig 18. OR Statement  

3-3. Rule  

 Rule은 training data 중 하나로 항상 사용하는 짧은 대화를 정의하는 데 사용한다. rule은 story와 다르게 정의되어 있지 않은 flow가 사용되었을 때 에러가 발생하기 때문에 사용에 주의해야 한다.  
또한 rule과 story에서 중복되는 경우 에러가 발생하기 때문에 example을 생성할 때 유의해야 한다.  
 Rule을 사용하기 위해서는 가장 먼저 config.yml의 policies에서 “RulePolicy”를 선언해주어야 한다.  

![image](https://user-images.githubusercontent.com/43739827/103651776-6ce3d200-4fa5-11eb-9215-cbe67b3c77b2.png)
> Fig 19. Define RulePolicy  

 선언한 후에 rule.yml 파일에 사용할 intent와 action을 정의하여 하나의 rule로 만든다. 위에서 언급했던 것처럼 rule과 story에서 겹치는 example이 존재하면  
에러가 발생하기 때문에 특히 주의해야 하는데, 예를 들어 rule에서 hello intent와 utter_hello action을 하나로 묶어 생성한 뒤 story에서 hello intent와 utter_how_are_you action을 example로 생성하면  
hello intent가 충돌하여 에러가 발생하게 된다.

![image](https://user-images.githubusercontent.com/43739827/103651855-8b49cd80-4fa5-11eb-9d57-58f9ab6d6f6d.png)
> Fig 20. Create Rule example  

만약 특정 rule을 대화가 시작됐을 때에만 사용하고자 한다면 “conversation_start: true”를 추가 작성해주면 해당 rule은 반드시 대화의 처음에서만 작동하게 된다.  

![image](https://user-images.githubusercontent.com/43739827/103651907-9f8dca80-4fa5-11eb-8430-40ab01fa7081.png)
> Fig 21. Rule using conversation_start   

 또한 rule에 특정 조건들을 선언하여 반드시 그 조건들을 따르도록 정의할 수 있다. 이 때에는 “condition” 키를 추가 작성해줘야 한다.  

![image](https://user-images.githubusercontent.com/43739827/103651913-a1f02480-4fa5-11eb-8504-b284f0f384cd.png)
> Fig 22. Rule using condition key  

 [Fig 22]의 경우 해당 rule은 userinfo_form action의 slot이 전부 채워질때까지 반복하게 되며 도중에 explain intent가 입력되면 utter_explain action을 한 번 출력한 뒤 다시 userinfo_form action의  slot이 전부 채워질때까지 반복한다. form action에 대한 설명은 6. Action에서 자세하게 다룬다.  

# 4. Domain

# 5. Configuration

# 6. Actions
