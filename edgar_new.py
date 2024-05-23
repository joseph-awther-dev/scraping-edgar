
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def login_to_website(username, password):
    driver = webdriver.Chrome()
    driver.get('https://www.filermanagement.edgarfiling.sec.gov/Welcome/EDGARLogin.htm')
    username_field = driver.find_element(By.NAME, 'CIK')
    password_field = driver.find_element(By.NAME, 'Password')
    login_button = driver.find_element(By.NAME, 'Logon')
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    return driver

def select_form(driver, form_text):
    driver.get('https://www.filermanagement.edgarfiling.sec.gov/faces/eis/ChooseForm.xhtml')
    dropdown_type_form = Select(driver.find_element(By.ID, 'form:formType'))
    dropdown_type_form.select_by_visible_text(form_text)
    go_to_form = driver.find_element(By.NAME, 'form:submitButton')
    go_to_form.click()


def main():
    username = '0002016449'
    password = 'uea$3wsgtdak'
    items_list = ['1.01', '1.02', '1.03', '1.04', '1.05', '2.01', '2.02', '2.03', '2.04', '2.05', '2.06', '3.01', '3.02', '3.03', '3.04', '4.01', '4.02', '5.01', '5.02', '5.03', '5.04', '5.05', '5.06', '5.07', '5.08', '6.01', '6.02', '6.03', '6.04', '6.05', '6.06', '7.01', '8.01', '9.01']
    # items_list = ['1.01', '1.02', '2.01', '5.01', '8.01']
    list_changes = []

    driver = login_to_website(username, password)
    
    list_Item_submission_type = ['425', 'DEFA14A', 'DFAN14A', 'SC TO-C']
    for item in items_list:
      select_form(driver, '8-K')
      time.sleep(5)
      dropdown_item = driver.find_element(By.ID, 'form:coregItems_table:0:coRegItem')
        # dropdown_item.clear()
      dropdown_item.send_keys(item)

      test_click = driver.find_element(By.XPATH, '//*[@id="form:coregItems_table:0:j_id238"]')
      test_click.click()
      time.sleep(3)
      
      try:
        dropdown_Item_submission_type = Select(driver.find_element(By.ID, 'form:submissionType'))
      except:
        driver.refresh()
          # print("No Item_submission_type")
          # continue
            
      for item_sub in list_Item_submission_type:
          form_info = {
            "Item": item,
            "Item_submission_type": "",
            "Filer_Information": {
               "Form": False
            },
            # "Filer_Information": {
            #     "Form": {
            #       "CIK": True,
            #       "CCC": True,
            #       "Depositor_CIK": False,
            #       "Sponsor_CIK": False,
            #     }
            # },
            "Subject_Company": False,
            "Group_Members": False,
            "Fiscal": False,
            "ABS_Asset_Class": False,
            "Emerging_Growth_Company": False,
            "Depositor_33_File_Number": False
          }
          # print(form_info)
          try:
            dropdown_Item_submission_type.select_by_visible_text(item_sub)
          except:
            list_changes.append(form_info)
            continue
          
          

          test_click = driver.find_element(By.XPATH, '//*[@id="form:coregItems_table:0:j_id238"]')
          test_click.click()
          time.sleep(6)
          html = driver.page_source
          soup = BeautifulSoup(html)
          if item in ['1.01', '1.02', '2.01', '5.01', '8.01']:
              print(item)
              print(item_sub)
              print('group a')
              time.sleep(3)
              if item_sub == '425':
                  if soup.find(id="form:subjcompCik") and soup.find(id="form:subjcompFileNum") and soup.find(id="form:subjcompName") and soup.find(id="form:group_table:0:group"):
                # if soup.find(id="form:subjectCompany") and soup.find(id="form:subjcompCik_lbl") and soup.find(id="form:subjcompFileNum") and soup.find(id="form:subjcompName") and soup.find(id="form:groupMembers"):
                    # form_info["Item_submission_type"] = item_sub
                    form_info["Item_submission_type"] = item_sub
                    form_info["Filer_Information"]["Form"] = {
                      "CIK": True,
                      "CCC": True,
                      "Depositor_CIK": False,
                      "Sponsor_CIK": False,
                    }
                    form_info["Subject_Company"] = {
                        "CIK": True,
                        "File_Number": True,
                        "Name": True
                    }
                    form_info["Group_Members"] = True
                    list_changes.append(form_info)
              elif item_sub in ['DFAN14A', 'SC TO-C']:
                  print(item)
                  print(item_sub)
                  if soup.find(id="form:subjcompCik") and soup.find(id="form:scIrsNumber") and soup.find(id="form:subjcompName") and soup.find(id="form:groupMembers"):
                    form_info["Item_submission_type"] = item_sub
                    form_info["Filer_Information"]["Form"] = {
                          "CIK": True,
                          "CCC": True,
                          "Depositor_CIK": False,
                          "Sponsor_CIK": False,
                        }
                    form_info["Subject_Company"] = {
                        "CIK": True,
                        "IRS_Number": True,
                        "Name": True
                    }
                    form_info["Group_Members"] = True
                    list_changes.append(form_info)
                  
                  elif soup.find(id="form:subjcompCik") and soup.find(id="form:scIrsNumber") and soup.find(id="form:subjcompName"):
                    form_info["Item_submission_type"] = item_sub
                    form_info["Filer_Information"]["Form"] = {
                          "CIK": True,
                          "CCC": True,
                          "Depositor_CIK": False,
                          "Sponsor_CIK": False,
                        }
                    form_info["Subject_Company"] = {
                        "CIK": True,
                        "IRS_Number": True,
                        "Name": True
                    }
                    list_changes.append(form_info)
              elif item_sub == "DEFA14A": 
                  form_info["Item_submission_type"] = item_sub
                  form_info["Filer_Information"]["Form"] = {
                          "CIK": True,
                          "CCC": True,
                          "Depositor_CIK": False,
                          "Sponsor_CIK": False,
                        }
                  list_changes.append(form_info)

          elif item == '5.03':
            print(item)
            print(item_sub)
            print('group b')
            if soup.find(id="form:fiscalYear"):
                  form_info["Item_submission_type"] = item_sub
                  form_info["Filer_Information"]["Form"] = {
                          "CIK": True,
                          "CCC": True,
                          "Depositor_CIK": False,
                          "Sponsor_CIK": False,
                        }
                  form_info["Fiscal"] = True
                  list_changes.append(form_info)
              
          elif item in ['6.01', '6.02', '6.03', '6.04', '6.05', '6.06']:
                print(item)
                print(item_sub)
                print('group c')
                if soup.find(id='form:depositorCikSic') and soup.find(id='form:sponsorCikSic') and soup.find(id='form:assetClass') and soup.find(id='form:eGCompany'):
                  if item == '6.01':
                    if soup.find(id='form:assetClassGroup'):
                      if soup.find(id='form:depositor33FileNumSic'):
                        form_info["Item_submission_type"] = item_sub
                        form_info["Filer_Information"]["Form"] = {
                          "CIK": True,
                          "CCC": True,
                          "Depositor_CIK": True,
                          "Sponsor_CIK": True,
                        }
                        # form_info["Form"] = {
                        #     "CIK": True,
                        #     "CCC": True,
                        #     "Depositor_CIK": True,
                        #     "Sponsor_CIK": True,
                        #   }
                        form_info["ABS_Asset_Class"] = True,
                        form_info["Emerging_Growth_Company"] = True,
                        form_info["Depositor 33 File_Number"] = True
                        list_changes.append(form_info)
          
                    else:
                      form_info["Item_submission_type"] = item_sub
                      form_info["Filer_Information"]["Form"] = {
                            "CIK": True,
                            "CCC": True,
                            "Depositor_CIK": True,
                            "Sponsor_CIK": True,
                          }
                      form_info["ABS_Asset_Class"] = True,
                      form_info["Emerging_Growth_Company"] = True,
                      list_changes.append(form_info)
          elif item in ['1.03', '1.04', '1.05', '2.02', '2.03', '2.04', '2.05', '2.06', '3.01', '3.02', '3.03', '3.04', '4.01', '4.02', '5.04', '5.05', '5.06', '5.07', '5.08', '9.01']:
              print(item)
              print(item_sub)
              list_changes.append(form_info) 
      # print(list_changes)
    driver.quit()
    print(list_changes)

if __name__ == "__main__":
    main()

