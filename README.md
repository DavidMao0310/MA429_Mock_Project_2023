
# MA429_Mock_Project_2023

*This is a Group Project on Machine Learning*

**We choose [Census-Income (KDD) Data Set](https://archive.ics.uci.edu/ml/datasets/Census-Income+%28KDD%29) to do analysis.** 

This project aims at classifying the income level ($\pm 50k$) of an individual based on 41 demographic and employment related attributes. Below are running steps for our project.

* We first download data from the website, and save the data in `.xlsx` form, then we get two files, namely `income_data.xlsx` and `income_test.xlsx`.
* Then we run `data_preprocessing.py` to transform the variables name based on `symbol_dictionary.xlsx`, we choose **name_abbreviation_new** as new names. After that we will get two files, namely `train_with_na.csv` and `test_with_na.csv`, we will do analysis on them.
* The notebook `EDA_and_preprocess.ipynb` will illustrate the whole EDA and preprocessing part, check it for details. In order to reduce the memory of Jupyter server, we output  `train_data_after_EDA.csv` to do modelling.
* The notebook `Model_building.ipynb` will give the details of modelling part, including features engineering, model fitting and model evaluation.  


This project can be found via [Github link](https://github.com/DavidMao0310/MA429_Mock_Project_2023).
