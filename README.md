<p align="center">
  <img src="/assets/wto.png" width="497" height="370">
</p>



# DeepWTO 
![ubuntu 16.04](https://img.shields.io/badge/ubuntu-16.04-blue.svg)
[![Python 3.6.8](https://img.shields.io/badge/python-3.6.8-blue.svg)](https://www.python.org/downloads/release/python-370/)
![TensorFlow 1.13.1](https://img.shields.io/badge/tensorflow-1.13.1-blue.svg)
![cuDNN 7.4.1](https://img.shields.io/badge/cudnn-7.4.1-blue.svg)
![cuda 10.0](https://img.shields.io/badge/cuda-10-blue.svg)

## About the Project 
__[DeepWTO](https://github.com/syyunn/DeepWTO)__ is a continuation work of previous project, 
__[Auto-generation of GATT/WTO panel report](https://github.com/syyunn/GATT_WTO)__. 
Compare to the previous project, this time the project has narrow down its scope 
to classification. The task is about to predict which articles of  __[WTO](https://www.wto.org)__ rulings could be applied to the given
textual description of Government Measure.  
         

## Goal of the Project
This project is assumed to achieve following two main goals:

1. Build a __dataset__ so that everyone can participate in this legal 
prediction/classification agenda in __objective manner__
2. Performs a __classification__ with neural networks to achieve the 
naive-baseline, __50% >__ accuracy of the classification task.


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
the strings that can be found under the chapter-name of __Factual Aspect__ in every __Panel Report__. 

Normally, description about the Government Measure could be found at following:

- Factual Aspects in Panel Report [[example](https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/46659/Q/WT/DS/161R.pdf)]
- Request for Consultations  [[example](https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/25382/Q/G/L/292.pdf)]
- Request for the Establishment of a Panel [[example](https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/46659/Q/WT/DS/161-5.pdf)]

#### Download of Data
- Download `train_data.json` and `test_data.json`

    [Googl Drive](https://drive.google.com/open?id=10cEqZg6syoixuoXSNahMUW4AtlJB_CIN) 

- data looks as following:
    
        {"testid": [DS_number]_[Article Name]
         "gov": Textual description of Goverment Measure
         "art": Article contents correponding to $Article Name 
         "label": [0] if not cited, [1] if cited}   

### Reproduce   
    git clone https://github.com/syyunn/DeepWTO
    cd DeepWTO
    conda env create -f environment.yaml 
    python -m spacy download en # download spacy model to tokenize 
    
    # One needs to prepare "GoogleNews-vectors-negative300.bin"

### Code Structure
    
| Path | Description
| :--- | :----------
| [DeepWTO](https://github.com/syyunn/DeepWTO) | Main folder.
|&boxvr;&nbsp; [assests](https://github.com/syyunn/DeepWTO/tree/master/assets) | Images required in README 
|&boxvr;&nbsp; [models](https://github.com/syyunn/DeepWTO/tree/master/models) | TF Models for different tasks code with data 
|&nbsp;&nbsp; &boxvr;&nbsp; [cite](https://github.com/syyunn/DeepWTO/tree/master/models/citability) | Prediction of which articles being cited without legal text (multi label classification)
|&nbsp;&nbsp; &boxur;&nbsp; [cite_wa](https://drive.google.com/open?id=100DJ0QXyG89HZzB4w2Cbyf4xjNK54cQ1) | Prediction of whether an article is cited with legal text (one label classification)
|&boxvr;&nbsp; [prep](https://github.com/syyunn/DeepWTO/tree/master/prep) | Storage of codes to prepare data for all different tasks 
|&nbsp;&nbsp; &boxvr;&nbsp; [download](https://github.com/syyunn/DeepWTO/tree/master/prep/download) | Codes to crawl/cleanse the data from WTO database / Crawl Results
|&nbsp;&nbsp; &boxvr;&nbsp; [factual](https://github.com/syyunn/DeepWTO/tree/master/prep/factual) | Codes to parse factual aspects parts from the Panel Report
|&nbsp;&nbsp; &boxvr;&nbsp; [label](https://github.com/syyunn/DeepWTO/tree/master/prep/label) | Codes and Raw data that is to be used as label
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&boxur;&nbsp; [cite](https://github.com/syyunn/DeepWTO/tree/master/prep/label/citability) | Codes and Raw data to prepare labels to be used in citability prediction task 
|&nbsp;&nbsp; &boxur;&nbsp; [provision](https://github.com/syyunn/DeepWTO/tree/master/prep/provision) | PDF and TEXT file that contains raw data of legal provisions
|&boxvr;&nbsp; [utils](https://github.com/syyunn/DeepWTO/tree/master/utils) | Simple util codes to use
|&boxur;&nbsp; [web](https://github.com/syyunn/DeepWTO/tree/master/web) | Front/Server codes to deploy the project 

### Achievement
The model has achieved `AUC-ROC metric 0.84 (max is 1)` in one-label-classification task (refers to [cite_wa](https://drive.google.com/open?id=100DJ0QXyG89HZzB4w2Cbyf4xjNK54cQ1)) on test dataset.  

### Author
[__Zachary Yoon__](https://github.com/syyunn)

### Sponsor
<p align="left">
  <img src="/assets/deepstudio.png" width="420" height="140">
</p>
