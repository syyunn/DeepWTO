<p align="center">
  <img src="/assets/wto.png" width="497" height="370">
</p>

<br />

# Important Notice (as of 28 Feb 2020)
Currently the DeepWTO project aims to publish the result to `2021 ICAIL` after some major addendum - such as analyzing the result with `xAI`. We are looking for some skilled engineers/researchers who are interseted in the field of `legalNLP`. Please check our project [organization](https://github.com/DeepWTO) and get in touch with `syyun@snu.ac.kr` to discuss with which research point you want to/can participate in the project! 

# DeepWTO 
![ubuntu 16.04](https://img.shields.io/badge/ubuntu-16.04-blue.svg)
[![Python 3.6.8](https://img.shields.io/badge/python-3.6.8-blue.svg)](https://www.python.org/downloads/release/python-370/)
![TensorFlow 1.13.1](https://img.shields.io/badge/tensorflow-1.13.1-blue.svg)
![cuDNN 7.4.1](https://img.shields.io/badge/cudnn-7.4.1-blue.svg)
![cuda 10.0](https://img.shields.io/badge/cuda-10-blue.svg)

<br />

## About the Project 
__[DeepWTO](https://github.com/syyunn/DeepWTO)__ is a continuation work of previous project, 
__[Auto-generation of GATT/WTO panel report](https://github.com/syyunn/GATT_WTO)__. 
Compare to the previous project, this time the project has narrowed down its scope 
to the binary classification. The task is about to predict whether an legal article of  __[WTO](https://www.wto.org)__ rulings could be applied to the given textual description of Government Measure.  
         
## Background of the Project
Currnetly there exists no publicly shared dataset that researchers can share and study together in the field of `LegalNLP`. One of the main reason of this vacancy is because of the locality of the law. Therefore, this repo aims to prepare publicly available `LegalNLP dataset` within the field of `International Law` which is operating globally in English. Moreover, to let the researchers to understand how the deep Learning model could be implemented, the repo provides [sample model code](https://github.com/syyunn/DeepWTO/tree/master/models/cite_wa) with the prepared dataset. 


## Goal of the Project
This project is assumed to achieve following two main goals:

1. Build a __Legal NLP Dataset__ so that everyone can participate in this legal 
prediction/classification agenda in __objective manner__
2. Performs a __classification__ with a neural network to achieve the 
naive-baseline, __0.5 >__ `AUC-ROC` of the classification task.


### Dataset  
Basically, the WTO panel process determines __whether a country's government 
measure at issue__ is __contrary or not contrary__ to __a certain article(s)
 of rules of WTO__, by explicitly saying as following : 

> "Korea’s domestic support for beef in 1997 and 1998 exceeded the de 
minimis level contrary to Article 6 of the Agreement on Agriculture." 


#### Government Measure

Government measure is the most __tricky__ part to prepare the data to train.
  Government measure is usually __descriptive__ and __case-specific__, therefore it is hard to be generalized across the cases. Moreover, Government measure
 __has no strictly enforced formatting 
 style__ but mainly depends on the preference of each panel body.
Therefore, for the first version of the dataset, we just naively includes all 
the text strings that can be found under the chapter-name of __Factual Aspect__ in every __Panel Report__. 

Normally, description about the Government Measure could be found at following classes of WTO documents:

- Factual Aspects in Panel Report [[example](https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/46659/Q/WT/DS/161R.pdf)]
- Request for Consultations  [[example](https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/25382/Q/G/L/292.pdf)]
- Request for the Establishment of a Panel [[example](https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/46659/Q/WT/DS/161-5.pdf)]

#### Download of Data
- Download `train_data.json` and `test_data.json`

    [Googl Drive](https://drive.google.com/drive/folders/1BpwYLqSBXxSgv8cmItwbohIkfebJr3lX?usp=sharing) 

- Each data instance looks as following:
    
        {"testid": [DS_number]_[Article Name]
         "gov": Textual description of Goverment Measure
         "art": Article contents correponding to [Article Name] 
         "label": [0] if not cited, [1] if cited}   
        
        * [DS_number] is an unique identification code for each case requested to WTO
        * Example of [Article Name] is Article I:1, Article III:4, etc.

- After Download

    place the downloaded `train_data.json` and `test_data.json` to your preferred `PATH`. 
    Then edit the `TRAININGSET_DIR` and `VALIDATIONSET_DIR` variable in `models/cite_wa/OneLabelTextCNN/train.py` with `PATH`.

- In case you don't have `GoogleNews-vectors-negative300.bin`

    Download `GoogleNews-vectors-negative300.bin.gz` from [Googl Drive](https://drive.google.com/drive/folders/1BpwYLqSBXxSgv8cmItwbohIkfebJr3lX?usp=sharing) and `gunzip` it to your preferred `PATH`. Then edit the `word2vec_path` argument at the last line of `models/cite_wa/OneLabelTextCNN/train.py` with `PATH`.
    
### Reproduce   
  
    git clone https://github.com/syyunn/DeepWTO
    cd DeepWTO
    conda env create -f environment.yaml 
    python -m spacy download en # download spacy model to tokenize 
    
    cd models/cite_wa/OneLabelTextCNN
    python train.py
    

### Code Structure
    
| Path | Description
| :--- | :----------
| [DeepWTO](https://github.com/syyunn/DeepWTO) | Main folder.
|&boxvr;&nbsp; [assests](https://github.com/syyunn/DeepWTO/tree/master/assets) | Images required in README 
|&boxvr;&nbsp; [models](https://github.com/syyunn/DeepWTO/tree/master/models) | TF Models for different tasks code with data 
|&nbsp;&nbsp; &boxvr;&nbsp; ~~[cite](https://github.com/syyunn/DeepWTO/tree/master/models/citability)~~ | Prediction of which articles being cited without legal text (multi label classification; Deprecated)
|&nbsp;&nbsp; &boxur;&nbsp; [cite_wa](https://github.com/syyunn/DeepWTO/tree/master/models/cite_wa) | Prediction of whether an article is cited with article content (one label classification)
|&boxvr;&nbsp; [prep](https://github.com/syyunn/DeepWTO/tree/master/prep) | Storage of codes to prepare data for all different tasks 
|&nbsp;&nbsp; &boxvr;&nbsp; [download](https://github.com/syyunn/DeepWTO/tree/master/prep/download) | Codes to crawl/cleanse the data from WTO database / Crawl Results
|&nbsp;&nbsp; &boxvr;&nbsp; [factual](https://github.com/syyunn/DeepWTO/tree/master/prep/factual) | Codes to parse factual aspects parts from the Panel Report
|&nbsp;&nbsp; &boxvr;&nbsp; [label](https://github.com/syyunn/DeepWTO/tree/master/prep/label) | Codes and Raw data that is to be used as label
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&boxur;&nbsp; [cite](https://github.com/syyunn/DeepWTO/tree/master/prep/label/cite) | Codes and Raw data to prepare labels to be used in citability prediction task 
|&nbsp;&nbsp; &boxur;&nbsp; [provision](https://github.com/syyunn/DeepWTO/tree/master/prep/provision) | PDF and TEXT file that contains raw data of legal provisions
|&boxvr;&nbsp; [utils](https://github.com/syyunn/DeepWTO/tree/master/utils) | Simple util codes to use
|&boxur;&nbsp; [web](https://github.com/syyunn/DeepWTO/tree/master/web) | Front/Server codes to deploy the project (Currently Working) 

### Achievement
The model has achieved `AUC-ROC 0.8432` in one-label-classification task ([cite_wa](https://github.com/syyunn/DeepWTO/tree/master/models/cite_wa)) with test data. 

The maximum of `AUC-ROC` is `1`.

<p align="left">
  <img src="/logs/aucroc.png">
</p>

Also, the model has achieved `Accuracy 92.04%` in test data set with following [statistics](https://github.com/syyunn/DeepWTO/tree/master/logs/sota_log.txt) : 

        Total Correct Prediction for label [1] is 37 out of 83
        Total Correct Prediction for label [0] is 2068 out of 2204

<br />

However, the preferred metric for the model performance is `AUC-ROC` because a naive-baseline of the `Accuracy` is `96.37% (2204/2287)`when the model just keep predicting `label [0]` for every case. Since only a few number of articles are cited `(label [1])` among entire articles for each case, it is more preferred to measure how the model [precisely](https://en.wikipedia.org/wiki/Precision_and_recall) predicts the `label [1]` with `AUC-ROC`.   

<br />


### Paper
More detailed and kind explanation about the project can be found in this __[paper](https://drive.google.com/file/d/1JXf-_p63UXuaSV89RvbTnLovMi3ylL62/view?usp=sharing)__ (or __[slides](https://docs.google.com/presentation/d/1ixUZoA_SBsjeoNaHpQBVabh1XYDqStB79DEGO3QywMQ/edit?usp=sharing)__)

<br />

### Author
[__Zachary Yoon__](https://github.com/syyunn)

<br />

### Sponsor
<p align="left">
  <img src="/assets/deepstudio.png" width="420" height="140">
</p>

<br />

### Special Thanks to __[RandolphIV](https://github.com/RandolphVI/Multi-Label-Text-Classification)__

[The repo](https://github.com/RandolphVI/Multi-Label-Text-Classification) has provided awesome model code to conduct document classification that this repo has referred to.
