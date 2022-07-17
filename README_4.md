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

# Selected topic
x`
# :one: What are the key metrics which contributes the most towards predicting a shopper's behavior?

Seeing these feature importances, we want to simplify our model to only use features that may heavily contribute to our classification. Using our feature importance chart, we will take the top 5 most impactful features: PageValues, ExitRates, ProductRelated_Duration, BounceRates, ProductRelated. In addition, after creating the simplififed model, we want to measure the effectiveness of our model by using cross validation.

![Attributes](https://user-images.githubusercontent.com/98929742/179428673-214c778c-8943-4421-b974-27d2c8a19a88.PNG)


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



# Questions that we hope to answer with the data
What are the key metrics which contributes the most towards predicting a shopper's behavior?

What variables are most important to explain Revenued sessions?

What is the profile of the 'Right Customer' based on the metrics and variables included in the dataset?
- We concluded that the "Right Customer" is based off of being a returing customer with low bounce and exit rates. This customer also ends up buying products in high seasons that includ the months of November and May and where the result of Revenue was "TRUE" because it means the visitor made a purchase. it is important to note that this customer spent more time on the webpage and we would know this by the variable Product Related Duration. 

<img width="500" alt="image" src="https://user-images.githubusercontent.com/92067596/179364455-58e9f411-67c6-4afa-91d0-e395d78b04df.png">


Are the conversion rates of new visitors high when compared to those of returning customers?
- In the conversion rate it is the percentage of users who take the desrired action. In this example, the new visitors are compared to returning visitors who buy something on the website. 
- 
 <img width="500" alt="image" src="https://user-images.githubusercontent.com/92067596/179363961-ab5cc804-1808-4d1d-9007-9cbfed0053ad.png">
 
 ### Tableau Dashboard
 
 [Dashboard Link](https://public.tableau.com/app/profile/leonardo.domenico.bologni/viz/Online_Shoppers_Behavior/Online_Shoppers_Behavior?publish=yes)
