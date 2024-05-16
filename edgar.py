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




items_list = ['1.01', '1.02', '1.03', '1.04', '1.05' ,'2.01' ,'2.02' ,'2.03' ,'2.04' ,'2.05', '2.06', '3.01', '3.02', '3.03' ,'3.04', '4.01', '4.02' ,'5.01', '5.02', '5.03', '5.04', '5.05', '5.06', '5.07', '5.08', '6.01', '6.02', '6.03', '6.04', '6.05', '6.06', '7.01', '8.01', '9.01']
# items_list = ['1.01']
list_changes = []

for item in items_list:
  time.sleep(5)
  dropdown_item = driver.find_element(By.ID, 'form:coregItems_table:0:coRegItem')
  # dropdown_item.clear()
  dropdown_item.send_keys(item)

  test_click = driver.find_element(By.XPATH, '//*[@id="form:coregItems_table:0:j_id238"]')
  test_click.click()

  list_item_submission_type = ['425', 'DEFA14A', 'DFAN14A', 'SC TO-C']
  time.sleep(3)
  try:
    dropdown_item_submission_type = Select(driver.find_element(By.ID, 'form:submissionType'))
  except:
     driver.refresh()
    # print("No Item Submission Type")
    # continue
       
  for item_sub in list_item_submission_type:
    try:
      dropdown_item_submission_type.select_by_visible_text(item_sub)
    except:
      list_changes.append({
          "item": item,
          "item Submission Type": item_sub,
          "Subject Company": False,
          "Group Members": False
      })
      # driver.refresh()
    # print("No Item Submission Type")
      continue
    # 

    test_click = driver.find_element(By.XPATH, '//*[@id="form:coregItems_table:0:j_id238"]')
    test_click.click()
    time.sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html)
    time.sleep(3)
    if soup.find(id="form:groupMembers"):
      if soup.find(id="form:subjectCompany") and soup.find(id="form:subjcompCik_lbl") and soup.find(id="form:subjcompFileNum") and soup.find(id="form:subjcompName"):
          list_changes.append({
            "item": item,
            "item Submission Type": item_sub,
            "Subject Company": {
              "CIK": True,
              "FILE Number": True,
              "Name": True
            },
            "Group Members": True
          })
      elif soup.find(id="form:subjectCompany") and soup.find(id="form:subjcompCik") and soup.find(id="form:scIrsNumber") and soup.find(id="form:subjcompName"):
        list_changes.append({
            "item": item,
            "item Submission Type": item_sub,
            "Subject Company": {
              "CIK": True,
              "IRS Number": True,
              "Name": True
            },
            "Group Members": True
          })

      else: 
        list_changes.append({
          "item": item,
          "item Submission Type": item_sub,
          "Subject Company": False,
          "Group Members": True
        })
    else:
      if soup.find(id="form:subjectCompany"):
        if soup.find(id="form:subjcompCik_lbl") and soup.find(id="form:subjcompFileNum") and soup.find(id="form:subjcompName"):
          list_changes.append({
            "item": item,
            "item Submission Type": item_sub,
            "Subject Company": {
              "CIK": True,
              "FILE Number": True,
              "Name": True
            },
            "Group Members": False
          })
        elif soup.find(id="form:subjectCompany") and soup.find(id="form:subjcompCik") and soup.find(id="form:scIrsNumber") and soup.find(id="form:subjcompName"):
          list_changes.append({
              "item": item,
              "item Submission Type": item_sub,
              "Subject Company": {
                "CIK": True,
                "IRS Number": True,
                "Name": True
              },
              "Group Members": True
            })
        else: 
          list_changes.append({
            "item": item,
            "item Submission Type": False,
            "Subject Company": False,
            "Group Members": False
          })
      else:
        list_changes.append({
            "item": item,
            "item Submission Type": False,
            "Subject Company": False,
            "Group Members": False
          })
    #     if soup.find(id="form:groupMembers"):
    #       if soup.find(id="form:subjcompCik_lbl") and soup.find(id="form:subjcompFileNum") and soup.find(id="form:subjcompName"):
    #         list_changes.append({
    #           "item": item,
    #           "item Submission Type": item_sub,
    #           "Subject Company": {
    #              "CIK": True,
    #              "FILE Number": True,
    #              "Name": True
    #           },
    #           "Group Members": True
    #         })
    #       else:
    #          list_changes.append({
    #           "item": item,
    #           "item Submission Type": item_sub,
    #           "Subject Company": False,
    #           "Group Members": True
    #         })
    #     else:
    #        list_changes.append({
    #           "item": item,
    #           "item Submission Type": item_sub,
    #           "Subject Company": False,
    #           "Group Members": False
    #         })
    # else:
    #     list_changes.append({
    #       "item": item,
    #       "item Submission Type": False,
    #       "Subject Company": False,
    #       "Group Members": False
    #     })
   
  driver.refresh()
  time.sleep(5)  
  
driver.quit()
print(list_changes)
