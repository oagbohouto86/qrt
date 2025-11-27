# qrt
**Prediction of overall survival in patients with Myeloid Leukemia**

## Challenge description

### A- Goal

The goal of this challenge organized by QRT and Institut Gustave Roussy - 2025, is to predict accurately survival for patients diagnosed with blood cancer, specifically within subtypes of adult myeloid leukemias. Overall survival is described by the period between the initial diagnosis to either the patient’s death or the lost to follow-up.
Accurate risk predictions could lead to better clinical decision-making, improved patient outcomes, and more efficient resource allocation within healthcare facilities.

## B- Data Overview

We get two sets of data:

training set with 3323 patients which will be used to set our model (feature management and engineering, hyperparameters tuning and learning)
test set with 1193 patients for which we will predict the risk score using their features.
There are two types of features:

clinical features (one row per patient) including the clinical center, bone marrow blasts percentage, WBC count, ANC count, monocytes count, HB level, platelet count and cytogenetics.
Gene molecular features (one row per somatic mutation per patient). Somatic (acquired) mutations are mutations specific to cancerous cells, not found in the patient’s normal cells.
The outcomes provided in Y_train set are the overall survival time in years from diagnosis (OS_YEARS) and the censoring indicator (OS_STATUS) denoting death or alive or lost to FUP of each patient in training set. Then the expected output will be the predicted risk of death (risk score) for each patient in test set.

## C- Metric

The loss metric is the Concordance Index for Right-Censored Data with IPCW (IPCW-C-index). This metric is an extension of classical c-index used to measures how well a predictive model can correctly rank survival times. This extension apply inverse probability of censoring weights (IPCW) depending on censored data to better handle right-censored data.
This metric as well as classical c-index are implemented in scikit-survival python package.

## D- Benchmark

The first benchmark (LGBM model) is provided as an example. The actual score obtained with the second benchmark (Cox model) is equal to 0.6541 and is the one expected to exceed. Available here ~notebook\Benchmark_nqBJ7fO.ipynb 


