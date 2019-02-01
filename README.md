# DeepWTO

## About the project 
This project is a continuation work of previous project, 
__[Auto-generation of GATT_WTO panel report](https://github.com/syyunn/GATT_WTO)__. 
Compare to the this previous project, this time the project has narrow downed to the classification task to predict 
which country wins the legal battle in __[WTO](https://en.wikipedia.org/wiki/World_Trade_Organization)__ 
from the task of panel report generation. 

This project is assumed to achieve following two main goals:
1. Build a __dataset__ that everyone can participate in this legal prediction agenda in __objective manner__
2. Performs a classification with simple __neural network__ to set the baseline of the classification task.

Sometime later on, above two will be branched and managed to separate projects, however, those two are in a same
 repository at present. 


### Dataset 
Basically, the WTO panel process is to determine __whether a country has breached__ __a specific article of WTO rulings__,
by explicitly saying as following : 


> "that Korea’s domestic support for beef in 1997 and 1998 exceeded the de minimis level contrary to Article 6 of the Agreement on Agriculture"


This quotes from WTO determines `Korea` has breached `Article 6 of the Agreement on Agriculture` with `domestic support for beef`. 

Therefore, our dataset is aimed to provide useful accessibility to train the neural network, which will predict 

`breach` or `not` with given `Who (Korea)`, `Government Measure (domestic support for beef)`, `Article 6 of the Agreement on Agriculture`  





 From the __[WTO official website]()__ we can publicly get access to the legal decision of panel report with facts of circumstances and its 