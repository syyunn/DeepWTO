<p align="center">
  <img src="/assets/wto.png" width="497" height="370">
</p>



# DeepWTO 

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)


## About the Project 
__[DeepWTO](https://github.com/syyunn/DeepWTO)__ is a continuation work of previous project, 
__[Auto-generation of GATT/WTO panel report](https://github.com/syyunn/GATT_WTO)__. 
Compare to the previous project, this time the project has narrow down its 
task to classification. The task is about to predict each legal provision of
 __[WTO](https://www.wto.org)__ falls into which one of the following 3 
 classes upon the given government measure.

    Class 1: the provision is not applicable to the given government measure.   
    Class 2: the provision is applicable, but the given government measure is consistent with the provision.   
    Class 3: the provision is applicable and those government measure is inconsistent with the provision.
         

## Goal of the Project
This project is assumed to achieve following two main goals:

1. Build a __dataset__ so that everyone can participate in this legal 
prediction/classification agenda in __objective manner__
2. Performs a __prediction__ with simple neural networks to achieve the 
naive-baseline, __33% >__ accuracy of the classification task.


### Dataset 
Basically, the WTO panel process determines __whether a country's government 
measure at issue__ is __contrary or not contrary__ to __a certain article(s)
 of rules of WTO__, by explicitly saying as following : 

> "Korea’s domestic support for beef in 1997 and 1998 exceeded the de 
minimis level contrary to Article 6 of the Agreement on Agriculture." 

Therefore, our dataset is comprised of mainly 3 components - 
[__Government Measure__](https://github.com/syyunn/DeepWTO/tree/master/data/factual), 
[__Legality with Cited Provision__](https://github.com/syyunn/DeepWTO/blob/master/data/label/legality.xlsx),
[__WTO Legal Provisions__](https://github.com/syyunn/DeepWTO/tree/master/data/provision). 


### Government Measure

Government measure is the most __tricky__ part to prepare the data to train.
  Government measure is usually __descriptive__ and __case-specific__, therefore it is hard to be generalized across the cases. Moreover, Government measure
 __has no strictly enforced formatting 
 style__ but mainly depends on the preference of each panel body and its 
 included personnel. 
Therefore, for the first version of the dataset, we just naively includes all 
the strings that can be found under the chapter-name of __Factual Aspect__ in every __Panel Report__. 

Normally, description about Government Measure is included in the following:

- Factual Aspects in Panel Report [[example](https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/46659/Q/WT/DS/161R.pdf)]
- Request for Consultations  [[example](https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/25382/Q/G/L/292.pdf)]
- Request for the Establishment of a Panel [[example](https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/46659/Q/WT/DS/161-5.pdf)]

### Reproduce   
    git clone https://github.com/syyunn/DeepWTO
    cd DeepWTO
    conda env create -f env.yaml


### Author
[__Zachary Yoon__](https://github.com/syyunn)

### Sponsor
<p align="left">
  <img src="/assets/deepstudio.png" width="420" height="140">
</p>

This project is financially supported by __deepstudio Co.Ltd__ 

#### ToDo  
- [x] Parse semi-colon linked urls to make/re-save pdf_urls_parsed.pkl
- [ ] Convert image-based pdf to text-based pdf 
- [ ] Add parser to count the articles other than GATT, especially ATC 
- [ ] Make Article Dictionary, e.g. {'GATT:III.1' : "Each contracting party 
shall .."
- [ ] Review the current labelling before DS67 which is conducted without 
reading raw document 
- [ ] Construct a new query system and embed it on github so that people can
 search more fast on target document.
- [ ] Write fine-tune code of every texts in 2,8000 pdfs to GloVec
- [ ] Cleanse the Factual Aspect to deprive after factual (usually after III
. Preliminary ...)
- [ ] Change README of Government Measure to Factual Aspect centered way
- [ ] Change README in a way those who don't know WTO Rulings can understand.
- [ ] Determine whether to use conditional classification with 
Panel/AppellateBody

#### Labelling On Progress
- [ ] 2
- [ ] 7
- [ ] 8
- [ ] 10
- [ ] 11
- [ ] 12
- [ ] 14
- [ ] 18
- [ ] 22
- [ ] 24
- [ ] 31
- [ ] 33
- [ ] 34
- [ ] 46
- [ ] 50
- [ ] 56
- [ ] 58
- [ ] 60
- [ ] 62
- [ ] 67
- [ ] 68
- [ ] 69
- [ ] 70
- [ ] 72
- [ ] 76
- [ ] 79
- [ ] 87
- [ ] 90
- [ ] 98
- [ ] 99
- [ ] 103
- [ ] 108
- [ ] 110
- [ ] 113
- [ ] 114
- [ ] 121
- [ ] 122
- [ ] 126
- [ ] 132
- [ ] 135
- [ ] 136
- [ ] 138
- [ ] 139
- [ ] 141
- [ ] 142
- [ ] 146
- [ ] 152
- [ ] 155
- [ ] 156
- [x] 161
- [x] 162
- [x] 163
- [x] 165
- [x] 166
- [x] 169
- [x] 170
- [x] 174
- [x] 175
- [x] 177
- [x] 178
- [x] 184
- [x] 189
- [x] 192
- [x] 202
- [x] 204
- [x] 207
- [x] 212
- [x] 213
- [x] 217
- [ ] 219
- [ ] 221
- [ ] 231
- [ ] 234
- [ ] 238
- [ ] 243
- [ ] 244
- [ ] 245
- [ ] 246
- [ ] 248
- [ ] 249
- [ ] 251
- [ ] 252
- [ ] 253
- [ ] 254
- [ ] 257
- [ ] 258
- [ ] 259
- [ ] 264
- [ ] 265
- [ ] 266
- [ ] 267
- [ ] 268
- [ ] 269
- [ ] 276
- [ ] 282
- [ ] 283
- [ ] 285
- [ ] 286
- [ ] 290
- [ ] 294
- [ ] 295
- [ ] 296
- [ ] 301
- [ ] 302
- [ ] 308
- [ ] 312
- [ ] 315
- [ ] 316
- [ ] 320
- [ ] 321
- [ ] 322
- [ ] 323
- [ ] 332
- [ ] 336
- [ ] 339
- [ ] 340
- [ ] 342
- [ ] 343
- [ ] 344
- [ ] 345
- [ ] 350
- [ ] 353
- [ ] 360
- [ ] 363
- [ ] 366
- [ ] 367
- [ ] 371
- [ ] 379
- [ ] 381
- [ ] 384
- [ ] 386
- [ ] 391
- [ ] 392
- [ ] 394
- [ ] 395
- [ ] 396
- [ ] 397
- [ ] 398
- [ ] 399
- [ ] 400
- [ ] 401
- [ ] 403
- [ ] 406
- [ ] 412
- [ ] 413
- [ ] 414
- [ ] 415
- [ ] 416
- [ ] 417
- [ ] 418
- [ ] 422
- [ ] 425
- [ ] 426
- [ ] 427
- [ ] 429
- [ ] 430
- [ ] 431
- [ ] 432
- [ ] 433
- [ ] 435
- [ ] 436
- [ ] 437
- [ ] 438
- [ ] 440
- [ ] 441
- [ ] 442
- [ ] 444
- [ ] 445
- [ ] 447
- [ ] 449
- [ ] 453
- [ ] 454
- [ ] 456
- [ ] 457
- [ ] 458
- [ ] 460
- [ ] 461
- [ ] 464
- [ ] 467
- [ ] 468
- [ ] 471
- [ ] 472
- [ ] 473
- [ ] 475
- [ ] 476
- [ ] 477
- [ ] 478
- [ ] 479
- [ ] 480
- [ ] 482
- [ ] 483
- [ ] 484
- [ ] 485
- [ ] 486
- [ ] 487
- [ ] 488
- [ ] 490
- [ ] 491
- [ ] 492
- [ ] 493
- [ ] 495
- [ ] 496
- [ ] 497
- [ ] 499
- [ ] 504
- [ ] 505
- [ ] 513
- [ ] 518
- [ ] 523

### Keywords

text classification/ word embedding/ character embedding/ 1D Convolution/ 
document understanding

### RoadMap: Critical Issues
- [ ] Decide which embedding (char/word) to use 
- [ ] How to mingle the Provisions emb together with Factual Aspects emb : 
might the resNet-like OP would be workable 

### Further Issues:
- [ ] In case gov_measure just given by consultation and establishment is 
__insufficient__, one needs to track how panels get more information on each
 specific cases.
 
### Difference between Panel and this Prediction Task 
- [ ] This task only mimic the __binary__ result of panel decision. Thus 
this one do not consider the way of assessing the case directly, but just 
trying to efficiently provides the correct answer for given gov_measure and 
provisions 
- [ ] As a development of the above question, how could one can train the 
neural network with Panel Reasoning?

### For more descriptive explanation about this project
Check this [google slides](https://docs.google.com/presentation/d/13ksFl0xovBWGgMqyHnBjkTJEzpUaolKg5HCeTErOJnk/edit?usp=sharing)

### How to Parse the Numeric Tables 

### Issues in Downloads
current urls dropped :

https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/22235/Q/WT/DS/162R-01.pdf 
https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/13458/Q/WT/DS/170R-01.pdf

### Issue in Network Structure
Look up the general network architecture that can parse and understand 
chart, number and table-like structure of document, such as shown in factual
 of 
DS165:
<p align="center">
  <img src="/assets/ds165_bar_chart_in_factual.png">
</p>

### Scope of Provision:
sometimes the scope is get magnified into "sentence-level", such as, 

    The increased bonding requirements of the 3 March Measure as such led to violations
    of Articles II:1(a) and II:1(b), first sentence; the increased interest charges, costs and
    fees resulting from the 3 March Measure violated Article II:1(b) last sentence. The
    3 March Measure also violated Article I of GATT;

but this project decided to limit its scope to the next depth of 
"clause-level", e.g., GATT III:__4__ 


### Fine Tuning of GloVec
Write or Find the code of fine-tune the pre-trained embedding to whole 
documents of WTO.

### Miscellaneous
In DS-175, there exist AppellateBody Report, but it's about giving-up of 
appeal of the India in the middle of Appellate Body process.

### Linked Case Issue:
We always represent the aggregated cases with the first one, such as for the
 case of "United States — Safeguard Measure on Imports of Fresh, Chilled or 
 Frozen Lamb" case, ds-177(complaint by New Zealand) and ds-178
 (complaint by Austrailia), we use ds-177 as the marker in train/test data.
 
### About Cited, but Consistent Measures
the project sets up the policy applied to the cases which are 
"cited but consistent (evaluated by Panel/AB but things are turns out to be 
consistent)" to label those with the 0.5 level of inconsistency.  Since the 
network will be used to find the possible applicable provisions in given 
situation, we naively-assumed that just setting those with 0- which are 
treated with non-cited provisions in other provisions, would be wasteful of 
information.

### There exist a unclear boundary between Measure Description and Reason of Breach  

### Issues on Rare Provisions
- [ ] In DS204, can't find Mexico's Reference Paper regarding GATS

### Regarding Provisions  
- [ ] Can't locate the Mexico's SECTION 2 OF THE REFERENCE PAPER of GATS

### Case Number whose Panel/AB report requires OCR to parse

- In case one found a case that is not available to copy, check there exists
 corresponding .doc file first.
- [ ] https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/62149/Q/WT/DS/207R.pdf

