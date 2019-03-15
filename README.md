<p align="center">
  <img src="/assets/wto.png" width="497" height="370">
</p>



# DeepWTO 

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)


## About the Project 
__[DeepWTO](https://github.com/syyunn/DeepWTO)__ is a continuation work of previous project, 
__[Auto-generation of GATT/WTO panel report](https://github.com/syyunn/GATT_WTO)__. 
Compare to the previous project, this time the project has narrow down its 
task to classification. The task is about to predict to which one of the following 3 classess the given provision of
 __[WTO](https://www.wto.org)__ falls into upon the given potentially-problematic government measure.

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

This project is supported by __deepstudio Co.Ltd__ 

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
- [ ] Find BERT for classification model 
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
- [x] 219
- [x] 221
- [x] 231
- [x] 234
- [x] 238
- [x] 243
- [x] 244
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
document understanding/ Multi-Label-Text-Classification

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
this one do not consider the legal way of assessing the case directly, but utmostly aims to numerically provide the correct answer for the given gov_measure and provisions 
- [ ] As a continued development of the above shortage, how could one can train the neural network the Panel Reasoning?

### For more descriptive explanation about this project
Check this [google slides](https://docs.google.com/presentation/d/13ksFl0xovBWGgMqyHnBjkTJEzpUaolKg5HCeTErOJnk/edit?usp=sharing)

### How to Parse the Numeric Tables 

### Issues in Downloads
current urls dropped :

https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/22235/Q/WT/DS/162R-01.pdf 
https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/13458/Q/WT/DS/170R-01.pdf

### Issue in Network Structure
Look up the general network architecture that can parse and understand chart, number and table-like structure of document, such as shown in the factual aspect of DS165 as following:
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
- [ ] https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/1581/Q/WT/DS/243R.pdf
- [ ] https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/1581/T/WT/DS/243R.doc
- [ ] https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/19168/Q/WT/DS/244R-00.pdf
(pdf readible and unreadible mixed. chapter III cannot be read into.)
- [ ] 34R.pdf has only "page 3" image-based (not its fore/back)

### Further Steps - "Narrow down the scope of reasoning"
With ***DS231 EC-Sardines*** case as an example, this case not just directly
 get to the simple conclusion, "inconsistent with TBT 2.4". It checked whether the 
problematic measure actually falls into the scope of TBT and there exists 
another steps that Panel/AB shares and follows. Therefore, for the 
development of the process, one must consider how to train the network with 
more high resolution of reasoning, including how to gather the dataset to 
train. 

### Regarding Footnotes
Currently the body number and footnote numbers are not corresponding. 
Therefore, One needs to figure out how to parse the footnote or let the 
network knows about the footnote. 

### Too Insufficient Description of Government Measure Problem in Factual Aspect
For example, in case of 234, there's no 

### Change of Labelling plan
From the DS244, changed 


### Log of DataPrep

As of DS248, I had gave up to track the inconsistency of Safeguard Measures(SA)

### Issues 

- [x] {75, 84} being out-scoped from the DS panel numbers -> Manually Added 
- [ ] Track why {75, 84} being omitted from the automated process of 
checking ds_numb that has panel report

### WPF
DS8 has WPF file format and pdf is image-based. Find the solution to open it.

### Footnotes
The network that understands that holds a footnote in beneath

### WT/DS438/R • WT/DS444/R • WT/DS445/R 
Above being omitted since the panel report doesn't have factual 

### Current Commercial Database Available:

- [ ] https://www.tradelawguide.com/Cms?Id=2210
- [ ] http://worldtradelaw.net/

### Pretrained links
- [ ] Google [Word2Vec](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit)
 
### Google W2V
- [ ] 13248 is the max numb
    limit: 3000000 13248
    limit: 2500000 13228
    limit: 2000000 13174
    limit: 1500000 13063
    limit: 1000000 12885
    limit: 500000 12496
    limit: 400000 12320
    limit: 300000 12080
    limit: 200000 11667
    limit: 100000 10776

### List of Token Lengths
    {longest: 35880, shortest: 38
    0 2301
    1 6577
    2 500
    3 4484
    4 7683
    5 1001
    6 3036
    7 5568
    8 462
    9 4894
    10 4894
    11 4894
    12 1363
    13 7906
    14 4562
    15 4545
    16 5301
    17 434
    18 8418
    19 1609
    20 1034
    21 1151
    22 856
    23 2429
    24 5082
    25 947
    26 1240
    27 2514
    28 4292
    29 4580
    30 3153
    31 7448
    32 2254
    33 1880
    34 1498
    35 5191
    36 2638
    37 1292
    38 3860
    39 14036
    40 1130
    41 2181
    42 2251
    43 1660
    44 1956
    45 3592
    46 795
    47 4851
    48 1104
    49 7295
    50 432
    51 749
    52 1958
    53 1958
    54 209
    55 584
    56 5462
    57 175
    58 1412
    59 1958
    60 5462
    61 1431
    62 1893
    63 2327
    64 565
    65 203
    66 752
    67 1221
    68 1256
    69 11050
    70 2389
    71 1347
    72 1345
    73 1262
    74 2845
    75 471
    76 934
    77 6177
    78 505
    79 5318
    80 761
    81 248
    82 190
    83 1349
    84 6931
    85 2131
    86 4649
    87 8748
    88 1757
    89 4946
    90 2261
    91 29384
    92 279
    93 205
    94 891
    95 5356
    96 741
    97 591
    98 3717
    99 2024
    100 676
    101 1322
    102 2403
    103 11398
    104 4764
    105 27457
    106 1351
    107 38
    108 1915
    109 220
    110 8923
    111 410
    112 14587
    113 57
    114 941
    115 976
    116 8691
    117 1164
    118 1042
    119 893
    120 35880
    121 531
    122 3753
    123 16601
    124 19205
    125 98
    126 1461
    127 760
    128 877
    129 1883
    130 353
    131 149
    132 695
    133 723
    134 1836
    135 903
    136 30235
    137 681
    138 1208
    139 432
    140 190
    141 368
    142 94
