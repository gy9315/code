# transfer_learning

## D0416

### 학습내용
AlexNet 구조와 CIFAR-10 분류를 학습하며, CNN의 기본 구조부터 순차 구성 및 flatten, ReLU, MaxPool의 흐름을 익힘. OpenCV를 활용해 이미지 데이터를 불러오고 배열 분할 실습도 병행함.

### 개인 복습/실습
- AlexNet의 구조를 torch.nn.Sequential로 구현하고 layer별 의미 정리
- CIFAR-10 데이터를 불러와 학습/검증용 DataLoader 구성 실습
- Conv2D → ReLU → MaxPool 반복 구조를 시각화하며 차원 축소 흐름 이해
- OpenCV로 이미지 분할 후 numpy 배열로 변환하고 torch Tensor로 처리 실험
- 'flatten은 어디서, 왜 써야 할까?', 'Conv 뒤에 반드시 MaxPool이 필요할까?' 등의 질문 기반 구조 실험 수행

### 회고
CNN의 기본 구조를 직접 구현하면서 conv-layer가 단순 이미지 필터링이 아니라 정보 요약의 중심이 된다는 감각을 실무와 연결지어 체득함.

## D0417

### 학습내용
VGGNet과 ResNet의 구조를 비교하며 깊은 층의 CNN을 어떻게 구성하고 residual connection이 왜 필요한지 실습을 통해 확인함.

### 개인 복습/실습
- VGGNet 구성 시 동일한 conv-layer 반복과 채널 확장 흐름 구현
- ResNet의 skip connection을 직접 구현하고 기존 구조와의 차이 실험
- A100 환경(GPU) 기준에서 BatchNorm 위치에 따른 성능 차이 실험
- 모델 구조를 수기로 구성하며 block 형태의 코드 재사용 실습
- '왜 깊어질수록 학습이 어렵고 ResNet이 이를 해결하는가?'라는 질문으로 학습 안정성 개념 이해

### 회고
단순히 레이어를 늘리는 것이 성능 향상이 아님을 느꼈고, ResNet처럼 학습 흐름을 끊지 않는 구조가 실제로 얼마나 효과적인지 처음으로 이해함.

## D0421

### 학습내용
Faster R-CNN 객체 탐지 모델을 구성하고, Feature Map과 Anchor 설정, ROI Align, NMS 흐름을 실습하며 실제 Detection Pipeline을 구성함.

### 개인 복습/실습
- torchvision.models.detection.fasterrcnn_resnet50_fpn을 활용한 사전 학습 모델 기반 실습
- Custom Dataset 구성, get_target 함수 작성, BBox와 Label 구조 정의
- 이미지 annotation → transform → tensor 변환 흐름 직접 설계
- '왜 BBox는 float32로 지정해야 하나?', 'NMS는 어떤 기준으로 작동하는가?' 등 질문 기반 실습
- Anchor 기반 탐지 → ROI Align → Classifier 흐름 정리 및 각 단계 출력값 확인

### 회고
단순 분류와는 달리 객체 탐지에서는 위치 정보와 분류가 함께 고려되어야 함을 체감했고, Anchor, ROI, NMS 같은 개념들이 어떻게 실제 모델 구조에 녹아드는지를 실감했다.
