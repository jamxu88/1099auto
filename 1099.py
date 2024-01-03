import pyautogui
import csv
import time
pyautogui.PAUSE = 0.01
filename = input('Input the filename (including extension, i.e. ".csv"): ')
with open(filename) as file:
    time.sleep(10)
    csv_reader = csv.reader(file, delimiter=',')
    reader = csv.DictReader(file)

    # Loop through each row
    for row in reader:
        tin = row["TIN"]
        amount = row["Amount"]
        first_name = row["First Name"]
        last_name = row["Last Name"]
        middle_initial = row["M.I."]
        business_name = row["Business Name"]
        address_line_1 = row["Address Line 1"]
        address_line_2 = row["Address Line 2"]
        zip = row["Zip"]

        # Print out the values in the row
        print(tin, amount, first_name, last_name, middle_initial, business_name, address_line_1, address_line_2, zip)
        pyautogui.write(f'{tin}')  ## SSN
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.write(f'{first_name}') ## FNAME
        pyautogui.press('tab')
        time.sleep(1)
        if middle_initial != "":
            pyautogui.write(f'{middle_initial}') ## MNAME
        pyautogui.press('tab') 
        pyautogui.write(f'{last_name}') ## LNAME
        pyautogui.press('tab')
        pyautogui.press('tab')
        time.sleep(1)
        if business_name != "":
            pyautogui.write(f'{business_name}') ## Business
        pyautogui.press('tab') 
        pyautogui.write(f'{address_line_1}') ## Street ln 1
        pyautogui.press('tab')
        time.sleep(1)
        if address_line_2 != "":
            pyautogui.write(f'{address_line_2}') ## Street ln2
        pyautogui.press('tab') 
        pyautogui.write(f'{zip}') ## ZIP
        pyautogui.press('tab')
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.write(f'{amount}')
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.write(f'{amount}')
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)
