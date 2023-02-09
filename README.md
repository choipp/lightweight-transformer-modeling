# **BoostFormer**

![Main](https://user-images.githubusercontent.com/103131249/217564941-4a04a02f-57fe-4a85-9cdc-6ff287687cba.png)

</br>

## 📰 **Contributors**

**CV-16조 💡 비전길잡이 💡**</br>NAVER Connect Foundation boostcamp AI Tech 4th

|민기|박민지|유영준|장지훈|최동혁|
|:----:|:----:|:----:|:---:|:---:|
|[<img alt="revanZX" src="https://user-images.githubusercontent.com/70796031/217557235-d89557b2-a178-4650-8c21-20cf2b7f80b8.png" width="100%">](https://github.com/revanZX)|[<img alt="arislid" src="https://user-images.githubusercontent.com/70796031/217557228-c0e572a4-40c6-44ae-8d53-f28c32fe4e6d.png" width="100%">](https://github.com/arislid)|[<img alt="youngjun04" src="https://user-images.githubusercontent.com/70796031/217557229-e42381d6-4c27-482c-801e-49872bcedd30.png" width="100%">](https://github.com/youngjun04)|[<img alt="FIN443" src="https://user-images.githubusercontent.com/70796031/217557222-1491ed63-3587-42a1-9bf2-591c91e52e36.png" width="100%">](https://github.com/FIN443)|[<img alt="choipp" src="https://user-images.githubusercontent.com/70796031/217557214-03420adf-5950-4710-b857-a289961989c6.png" width="100%">](https://github.com/choipp)|
<!-- |Remove SelfOutput</br>Separable Attention</br>Inverted Residual Mobile Block</br>Project GitHub Management | Cross-Covariance Attention</br>Inverted Residual Mobile Block</br>실험 기록 · 매뉴얼 작성 및 관리</br>Hyperparameter Tuning (Batch Size)</br>Deploy models on Jetson Nano | Weighted Sum</br>Sequence Reduction Pooling</br>개선된 구조 및 기법 병합</br>Project Documentation</br>Ablation Study | Deformable Attention</br>MixCFN</br>Local Connection</br>Inference Results 추출 · 분석</br>Profiling Tool 코드 개선 | PM</br>Pool Former</br>Pooling Patch Embedding</br>Learnable Resizer</br>레이어별 Params · FLOPs 분석| -->

<!-- ![profile](https://user-images.githubusercontent.com/70796031/217537194-9a9af88d-bd74-4421-bb9e-43ccd302f916.png) -->
</br>

## 📰 **Links**

- [비전 길잡이 Notion 📝](https://vision-pathfinder.notion.site/NOTA-AI-Semantic-Segmentation-1669f7d1c9bc4f39b83ac05dd547da9b)
- [비전 길잡이 발표자료 & WrapUpReport](./appendix/)

## 📰 **Objective**
![image](https://user-images.githubusercontent.com/103131249/217568159-2cbb62b9-ff6c-4795-8d7c-7f637f90e95e.png)
- **SegFormer** : 임베디드 및 모바일 기기를 위한 Transformer 기반 Semantic Segmentation 모델 경량화
- **Model driven approach** : 하이퍼파라미터 튜닝 등 고도화된 학습 기법 배제 · 순수 모델링을 통한 성능 향상
- Pruning 및 quantization 등 **compression 방법 배제** : 모델 블록 · 레이어 재설계 등 경량화 구조변경 진행


## 📰 **Dataset**

||Tiny-ImageNet|ADE20K|
|:----:|:---:|:---:|
||<img src="https://user-images.githubusercontent.com/113173095/217479439-5492f4b3-a115-43b7-9952-b1c1a5c850b9.png" width="300" height="300">|<img src="https://user-images.githubusercontent.com/113173095/217480114-cc9dbb9b-deaa-4620-bb78-920da8d06b84.png" width="300" height="150">|
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
![Segformer](https://user-images.githubusercontent.com/103131249/217569843-478c191b-e431-4903-9e36-6259d2bd990a.png)
<!-- <img src="https://user-images.githubusercontent.com/113173095/217485570-003dd0a5-6f0d-4195-8e73-c9ca64f57e02.png" width="400" height="300"> -->
|Encoder|Decoder|
|:---:|:---:|
|Overlap Patch Embedding|MLP Layer (upsampling)|
|SegFormer Block|Concat|
|Efficient Self-Attention|Linear-Fuse|
|Mix-FFN|Classifier|
---

## 📰 **BoostFormer(Ours)**
![boostformer](https://user-images.githubusercontent.com/70796031/217690146-e7e226df-4a8b-4d99-a1b6-d5d7f3517d9f.png)

|Encoder|Decoder|
|:---:|:---:|
|**Poolin Patch Embedding**|MLP Layer (upsampling)|
|**PoolFormer Block**|**Weighed Sum**|
|**SegFormerV2 Block**|Classifier|
|**Custom Efficient Self-Attention**|-|
|**Mix-CFN**|-|

---

## 📰 **Strategy**

![image](https://user-images.githubusercontent.com/103131249/217567344-f2be7b76-c18c-4157-8770-ba80142540b9.png)

- Segformer-B2와 custom model 성능 비교 및 Params와 Flops 측정 (util/get_flops_params.py)

---

## 📰 **Method**

### 1. Patch Embedding

<img src="https://user-images.githubusercontent.com/25689849/217509298-cabb401f-e736-4c44-8719-15830b487b97.svg">

- NxN Conv를 Pooling + 1x1 Conv로 대체

    <img src="https://user-images.githubusercontent.com/103131249/217582684-3601ac28-0886-481a-aee0-bd52b26fa7f9.png" width="150">
    

### 2. Transformer Block
<img src="https://user-images.githubusercontent.com/25689849/217509038-98c57ecc-ff32-4f74-8f36-caab02bc1fcb.svg">

- Token Mixer : MHSA 대신 Pooling으로 feature 추출
    - $\hat {F_0}=\mathrm {LayerScale}(\mathrm {Pooling}(F_{in}))+F_{in}$
    - $\hat {F_1}=\mathrm {LayerScale}(\mathrm {MixCFN}(\hat {F_0}))+\hat {F_0}$
- 기존 Self Output 모듈 삭제
    - $\hat {F_0}=\mathrm {CSA}(F_{in})+F_{in}$
    - $\hat {F_1}=\mathrm {MixCFN}(\hat {F_0})+\hat {F_0}$

### 3. Attention Layer

<img src="https://user-images.githubusercontent.com/25689849/217508647-14b486db-85ed-4684-a652-d3bc30c6e334.svg">

- Pooling으로 K, V 차원 축소
    - $K, V=\mathrm {Pooling}(F_C)$
    
- 1x1 Convolution 삭제
    - $\mathrm {Attention}(Q,K,V)=\mathrm {Softmax}({{QK^T}\over {\sqrt {d_{head}}}}V)$

### 4. FFN

<img src="https://user-images.githubusercontent.com/25689849/217507844-f29f7b99-d143-4166-b60a-4a29f643e38e.svg">

- 기존의 Linear(dense) embedding 연산을 1x1 Conv로 변경
    - $\hat {F_C}=\mathrm {Conv}_{1 \times 1}(F_C)$
- 3x3 DWConv를 3x3과 5x5 DWConv로 channel-wise로 나누어 연산 후 Concat (Mix-CFN)

    - <img src="https://user-images.githubusercontent.com/103131249/217580303-84047ad0-3197-419f-b83e-ffccf3ca53b9.png" width="180">

    - $\hat {F_C}=\mathrm {Conv}_{1 \times 1}(\mathrm {Concat}(\hat {F_1},\hat {F_2}))$
- Batch-Normalization 추가


### 5. Decode Head

<img src="https://user-images.githubusercontent.com/25689849/217508282-bb070e23-280f-4268-a2cc-2d7021c2eab7.svg">

- Stage Features Upsample
    - <img src="https://user-images.githubusercontent.com/103131249/217580836-fd09f784-b0b8-497b-b58f-7b64466106fd.png" width="200">
    
- **Weighted Sum 적용**
    - <img src="https://user-images.githubusercontent.com/103131249/217582409-9b7e3443-4b72-42c2-8017-2b539fbc8167.png" width="150">


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
## 📰 **Qualitative results on ADE20K**
![results](https://user-images.githubusercontent.com/103131249/217559500-9d9765f5-96f5-4e2d-81c5-3dd2a89fd7a4.png)

## 📰 **Mobile Inference Time Comparison**
![image](https://user-images.githubusercontent.com/103131249/217567804-d8c6cde7-f991-4039-a409-2783600f0a33.png)



## 📰 **NVIDIA Jetson Nano Time Comparision**
![image](https://user-images.githubusercontent.com/103131249/217698136-70bf4eaf-2709-4689-a0ac-9f6642b83868.png)

---


## ⚙️ **Installation**

```bash
git clone https://github.com/boostcampaitech4lv23cv3/final-project-level3-cv-16.git
```

## 🧰 **How to Use**
### Pretraining (tiny_imagenet)
```bash
bash dist_train.sh {사용하는 gpu 개수} \
    --data-path {tiny_imagenet path} \ # 이름에 tiny가 포함되어야함
    --output_dir {save dir path} \
    --batch-size {batch size per gpu } # default=128

# example
bash dist_train.sh 4 \
    --data-path /workspace/dataset/tiny_imagenet \
    --output_dir result/mod_segformer/ \
    --batch-size 64

```
### ADE20K fine-tuning
```bash
# 현재 디렉토리: /final-project-level3-cv-16
python train.py \
    --data_dir {ADE20K의 path} \
    --device 0,1,2,3 \ # 환경에 맞게 수정 
    --save_path {save하고자 하는 dir의 path} \ 
    --pretrain {pretrain 모델 dir 혹은 .pth의 path} # .pth(pretrain의 output), dir(huggingface의 모델허브에서 제공하는 형태)
    --batch_size {batch size} # default=16
```

### Evaluation 수행
```bash
# phase를 통해 val 또는 test set 설정
python eval.py \ # eval.py 내의 model을 정의하는 코드 수정
    --data_dir {ADE20K의 path} \
    --pretrain {pretrain 모델 dir의 path}
```
### Params, FLOPs 확인
```bash
python util/get_flops_params.py \ # get_flops_params.py 내의 model을 정의하는 코드 수정
    --data_dir {ADE20K의 path}
```

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
