from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import random
import time
import win32clipboard

driver_temp_email = webdriver.Chrome()
driver_temp_email.get("https://mail.tm/en/")
time.sleep(3)

df = pd.read_excel(r'C:\Users\Martin\Desktop\Python\Automation\Users.xlsx', dtype=str)
print(df)
for ind in df.index:

    first_name = df['First name'][ind]
    last_name = df['Last name'][ind]
    city = df['City'][ind]
    email = df['Email'][ind]
    phone_number = df['Phone number'][ind]
    sex = df['Sex'][ind]

    accounts_menu = driver_temp_email.find_element_by_id('accounts-menu')
    # print(accounts_menu.get_attribute('innerHTML'))
    accounts_menu.click()
    time.sleep(1)

    create_new_acc = driver_temp_email.find_element_by_xpath("//div[@class='py-1']")
    print(create_new_acc.get_attribute('innerHTML'))
    create_new_acc.click()
    time.sleep(1)

    username = driver_temp_email.find_element_by_id('username')
    username.clear()
    random_username = first_name + '.' + last_name + str(random.randint(100, 999))
    print(f'random_username: {random_username}')
    username.send_keys(random_username)
    time.sleep(1)

    password = driver_temp_email.find_element_by_id('password')
    password.clear()
    random_password = first_name + '.' + last_name + str(random.randint(100, 999))
    print(f'random_password: {random_password}')
    password.send_keys(random_username)
    time.sleep(1)

    create_butt = driver_temp_email.find_element_by_xpath("//span[@class='flex w-full rounded-md shadow-sm sm:col-start-2']")
    create_button = create_butt.find_element_by_xpath("//button[@type='button']")
    create_button.click()
    time.sleep(3)

    temp_email = driver_temp_email.find_element_by_id('address').click()
    time.sleep(1)
    
    win32clipboard.OpenClipboard()
    temp_email = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    print(f'temp_email: {temp_email}')

    df['Email'][ind] = temp_email

    driver = webdriver.Chrome()
    driver.get("https://sendmail.winwin.rs/winwin-rodjendan")
    # driver.maximize_window()
    print(driver.title)
    time.sleep(3)

    first_name_input = driver.find_element_by_id('mauticform_input_digitalprijavnaformawwrodjendansajt_ime')
    first_name_input.clear()
    first_name_input.send_keys(first_name)
    time.sleep(1)

    last_name_input = driver.find_element_by_id('mauticform_input_digitalprijavnaformawwrodjendansajt_prezime')
    last_name_input.clear()
    last_name_input.send_keys(last_name)
    time.sleep(1)

    city_input = driver.find_element_by_id('mauticform_input_digitalprijavnaformawwrodjendansajt_grad')
    city_input.clear()
    city_input.send_keys(city)
    time.sleep(1)
   
    email_input = driver.find_element_by_id('mauticform_input_digitalprijavnaformawwrodjendansajt_email')
    email_input.clear()
    email_input.send_keys(temp_email)
    time.sleep(1)
    
    phone_input = driver.find_element_by_id('mauticform_input_digitalprijavnaformawwrodjendansajt_broj_telefona')
    phone_input.clear()
    phone_input.send_keys(phone_number)
    time.sleep(1)

    sex_input = driver.find_element_by_id('mauticform_radiogrp_radio_pol1_m0')
    sex_input.click()
    time.sleep(1)

    checkbox1 = driver.find_element_by_id('mauticform_checkboxgrp_checkbox_prijavljujem_se_za_obaves_1')
    checkbox1.click()
    time.sleep(1)

    checkbox2 = driver.find_element_by_id('mauticform_checkboxgrp_checkbox_slazem_se_sa_winwin_polit_1')
    checkbox2.click()
    time.sleep(1)

    checkbox3 = driver.find_element_by_id('mauticform_checkboxgrp_checkbox_zelim_da_dobijam_obaveste_1')
    checkbox3.click()
    time.sleep(1)

    checkbox4 = driver.find_element_by_id('mauticform_checkboxgrp_checkbox_zelim_da_me_kontaktirate_1')
    checkbox4.click()
    time.sleep(1)

    sign_up = driver.find_element_by_id('mauticform_input_digitalprijavnaformawwrodjendansajt_submit')
    sign_up.click()
    time.sleep(1)

    # driver.close()

print(df)
df.to_excel(r'C:\Users\Martin\Desktop\Python\Automation\Users.xlsx', dtype=str)