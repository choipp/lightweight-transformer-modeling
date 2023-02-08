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

![boostformer](https://user-images.githubusercontent.com/113173095/217485570-003dd0a5-6f0d-4195-8e73-c9ca64f57e02.png)
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

## 📰 **Ours Model**

![boostformer](https://user-images.githubusercontent.com/70796031/217485857-cb57f4fe-ec1d-451d-adc6-829fbecf24d9.png)

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

- **Tiny-ImageNet Encoder pretrain** + **ADE20k fine-tuning**
    - 컴퓨팅 용량 제한으로 인해 Tiny-ImageNet 활용
- Segformer-B2와 custom model 성능 비교 및 Params와 Flops 측정 (util/get_flops_params.py)

---
## 📰 **Method**
### 1. Patch Embedding
<img src="https://user-images.githubusercontent.com/113173095/217486653-4cbb9082-d4a9-42ab-a131-2fb7066b2b53.png" width="250">

$F_{out}=\mathrm{Conv}(\mathrm{Pooling}_{1\times1}(F_{in}))$

### 2. Transformer Block
<img src="https://user-images.githubusercontent.com/113173095/217488041-a6efbe54-3983-4f8c-ae45-45ab9d09e859.png" height="200">

- Token Mixer : MHSA 대신 Pooling으로 feature 추출
    - $\hat{F_0}=\mathrm{LayerScale}(\mathrm{Pooling}(F_{in}))+F_{in}$
    - $\hat{F_1}=\mathrm{LayerScale}(\mathrm{MixCFN}(\hat{F_0}))+\hat{F_0}$
- 기존 Self Output 모듈 삭제
    - $\hat{F_0}$
---

### 3. Attention Layer

## 📰 **Result**

![result graph](https://user-images.githubusercontent.com/25689849/217489238-0ca18321-3e7a-4bd3-90aa-51bd052d1e83.svg)

| model  | Params| Flops | Acc<sub>val<sup> (%) | mIoU<sub>val<sup> (%) |
| ------------- | -------------------- | ----------------------- | ---------------------- | ----------------------- |
|SegFormer-B2|27.462M|58.576G|66.48|29.84|
|BoostFormer (Ours)|17.575M|15.826G|72.28|34.29|

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