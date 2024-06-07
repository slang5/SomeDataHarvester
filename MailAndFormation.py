import pandas as pd
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,random

def remplace(string):
    result = string.replace('--', '-')
    result = result.replace(' ', '-')
    return result

def DriverAndOptions():
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-application-cache')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
    driver = webdriver.Edge()
    return [options, driver]

def Connection(userid,password,driver,UrlLoginPage):
    username = userid
    password = password

    driver.get(UrlLoginPage)
    actions = ActionChains(driver)
    actions.move_by_offset(10, 20).perform() 
    time.sleep(int(random.random()*3.3)+1)

    username_field = driver.find_element(By.ID,"username")
    password_field = driver.find_element(By.ID,"password")
    username_field.send_keys(f"{username}")
    password_field.send_keys(f"{password}")
    login_button = driver.find_element(By.NAME,"submitBtn")
    login_button.click()
    driver.execute_script("document.body.style.zoom='100%'")
    return 'OUGA'

def getMailAndFormation(IDformated,driver,URLBase):
    rand = 3 #possible de faire une un int() sur une variable aléatoire
    hauteur = driver.execute_script("return document.body.scrollHeight")/2
    driver.execute_script(f"window.scrollTo(0, {hauteur});")
    mail,formation = "NA","NA"

    if True:
        URL = URLBase+IDformated
        driver.get(URL)
        
        try:
            mail = WebDriverWait(driver,rand).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/a')))
            mail = mail.text

        except Exception as e:
            print(f"Get Mail : Une erreur s'est produite : {e}")
            mail = "NA"

        try:
            formation = WebDriverWait(driver,rand).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div[4]/div/a')))
            formation = formation.text

        except Exception as e:
            print(f"Get Formation : Une erreur s'est produite : {e}")
            formation = "NA"
    return mail, formation

def Collection(Matrice, id, pw,UrlLoginPage, URLBase):

    NomPrenomMail = []
    for i in range(0,len(Matrice)):
        nom, prenom = remplace(Matrice['Nom'][i]),remplace(Matrice['Prenom'][i])
        tmp = [f'{prenom}.{nom}@etu','0','0',nom, prenom]
        NomPrenomMail.append(tmp)


    [Options, Driver] = DriverAndOptions()
    Connection(id,pw,Driver,UrlLoginPage)


    for i in range(0,len(Matrice)):
        userEPI = NomPrenomMail[i][0]
        mail, formation = getMailAndFormation(userEPI,Driver,URLBase)
        NomPrenomMail[i][1],NomPrenomMail[i][2] = mail, formation
    time.sleep(4)
    Driver.quit()

    NomPrenomMail = pd.DataFrame(NomPrenomMail)
    NomPrenomMail.columns = ['UserURL','Mail',"Formation",'Nom','Prenom']
    NomPrenomMail.to_csv("Data.csv",sep=',')