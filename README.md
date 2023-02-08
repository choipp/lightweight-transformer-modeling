# **SegFormer-B2 경량화 프로젝트**

<div align="center">
    <img src="https://user-images.githubusercontent.com/113173095/217482605-77fc5273-9a6d-4e6b-bf34-89fbdf05b093.png" width=30%>
</div>

## 📰 **Contributors**

**CV-16조 💡 비전길잡이 💡**</br>NAVER Connect Foundation boostcamp AI Tech 4th

|민기|박민지|유영준|장지훈|최동혁|
|:----:|:----:|:----:|:---:|:---:|
|[<img alt="revanZX" src="https://avatars.githubusercontent.com/u/25689849?v=4&s=100" width="100">](https://github.com/revanZX)|[<img alt="arislid" src="https://avatars.githubusercontent.com/u/46767966?v=4&s=100" width="100">](https://github.com/arislid)|[<img alt="youngjun04" src="https://avatars.githubusercontent.com/u/113173095?v=4&s=100" width="100">](https://github.com/youngjun04)|[<img alt="FIN443" src="https://avatars.githubusercontent.com/u/70796031?v=4&s=100" width="100">](https://github.com/FIN443)|[<img alt="choipp" src="https://avatars.githubusercontent.com/u/103131249?v=4&s=117" width="100">](https://github.com/choipp)|
|Remove SelfOutput</br>Separable Attention</br>Inverted Residual Mobile Block</br>Project GitHub Management | Cross-Covariance Attention</br>Inverted Residual Mobile Block</br>실험 기록 · 매뉴얼 작성 및 관리</br>Hyperparameter Tuning (Batch Size)</br>Deploy models on Jetson Nano | Weighted Sum</br>Sequence Reduction Pooling</br>개선된 구조 및 기법 병합</br>Project Documentation</br>Ablation Study | Deformable Attention</br>MixCFN</br>Local Connection</br>Inference Results 추출 · 분석</br>Profiling Tool 코드 개선 | PM</br>Pool Former</br>Pooling Patch Embedding</br>Learnable Resizer</br>레이어별 Params · FLOPs 분석|

</br>


## 📰 **Links**

- [비전 길잡이 Notion 📝](https://vision-pathfinder.notion.site/NOTA-AI-Semantic-Segmentation-1669f7d1c9bc4f39b83ac05dd547da9b)
- [비전 길잡이 발표자료 & WrapUpReport](./appendix/)

## 📰 **Objective**

>모델 Params 및 FLOPs 및 각각 20% 이상 감소<br/>성능 하락 1% 미만으로 최소화
- **SegFormer** : 임베디드 및 모바일 기기를 위한 Transformer 기반 Semantic Segmentation 모델 경량화
- **Model driven approach** : 하이퍼파라미터 튜닝 등 고도화된 학습 기법 배제 · 순수 모델링을 통한 성능 향상
- Pruning 및 quantization 등 **compression 방법 배제** : 모델 블록 · 레이어 재설계 등 경량화 구조변경 진행


## 📰 **Dataset**

||Tiny-ImageNet|ADE20K|
|:----:|:---:|:---:|
||<img src="https://user-images.githubusercontent.com/113173095/217479439-5492f4b3-a115-43b7-9952-b1c1a5c850b9.png" width="200" height="200">|<img src="https://user-images.githubusercontent.com/113173095/217480114-cc9dbb9b-deaa-4620-bb78-920da8d06b84.png" width="200" height="100">|
|Purpose|Pre-training|Fine-tuning|
|Num_classes|200|150|
|Training set|100,000 images|20,210 images|
|Validation set|10,000 images|2,000 images|

```
|-- ADEChallengeData2016
|   |-- image
|   |   |-- train
|   |   `-- val
|   `-- mask
|       |-- train
|       `-- val
`-- tiny-imagenet-200
    |-- train
    |-- val
```
<!-- ### Tiny-ImageNet (Pre-training)
<img src="https://user-images.githubusercontent.com/113173095/217479439-5492f4b3-a115-43b7-9952-b1c1a5c850b9.png" width="200" height="200">

- Num_classes : 200
- Training set : 100,000 images
- Validation set : 10,000 images
- Image Size : 64 x 64

### ADE20K (Fine-tuning)
<img src="https://user-images.githubusercontent.com/113173095/217480114-cc9dbb9b-deaa-4620-bb78-920da8d06b84.png" width="200" height="100">

- Num_classes : 150
- Training set : 20,210 images
- Validation set : 2,000 images -->

## 📰 **Base Model**

![Segformer](https://user-images.githubusercontent.com/25689849/217527787-be5e3a78-0986-4b83-9ec6-85ce65bb4562.svg)
<!-- <img src="https://user-images.githubusercontent.com/113173095/217485570-003dd0a5-6f0d-4195-8e73-c9ca64f57e02.png" width="400" height="300"> -->

### Encoder

- Overlap Patch Embedding
- SegFormer Block
- Efficient Self-Attention
- Mix-FFN

### Decoder

- MLP Layer
- Concat, Linear-Fuse
- Classifier
---

## 📰 **BoostFormer(Ours)**

![boostformer](https://user-images.githubusercontent.com/25689849/217526183-bdfe4c9f-a497-4cde-9dcb-5e00d8dfba11.svg)

### Encoder

- **Pooling Patch Embedding**
- **PoolFormer Block**
- **SegFormerV2 Block**
- **Custom Efficient Self-Attention**
- **Mix-CFN**

### Decoder

- MLP Layer
- **Weighted Sum**
- Classifier

---

## 📰 **Strategy**

![Strategy](https://user-images.githubusercontent.com/25689849/217510697-19b79b6d-f144-4290-8c50-47a7a75ff98b.svg)

- **Tiny-ImageNet Encoder pretrain** + **ADE20k fine-tuning**
    - 컴퓨팅 용량 제한으로 인해 Tiny-ImageNet 활용
- Segformer-B2와 custom model 성능 비교 및 Params와 Flops 측정 (util/get_flops_params.py)

---

## 📰 **Method**

### 1. Patch Embedding

<img src="https://user-images.githubusercontent.com/25689849/217509298-cabb401f-e736-4c44-8719-15830b487b97.svg">

- NxN Conv를 Pooling + 1x1 Conv로 대체
    - $F_{out}=\mathrm{Conv}(\mathrm{Pooling}_{1\times1}(F_{in}))$

### 2. Transformer Block

<img src="https://user-images.githubusercontent.com/25689849/217509038-98c57ecc-ff32-4f74-8f36-caab02bc1fcb.svg">

- Token Mixer : MHSA 대신 Pooling으로 feature 추출
    - $\hat{F_0}=\mathrm{LayerScale}(\mathrm{Pooling}(F_{in}))+F_{in}$
    - $\hat{F_1}=\mathrm{LayerScale}(\mathrm{MixCFN}(\hat{F_0}))+\hat{F_0}$
- 기존 Self Output 모듈 삭제
    - $\hat{F_0}=\mathrm{CSA}(F_{in})+F_{in}$
    - $\hat{F_1}=\mathrm{MixCFN}(\hat{F_0})+\hat{F_0}$

### 3. Attention Layer

<img src="https://user-images.githubusercontent.com/25689849/217508647-14b486db-85ed-4684-a652-d3bc30c6e334.svg">

- Pooling으로 K, V 차원 축소
    - $K, V=\mathrm{Pooling}(F_C)$
- 1x1 Convolution 삭제
    - $\mathrm{Attention}(Q,K,V)=\mathrm{Softmax}({{QK^T}\over{\sqrt{d_{head}}}}V)$

### 4. FFN

<img src="https://user-images.githubusercontent.com/25689849/217507844-f29f7b99-d143-4166-b60a-4a29f643e38e.svg">

- 기존의 Linear(dense) embedding 연산을 1x1 Conv로 변경
    - $\hat{F_C}=\mathrm{Conv}_{1\times1}(F_C)$
- 3x3 DWConv를 3x3과 5x5 DWConv로 channel-wise로 나누어 연산 후 Concat (Mix-CFN)
    - $\hat{F_1}=\mathrm{DWConv}_{3\times3}(\hat{F}_{C/2}), \hat{F_2}=\mathrm{DWConv}_{5\times5}(\hat{F}_{C/2})$
    - $\hat{F_C}=\mathrm{Conv}_{1\times1}(\mathrm{Concat}(\hat{F_1},\hat{F_2}))$
- Batch-Normalization 추가


### 5. Decode Head

<img src="https://user-images.githubusercontent.com/25689849/217508282-bb070e23-280f-4268-a2cc-2d7021c2eab7.svg">

- Stage Features Upsample
    - $\hat{F}_i=\mathrm{Upsample}(\mathrm{MLP}(F_{in}))$
- **Weighted Sum 적용**
    - $\hat{F}=\sum^3_{i=0}(w_i\hat{F_i})$

---

## 📰 **Result**

![result graph](https://user-images.githubusercontent.com/25689849/217506475-2bd67040-3f76-4d52-b61d-024bf880c99f.svg)

| model  | Params| Flops | Acc<sub>val<sup> (%) | mIoU<sub>val<sup> (%) |
| :-------------: | :--------------------: | :-----------------------: | :----------------------: | :-----------------------: |
|SegFormer-B2|27.462M|58.576G|66.48|29.84|
|**BoostFormer</br>(Ours)**|**17.575M</br>(-36.00%)**|**15.826G</br>(-72.98%)**|**72.28</br>(+8.72%)**|**34.29</br>(+14.91%)**|


- **기존 모델 대비 Params 36% 감소, FLOPs 72% 감소, mIoU 성능 14% 향상**
<br/><br/>
---
## 📰 **Directory Structure**

```
|-- 🗂 appendix          : 발표자료 및 WrapUpReport
|-- 🗂 segformer         : HuggingFace 기반 segformer 모델 코드
|-- 🗂 boostformer       : Segformer 경량화 모델 코드
|-- 🗂 imagenet_pretrain : Tiny-ImageNet encoder 학습시 사용한 코드
|-- 🗂 util              : tools 코드 모음
|-- Dockerfile
|-- train.py             : ADE20K Finetuning 코드
|-- eval.py              : 모델 Inference 결과 출력 코드
|-- requirements.txt
`-- README.md
```