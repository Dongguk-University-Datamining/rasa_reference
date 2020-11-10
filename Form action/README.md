# Form action


## break 작성 예제
: 사용자가 Form을 탈출하고 싶을 때, 탈출할 수 있도록 설정하는 방법 

```
stoires:
- story: 
  steps:
  - intent: 'form을 수행할 intent'
  - action: 'your_form'
  - active_loop: 'your_form'
  - intent: 'stop (사용자가 form을 그만두고 싶음을 나타내는 intent)'
  - action: action_deactivate_loop
  - active_loop: null
```

혹은 rule로 정의하여 사용할 수도 있다.
