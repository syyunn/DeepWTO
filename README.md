# DeepWTO

## About the project 
This project is a continuation work of previous project, 
__[Auto-generation of GATT_WTO panel report](https://github.com/syyunn/GATT_WTO)__. 
Compare to the this previous project, this time the project has narrow downed 
to the classification task to predict 
which country wins the legal battle in __[WTO](https://en.wikipedia.org/wiki/World_Trade_Organization)__. This project is assumed to achieve following two main goals:

1. Build a __dataset__ so that everyone can participate in this legal prediction 
agenda in __objective manner__
2. Performs a classification with simple neural networks to set the baseline 
of the classification task.

Above two will be branched and managed into a separate project later, 
however, handled in the same repository at present. 


### Dataset 
Basically, the WTO panel process determines __whether a country's government 
measure__ is __contrary or not contrary__ to __a certain article(s) of rules of WTO__,
by explicitly saying as following : 

> "Korea’s domestic support for beef in 1997 and 1998 exceeded the de 
minimis level contrary to Article 6 of the Agreement on Agriculture." 

Therefore, our dataset is comprised of mainly 3 components - [__Government 
Measure__](https://www.wto.org/english/tratop_e/dispu_e/disp_settlement_cbt_e/c5s3p1_e.htm), 
__Legality__, [__Article Code__](https://www.wto.org/english/docs_e/legal_e/legal_e.htm#gatt47). 


#### Government Measure (or Measure at Issue)

Government measure is the most __tricky__ part to prepare the data to train.
  Government measure is usually __descriptive__ and __specific__ to each 
case therefore it is hard to be generalized across the cases. Moreover Government measure
 is given in a form of __text data__ without strictly enforced formatting 
 style but mainly depends on the preference of each panel body and its included personnel. 
Therefore, for the first version of the dataset, we just naively parse all 
the strings included in __Panel(or Appellate Body if exists) Report__ to 
check whether this naive dataset - which lacks a hierarchical structure of 
document, could be also analyzed with deep learning approach. 

# Author
Zachar Yoon
Senior Research Scientist @ Deep Studio Co. Ltd. 

#### ToDo  
0. Parse semi-colon linked urls to make/re-save pdf_urls_parsed.pkl
1. Merger parser to crawler 
2. Convert image-based pdf to text-based pdf 



