import pandas as pd
from datetime import datetime


def fetch_labels():
    labels_df = pd.read_csv('train.csv', header=None, names=['Filename', 'Label'], skiprows=1)
    print(labels_df)



def calculate_age(ds):
    birth_date_str = ds.PatientBirthDate
    study_date_str = ds.StudyDate
    birth_date = datetime.strptime(birth_date_str, "%Y%m%d")
    study_date = datetime.strptime(study_date_str, "%Y%m%d")
    
    age = study_date.year - birth_date.year - ((study_date.month, study_date.day) < (birth_date.month, birth_date.day))
    return age