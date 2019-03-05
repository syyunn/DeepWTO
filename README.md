<p align="center">
  <img src="/assets/wto.png" width="497" height="370">
</p>


# DeepWTO 

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)


## About the project 
__[DeepWTO](https://github.com/syyunn/DeepWTO)__ is a continuation work of previous project, 
__[Auto-generation of GATT/WTO panel report](https://github.com/syyunn/GATT_WTO)__. 
Compare to the this previous project, this time the project has narrow downed 
to the classification task to predict 
which country wins the legal battle in __[WTO](https://www.wto.org)__. This project is assumed to achieve following two main goals:

1. Build a __dataset__ so that everyone can participate in this legal prediction 
agenda in __objective manner__
2. Performs a __classification__ with simple neural networks to achieve the naive-baseline, __50% >__ accuracy 
of the classification task.
=============================================================================
This project changed its direction to predict the density of probability of 
inconsistency upon all the provisions provided in WTO upon given textual 
data of factual aspect

### Dataset 
Basically, the WTO panel process determines __whether a country's government 
measure at issue__ is __contrary or not contrary__ to __a certain article(s)
 of rules of WTO__, by explicitly saying as following : 

> "Korea’s domestic support for beef in 1997 and 1998 exceeded the de 
minimis level contrary to Article 6 of the Agreement on Agriculture." 

Therefore, our dataset is comprised of mainly 4 components - 
[__Factual Aspects__], [__Government 
Measure__](https://github.com/syyunn/DeepWTO/tree/master/dataset/measure), 
[__Legality__](https://github.com/syyunn/DeepWTO/blob/master/dataset/label/legality.yaml),
[__WTO Legal Provisions__](https://github.com/syyunn/DeepWTO/tree/master/dataset/provision). 


### Government Measure

Government measure is the most __tricky__ part to prepare the data to train.
  Government measure is usually __descriptive__ and __case-specific__, therefore it is hard to be generalized across the cases. Moreover, Government measure
 __has no strictly enforced formatting 
 style__ but mainly depends on the preference of each panel body and its 
 included personnel. 
Therefore, for the first version of the dataset, we just naively parse all 
the strings included in __Panel(or Appellate Body if exists) Report__ to 
check whether this naive dataset - which lacks a hierarchical structure of 
document, could be also analyzed with deep learning approach. 

Normally, description about Government Measure is included in the following:
  retains GOV measure description 
  
- Request for Consultations  [[example](https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/25382/Q/G/L/292.pdf)]
- Request for the Establishment of a Panel [[example](https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/46659/Q/WT/DS/161-5.pdf)]

### Reproduce   
    git clone https://github.com/syyunn/DeepWTO
    cd DeepWTO
    conda env create -f environment.yaml


### Author
[__Zachary Yoon__](https://github.com/syyunn)

### Sponsor
<p align="center">
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

#### Labelling On Progress
- [x] 2
- [x] 7
- [x] 8
- [x] 10
- [x] 11
- [x] 12
- [x] 14
- [x] 18
- [x] 22
- [x] 24
- [x] 31
- [x] 33
- [x] 34
- [x] 46
- [x] 50
- [x] 56
- [x] 58
- [x] 60
- [x] 62
- [x] 67
- [x] 68
- [x] 69
- [x] 70
- [x] 72
- [x] 76
- [x] 79
- [x] 87
- [x] 90
- [x] 98
- [x] 99
- [x] 103
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
- [ ] 161
- [ ] 162
- [ ] 163
- [ ] 165
- [ ] 166
- [ ] 169
- [ ] 170
- [ ] 174
- [ ] 175
- [ ] 177
- [ ] 178
- [ ] 184
- [ ] 189
- [ ] 192
- [ ] 202
- [ ] 204
- [ ] 207
- [ ] 212
- [ ] 213
- [ ] 217
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


