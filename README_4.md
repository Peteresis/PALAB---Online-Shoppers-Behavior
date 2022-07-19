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

# :one: Selected topic: Predicting the behavior of online shoppers

When researching the possible topics for this project we focused on datasets that ticked the following 3 boxes:

✔️ The dataset is well-suited for machine learning analyses.

✔️ Everyone in the group would find the subject exciting.

✔️ The topic must be relevant to the business world, so that the project can be included in our professional portfolio.

# :two: Data Exploration

## :two::one: Dataset Source

**UCI Machine Learning Repository: Online Shoppers Purchasing Intention Dataset Data Set**, https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset#

This dataset contains **12330** entries, which are divided into **10,422** records in which shoppers did not purchase and **1908** instances in which shoppers did purchase. Each entry is based on unique users over a one-year period to avoid any campaign-specific trends. **There are 10 numerical and 8 categorical attributes in total. The Revenue column is the target variable that can take two values TRUE or FALSE**.

## :two::two: Data Wrangling

The dataset was explored using Python and we checked for the following:
  1. Checking for **Null** values in data
  2. Verify the type of data per column
  3. Check that all the rows have the same number of elements
  4. Decide if the data is balanced or imbalanced for Machine Learning

The code used to verify the data can be found here:
https://github.com/Peteresis/PALAB---Online-Shoppers-Behavior/blob/main/Data_Cleaning_and_Preparation.ipynb

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







# :one: What are the key metrics

According to the machine learning results we obtained, PageValues, ExitRates, ProductRelated Duration, ProductRelated, and BounceRates are the top 5 attributes with the greatest influence.

<p align="center">
 <img src="https://user-images.githubusercontent.com/98929742/179428811-20ae02ea-0f60-4248-987c-97be32b8014a.PNG" width="25%" height="25%">
</p>

# :two: What variables are most important

The most important attribute obtained from the Machine Learning results are the following:

- **Page Value** that is defined as the the average value for a page that a user visited before landing on the goal page or completing an Ecommerce transaction.
- **ExitRates** that is defined the percentage that were the last in the session.
- **ProductRelated_Duration** that is defined as the duration for which Client's Authorized Users are granted access to the Licensed Products.
- **ProductRelated** that is defined as products whose demand is influenced by a price change of another related product.
- **BounceRates** that is defined as the percentage of visitors to a particular website who navigate away from the site after viewing only one page.


<p align="center">
 <img src="https://user-images.githubusercontent.com/98929742/179434657-b1a86274-b0ac-473d-b1b7-f061c96bf1c8.png" width="100%" height="100%">
</p>




# Database Schema

<p align="center">
 <img src="https://user-images.githubusercontent.com/98360572/179361359-385f14e0-5f53-4dfa-8b47-5b12a07aac1c.png" width="50%" height="50%">
</p>

# :four: Comparison of the Results of the Models

| Model Name | Max Accurary Obtained<br>Using the Streamlit App |
| -----------   | -----------  |
| Naive Random Oversampling | 0.8182538793439996 |
| SMOTE Oversampling | 0.8086832465976176 |
| Undersampling | 0.5409592868321265 |
| SMOTEENN | 0.8333197543563056 |
| **Random Forest Classifier** | **0.8612784437134429** |
| AdaBoost Classifier | 0.8487314689397873 |

 
 ### Tableau Dashboard
 
 [Dashboard Link](https://public.tableau.com/app/profile/leonardo.domenico.bologni/viz/Online_Shoppers_Behavior/Online_Shoppers_Behavior?publish=yes)
