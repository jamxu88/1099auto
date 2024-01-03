# 1099auto
Automatically fill out ATXW2 forms.

## Preparing the CSV file
There is a file called `1099 Program Template` to help you format your CSV.

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

The order does not matter, but the column names must be exactly as shown above.

2. Save the excel file as a CSV file in the same directory as the 1099.exe file.

## Usage
Run `1099.exe`, enter the filename of the CSV you just saved, and switch to the ATX W-2 program. Click on the RECIPIENT'S TIN field. The program will automatically fill out the forms. There will be a 10 second delay between running the program and the form being filled so you can navigate to the field in time.