# DeepWTO

## About the project 
This project is a continuation work of previous project, 
__[Auto-generation of GATT_WTO panel report](https://github.com/syyunn/GATT_WTO)__. 
Compare to the this previous project, this time the project has narrow downed 
to the classification task to predict 
which country wins the legal battle in __[WTO](https://en.wikipedia.org/wiki/World_Trade_Organization)__ 
from the task of panel report generation. This project is assumed to achieve following two main goals:
1. Build a __dataset__ that everyone can participate in this legal prediction 
agenda in __objective manner__
2. Performs a classification with simple __neural network__ to set the baseline 
of the classification task.

Sometime later on, above two will be branched and managed to separate projects, 
however, those two are in a same repository at present. 


### Dataset 
Basically, the WTO panel process determines __whether a country's government 
measure__ is __legal or not__ to __a certain article of WTO rulings__,
by explicitly saying as following : 

> "Korea’s domestic support for beef in 1997 and 1998 exceeded the de 
minimis level contrary to Article 6 of the Agreement on Agriculture." 

Therefore, our dataset is comprised of mainly 3 components - `Government Measure`, `Legality`, `Article Code`. 


#### Government Measure 
`Government Measure` is the most tricky part to prepare the data to train.  `Government measure` is usually __descriptive__ and __specific__ on each 
case, which is hard to generalize across the cases. 


