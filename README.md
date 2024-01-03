# 1099auto
Automatically fill out ATXW2 forms.

## Preparing the CSV file
1. Ensure that the Excel file has the following columns:
- `TIN`
- `Amount` (Compensation/Income)
- `First Name`
- `Last Name`
- `M.I.`
- `Business Name`
- `Address Line 1`
- `Address Line 2`
- `Zip`

2. Save the excel file as a CSV file.

## Usage
Install python and dependencies in `requirements.txt`.

In `1099.py`, replace `FILENAME.csv` in line 5 with the name of the CSV file you saved.

Run `python 1099.py` and switch to the ATX W-2 program. Click on the RECIPIENT'S TIN field. The program will automatically fill out the forms. There will be a 10 second delay between running the program and the form being filled so you can navigate to the field in time.