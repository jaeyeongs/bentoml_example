# BentoML 실습해보기

[MLflow 실습](https://github.com/jaeyeongs/mlflow_example) 레파지토리에 이어 여러 BentoML 프레임워크 사용법을 알아보았다.
BentoML은 API Serving이 편리하다는 장점이 있어 이를 활용하고자 한다. 추가로 BentoML은 MLFlow를 지원하기 때문에 모델 관리는 MLflow, API Serving은 BentoML 두 가지의 프레임워크를 동시에 활용하여 모델 관리 및 배포까지의 과정을 살펴본다.

## 1. 개발 환경

```
python=3.8
mlflow>=1.0
scipy
scikit-learn
bentoml>=1.0.0rc3
```

## 2. BentoML 실행

### (1) BentoML Build

```
bentoml build
```

![image](https://user-images.githubusercontent.com/87981867/220234349-263b854a-0868-41b9-8461-beae029d8ac4.png)

- Terminal 창에서 도커를 빌드하면 위와 같이 모델 파일, dockerfile 등이 생성 

### (2) Docker image

```python
bentoml containerize iris_classifier:latest
```

![image](https://user-images.githubusercontent.com/87981867/220234082-2591ac3b-d058-4d96-8d00-d33fd29d9715.png)

- 생성된 도커 파일로 위와 같은 명령어로 컨테이너를 생성할 수 있음
- 단, 서버 환경이 docker 명령어가 입력되는 컨테이너 환경이어야 함(로컬에서는 docker 설치가 필요)

### (3) API Serving

```python
bentoml serve iris_classifier:4dbmbmvcakkyjb4w
```

![image](https://user-images.githubusercontent.com/87981867/220235020-61d9b0de-3441-4f37-bc04-d3a8fe75aad7.png)

![image](https://user-images.githubusercontent.com/87981867/220235197-0abca161-f2c2-4191-a8d6-e6b10dbdd280.png)

- 명령어를 실행하고 127.0.0.1:3000 주소로 접속하면 Web UI가 호출 됨

## 3. BentoML를 활용한 MLFlow

### 연동

```python
lr_model_runner = bentoml.mlflow.get("logistic_regression_model:latest").to_runner()
```

- bentoml은 mlflow를 지원하기 때문에 mlflow에 저장했던 Logistic Regression 모델을 bentoml에서 불러올 수 있


## 실습 결론

bentoml은 코드 몇 줄로 간단히 API를 생성하여 모델을 배포할 수 있고, Dockerize가 가능하여 모델 패키징이 매우 편리하다. 전체적인 모델 배포 환경에서 MLFlow를 통해 모델을 튜닝하고 최적화된 모델을 패키징하고 배포하는 것은 BentoML을 활용하는 것이 매우 편리함을 느꼈다. 머신러닝을 다루는 실무자에겐 매우 유용한 프레임워크이기 때문에 유용하게 활용될 것이다.
