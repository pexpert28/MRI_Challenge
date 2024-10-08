import pydicom
from utils import *
def identify_sequence(dicom_file):
    # Read the DICOM file
    ds = pydicom.dcmread(dicom_file)

    # Initialize variables for sequence identification
    sequence_type = "Unknown"
    print(calculate_age(ds))
    # Check for ProtocolName or SeriesDescription or SequenceName
    if 'ProtocolName' in ds:
        protocol_name = ds.ProtocolName.lower()
    elif 'SeriesDescription' in ds:
        protocol_name = ds.SeriesDescription.lower()
    else:
        protocol_name = ""

    if 'SequenceName' in ds:
        sequence_name = ds.SequenceName.lower()
    else:
        sequence_name = ""
    # Heuristic checks to identify T1, T2, and FLAIR
    if 't1' in protocol_name or 't1' in sequence_name:
        sequence_type = "T1"
    elif 't2' in protocol_name or 't2' in sequence_name:
        sequence_type = "T2"
    elif 'flair' in protocol_name or 'flair' in sequence_name:
        sequence_type = "FLAIR"

    return sequence_type

# Example usage
dicom_file = '/home/pooya/Projects/MRI_challenge/New folder/1.3.46.670589.11.10042.5.0.920.2023123109160568667/1.3.46.670589.11.10042.5.0.920.2023123109165048675.dcm'
sequence_type = identify_sequence(dicom_file)
print(f"The sequence type is: {sequence_type}")
