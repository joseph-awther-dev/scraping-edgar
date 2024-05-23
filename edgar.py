from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# Set up the WebDriver (make sure to specify the path to your WebDriver executable)
driver = webdriver.Chrome()

driver.get('https://www.filermanagement.edgarfiling.sec.gov/Welcome/EDGARLogin.htm')

# Find the username and password input fields and the login button
username_field = driver.find_element(By.NAME, 'CIK')  # Update 'username' if the name attribute is different
password_field = driver.find_element(By.NAME, 'Password')  # Update 'password' if the name attribute is different
login_button = driver.find_element(By.NAME, 'Logon')  # Update 'login' if the name attribute is different

# # Enter your username and password
username_field.send_keys('0002016449')
password_field.send_keys('uea$3wsgtdak')

# # Click the login button
login_button.click()

driver.get('https://www.filermanagement.edgarfiling.sec.gov/faces/eis/ChooseForm.xhtml')

dropdown_type_form = Select(driver.find_element(By.ID, 'form:formType'))
dropdown_type_form.select_by_visible_text('8-K')



go_to_form = driver.find_element(By.NAME, 'form:submitButton')
go_to_form.click()




items_list = ['1.01',
                '1.02',
                '1.03',
                '1.04',
                '1.05',
                '2.01',
                '2.02',
                '2.03',
                '2.04',
                '2.05',
                '2.06',
                '3.01',
                '3.02',
                '3.03',
                '3.04',
                '4.01',
                '4.02',
                '5.01', 
                '5.02', 
                '5.03', 
                '5.04', 
                '5.05', 
                '5.06', 
                '5.07', 
                '5.08', 
                '6.01', 
                '6.02', 
                '6.03', 
                '6.04', 
                '6.05', 
                '6.06', 
                '7.01', 
                '8.01', 
                '9.01']
# items_list = ['1.01']
list_changes = []

for item in items_list:
  time.sleep(5)
  list_Item_submission_type = ['425', 'DEFA14A', 'DFAN14A', 'SC TO-C']
  
  if item in ['1.01', '1.02', '2.01', '5.01', '8.01']:
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
      # print(item_sub == 'DFAN14A')
      # print(item_sub, '== DFAN14A')
      try:
        dropdown_Item_submission_type.select_by_visible_text(item_sub)
      except:
        list_changes.append({
            "Item": item,
            "Item_submission_type": item_sub,
            "Filer_Information": {
              "Form": {
                "CIK": True,
                "CCC": True,
                "Depositor_CIK": False,
                "Sponsor_CIK": False,
              },
              "Subject Company": False,
              "Group_Members": False,
              "Fiscal": False,
              "ABS_Asset_Class": False,
              "Emerging_Growth_Company": False,
              "Depositor 33 File_Number": False
            }
        })
        # driver.refresh()
      # print("No Item_submission_type")
        continue
      # 
      
    # if item in ['1.01', '1.02', '2.01', '5.01', '8.01']:
      test_click = driver.find_element(By.XPATH, '//*[@id="form:coregItems_table:0:j_id238"]')
      test_click.click()
      time.sleep(3)
      html = driver.page_source
      soup = BeautifulSoup(html)
      time.sleep(3)
      # if :
      print(item)
      if item_sub == '425':
        print('a')
        if soup.find(id="form:subjectCompany") and soup.find(id="form:subjcompCik_lbl") and soup.find(id="form:subjcompFileNum") and soup.find(id="form:subjcompName") and soup.find(id="form:groupMembers"):
            print('b')
            list_changes.append({
              "Item": item,
              "Item_submission_type": item_sub,
              "Filer_Information": {
                "Form": {
                  "CIK": True,
                  "CCC": True,
                  "Depositor_CIK": False,
                  "Sponsor_CIK": False,
                },
                "Subject Company": {
                  "CIK": True,
                  "File_Number": True,
                  "Name": True
                },
                "Group_Members": True,
                "Fiscal": False,
                "ABS_Asset_Class": False,
                "Emerging_Growth_Company": False,
                "Depositor 33 File_Number": False
              }
            })

      elif item_sub in ['DFAN14A', 'SC TO-C']:
          print('c')
          if soup.find(id="form:subjcompCik") and soup.find(id="form:scIrsNumber") and soup.find(id="form:subjcompName") and soup.find(id="form:groupMembers"):
            print('d')
            list_changes.append({
                "Item": item,
                "Item_submission_type": item_sub,
                "Filer_Information": {
                    "Form": {
                    "CIK": True,
                    "CCC": True,
                    "Depositor_CIK": False,
                    "Sponsor_CIK": False,
                  },
                  "Subject Company": {
                    "CIK": True,
                    "IRS Number": True,
                    "Name": True
                  },
                  "Group_Members": True,
                  "Fiscal": False,
                  "ABS_Asset_Class": False,
                  "Emerging_Growth_Company": False,
                  "Depositor 33 File_Number": False
                }
              })
          elif soup.find(id="form:subjcompCik") and soup.find(id="form:scIrsNumber") and soup.find(id="form:subjcompName"):
            list_changes.append({
              "Item": item,
              "Item_submission_type": item_sub,
              "Filer_Information": {
                "Form": {
                  "CIK": True,
                  "CCC": True,
                  "Depositor_CIK": False,
                  "Sponsor_CIK": False,
                },
                "Subject Company": {
                  "CIK": True,
                  "IRS Number": True,
                  "Name": True
                },
                "Group_Members": False,
                "Fiscal": False,
                "ABS_Asset_Class": False,
                "Emerging_Growth_Company": False,
                "Depositor 33 File_Number": False
              }
            }) 
  elif item == '5.03':
         print('e')
         if soup.find(id="form:fiscalYear"):
           print(f)
           list_changes.append({
              "Item": item,
              "Item_submission_type": item_sub,
              "Filer_Information": {
                "Form": {
                  "CIK": True,
                  "CCC": True,
                  "Depositor_CIK": False,
                  "Sponsor_CIK": False,
                },
                "Subject Company": False,
                "Group_Members": False,
                "Fiscal": True,
                "ABS_Asset_Class": False,
                "Emerging_Growth_Company": False,
                "Depositor 33 File_Number": False
              }
            }) 
  elif item in ['6.01', '6.02', '6.03', '6.04', '6.05', '6.06']:
        if soup.find(id='form:depositorCikSic') and soup.find(id='form:sponsorCikSic') and soup.find(id='form:assetClass') and soup.find(id='form:eGCompany'):
          if item == '6.01':
            if soup.find(id='form:assetClassGroup'):
              if soup.find(id='form:depositor33FileNumSic'):
                list_changes.append({
                  "Item": item,
                  "Item_submission_type": item_sub,
                  "Form": {
                    "CIK": True,
                    "CCC": True,
                    "Depositor_CIK": True,
                    "Sponsor_CIK": True,
                  },
                  "Subject Company": False,
                  "Group_Members": False,
                  "Fiscal": False,
                  "ABS_Asset_Class": True,
                  "Emerging_Growth_Company": True,
                  "Depositor 33 File_Number": True
                })
            else:
                list_changes.append({
                  "Item": item,
                  "Item_submission_type": item_sub,
                  "Form": {
                    "CIK": True,
                    "CCC": True,
                    "Depositor_CIK": True,
                    "Sponsor_CIK": True,
                  },
                  "Subject Company": False,
                  "Group_Members": False,
                  "Fiscal": False,
                  "ABS_Asset_Class": True,
                  "Emerging_Growth_Company": True,
                  "Depositor 33 File_Number": False
                })

  else:
        list_changes.append({
            "Item": item,
            "Item_submission_type": item_sub,
            "Filer_Information": {
              "Form": {
                "CIK": True,
                "CCC": True,
                "Depositor_CIK": False,
                "Sponsor_CIK": False,
              },
              "Subject Company": False,
              "Group_Members": False,
              "Fiscal": False,
              "ABS_Asset_Class": False,
              "Emerging_Growth_Company": False,
              "Depositor 33 File_Number": False
            }
        })
        # elif soup.find(id="form:subjectCompany") and soup.find(id="form:subjcompCik") and soup.find(id="form:scIrsNumber") and soup.find(id="form:subjcompName"):
        #   list_changes.append({
        #       "Item": item,
        #       "Item_submission_type": item_sub,
        #       "Subject Company": {
        #         "CIK": True,
        #         "IRS Number": True,
        #         "Name": True
        #       },
        #       "Group_Members": True
        #     })

        # else: 
        #   list_changes.append({
        #     "Item": item,
        #     "Item_submission_type": item_sub,
        #     "Subject Company": False,
        #     "Group_Members": True
        #   })
      # else:
      #   
      #     else: 
      #       list_changes.append({
      #         "Item": item,
      #         "Item_submission_type": False,
      #         "Subject Company": False,
      #         "Group_Members": False
      #       })
      #   else:
      #     list_changes.append({
      #         "Item": item,
      #         "Item_submission_type": False,
      #         "Subject Company": False,
      #         "Group_Members": False
      #       })
  # else:
  #   continue
   
  driver.refresh()
  time.sleep(5)  
  
driver.quit()
print(list_changes)
