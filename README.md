# fake-news-extension

The following project runs a series of models on the dataset of [fake/real news](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset) to identify the best fit model for detecting fake news. The best fit model will be imported into the chrome extension to identify fake or real articles on the browser.

### Sequence of project

* data_analysis.ipynb
* data_processing.ipynb
* models.ipynb (runs through series of model training)
* LR_classifier.ipynb (export model as jolib file for extension)


### How to run the project
* unpack the chrome extension (chrome folder) in developer mode of the chrome browser
* go to root directory of project and run the following:
* python server.py

Take note that the classifier model.pkl has already been exported, hence the project is ready to run without going through the jupyter notebooks.


### Screenshots
![image](https://user-images.githubusercontent.com/58553029/188448426-4c02130d-801e-4821-a53a-48015fc7157d.png)
