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

# :one: Machine Learning Models

Our dataset `online_shoppers_intention.csv' can be analyzed using 6 different models that were introduced during the second week of the final project.  The mentioned models are:

Resampling Models:
* Naive Random Oversampling
* SMOTE Oversampling
* Undersampling
* SMOTEENN

Ensemble Models:
* Random Forest Classifier
* AdaBoost Classifier

The models listed can be run using the two Jupyter notebooks included in this repository:
[shoppers_ML_resampling.ipynb](https://github.com/Peteresis/PALAB---Online-Shoppers-Behavior/blob/b704d5d281091d6528f9e7964ddcab190bd2a301/shoppers_ML_resampling.ipynb) and [shoppers_ML_ensemble.ipynb](https://github.com/Peteresis/PALAB---Online-Shoppers-Behavior/blob/b704d5d281091d6528f9e7964ddcab190bd2a301/shoppers_ML_ensemble.ipynb) 

However, we found a better way to run these models using a Python library called **Streamlit**.

The link to the App and the Python file that is the 'brain' of the App are:


| Link to the Streamlit App | Link to the Python Code File |
| ----------- | ----------- |
| [Streamlit App](https://peteresis-palab---online-shoppers-behavior-classifier-d9vdom.streamlitapp.com/) |[Python Code](https://github.com/Peteresis/PALAB---Online-Shoppers-Behavior/blob/4b90fab3247f9a3d1a73165677df6d63292cd6c6/Classifier.py) |

<p align="center">
 <img src="https://user-images.githubusercontent.com/98360572/178845353-37f1c5d3-7251-4150-9800-ed03110f02e0.png" width="25%" height="25%">
</p>

It is possible to create an online app and connect it to the Github repository using Streamlit. The library allows you to add a sidebar that contains the controls for running the app, and the results are displayed immediately on the right pane.

Our Streamlit App allows you to run six Machine Learning Models on the `online shoppers intention.csv` dataset and immediately see the output showing the main metrics of the model such as accuracy score, original dataset shape, resampled dataset shape, classification report, feature importance chart (available for some models only), correlation matrix, and confusion matrix.

Furthermore, each model can be fine-tuned by modifying the main parameters of the model, such as sampling strategy, number of estimators, best split, and others, using the controls on the sidebar.

<p align="center">
 <img src="https://user-images.githubusercontent.com/98360572/178850872-256fd225-a0d0-4000-8ea5-58a7d67a82ee.png" width="50%" height="50%">
</p>

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

# :two: Comparison of the Results of the Models

| Model Name | Max Accurary Obtained<br>Using the Streamlit App |
| -----------   | -----------  |
| Naive Random Oversampling | 0.8182538793439996 |
| SMOTE Oversampling | 0.8086832465976176 |
| Undersampling | 0.5409592868321265 |
| SMOTEENN | 0.8333197543563056 |
| **Random Forest Classifier** | **0.8612784437134429** |
| AdaBoost Classifier | 0.8487314689397873 |

# :three: Conclusion

Based on the comparison table above, the best accuracy is obtained with the **Random Forest Classifier** model, which gives an accuracy of 86%.

In order to improve the results, we believe that the variables with low correlation on the output variable `Revenue` have to be dropped.  Once the number of variables is reduced, it is to be expected that the models produce an accuracy closer to 90% or more.


---
# :four: References

Streamlit: A faster way to build and share data apps, https://streamlit.io/

