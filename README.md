# Glitch Guru

Glitch Guru is an software bug classifier, which can tell whether a ticket is a bug or not, using the title and summary of the ticket.

The model that this application uses, is powered by OneAPI libraries for faster inference and other benefits.

<img src="https://user-images.githubusercontent.com/25586296/227501224-59e10c2c-80fa-44bc-af0d-6184514588e8.png" height=400/>

## Video

https://drive.google.com/file/d/10TWvMwMLxBaly1npYiAQLV_0cAAAiGND/view?usp=share_link

## Methodology
The dataset used for this project is from a study ["Classifying Bug Reports to Bugs and Other Requests Using Topic Modeling"](https://github.com/hideakihata/BugReportClassificationDataset/tree/master). The tickets from the open-source projects HTTPCLIENT, JACKRABBIT, LUCENE have been taken for analysis.

The following steps have been followed to create the model:
- Data Cleaning and Preprocessing
    - There were multiple XML files, which had to be brought together into a single dataframe.
    - Relevant information such as title and description of a ticket was processed from each XML file.
- Feature Extraction (through TFIDF Vectorization and Chi Squared Test)
    - A corpus of words was formed by boosting the description and title of the ticket together.
    - TFIDF Vectorization was done on this corpus of words, to quantify the importance/relevance of certain strings.
    - Since there were lots of features after the previous steps, 50000 best features were taken with the help of the Chi-Squared Test.
- Classifier and Neural Network Identification (compiled using OneAPI libraries)
    - Multiple classifiers were tested on this dataset, in order to find the one which is most optimal.
    - The time difference between OneAPI and non-OneAPI versions of these classifiers have also been tested.
    - Results:        
        | Classifiers         | Precision  |
        |---------------------|------------|
        | MLPClassifier       | **0.9094** |
        | SVM                 | 0.8945     |
        | SGDClassifier       | 0.8825     |
        | LightGBM            | 0.8402     |
        | Logistic Regression | 0.7740     |
        | XGBoost             | 0.81       |
    - A neural network with 4 Dense Layers, Dropout Layers and PReLU Activation Layers was also trained.
        | Metric                   | Value  |
        |--------------------------|--------|
        | Best Training Accuracy   | 0.9591 |
        | Training Loss            | 0.1187 |
        | Best Validation Accuracy | 0.9058 |
        | Validation Loss          | 0.2478 |
    - Hence, the MLPClassifier performed the best among all the classifiers. This classifier also beats the methods presented in the dataset paper.

All the code related to model analysis is present in this [Jupyter Notebook](./FinalBugClassification.ipynb).

## Usage

To setup Glitch Guru in your local machine, follow these steps:
- Clone the repo
- Create and activate virtualenv
```
python -m venv venv
. venv/bin/activate
```
- Install required packages
```
pip install -r requirements.txt
```
- Download the model files from this [link](https://drive.google.com/drive/folders/1wVfaybluH66AGRphDewZdW-YwE784O9l?usp=share_link), and put them in a new folder called `model_files`.
- Start the API using the following command:
```
python3 app.py
```
- Visit `localhost:8000` and view the application.

## Tech Stack
- Tensorflow
- Scikit-Learn
- OneAPI (daal4py)
- FastAPI
