import os
import pydicom
import pandas as pd

# Base directory where DICOM folders are located
base_dicom_dir = r'D:\uni\iAAA\python\mri\data'

# Initialize an empty dictionary to hold the metadata
patient_data = {}

# Iterate through each folder in the base directory
for dicom_folder in os.listdir(base_dicom_dir):
    dicom_path = os.path.join(base_dicom_dir, dicom_folder)
    
    if os.path.isdir(dicom_path):  # Ensure it's a directory
        # List all DICOM files in the folder
        dicom_files = [f for f in os.listdir(dicom_path) if f.endswith('.dcm')]
        
        # Initialize a list to hold metadata for this folder
        folder_metadata = []

        for dicom_file in dicom_files:
            dicom_file_path = os.path.join(dicom_path, dicom_file)
            
            # Read the DICOM file
            ds = pydicom.dcmread(dicom_file_path)
            
            # Extract the PatientID and other metadata
            patient_id = ds.PatientID
            metadata = {
                'PatientID': ds.PatientID,
                'StudyDate': ds.StudyDate,
                'Modality': ds.Modality,
                # Add other relevant DICOM fields here
            }
            
            # Add metadata to the list
            folder_metadata.append(metadata)
        
        # Check if the PatientID already exists in the dictionary
        if patient_id not in patient_data:
            patient_data[patient_id] = {}
        
        # Store the metadata for this folder (without label yet)
        patient_data[patient_id][dicom_folder] = {
            'Metadata': folder_metadata,
            'Label': None  # Placeholder for label, to be added later
        }

# Load the CSV file (replace 'your_file.csv' with your actual file path)
csv_file = r'D:\uni\iAAA\python\mri\train.csv'
df = pd.read_csv(csv_file, header=None, names=['DICOM_Folder', 'Label'])

# Iterate through the DataFrame and update the dictionary with labels
for index, row in df.iterrows():
    dicom_folder = row['DICOM_Folder']
    label = row['Label']
    
    # Find the folder in the dictionary and update the label
    for patient_id, folders in patient_data.items():
        if dicom_folder in folders:
            patient_data[patient_id][dicom_folder]['Label'] = label
            break

# Now, patient_data contains all the information grouped by PatientID, including labels
