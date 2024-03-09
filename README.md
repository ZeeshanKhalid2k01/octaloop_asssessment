# octaloop_asssessment
Quiz bot from 3 different categories


# Assessment Repository

This repository contains scripts and resources for an assessment project.

## Setting up the Free API from Gemini

To set up the free API provided by Gemini (Google), follow these steps:

1. Obtain the API credentials and documentation for accessing the free API, from Google.
2. Copy the API key to .env

## Downloading Folders from Google Drive

Download the following folders from Google Drive (vector-DBs):

1. [Folder 1](https://drive.google.com/drive/folders/1Ai0jTpYnQ-gXzZCpLi4IRxcGS812qfWa?usp=sharing)
2. [Folder 2](https://drive.google.com/drive/folders/1tEOwvjD992x92iqU7-Z9uwwVprAm7iBg?usp=sharing)
3. [Folder 3](https://drive.google.com/drive/folders/1w3ARprTaO7Ucm3pTSNsbV9c4eMFtH6My?usp=sharing)

## Extract Downloaded Folders from Zip Files
1. Extract all the 3 zip files, in the same directory where program files are saved
2. After Extraction, faiss_sports, faiss_movie, faiss_history will be shown
3. Do not change their names, as these files are being called from .py files from their names

## Installing Requirements

Install the required packages by running the following command:

```bash
pip install -r requirements.txt


Running the Script
To run the script, execute the following command:
streamlit run check.py


Extra Files
mcq_generator.ipynb: This file was previously used for generating MCQs but has been replaced by the free API due to resource constraints.

# Note:
Make sure to Add 3-folders, which will be downloaded from links, and Add API in .env
