# deep_learning

## D0326

### 학습내용
PyTorch의 Tensor 객체 생성, 형태 변경(reshape, view), 브로드캐스팅 개념을 중심으로 텐서 연산을 학습함. torch.tensor와 numpy 배열 간 상호 변환도 함께 실습함.

### 개인 복습/실습
- torch.tensor, torch.arange, torch.ones, torch.eye 등 다양한 텐서 생성 방식을 학습함
- view(), reshape()의 차이점과 메모리 공유 여부에 대해 질문하고 실험함
- unsqueeze(), squeeze(), expand(), repeat()을 활용한 브로드캐스팅 시도
- numpy → torch, torch → numpy 변환 과정에서 clone(), detach()의 필요성과 동작 방식을 실습하며 내부 메모리 구조에 대한 이해를 넓힘

### 회고
기본 텐서 조작이라고 생각했지만, 텐서의 shape 변경이나 메모리 공유 문제는 실전에서 오류를 방지하는 핵심이 될 수 있음을 체감했다.

## D0327

### 학습내용
PyTorch 기반으로 단순 선형 회귀를 구현하고, 커스텀 모델 클래스를 설계함. nn.Module을 상속한 구조에서 forward() 정의, optim 설정 및 모델 학습 흐름을 정리함.

### 개인 복습/실습
- torch.nn.Module을 상속받은 사용자 정의 모델 클래스를 직접 설계함
- 파라미터 업데이트를 위한 optim.SGD, optim.Adam 등의 차이점을 질문하고 실습함
- 모델 훈련 흐름(모델 정의 → 손실 함수 → optimizer → 반복학습)을 구조화함
- 'Perceptron의 원리와 단층 신경망이 같은 개념인가?'라는 질문을 통해 역사적 개념과 코드 구현 간의 차이를 정리함

### 회고
모델을 클래스화하면서 코드가 더 길어졌지만, 다양한 실험을 구조적으로 반복할 수 있고 디버깅과 재사용이 쉬워지는 구조의 중요성을 느꼈다.

## D0328

### 학습내용
모델 저장과 불러오기, 커스텀 학습 루프 구현, 함수화 및 파라미터 전달 방식 학습. 학습 중 손실 추적 및 그래프 출력, GPT에 질문한 내용 기반 디버깅과 구조 개선도 함께 병행함.

### 개인 복습/실습
- torch.save(), torch.load()를 사용한 모델 저장 및 불러오기 과정 실습
- 학습 루프 내 주요 과정을 함수로 분리하여 가독성과 재사용성 향상
- '모델 저장 시 state_dict로 저장하는 이유는?', '학습 루프를 왜 함수화하지?' 등 질문하며 구조 개선
- 손실값 저장 리스트 작성 및 epoch별 loss 시각화 코드 구현
- 최종적으로 사용자 정의 모델 + 함수형 루프 + 시각화 기능이 결합된 학습 구조 구성

### 회고
모델 구현에서 끝나는 것이 아니라, 학습 흐름 전체를 설계하고 재사용 가능하게 구성하는 것이 실제 프로젝트에 훨씬 가깝다는 것을 체감함.

## D0331

### 학습내용
다중 클래스 분류 문제를 위한 one-hot encoding과 softmax, cross entropy loss 개념을 학습하고, 정답 예측률과 정확도 지표 계산 방식을 정리함.

### 개인 복습/실습
- torch.nn.functional.one_hot을 이용한 정답 인코딩 실습
- softmax 함수를 수식과 코드 양쪽으로 구현하고 torch.nn.CrossEntropyLoss와의 관계 정리
- 'CrossEntropyLoss는 왜 softmax와 log를 포함하고 있을까?'라는 질문을 반복 확인
- torch.argmax를 통해 예측된 클래스 추출 후 정확도(accuracy) 계산 함수 구현
- 정답률 시각화 및 혼동행렬 시각화까지 확장 학습 시도

### 회고
분류 모델을 단순하게 정확도만 보는 것이 아니라, 그 안에서 어떤 클래스를 잘못 분류하는지를 해석하는 과정의 중요성을 처음으로 느꼈다.

## D0401

### 학습내용
복잡한 모델 구조에서 nn.ModuleList 사용법을 학습하고, torchinfo를 활용한 모델 구조 출력과 optimizer scheduler의 동작 방식을 실험함.

### 개인 복습/실습
- torch.nn.ModuleList로 여러 층을 반복 구성하는 모델 설계 실습
- 'ModuleList와 Sequential의 차이는?'에 대해 질문하고 실습 예제를 비교함
- torchinfo.summary()를 통해 입력 사이즈와 파라미터 수를 직관적으로 확인
- torch.optim.lr_scheduler.StepLR을 사용해 epoch에 따른 learning rate 변화를 확인
- scheduler.step() 호출 타이밍에 따른 성능 차이를 실험함

### 회고
복잡한 네트워크를 구성하기 위한 객체 지향적인 구조와, 학습 속도 조절을 위한 scheduler의 역할이 훈련 성능에 미치는 영향력을 실감했다.

## D0402

### 학습내용
이미지 분류 과제로 고양이 vs 강아지 문제를 설정하고, 데이터 불러오기부터 학습/평가까지 전체 과정을 직접 설계하며 실습함.

### 개인 복습/실습
- torchvision.transforms를 사용하여 이미지 전처리 pipeline을 구성함
- ImageFolder를 이용한 디렉토리 기반 라벨링과 DataLoader 구현
- CNN 구조 설계와 성능 향상을 위한 dropout, ReLU, flatten 등 조합 실험
- 'DataLoader에서 shuffle을 왜 사용하는가?', 'batch_size는 어떻게 성능에 영향을 주는가?' 질문에 대해 실험하며 설정값 조정
- 최종적으로 훈련 정확도 vs 검증 정확도 비교를 통해 과적합 여부 분석함

### 회고
이미지 기반 과제를 처음부터 끝까지 구성하며 실전 프로젝트 구성 능력과 하이퍼파라미터의 영향력을 동시에 체득할 수 있는 계기가 되었다.
