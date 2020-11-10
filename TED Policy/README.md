# TED(Transformer Embedding Dialogue) Policy

## Introduction  

**TED Policy**는 이름에서 나타난 것처럼 **트랜스포머 아키텍처**를 기반으로 하는 Rasa의 policy다. 기존의 Rasa는 계층적인(hierarchical) RNN 구조를 사용해왔다.  
그러나 기본적으로 RNN 아키텍처는 하나의 시퀀스에 포함된 모든 데이터가 전체 시퀀스가 인코딩되어 생성되는 결과에 영향을 미친다고 추측한다. 하지만 인간의 대화에서  
단일 대화 내 발화자들이 여러 주제를 말함으로써 여러 주제가 섞일 수 있다. 이는 단순 발화가 전체 대화에 영향을 미치지 않을 수 있다는 것이다.  
이러한 이유로 Rasa는 기존의 RNN에서 TED Policy로 넘어가는 선택을 하게 된다.  

Rasa 0.x.x 혹은 1.x.x 버전에서 사용되던 **embedding_policy** , **keras_policy** 는 2.x.x 버전으로 업그레이드되면서 TED Policy로 통합되었다.  

<img src="https://user-images.githubusercontent.com/43739827/98545008-268d3200-22d8-11eb-8065-050f499198dc.PNG"></img>  
> Fig 1. Embedding Policy Rasa Docs 안내문

<img src="https://user-images.githubusercontent.com/43739827/98545294-9f8c8980-22d8-11eb-8026-b478d5471691.png"></img>  
> Fig 2. Legacy Rasa에서 keras policy를 사용했을 때 나타나는 경고문  

## Feature

TED policy의 특징은 training story를 통해 대화의 flow가 방해되지 않도록 할 수 있다는 점이다.  

아래와 같은 스토리가 있다고 가정한다.  

<img src="https://user-images.githubusercontent.com/43739827/98654075-2e54e100-2381-11eb-8f5e-6b35a1ffb531.PNG"></img>  
> Fig 3. example story  

이 story를 테스트하기 위해서 **config.yml** 의 policy에서 TED Policy를 선언하고 **max_history** 파라미터의 값을 지속적으로 변경해보고자 한다.  

<img src="https://user-images.githubusercontent.com/43739827/98654477-b804ae80-2381-11eb-9ba6-079fcb7c7c04.PNG"></img>  
> Fig 4. config.yml policies  

## TED with max_history  

## Reference  

[1] [Demonstration of TED Policy in Rasa Dialogue Management](https://blog.rasa.com/demonstration-of-our-ted-policy/)  

[2] [Unpacking the TED Policy in Rasa Open Source](https://blog.rasa.com/unpacking-the-ted-policy-in-rasa-open-source/)  

[3] [Dialogue Transformers](https://arxiv.org/pdf/1910.00486.pdf)  
 Vladimir Vlasov, Johannes E. M. Mosig, Alan Nichol

[4] [Rasa Algorithm Whiteboard - TED Policy](https://www.youtube.com/watch?v=j90NvurJI4I)

[5] [Rasa Algorithm Whiteboard - TED in Practice](https://www.youtube.com/watch?v=d8JMJMvErSg&feature=emb_title)
