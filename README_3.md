<p align="center">
 <img src="https://user-images.githubusercontent.com/98360572/178841181-f612e874-4154-43d8-ac54-5acd461ce6e5.png" width="100%" height="50%">
</p>

# Final Project - 🛒 Online Shoppers Behavior - Week 3🛍️

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

# Machine Learning Models

Our dataset `online_shoppers_intention.csv' can be analyzed using 6 different models that were introduced during the second week of the final project.  The mentioned models are:

Resampling Models:
* Naive Random Oversampling
* SMOTE Oversampling
* Logistic Regression
* SMOTEENN

Ensemble Models:
* Balanced Random Forest Classifier
* Easy Ensemble AdaBoost Classifier

The models listed can be run using the two Jupyter notebooks included in this repository:
[shoppers_ML_resampling.ipynb](https://github.com/Peteresis/PALAB---Online-Shoppers-Behavior/blob/b704d5d281091d6528f9e7964ddcab190bd2a301/shoppers_ML_resampling.ipynb) and [shoppers_ML_ensemble.ipynb](https://github.com/Peteresis/PALAB---Online-Shoppers-Behavior/blob/b704d5d281091d6528f9e7964ddcab190bd2a301/shoppers_ML_ensemble.ipynb) 

However, we found a better way to run these models using a Python library called **Streamlit**.

The link to the App and the Python file that is the 'brain' of the App are:

[Streamlit App](https://peteresis-palab---online-shoppers-behavior-classifier-d9vdom.streamlitapp.com/)

[Python Code](https://github.com/Peteresis/PALAB---Online-Shoppers-Behavior/blob/4b90fab3247f9a3d1a73165677df6d63292cd6c6/Classifier.py)

<p align="center">
 <img src="https://user-images.githubusercontent.com/98360572/178845353-37f1c5d3-7251-4150-9800-ed03110f02e0.png" width="25%" height="25%">
</p>

It is possible to create an online app and connect it to the Github repository using Streamlit. The library allows you to add a sidebar that contains the controls for running the app, and the results are displayed immediately on the right pane.

Our Streamlit App allows you to run six Machine Learning Models on the `online shoppers intention.csv` dataset and immediately see the output showing the main metrics of the model such as accuracy score, original dataset shape, resampled dataset shape, classification report, feature importance chart (available for some models only), correlation matrix, and confusion matrix.

Furthermore, each model can be fine-tuned by modifying the main parameters of the model, such as sampling strategy, number of estimators, best split, and others, using the controls on the sidebar.

The App produces several charts that allow the visualization of the results produced by each model for an easier understanding.

<p align="center">
 <img src="https://user-images.githubusercontent.com/98360572/178847433-4b4103e1-0fae-47a2-bce8-ec32d9249100.png" width="50%" height="50%">
</p>

<p align="center">
 <img src="https://user-images.githubusercontent.com/98360572/178847514-b0e69c46-5723-4c0e-8efd-72240e696e2d.png" width="50%" height="50%">
</p>

<p align="center">
 <img src="https://user-images.githubusercontent.com/98360572/178847578-98e8e776-568b-4cd5-b648-0c017ccfec9f.png" width="50%" height="50%">
</p>






