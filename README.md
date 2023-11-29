# CarPricePrediction

## About Data 
This data is collected from the Kaggle . You will get this dataset from here "https://www.kaggle.com/datasets/balaka18/quikr-cars-scraped"



## Data Quality 
- year column has many no-year values
- year object is object 
- price column has ask for price string values 
- price columns is object
- kms_driven object to int
- kms_driven has nan values 
- fuel_type has nan values
- keep first 3 words from name column

## Performed Steps
- Data Cleaning,
- Data Processing,
- EDA
- Features Extraction,
- One Hot Encoding using column_transformer from scikit-learn
- Making Pipeline for the categorical features
- Model Selection
- Run 1000 times of for loop to get the best r2_score 
- build website using flask 
- deployed the model with streamlit website 



# Want to check real time ?


Clone the repository

```bash
https://github.com/mdnazrulislam-code/CarPricePrediction.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n py310 python==3.10 -y
```

```bash
conda activate py310
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
streamlit run main.py
python application.py
```

Now,
```bash
open up you local host and port