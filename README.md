<p align="center">
 <img src="https://user-images.githubusercontent.com/98360572/175793026-d27ee45a-b260-400e-9a65-0e5ebf170e86.png" width="50%" height="50%">
</p>

# Final Project - 🛒 Online Shoppers Behavior 🛍️

# Selected topic

## **Predicting the behavior of online shoppers**

Shopping online is a massive and rapidly expanding market segment, contributing significantly to B2C (Business to Customer) earnings. Businesses can boost sales and revenue by better targeting advertising, marketing, and discounts based on customers' demographics and other characteristics gathered from their knowledge of when and how customers conduct research and make purchases online.

# Reason for selection of the topic

When researching the possible topics for this project we focused on datasets that ticked the following 3 boxes:

✔️ The dataset is well-suited for machine learning analyses.

✔️ Everyone in the group would find the subject exciting.

✔️ The topic must be relevant to the business world, so that the project can be included in our professional portfolio.

# Description of the source of data

## Dataset source:

UCI Machine Learning Repository: Online Shoppers Purchasing Intention Dataset Data Set, https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset# <br>
Citation from Original: Sakar, C.O., Polat, S.O., Katircioglu, M. et al. Neural Comput & Applic (2018). [Web Link](https://link.springer.com/article/10.1007/s00521-018-3523-0)

This dataset contains `12330 entries`, which are divided into `10,422 records in which shoppers did not purchase and 1908 instances in which shoppers did purchase`. Each entry is based on unique users over a one-year period to avoid any campaign-specific trends.  There are 10 numerical and 8 categorical attributes in total. The `Revenue` column is the target variable that can take two values `TRUE` or `FALSE`.

![image](https://user-images.githubusercontent.com/98360572/175793721-83bc4bac-d297-49bf-ac80-beba490c9550.png)

## Columns Description

`Administrative` - count of pages visited by the visitor (e.g. user details and account).<br>
`Administrative_Duration` - total time spent (seconds) in on Administrative type of page.<br>
`Informational` - count of pages visited by the visitor (e.g. about and contact of the website).<br>
`Informational_Duration` - total time spent (seconds) in on Informational type of page.<br>
`ProductRelated` - count of pages visited by the visitor (e.g. product details).<br>
`ProductRelated_Duration` - total time spent (seconds) in on ProductRelated type of page.<br>
`BounceRates` - percentage of visitors who enter the site from that page and then leave ("bounce") without triggering any other requests to the analytics server.<br>
`ExitRates` - the percentage of visitors to a page on the website from which they exit the website to a different website.<br>
`PageValues` - the average value for a page that a user visited before landing on the goal page.<br>
`SpecialDay` - indicates the closeness of the site visiting time to a specific special day (e.g. Mother’s Day, Valentine's Day).<br>
`Month` - the month of the visit to the website.<br>
`OperatingSystems` - the type of operation system used by the visitor.<br>
`Browser` - the type of browser used by the visitor.<br>
`Region` - the geographic region from which the session started.<br>
`TrafficType` - describes how traffic arrived on the website (Direct, Organic, Referral, Social, Email, Display and Paid).<br>
`VisitorType` - returning or new visitor or other.<br>
`Weekend` - indicating whether the date of the visit is weekend.<br>
`Revenue` - indicates whether the visitor made a purchase or not.<br>

**NOTE**: The `SpecialDay` feature indicates the closeness of the site visiting time to a specific special day (e.g. Mother’s Day, Valentine's Day) in which the sessions are more likely to be finalized with transaction. The value of this attribute is determined by considering the dynamics of e-commerce such as the duration between the order date and delivery date. For example, for Valentine’s day, this value takes a nonzero value between February 2 and February 12, zero before and after this date unless it is close to another special day, and its maximum value of 1 on February 8.

# Questions that we hope to answer with the data

What are the key metrics which contributes the most towards predicting a shopper's behavior?

What variables are most important to explain Revenued sessions?

What is the profile of the 'Right Customer' based on the metrics and variables included in the dataset?

Are the conversion rates of new visitors high when compared to those of returning customers?




