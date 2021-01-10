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
 시작하기 앞서 여기서 설명하는 action 서버란 사용자의 task에 맞게 설계되어 있는 actions.py를 bot이 사용하도록 하는 것으로, 후에 서술할 domain에 정의되어있는 utterance만을 사용한다면 action 서버를 사용하지 않아도 된다.  
만약 actions.py를 사용하는 프로젝트라면 터미널을 통해 해당 프로젝트의 디렉토리로 이동한 뒤 **rasa run actions** 를 입력하여 action 서버를 실행시킨다.  
후에 별도의 터미널을 실행하여 마찬가지로 해당 프로젝트의 디렉토리로 이동한 뒤 rasa shell을 입력하여 model을 불러온다.  
정상적으로 실행된다면 rasa shell을 입력한 터미널에서 사용자의 input을 받으며 bot의 output이 출력된다.

![image](https://user-images.githubusercontent.com/43739827/103650320-2c835480-4fa3-11eb-9c88-e98dc0932d61.png)
> Fig 5. Rasa run actions and rasa shell

2-2 외부 연결
 Rasa를 외부 인터페이스나 다른 서버에 연결시키기 위해서는 프로젝트 파일 내부의 credentials.yml 파일에서 token이나 proxy등을 일치시켜 사용해야한다.  
대부분 양 쪽의 포트가 일치해야 하기 때문에 이 때 action 서버를 사용하지 못하는 경우가 많으며, 이런 부분을 보완하기 위해 facebook messenger나 telegram 등에서는 별도의 기능들이 존재한다.  

![image](https://user-images.githubusercontent.com/43739827/103650400-4d4baa00-4fa3-11eb-87c0-ad462de9fc35.png)
> Fig 6. Facebook messenger channel connect example

# 3. Training Data

 Rasa가 사용자의 input을 이해하고 정의되어있는 output을 출력하기 위해서는 반드시 training data가 필요하다. 세 가지의 범주가 존재하며 각각 (1) NLU, (2) Story, (3) Rule이라 불린다. Rasa 2.0 버전부터 세 가지 전부 yaml 형식을 따르며, 프로젝트 파일 내부에서 data 폴더 내에 위치한다.  

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
1.	[entity value](entity name)
2.	[entity value]{entity : entity name}
1과 2는 기능상 동일하게 작동을 한다. 그럼에도 양식이 나뉘게 된 이유는 2를 사용하여 entity의 role과 group을 지정해 줄 수 있기 때문이다.  
예를 들어 비행기 예약에 대한 챗봇을 만든다면 사용자의 문장에서는 출발지와 도착지에 대한 정보가 필요하게 된다.  
이 때 role을 사용하여 출발지와 도착지를 지정해 두 개의 city entity가 구분되는 다른 역할을 수행하도록 할 수 있다.

![image](https://user-images.githubusercontent.com/43739827/103650864-0316f880-4fa4-11eb-97d6-2c3a5809bd47.png)
> Fig 10. Entity role  

 group은 entity들을 하나의 집합으로 취급하여 다른 entity들과 구분되도록 하기 위하여 사용된다. 예를 들어 피자 주문에 관한 챗봇을 만든다면 사용자가 2판 이상을 주문했을 때 각각의 사이즈나 토핑이 다를 수 있다. 이런 경우 group을 사용하여 entity들을 각각의 집합으로 나눌 수 있다.  

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

 Story는 사용자와 bot의 대화 flow를 관리하는 training data이다. 또한 transformer architecture를 사용하여 정의된 story flow가 아니더라도 대화가 끊기지 않도록 모델을 training하는 역할을 한다.  
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
예를 들어 story example에서 hello intent가 입력되고 그에 대한 action으로 utter_hello가 출력된 후에 stop_dialog나 confused intent가 입력되었을 때 flow가 진행되게끔 하고 싶다면, 두 개의 story example을 생성할 필요 없이 “or:”를 사용하고 그 안에 두 개의 intent를 정의해주면 원하는 기능을 수행할 수 있다.

![image](https://user-images.githubusercontent.com/43739827/103651681-53428a80-4fa5-11eb-8288-d6faa9103fde.png)
> Fig 18. OR Statement  

3-3. Rule  

 Rule은 training data 중 하나로 항상 사용하는 짧은 대화를 정의하는 데 사용한다. rule은 story와 다르게 정의되어 있지 않은 flow가 사용되었을 때 에러가 발생하기 때문에 사용에 주의해야 한다.  
또한 rule과 story에서 중복되는 경우 에러가 발생하기 때문에 example을 생성할 때 유의해야 한다.  
 Rule을 사용하기 위해서는 가장 먼저 config.yml의 policies에서 “RulePolicy”를 선언해주어야 한다.  

![image](https://user-images.githubusercontent.com/43739827/103651776-6ce3d200-4fa5-11eb-9215-cbe67b3c77b2.png)
> Fig 19. Define RulePolicy  

 선언한 후에 rule.yml 파일에 사용할 intent와 action을 정의하여 하나의 rule로 만든다. 위에서 언급했던 것처럼 rule과 story에서 겹치는 example이 존재하면 에러가 발생하기 때문에 특히 주의해야 하는데, 예를 들어 rule에서 hello intent와 utter_hello action을 하나로 묶어 생성한 뒤 story에서 hello intent와 utter_how_are_you action을 example로 생성하면 hello intent가 충돌하여 에러가 발생하게 된다.

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

Domain은 bot이 반드시 알고 있어야 하는 (1) intent, (2) entity, (3) slot, (4) response, (5) form, (6) action을 명시한다.  

![image](https://user-images.githubusercontent.com/43739827/104021260-d102d200-5201-11eb-9fdc-51d2dcc0b248.png)
> Fig 23. Rasa Domain file  

4-1. Intent Section  

3-1-1에서 언급했던 것처럼 Intent를 사용하기 위해서는 nlu.yml 파일에서 example을 추가하는 것과 domain에서 intent를 추가하는 것, 총 두 가지의 절차가 반드시 요구된다.  

![image](https://user-images.githubusercontent.com/43739827/104021335-eed03700-5201-11eb-875f-0f0a01c80807.png)
> Fig 24. Domain defines intent  

또한 domain의 intent section에서 특정 entity의 사용을 허가하거나(use_entities) 거부할 수 있다(ignore_entities).  
만약 특정 intent가 모든 entity를 거부한다면 해당 intent에 “use_entities: []”를 추가한다.  

![image](https://user-images.githubusercontent.com/43739827/104021374-fee81680-5201-11eb-8469-932517f2a184.png)
> Fig 25. Intent ignores all entities  

모든 entity가 아닌 특정 entity만을 사용하거나 거부하고자 한다면 아래의 format을 사용한다.  

![image](https://user-images.githubusercontent.com/43739827/104021414-0e675f80-5202-11eb-9302-d600ea4cbdd5.png)
> Fig 26. Use_entities and ignore_entities  

[Fig 24]를 예로 들면, greet intent는 name, first_name entity를 사용하며 location, age entity는 사용할 수 없다.  
사용 거부된 entity들은 다음 action을 예측하는 데 사용되지 않는다.  

4-2. Entity section  

 Entity section에서는 nlu에서 사용하고자 하는 모든 entity를 모두 선언해준다. 3-1-2에서 설명했던 entity의 2번째 format으로 사용할 수 있는 group, role은 이 entity section에서 정의되어야지만 사용할 수 있다.  

![image](https://user-images.githubusercontent.com/43739827/104021491-322aa580-5202-11eb-91eb-dadae9f125ba.png)
> Fig 27. Entity section  

4-3. Slot section  

Slot은 bot의 메모리이다. key-value 쌍으로 저장되며 entity와 같은 이름으로 사용된다.  

![image](https://user-images.githubusercontent.com/43739827/104021542-48d0fc80-5202-11eb-973e-af0bb6872b64.png)
> Fig 28. Slot format  

Slot이 다음 action을 예측하는 데 영향을 미치지 않도록 하고 싶다면 influence_conversation을 추가하고 해당 값으로 false를 정의한다. 그러나 slot이 다음 액션을 예측하는데 영향을 주도록 하고 싶다면 influence_conversation을 기입하지 않거나 해당 값으로 “true”를 입력한다.
 예를 들어 home_city라는 slot이 있고 influence_conversation의 값이 true라고 하자. 두 개의 문장 “What is the weather like?”와 “What is the weather like in [Bangalore](home_city)?”를 입력한다면 두 번째 문장의 경우 home_city entity value는 다음 action을 예측하는 데 영향을 주어 intent에 대응하는 action을 출력할 수 있으나, 첫 번째 문장의 경우 bot이 단순히 intent만 보고 다음 action을 예측하기 때문에 fallback action이나 원치 않는 다른 action이 출력될 수 있다.  

![image](https://user-images.githubusercontent.com/43739827/104021572-5be3cc80-5202-11eb-8c02-566dc8d06e1d.png)
> Fig 29. Influence conversation example  

위의 예에서도 확인할 수 있듯이 slot에는 모두 “type”을 지정해주어야 한다. 이 type은 총 6개가 있으며 각각 (1) Text, (2) Boolean, (3) Categorical, (4) Float, (5) List, (6) Any다.
(1) Text는 Slot에 문자가 채워짐을 의미하며, (2) Boolean은 true 값이나 false값이 채워짐을 의미한다. (3) Categorical의 경우 slot에 N개의 값 중 하나가 저장될 수 있으며, 들어갈 수 있는 값들을 전부 나열해주어야 한다.

![image](https://user-images.githubusercontent.com/43739827/104021643-77e76e00-5202-11eb-9039-1ea831788fb3.png)
> Fig 30. Categorical type example  

(4) Float은 실수(real number)의 범위를 소수로 정하여 Slot의 값이 정해진 범위 내의 값이된다.

![image](https://user-images.githubusercontent.com/43739827/104021687-8897e400-5202-11eb-8f91-29def85d23c3.png)
> Fig 31. Float type example  

(5) list는 리스트 형태의 값이 Slot에 저장됨을 의미하며 리스트가 비어있는지 혹은 비어있지 않은지만 중요하고 길이는 대화에 영향을 끼치지 않는다.
(6) any는 위에서 사용되지 않은 type이 저장되는 slot으로써 대표적인 예로 딕셔너리가 있다.  
이렇게 다양한 slot들은 저장되는 값이 상당히 중요하다. 그러나 slot이 대화 도중에 채워지지 않아 원치 않는 흐름으로 대화가 이어질 수 있는데, 이러한 경우를 대비하여 slot에는 “initial_value”가 존재한다. 이 initial_value에 특정 값을 정해주면 해당 slot은 bot이 시작될 때부터 특정 값을 memory에 저장하고 있는다.

![image](https://user-images.githubusercontent.com/43739827/104021739-9f3e3b00-5202-11eb-9c62-8638509d622b.png)
> Fig 32. initial value example  

4-4. Response section  

 Response는 6. Action에서 상세하게 설명하지만 요약하자면 action 서버를 따로 실행하지 않고 사용자의 input에 대한 반응을 출력하는 action의 한 종류이다. response는 단순히 domain에서 정의하여 사용하며, slot을 통해 memory에 저장된 value를 출력할 수 있다.

4-5. Form section  

 Form은 action의 한 종류로 챗봇이 사용자가 올바른 정보를 입력할 수 있도록 돕는 역할을 한다. 구체적인 설명은 후술할 6. Action을 참고한다.

4-6. Action section  

 Domain에서는 custom action의 이름을 action section에 명시해야한다. 만약 이를 어기고 사용할 시엔 Rasa를 training 할 시 core를 training 할 때 오류가 발생하면서 모델이 생성되지 않는다. 모델의 크기가 크면 클수록 training의 시간이 길어지는데 가장 마지막에 domain에 명시된 action과 사용된 action을 대조하기 때문에 만약 명시되어있지 않은 action이 있다면 수정 후 다시 긴 시간을 들여 training 해야 한다는 문제점이 있으니 주의해야한다.

![image](https://user-images.githubusercontent.com/43739827/104021773-b2510b00-5202-11eb-9b39-79ad3f0caf88.png)
> Fig 33. Domain action section  

# 5. Configuration

Configuration 파일은 component와 policy를 정의하여 모델이 사용자의 input을 기반으로 예측할 수 있도록 하는 역할을 한다. 파일 내부에선 (1) language, (2) pipeline, (3) policies를 명시해야 하는데 (1) language와 (2) pipeline은 component를 명시해 모델이 Nlu 예측을 하도록 하는 역할을 하며 (3) policies는 모델이 다음 action을 예측하도록 하는 역할을 한다.  
이 configuration 파일은 프로젝트 폴더 내부의 config.yml이 담당하고 있다.  

![image](https://user-images.githubusercontent.com/43739827/104092269-36b89200-52c6-11eb-91cf-0d542b8f372f.png)
> Fig 34. config.yml

5-1. Language support  

Rasa를 이용한 챗봇을 설계할 때는 모델에서 사용될 언어 코드를 기입해야 한다. 어떤 언어든 사용할 수 있으며 language model로부터 pre-train된 word vector를 불러와 유사도를 측정하지만 만약 pre-train된 모델이 존재하지 않은 언어라면 training data에서 스스로 언어의 특징을 training한다. Rasa에서는 language model로 spaCy를 지원하고 있으므로 지원하는 언어 모델을 패키지 사이트에서 사전에 확인하는 것이 좋다.

![image](https://user-images.githubusercontent.com/43739827/104092277-49cb6200-52c6-11eb-9a31-2550cf53728e.png)
> Fig 35. Support language list  

만약 사용하고자 하는 언어가 spaCy에서 지원하지 않는다면 “xx(multi-language)”로 언어를 정의하고 사용하면 된다.  

Pre-train된 language model을 사용하는 이유로는 이런 모델들이 위키피디아 같은 방대한 양의 텍스트를 train하여 word vector를 이미 구해놨기 때문에 개발자는 적은 training data 만으로도 훌륭한 성능을 낼 수 있기 때문이다.

5-2. Components  

Rasa에서 사용되는 component들은 (1) Tokenizer, (2) Featurizer, (3) Intent classifier, (4) Entity extractor, (5) Selector, (6) Custom component 총 6개의 범주로 나뉜다.

![image](https://user-images.githubusercontent.com/43739827/104092302-77181000-52c6-11eb-82fe-020bc7bb6236.png)
> Fig 36. Components pipeline

5-2-1. Tokenizers  

Tokenizer의 역할은 문장 텍스트를 나누어 토큰화하는 것이다. [Fig 36]에서는
“WhitespaceTokenizer”가 사용되었으며 사용자의 메시지, response, intent를 공백을 기준으로 나누는 역할을 한다.

5-2-2. Featurizers  

Featurizer는 (1) sparse featurizer와 (2) dense featurizer 2개의 type으로 나뉜다. (1) sparse featurizer의 경우 featurize할 때 많은 결측 값들을 포함한 feature vector를 반환한다(ex. 영행렬). feature vector는 일반적으로 bot의 많은 메모리를 차지하는 데, sparse featurizer는 0이 아닌 값과 벡터 내부 값들의 위치만을 저장해 메모리를 많이 절약할 수 있고 방대한 training data를 train하기에 적합하다.  

또한 모든 featurizer (1) sequence featurize, (2) sentence featurize 두 종류의 featurize를 반환한다. (1) sequence featurize의 행렬 크기는 [(토큰의 개수) X (feature 차원)]이며 이 행렬엔 모든 토큰의 feature vector를 순차적으로(in the sequence) 포함하고 있다. 즉, sequence model을 training 할 수 있도록 하는 것이다. (2) sentence featurize의 행렬 크기는 [1 X (feature 차원)]이며 이 행렬엔 온전한 발화(complete utterance)의 feature vector를 포함한다. 이 sentence featurize는 bag-of-words 모델에 사용할 수 있다는 장점이 있다.  

[Fig 36]에서는 “RegexFeaturizer”, “LexicalSyntacticFeaturizer”, “CountVectorsFeaturizer”가 featurizer로써 사용되었다. RegexFeaturizer는 sparce featurizer로 정규 표현식을 사용하여 사용자의 메시지에서 벡터를 생성한다. 생성한 feature는 entity 추출이나 intent 분류에 사용되며, 이 featurize에서 사용될 정규 표현식은 nlu에서 정의하며 regex의 이름을 intent나 entity 이름과 대응시킬 필요는 없다.

![image](https://user-images.githubusercontent.com/43739827/104092334-a9297200-52c6-11eb-975a-f64c99600ef7.png)
> Fig 37. Regex expression example  

LexicalSyntacticFeaturizer는 sparse featurizer로 엔티티 추출을 위해 사용자의 메시지에서 lexical/syntactic feature를 생성한다.  

CountVectorsFeaturizer는 sparse featurizer로 사용자의 메시지, intent, response를 bag-of-words로 생성한다. [Fig 36]을 예로 들면 analyzer char_wb는 character n_gram을 사용하며 boundary를 min_ngram, max_ngram으로 설정하고 특정 값을 명시해주지 않는다면 default value는 각각 1이다.

5-2-3. Intent classifier  

Intent classifier는 domain에 정의되어 있는 intent중 하나를 user message에 할당하는 역할을 한다. 이 중 DIET(Dual Intent Entity Transformer) Classifier는 Intent 분류와 Entity 추출에 사용된다. 만약 DIETClassifier를 Intent 분류에만 사용하고 싶다면 “entity_recognition”의 값을 false로 정의하고, 반대로 entity 추출에만 사용하고 싶다면 “intent_classification”의 값을 true로 정의하면 된다. 아무런 값도 정의하지 않는다면 entity_recognition과 intent_classification의 값은 true로 인식된다.  

다른 intent classification인 FallbackClassifier는 입력받은 메시지에 대해 nlu classification의 값이 모호하다면 nlu_fallback intent로 처리하는 역할을 한다. 이 때 nlu_fallback의 confidence는 “1-top intent confidence”이다.

5-2-4. Entity extractor  

Entity extractor는 사용자의 메시지로부터 이름이나 장소 같은 entity value를 추출한다. 이 중 EntitySynonymMapper는 training data에 정의되어 있는 synonym을 문장의 entity와 동일하게 mapping하는 역할을 한다.

5-2-5. Selector  

Selector는 response action을 사용하기 위해서 반드시 정의해야 하는 component이다. training epoch와 retrieval intent를 명시하여 해당 intent에 대한 training을 진행한다. 자세한 내용은 6. Action에서 서술한다.

5-3. Policies  

Policy는 사용자의 메시지가 입력되고 난 후 다음에 출력될 action을 예측하는 역할을 한다. config.yml에서 policies 아래에 명시하며, (1) machine-learning policy와 (2) rule-based policy로 나뉜다.

![image](https://user-images.githubusercontent.com/43739827/104092376-e4c43c00-52c6-11eb-8f49-5a3136cafa5a.png)
> Fig 38. Defines policies  

5-3-1. Machine-leaning policy  

Machine-leaning policy는 대표적으로 (1) TED policy와 (2) Memoization policy 2개가 있다.
(1) TED(Transformer Embedding Dialogue) policy는 “Transformer architecture”를 기반으로 하는 policy이다. 기존의 Rasa는 계층적인(hierarchical) RNN 구조를 사용해왔다. 그러나 기본적으로 RNN 아키텍처는 하나의 시퀀스에 포함된 모든 데이터가 전체 시퀀스로부터 인코딩되어 생성되는 결과에 영향을 미친다고 추측한다. 하지만 인간의 대화에서 단일 대화 내 발화자들이 여러 주제를 말하는 경우가 존재한다. 이는 한 번의 발화가 전체 대화의 흐름에 영향을 미치지 않을 수 있다는 것이다. 이런 이유로 Rasa는 기존 RNN 아키텍처를 포기하고 TED policy를 사용하게 되었다.  

TED policy의 특징 중 하나는 train story를 통해 대화의 flow가 방해되지 않도록 할 수 있는 점이다. 아래의 [Fig 39]와 같은 story example이 있다고 가정하자.

![image](https://user-images.githubusercontent.com/43739827/104092395-01607400-52c7-11eb-8ce9-4aacdd5ce7fa.png)
> Fig 39. Story example  

또한 config.yml에서 TED policy를 선언하고 max_history 파라미터의 값으로 정수를 선언한 뒤 정해진 story flow에서 벗어났을 때 다시 돌아올 수 있는지를 확인한다.  

![image](https://user-images.githubusercontent.com/43739827/104092403-0f15f980-52c7-11eb-8b55-fc666bd9cf19.png)
> Fig 40. TED policy and parameter  

![image](https://user-images.githubusercontent.com/43739827/104092409-1a692500-52c7-11eb-981c-4ef58b6a2db7.png)
> Fig 41. Story flow test  

정의된 story의 flow대로라면 ask_emotion intent에서 bot_emotion의 entity value가 happy이면 두 개의 action이 출력된 후 change_topic intent가 입력되고 이에 대응하여 정의된 action이 출력되면서 story의 flow가 끝나야 한다. 그러나 위의 예제에서 story flow에서 정의되어 있지 않은 intent의 문장 “Wait Wait, I have to pick this phone call.”이 입력되었고 bot 또한 story에 정의되어있지 않은 action(fallback action)이 출력되었다. max_history는 사용자와 bot의 대화들을 저장해 둔 turn의 값 만큼 저장해놓기 때문에 flow가 방해된 후 정의된 intent를 입력하여 story의 flow를 끝마치는 것을 확인할 수 있다.  

max_history 값은 story의 길이를 고려하여 정의해야 한다. 하나의 turn은 사용자가 문장을 입력할 때 까지로 취급한다. 예를 들어 [Fig 39]의 경우 사용자가 3번을 입력하기 때문에 [Fig 39]의 flow를 정상적으로 마치기 위해서는 적어도 4의 max_history가 필요하다. 만약 max_history가 3이라면 utter_you_are_welcome까지 flow가 진행되고 change_topic intent를 사용자가 입력했을 때 bot은 새로운 story가 시작되었다고 판단하게 된다. 그렇기 때문에 story의 flow가 벗어남을 감안한다면 max_history는 최소 5 이상이어야 한다.  

(2) Memoization policy는 training data의 story들을 memory를 통해 기억하고 있다가 현재 user와 bot의 대화가 stories.yml 파일에 선언된 story와 대응하는지를 확인한다. 만약 대응하는 story가 존재한다면 해당 story를 통해 다음 action을 예측하고(confidence: 1.0), 만약 대응하는 story가 없다면 None을 예측한다(confidence: 0.0)
Memoization이 story를 대응시킬 때 TED policy와 마찬가지로 “max_history”를 사용한다.

![image](https://user-images.githubusercontent.com/43739827/104092420-3240a900-52c7-11eb-94ad-4b90377f2230.png)
> Fig 42. Memoization Policy  

5-3-2. Rule-based policy  

Rule Policy는 대화에서 반드시 사용되는 일부분을 다루는 역할을 한다. 예를 들어 사용자가 “hi, how are you?”라고 물었을 때 “good” 혹은 “fine”을 반드시 bot이 출력하도록 하는 것이다.  

또한 Rule Policy는 fallback action을 사용하기 위해서 반드시 정의해주어야 한다. 이 때 사용해야하는 설정으로 “core_fallback_threshold”, “core_fallback_action_name”, “enable_fallback_prediction”이 있다.

![image](https://user-images.githubusercontent.com/43739827/104092430-42f11f00-52c7-11eb-80a2-6ba13429c4f1.png)
> Fig 43. RulePolicy  

core_fallback_threshold는 user의 메시지 이후 예측되는 다음 action들의 confidence가 일정 값 미만이라면 fallback action을 출력하도록 하는 것이다.  

core_fallback_action_name에서는 사용할 fallback action의 이름을 명시하며, enable_fallback_prediction은 fallback action을 출력할 지 여부를 boolean 값으로 정의한다.

# 6. Actions

사용자의 message가 입력될 때 마다 모델은 bot이 다음에 수행 할 action을 출력한다. action의 범주는 1) Response, 2) Retrieval action, 3) Custom action, 4) Form action, 5) Fallback action, 6) Default action으로 나뉜다.

6-1. Response  

Response는 bot이 사용자에게 보내는 메시지다. 텍스트로만 사용할 수 있으나 이미지나 버튼만은 사용이 가능하다.  
Response의 정의는 Domain의 response section에 정의한다(4-4 참조). 각 response의 이름 앞에는 반드시 “utter_”로 시작해야 함을 인지해야 한다.

![image](https://user-images.githubusercontent.com/43739827/104123626-a8104780-538f-11eb-8ecc-a66cc202ec22.png)
> Fig 44. Response example  

[Fig 44]에서 볼 수 있는 것처럼 각 문장은 “- text”로 표기를 해주어야 하며 큰 따옴표를 사용하지 않아도 된다. 또한 문장 내에서 {}를 통해 채워진 slot을 출력할 수 있다.   

![image](https://user-images.githubusercontent.com/43739827/104123641-b8282700-538f-11eb-9969-7ca2bcf15b80.png)
> Fig 45. Response uses slot value  

이렇게 작성된 response는 story에서 action으로 사용된다.  

![image](https://user-images.githubusercontent.com/43739827/104123650-cd9d5100-538f-11eb-8dd6-36cc74ccbfaf.png)
> Fig 46. Story uses utter action  

또한 actions.py에서 dispatcher를 통해 action server에서 response message를 출력할 수 있다.  

![image](https://user-images.githubusercontent.com/43739827/104123660-e1e14e00-538f-11eb-8422-408776afa844.png)
> Fig 47. Dispatcher  

6-2. Retrieval action  

Retrieval은 하나의 intent를 작은 소분류로 나누고 이에 해당하는 action을 출력하도록 하는 것이다. 먼저 retrieval intent를 다른 intent와 마찬가지로 nlu.yml에서 정의한다. 이 때 “/”를 이용해 각 범주에 대해 명시해야 한다.

![image](https://user-images.githubusercontent.com/43739827/104123668-f0c80080-538f-11eb-89a3-a87a35a36f0b.png)
> Fig 48. Retrieval intent  

Retrieval action을 사용하기 위해서는 먼저 config.yml에서 ResponseSelector를 pipeline에 선언하고 “retrieval_intent”에 사용할 intent의 이름을 명시한다.  

![image](https://user-images.githubusercontent.com/43739827/104123685-03423a00-5390-11eb-8c07-519e18353f22.png)
> Fig 49. ResponseSelector  

다음으로 domain에서 response section에 retrieval action을 정의하며, response처럼 이름 앞에 “utter_”를 추가해야 한다.  

![image](https://user-images.githubusercontent.com/43739827/104123697-1228ec80-5390-11eb-897e-8593652eea5a.png)
> Fig 50. Retrieval action  

Retrieval은 최종적으로 rule.yml에서 intent와 action을 명시한다. 즉, retrieval intent는 다른 action과 함께 쓰일 수 없고 반대로 retrieval action은 다른 intent와 함께 쓰일 수 없다.  

![image](https://user-images.githubusercontent.com/43739827/104123712-27058000-5390-11eb-81db-98e4db1d93fb.png)
> Fig 51. Rule defines retrieval  

6-3. Custom action  

Action server를 실행시키기 위해서는 actions.py를 이용해 코드를 작성해야 한다. 일반적인 action과의 차이점으로는 bot의 출력으로 외부 api를 불러오거나 특정 slot value에 대한 조건을 정할 수 있다. actions.py에서는 일반적으로 rasa_sdk 패키지가 주로 사용된다.

![image](https://user-images.githubusercontent.com/43739827/104123734-384e8c80-5390-11eb-97dc-0c8d4ea7f595.png)
> Fig 52. actions.py libraries  

하나의 action은 class 내부에 함수가 선언되어 세부 사항을 정의하는 방식이다.  

![image](https://user-images.githubusercontent.com/43739827/104123746-47353f00-5390-11eb-81a1-e4494714ba97.png)
> Fig 53. Custom action  

위의 틀은 크게 바뀌지 않는다. class로 (Action)을 선언하고 def name을 통해 action의 이름을 정의하며 이 이름은 domain의 action section에서 명시한 이름과 동일해야 한다. slot을 사용하기 위해서는 “tracker.get_slot(“<slot_name>”)”을 사용하며 이 때 선언한 변수의 이름으로 slot에 대한 조건문을 정의할 수 있다.  

6-4. Form action  

Form은 외부 api 실행이나 식당 예약등을 위해 몇 번의 대화를 모아 하나의 정보를 완성시키는 역할을 한다. Form action을 사용하기 위해서는 config.yml에서 RulePolicy를 선언해야 한다.  
Form은 domain에서 정의해 사용한다. 이 때 명시한 form의 이름은 story나 rule에서 action으로 사용한다.

![image](https://user-images.githubusercontent.com/43739827/104123764-5f0cc300-5390-11eb-847e-a404f5848d7d.png)
> Fig 54. Domain form section  

[Fig 54]를 예로 들면 해당 form의 이름은 “restaurant_form”으로 cuisine slot은 cuisine entity에서 값을 추출해 채우게되고, num_people slot은 number entity에서 값을 추출해 채우게된다.
Form을 활성화하기 위해서는 story나 rule에서 명시해야 한다.

![image](https://user-images.githubusercontent.com/43739827/104123772-6df37580-5390-11eb-9a87-a52111c682a0.png)
> Fig 55. Rule adds form action  

[Fig 55]의 경우 request_restaurant intent는 form action을 실행시키는 트리거다. 마지막에 사용된 “active_loop: restaurant_form”은 form action이 요구하는 slot이 전부 채워질 때 까지 반복하도록 하는 것이다.  

Form은 요구되는 모든 slot이 채워지면 스스로 비활성화 되도록 설계되어있다. 그러나 개발자는 story나 rule에서 form을 끝내는 특정 조건을 명시할 수 있다.  

![image](https://user-images.githubusercontent.com/43739827/104123791-806daf00-5390-11eb-8271-67eefd86e3a8.png)
> Fig 56. Form deactivate  

[Fig 56]에선 restaurant_form이 채워지면 utter_submit과 utter_slots_values가 출력된다.  
Form이 slot을 채우는 방식으로는 (1) from_entity, (2) from_text, (3) from_intent 세 가지가 존재하며 각각 type으로 명시한다. (1) from_entity는 추출된 entity를 기반으로 slot을 채운다. 이 때 entity name을 명시하여 추출할 entity를 지정해주고, 만약 특정 intent name을 명시해주게 되면 해당 intent에서 사용된 entity를 추출하게 된다. intent name을 명시하지 않는다면 전체 intent에서 해당하는 entity를 추출한다.  

![image](https://user-images.githubusercontent.com/43739827/104123820-9da27d80-5390-11eb-9111-e68d6d7ed825.png)
> Fig 57. Type from entity not uses specific intent  

(2) from_text는 사용자의 다음 발화를 slot에 채운다. 만약 특정 intent name을 명시하지 않는다면 slot은 intent에 의존하지 않고 발화를 slot에 채우지만 특정한 intent를 명시하였다면 해당 intent와 대응하는 발화를 slot에 채운다.  
만약 특정 intent는 slot에 채워지지 않도록 하기 위해서는 “not_intent: <intent_name>”을 명시한다.

![image](https://user-images.githubusercontent.com/43739827/104123835-b01cb700-5390-11eb-8db9-fb63c5f7e6e5.png)
> Fig 58. Type from text uses not_intent  

(3) from_intent는 사용자의 intent가 특정 intent이거나 None일 경우 지정한 value를 slot에 채운다. from_text와 마찬가지로 not_intent를 통해 특정 intent는 slot을 채우는 데 해당하지 않도록 지정할 수 있다. 그러나 from_intent는 form의 초기 실행에서는 사용할 수 없다는 단점이 있다.  

![image](https://user-images.githubusercontent.com/43739827/104123850-c460b400-5390-11eb-8d1a-7157e400ce22.png)
> Fig 59. Type from intent uses not_intent  

6-5. Fallback action  

Fallback action에는 두 가지가 존재한다.  
1.	nlu에 threshold를 지정하여 intent가 이 threshold를 넘지 못하면 특정 response를 출력  
2.	core에 threshold를 지정하여 예측되는 다음 action이 threshold를 넘지 못하면 custom action을 출력  

1의 경우 config.yml에서 pipeline의 component로 “FallbackClassifier”를 명시해야 한다. 해당 component에서는 threshold와 ambiguity_threshold를 정의할 수 있다. threshold는 user의 메시지로 예측되는 intent가 정의된 값을 넘지 못하면 fallback을 출력하는 역할을 하고, ambiguity_threshold는 가장 높은 confidence를 가진 두 개의 예측 intent가 정의된 값에 가깝다면 fallback을 출력하도록 하는 역할을 한다.  

![image](https://user-images.githubusercontent.com/43739827/104123879-e2c6af80-5390-11eb-94a7-a0818245a1ae.png)
> Fig 60. FallbackClassifier uses threshold and ambiguity threshold  

이후 domain의 response section에서 출력 될 fallback action을 생성한다.  

![image](https://user-images.githubusercontent.com/43739827/104123888-f245f880-5390-11eb-943b-19aa352ee676.png)
> Fig 61. Fallback action(response)  

사용될 action이 정의되면 rule.yml에서 fallback으로 intent와 생성된 action을 대응시켜줘야 하는데, 이 때 intent의 이름으로는 “nlu_fallback”을 사용한다.  

![image](https://user-images.githubusercontent.com/43739827/104123897-04279b80-5391-11eb-9c8c-11518efe8ee7.png)
> Fig 62. Defines fallback in rule.yml  

이 nlu_fallback은 threshold를 넘지 못한 intent를 통칭하는 것으로, 따로 nlu_fallback이라는 이름을 가진 intent를 생성할 필요는 없다.  
2의 경우 config.yml의 policies에서 RulePolicy를 선언하고 “core_fallback_threshold”, “core_fallback_action_name”, “enable_fallback_prediction”을 통해 action에 대한 fallback을 예측한다.

![image](https://user-images.githubusercontent.com/43739827/104123905-13a6e480-5391-11eb-9501-13f9768840f8.png)
> Fig 63. Defines core fallback  

core_fallback_threshold는 다음 출력으로 예상되는 action이 정의된 threshold를 넘지 못하면 특정 action을 출력되도록 하는 역할이며, core_fallback_action_name은 그 때 출력될 action의 이름을 enable_fallback_prediction은 fallback action의 사용 여부를 boolean 값으로 결정하는 역할을 한다.  
core fallback의 경우 nlu fallback과 다르게 rule이나 domain등에서 별도의 추가 없이 사용할 action만을 추가하면 된다. 만약 response가 아닌 custom action을 사용하고자 한다면,

![image](https://user-images.githubusercontent.com/43739827/104123914-23bec400-5391-11eb-953a-2937a6b955f4.png)
> Fig 64. Custom fallback action  

[Fig 64]와 같이 정의하며 action의 이름, dispatcher.utter_message의 template에 사용될 response의 이름만 명확하게 명시해주면 된다.

6-6. Default action  

Default action은 기본적으로 정의되어 있는 action으로 별도로 생성하지 않고 사용할 수 있으며 개발자는 해당 역할을 하는 action을 custom action으로 대체하여 사용할 수 있다.

6-6-1. action_listen  

이 action은 사용자의 input을 아무런 반응을 하지 않고 대기하는 것이다. action_listen은 사실 rule에서 생성한 example을 맨 마지막에 자동적으로 추가된다. 그러므로 하나의 rule이 끝나면 반드시 사용자의 input을 기다리게 되는데, 이것을 단점으로는 rule과 story가 합쳐져 사용될 경우 원하는 flow가 출력되지 않을 수 있다. 그렇기 때문에 action_listen을 사용하지 않기 위해서는 하나의 rule 마지막에 “wait_for_user_input: false”를 추가 작성해야 한다. 만약 이 값을 true로 사용하거나 따로 추가하지 않는다면 action_listen을 마지막에 사용하겠다는 의미가 된다.

![image](https://user-images.githubusercontent.com/43739827/104123927-346f3a00-5391-11eb-856e-c5286932066d.png)
> Fig 65. Ignore action_listen  

6-6-2. action_restart  

action_restart는 전체 대화의 history를 reset하는 역할을 한다. 이 action은 config.yml에서 RulePolicy가 사용될 때 input으로 “/restart”를 입력하면 작동한다.  
 만약 domain에 utter_restart라는 response를 생성하고 안에 문장을 추가한다면 “/restart”를 입력했을 때 세션이 reset 되는 동시에 특정 문장이 출력되게 된다.

6-6-3. action_default_fallback  

fallback action을 사용할 때 특정 fallback action을 생성하여 사용했으나 Rasa에는 기본적으로 제공되어 사용되는 기본 fallback action이 있다. 만약 fallback action을 따로 생성하지 않겠다면 rule이나 config에서 action_default_fallback을 action 이름으로 명시하면 된다.
