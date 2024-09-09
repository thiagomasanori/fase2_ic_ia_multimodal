# apply in terminal: 
#   pip install requests

import os 
import requests

def upload_dicom_file(file_path, orthanc_url):
    """
    Upload a single DICOM file to the Orthanc server.

    :param file_path: Path to the DICOM file
    :param orthanc_url: URL of the Orthanc API
    """
    # default username and password
    auth = ('orthanc', 'orthanc')
    with open(file_path, 'rb') as dicom_file:
        response = requests.post(orthanc_url, data=dicom_file, auth=auth)
        if response.status_code in [200, 201]:
            print(f"Successfully uploaded {file_path}")
        else:
            print(f"Failed to upload {file_path}. Status code: {response.status_code}, Response: {response.text}")

def upload_dicom_folder(folder_path, orthanc_url):
    """
    Upload all DICOM files in a folder to the Orthanc server.

    :param folder_path: Path to the folder containing DICOM files
    :param orthanc_url: URL of the Orthanc API (e.g., "http://localhost:8042/instances")
    """
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".dcm"):  # You can adjust this to detect DICOM files without extensions
                file_path = os.path.join(root, file_name)
                upload_dicom_file(file_path, orthanc_url)

# Specify the folder containing DICOM files
dicom_folder_path = '/Users/thiagohata/Documents/dicom_samples'

# Orthanc server API URL
orthanc_url = 'http://localhost:8042/instances'

# Call the function to upload the folder
upload_dicom_folder(dicom_folder_path, orthanc_url)