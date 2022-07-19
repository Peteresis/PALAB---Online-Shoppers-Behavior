<p align="center">
 <img src="https://user-images.githubusercontent.com/98360572/179120313-518b2e47-7ab9-494f-acfc-af7fe57c294c.png" width="100%" height="50%">
</p>


# Final Project - 🛒 Online Shoppers Behavior - Week 4 🛍️

## Team Members

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"><img src="https://user-images.githubusercontent.com/98360572/175794933-6c7f2b4c-5ae1-4ff7-8770-221fecb35a2c.png" alt="Image" width="25" height="25"><img src="https://user-images.githubusercontent.com/98360572/175794887-b999b803-cf8c-4191-9f21-c3a3e1f590fb.png" alt="Image" width="25" height="25"></th>
    <th class="tg-0pky">Analucia Roeder</th>
  </tr>
</thead>
<tbody>
  <tr>
    <th class="tg-0pky"><img src="https://user-images.githubusercontent.com/98360572/175794883-38b56033-f662-4e44-826a-b99f7a897e31.png" alt="Image" width="25" height="25"><img src="https://user-images.githubusercontent.com/98360572/175794887-b999b803-cf8c-4191-9f21-c3a3e1f590fb.png" alt="Image" width="25" height="25"></th>
    <th class="tg-0pky">Pablo Marrero</th>
  </tr>
  <tr>
    <th class="tg-0pky"><img src="https://user-images.githubusercontent.com/98360572/175794942-cc19186f-908a-4198-8b24-2cd20b6e8b04.png" alt="Image" width="25" height="25"><img src="https://user-images.githubusercontent.com/98360572/175794887-b999b803-cf8c-4191-9f21-c3a3e1f590fb.png" alt="Image" width="25" height="25"></th>
    <th class="tg-0pky">Leonardo Bologni</th>
  </tr>
</tbody>
</table>

---
# :one: Selected topic: Predicting the behavior of online shoppers

When researching the possible topics for this project we focused on datasets that ticked the following 3 boxes:

✔️ The dataset is well-suited for machine learning analyses.

✔️ Everyone in the group would find the subject exciting.

✔️ The topic must be relevant to the business world, so that the project can be included in our professional portfolio.

# :two: Data Exploration

## :two::one: Dataset Source

**UCI Machine Learning Repository: Online Shoppers Purchasing Intention Dataset Data Set**, https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset#

This dataset contains **12330** entries, which are divided into **10,422** records in which shoppers did not purchase and **1908** instances in which shoppers did purchase. Each entry is based on unique users over a one-year period to avoid any campaign-specific trends. **There are 10 numerical and 8 categorical attributes in total. The Revenue column is the target variable that can take two values TRUE or FALSE**.

---
## :two::two: Data Wrangling

The dataset was explored using Python and we checked for the following:
  1. Checking for **Null** values in data
  2. Verify the type of data per column
  3. Check that all the rows have the same number of elements
  4. Decide if the data is balanced or imbalanced for Machine Learning

The code used to verify the data can be found here:
https://github.com/Peteresis/PALAB---Online-Shoppers-Behavior/blob/main/Data_Cleaning_and_Preparation.ipynb

---
# :three: Database

* The CSV file was loaded into an **SQL database**
* The SQL database was connected to the Python code in the repository using **SQLAlchemy**
* The **database ERD** with the relationships was created in the [QuickDBD site](https://www.quickdatabasediagrams.com/) 

| Python Code for SQL Connection | Schema File |
| ----------- | ----------- |
| [Connecting Database to Jupyter Notebook.ipynb](https://github.com/Peteresis/PALAB---Online-Shoppers-Behavior/blob/057e134b7e558681bcd1b291df172701dd4010e5/Connecting%20Database%20to%20Jupyter%20Notebook.ipynb) |[Database ERD.txt](https://github.com/Peteresis/PALAB---Online-Shoppers-Behavior/blob/057e134b7e558681bcd1b291df172701dd4010e5/Database%20ERD.txt) |

### Database Schema

<p align="left">
 <img src="https://user-images.githubusercontent.com/98360572/179841575-2f5f1ed0-8cc3-4300-9ddf-5804c17d7931.png" width="50%" height="50%">
</p>

---
# :four: Machine Learning Models

The data was analyzed using the same models learned during the Bootcamp:

Resampling Models:

  * Naive Random Oversampling
  * SMOTE Oversampling
  * Logistic Regression
  * SMOTEENN

Ensemble Models:
  * Balanced Random Forest Classifier
  * Easy Ensemble AdaBoost Classifier

Two Jupyter notebooks were used to run the machine learning models, and a Streamlit application was also developed to enable live online interaction with the models.

| Jupyter Notebook Resampling Models | Jupyter Notebook Ensemble Models |
| ----------- | ----------- |
| [shoppers_ML_resampling.ipynb](https://github.com/Peteresis/PALAB---Online-Shoppers-Behavior/blob/f71f4c5ea9a71a6b97ae291917efa895100f2932/shoppers_ML_resampling.ipynb) |[shoppers_ML_ensemble.ipynb](https://github.com/Peteresis/PALAB---Online-Shoppers-Behavior/blob/f71f4c5ea9a71a6b97ae291917efa895100f2932/shoppers_ML_ensemble.ipynb) |

| Link to the Streamlit App | Link to the Python Code File |
| ----------- | ----------- |
| [Streamlit App](https://peteresis-palab---online-shoppers-behavior-classifier-d9vdom.streamlitapp.com/) |[Python Code](https://github.com/Peteresis/PALAB---Online-Shoppers-Behavior/blob/4b90fab3247f9a3d1a73165677df6d63292cd6c6/Classifier.py) |

---
# :five: Tableau Dashboard

The dashboard was done using Tableau.

It consists of several charts showing the relationships between the different variables of the dataset, some of them are:

  * Bar Chart - Month vs Revenue
  * Barc Chart - Revenue vs (Informational Duration, Browser, Visitor Type, Page Value)
  * Scatterplot - Bounce Rates vs Exit Rates
  * Bubble Graph - Page Value vs Month

<p align="center">
 <img src="https://user-images.githubusercontent.com/98360572/179845113-c570fbd5-d11f-483c-b882-51cf26bf0d3e.png" width="40%" height="40%">
 <img src="https://user-images.githubusercontent.com/98360572/179845420-db5640e1-3d03-45d4-95bd-b35d127a0b83.png" width="40%" height="40%">
</p>

<p align="center">
 <img src="https://user-images.githubusercontent.com/98360572/179845750-c5656792-0d0a-4f30-aebd-f0277903aea8.png" width="40%" height="40%">
 <img src="https://user-images.githubusercontent.com/98360572/179845980-7f89e98d-4879-4034-ae4e-36bfa8262314.png" width="40%" height="40%">
</p>

| Tableau Dashboard Link |
| ----------- |
| [Dashboard Link](https://public.tableau.com/app/profile/leonardo.domenico.bologni/viz/Online_Shoppers_Behavior/Online_Shoppers_Behavior?publish=yes) |

---
# :six: Results Obtained

## :six::one: What are the key metrics?

According to the machine learning results we obtained, `PageValues`, `ExitRates`, `ProductRelated Duration`, `ProductRelated` and `BounceRates` are the top 5 attributes with the greatest influence.

<p align="center">
 <img src="https://user-images.githubusercontent.com/98929742/179428811-20ae02ea-0f60-4248-987c-97be32b8014a.PNG" width="25%" height="25%">
</p>

## :six::two: What variables are most important?

The most important attribute obtained from the Machine Learning results are the following:

- **Page Value** This metric is designed to help answer the question –“How much is a web page worth?”.  The formula is:
<p align="center">
    ${Page Value} = {{Transaction Revenue + Total Goal Value} \over Unique Pageviews}$
</p>

- **ExitRates** that is defined the percentage that were the last in the session.
- **ProductRelated_Duration** that is defined as the duration for which Client's Authorized Users are granted access to the Licensed Products.
- **ProductRelated** that is defined as products whose demand is influenced by a price change of another related product.
- **BounceRates** that is defined as the percentage of visitors to a particular website who navigate away from the site after viewing only one page.

<p align="center">
 <img src="https://user-images.githubusercontent.com/98929742/179434657-b1a86274-b0ac-473d-b1b7-f061c96bf1c8.png" width="50%" height="50%">
</p>

## :six::three: Comparison of the Results of the Machine Learning Models

| Model Name | Max Accurary Obtained<br>Using the Streamlit App |
| -----------   | -----------  |
| Naive Random Oversampling | 0.8182538793439996 |
| SMOTE Oversampling | 0.8086832465976176 |
| Undersampling | 0.5409592868321265 |
| SMOTEENN | 0.8333197543563056 |
| **Random Forest Classifier** | **0.8612784437134429** |
| AdaBoost Classifier | 0.8487314689397873 |

<p align="left">
 <img src="https://user-images.githubusercontent.com/98360572/179851963-067a10bb-1dc2-4289-8928-af6c8dca7c1a.png" width="50%" height="50%">
</p>

<p align="left">
 <img src="https://user-images.githubusercontent.com/98360572/179851712-ec1013e3-7789-4533-ab13-a140b49fe274.png" width="50%" height="50%">
</p>

<p align="left">
 <img src="https://user-images.githubusercontent.com/98360572/179851776-f06083cc-1edb-4121-8657-115f365a1597.png" width="50%" height="50%">
</p>

<p align="left">
 <img src="https://user-images.githubusercontent.com/98360572/179851873-bfd49e28-bdd7-4197-a4f7-3ec6a44da814.png" width="30%" height="30%">
</p>

## :six::four: What is the profile of the 'Right Customer' based on the metrics and variables included in the dataset?

## :six::five: Are the conversion rates of new visitors high when compared to those of returning customers?
- In the conversion rate it is the percentage of users who take the desrired action. In this example, the new visitors are compared to returning visitors who buy something on the website
 <img width="500" alt="image" src="https://user-images.githubusercontent.com/92067596/179363961-ab5cc804-1808-4d1d-9007-9cbfed0053ad.png">
---
# :seven: Conclusion

We can achieve approximately **86%** accuracy by using a **Random Forest Classifier**. The other Ensemble model, **AdaBoost Classifier**, is the second best model in this study, with an accuracy of **85%**.

To improve the model's accuracy, it should be considered to remove variables that are only weakly related to revenue. These variables are likely just adding noise to the model and do not contribute to the prediction results.

It may also be worthwhile to run this dataset through Neural Networks to see if the accuracy of the prediction obtained improves.



 
