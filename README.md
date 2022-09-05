# fake-news-extension

The following project runs a series of models on the dataset of [fake/real news](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset) to identify the best fit model for detecting fake news. The best fit model will be imported into the chrome extension to identify fake or real articles on the chrome browser.

** take note that the dataset cannot be contained in this repository due to large file size

### Sequence of project

* data_analysis.ipynb
* data_processing.ipynb
* models.ipynb (runs through series of model training)
* LR_classifier.ipynb (export model as jolib file for extension)

### How it works
* the extension runs on a flask server that handles requests
* the extension retrieves the article's title through html tags, and sends it to the flask server
* the classifier imported into the server is then run on the news title
* prediction will be sent upon clicking the 'predict' button of the extension

### How to run the project
* unpack the chrome folder stored in the project in developer mode of the chrome browser
* go to root directory of project in terminal and run the following:
* python server.py

Take note that the classifier model.pkl has already been exported, hence the project is ready to run without going through the jupyter notebooks.


### Screenshots

#### Fake news prediction
![image](https://user-images.githubusercontent.com/58553029/188451295-fee7359c-17df-4e58-8948-5355d25e6eb4.png)
![image](https://user-images.githubusercontent.com/58553029/188451335-0d9ffde7-3340-4b7f-934c-c8e8f6733780.png)

#### Real news prediction
![image](https://user-images.githubusercontent.com/58553029/188451438-5b1c1c15-2440-486f-8a7a-089f45b10a70.png)
![image](https://user-images.githubusercontent.com/58553029/188451472-59ccfb66-8991-44c3-9029-4f927a25f38f.png)

