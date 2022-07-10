# 딥러닝 Deep Learning

## 딥러닝 연습

### [DNN_Fashion_MNIST](https://github.com/Chanmi-K/Python/blob/main/DL/DL_DNN_FashionMnist.ipynb)
* 인공 신경망 연습
* 심층 신경망 만들기 add() Flatten Relu
* 신경망 모델 훈련
  * Optimizer Adam
  * DropOut
  * CallBacks - ModelCheckpoint, EarlyStopping

### [DNN_basic](https://github.com/Chanmi-K/Python/blob/main/DL/DL_DNN_basic.ipynb)
* IRIS 데이터 분류
* 속성 데이터 회귀
* MNIST
	* 정규화, Flatten 사용
* 패션 MNIST
* 과대적합 방지 : Dropout, BatchNormalization, GaussianNoise, l1, l2
* Callbacks : PlotLosses, ModelCheckpoint, EarlyStopping, ReduceLROnPlateau, LearningRateScheduler


### [CNN_Fashion_MNIST](https://github.com/Chanmi-K/Python/blob/main/DL/DL_CNN_FashionMnist.ipynb)
* 합성곱 신경망 만들기
* 가중치 시각화
* 함수형 API
* 특성맵 시각화

### [CNN_basic](https://github.com/Chanmi-K/Python/blob/main/DL/DL_CNN_basic.ipynb)
* MNIST
* 패션 MNIST
* CIFAR10
	* PlotLosses, overfitting 방지
	* Callbacks 다 적용


### [RNN_IMDB_reviews](https://github.com/Chanmi-K/Python/blob/main/DL/DL_RNN_IMDB_reviews.ipynb)
* 데이터 길이 맞추기
* SimpleRNN
* Embedding
* LSTM
* GRU


### [data_augmentation](https://github.com/Chanmi-K/Python/blob/main/DL/DL_data_augmentation.ipynb)
* 로딩한 데이터에서 증강
* 파일에서 증강


### [TransferLearning](https://github.com/Chanmi-K/Python/blob/main/DL/DL_TransferLearning_basic.ipynb)
* 전이학습 데이터 증강 사용
	* VGG16
	* Resnet50
	* EfficientNetB1
* 예측 결과 출력


### [Korean_KeyBERT](https://github.com/Chanmi-K/Python/blob/main/DL/prac_Korean_KeyBERT_%ED%82%A4%EC%9B%8C%EB%93%9C%EC%B6%94%EC%B6%9C.ipynb)
* SentenceTransformer
* 문서와 가장 유사한 키워드 추출
* Max Sum Similarity 후보 간의 유사성 최소화, 문서와의 후보 유사성 극대화
* Maximal Marginal Relevance 중복 최소화, 결과 다양성 극대화
