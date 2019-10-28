# sklearn_powertranform
## By: Patrick Cavins, PhD 

### This repo contains files which were used for a lighting (or is it a power talk? I am confused...) talk on the sklearn preprocessing module powertransformers with help from the SciPy Box-Cox module. Also a code along style notebook is inside which was used in conjunction with a  [Sklearn's Power Transformer Module](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwjHos3Ip73lAhVTKH0KHYF4BM8QFjAAegQIABAG&url=https%3A%2F%2Fmedium.com%2F%40patricklcavins%2Fusing-scipys-powertransformer-3e2b792fd712&usg=AOvVaw1Iu9cCc3G1i1Y4IknM8nVr)  

**CONTENTS**
- ReadME.md 
- sklearn_powertranformer_codealong.ipynb (Medium Article)
- power_transformer.ipynb (Lighting Talk) 

## Goal

We want to take data that is non-normal/gaussian like and transform it into data that is normal/gaussian-like. We are therfore changing the **distribution** of the data.

**signal_boost** Using a power transformation on your data will change the distrubtion of the data! Make sure you think clearly about the implications of this... 

## What? 

The preprocessing module powertransformer contains two different transformations
- Box-Cox Transformation: Can be used on positive values only
- Seo-Johnson Transformation: Can be used on both positive and negative values 

https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html

We are actually fairly familiar with transformations, but of a different class. Here are some examples of linear transformations: 

- converting between celsius and farhenheit 
- converting between USD and GBP

*We call these linear because they are simiply a mathematic change (i.e. multplication by some constant) they **do not change the distribution of the data**


If the goal is perhaps...

- to remove heteroscedasticity?
- force data to be normally distributed?

### But, why? 

Remember those assumptions we made in in our linear regression model? 

- In LINE, **N** = Normality (the errors follow a normal distribution)  
- In LINE, **E** = Equality of Variance, homoscedasticity

### Enter the power transformers...

Herein lies the strength of the power transformers. Unlike linear transformations, a power transformation will **change the distribution** of the data. 

- This can remove heteroscedasticity and make the data look more normal-like. 








