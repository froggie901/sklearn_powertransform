# sklearn_powertranform
## By: Patrick Cavins, PhD 

### This repo contains files which were used for a lighting (or is it a power talk? I am confused...) talk on the sklearn preprocessing module powertransformers with help from the SciPy Box-Cox module. Also a code along style notebook is inside which was used in conjunction with a Medium Article,  [Sklearn's Power Transformer Module](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwjHos3Ip73lAhVTKH0KHYF4BM8QFjAAegQIABAG&url=https%3A%2F%2Fmedium.com%2F%40patricklcavins%2Fusing-scipys-powertransformer-3e2b792fd712&usg=AOvVaw1Iu9cCc3G1i1Y4IknM8nVr)  

**CONTENTS**
- ReadME.md 
- sklearn_powertranformer_codealong.ipynb (Medium Article)
- power_transformer.ipynb (Lighting Talk) 
- train.csv (Ames, IA Dataset)

## Goals
Data Scientists often need Gaussian like models to use many of the most common ML Models. In these notebooks, we are going to review methods whereby we can transform non-normal/gaussian like data into data that is normal/gaussian-like.    

We are therfore changing the **distribution** of the data.

## Tools (Libraries) Used
- Seaborn (Graphing) 
- Pandas (Data Management) 
- SciPy Stats (Box-Cox and Yeo-Johnson Transformations)
- SciPy Stats (Kurtoss and Skew) 
- SciPy Stats (Normality Test (D'Angostino K^2 Test) 
- SkLearn Preprocessing 

## Data 
For this project, the Ames,IA housing dataset is used. It publically avaiable via [Kaggle](https://www.kaggle.com/c/ames-housing-data). The training data is available in this repo, **train.csv**


## Issues
Sometimes the Sklearn module returns distributions which do not meet the criteria of being normal like. It appears that it is settling on a non-optimal lambda value in both the box-cox transformation & yeo-johnson transformation. 

## Questions 
Feel free to reach to me via Twitter, [@PatrickCavins](https://twitter.com/patrickcavins)








