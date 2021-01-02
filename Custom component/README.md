# Custom component

## Create custom component

Rasa를 사용할 때 있어서 패키지에서 지원하지 않는 자신의 task에 맞는 component를 사용해야 할 때가 있다.  
이 때는 패키지 내부에서 파일을 생성하고 등록을 해주어 완전 새로운 component로 사용하는것이 좋다.  

먼저 자신의 가상환경 경로를 통해 rasa 패키지 폴더에 진입해야 한다.  
anaconda3 폴더에 진입한 뒤 두 가지의 경우에 따라 진입 과정이 달라진다.  

1) 가상환경을 별도로 사용하지 않는 경우  
Lib 폴더에 들어간 뒤 **site-packages** 폴더에 들어가 rasa라는 폴더를 찾는다.  

2) 가상환경을 사용하는 경우  
**envs**라는 폴더에 들어가 자신이 rasa를 사용하는 가상환경의 이름과 같은 폴더로 들어간다. 이후에 1)과 같은 방법으로  
Lib 폴더에 들어가 site-packages의 rasa 폴더를 찾는다.  

rasa 패키지 폴더에 진입하면 내부에 여러 폴더와 파일이 존재한다. config.yml의 **pipeline** 에서 사용될 component들은  
**nlu** 폴더에 들어있다.  

![1](https://user-images.githubusercontent.com/43739827/103458085-1594f600-4d48-11eb-96ba-a9dfe524676e.PNG)

만약 자신의 언어에 맞는 tokenizer를 생성하고 싶다면 **tokenizers** 폴더에 진입한다.  
파이썬 파일을 생성하고 난 뒤에 반드시 import 해야하는 라이브러리들을 상단에 기입한다.  

![2](https://user-images.githubusercontent.com/43739827/103458119-64db2680-4d48-11eb-8e1e-c94b1c54be0f.PNG)

from rasa.nlu.tokenizers.tokenizer import Token, Tokenizer의 경우 tokenizer에서만 사용하는 라이브러리다.  
다시 말해 만약 extracter나 classifier를 만들 경우 해당 부분은 각 카테고리에 맞는 라이브러리가 존재하므로 다른 파일들을 확인하고 사용할 부분을 인지해야한다.  

![3](https://user-images.githubusercontent.com/43739827/103458175-e03cd800-4d48-11eb-811e-7c4a90b2b0d0.PNG)

불러온 라이브러리 밑에 class <custom component name> (Tokenizer) 라는 클래스를 생성해주고 마찬가지로 각 카테고리에 따라 괄호 안의  
**Tokenizer** 는 변경된다.  
아래의 함수는 하위 tokenizer를 관리하는 tokenizer.py에서 사용하는 변수들과 연결된다. 따라서 이미지에 나와있는대로 로컬 함수를 생성해준다.  

이렇게 custom component를 생성했으면 상위 폴더인 **nlu** 로 돌아가 registry.py 파일을 연다.  

import된 라이브러리들을 확인해보면 사용되는 component들이 import 되어있는것을 알 수 있다. 이 부분에 자신이 생성한 파일을 불러들인다.  

![4](https://user-images.githubusercontent.com/43739827/103458245-8557b080-4d49-11eb-836e-7b18143beef7.PNG)

아래로 내려보면 component_classes라는 리스트가 존재한다. 해당 리스트의 import name을 component의 카테고리 아래에 기입한다.  

![5](https://user-images.githubusercontent.com/43739827/103458265-b0420480-4d49-11eb-9011-fc1dcf98017c.PNG)

마지막으로 rasa config.yml의 pipeline에 자신이 생성한 component를 기입하고 train하면 자신의 task에 맞는 rasa model이 생성된다.  

![6](https://user-images.githubusercontent.com/43739827/103458292-e8e1de00-4d49-11eb-9d8b-075087f32d74.PNG)
