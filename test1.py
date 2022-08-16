from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Hier wird der Pfad zu ChromeDrive festgelegt
path = "/Users/ramin/Desktop/chromedriver"
#Hier wird die Sucheingabe festgelegt. Man kann individuell in die Console einen Suchbegriff eingeben
sucheingabe = input("Bitte Suchbegriff eingeben")   
x = sucheingabe.split(", ")

#Danach öffnet sich Chrome
webbrowser = webdriver.Chrome(path)    
#Google Adresse wird geöffnet    
          
aufruf_google = webbrowser.get("https://www.google.com/")   
# hier wird in der HTML nach dem Button gesucht, bei dem man zustimmen muss, um Google zu nutzen 
zustimmen_button = webbrowser.find_element(By.ID, "L2AGLb")  
#Der Button wird angeklickt
zustimmen_button.click()    
#Das Suchfeld aus Google wird gesucht bzw identifiziert
for i in range(len(x)):                               
    suchfeld = webbrowser.find_element(By.NAME,'q')   
    #Die Sucheingabe von davor wird in Google eingegeben  
    suchfeld.send_keys(x[i])
    #Die Sucheingabe wird abgeschickt
    suchfeld.submit()          
    #Es wird nach den ersten Treffern gesucht       
    ergebnis = webbrowser.find_element(By.CSS_SELECTOR, 'div.g')
    #Hier wird der erste Link gefunden
    link = ergebnis.find_element(By.TAG_NAME, 'a')
    #aus diesem wird der URL Link und der Titel identifiziert
    href = link.get_attribute('href')
    titel = link.find_element(By.XPATH,'//h3[@class="LC20lb MBeuO DKV0Md"]')
    #Das Ergebnis wird geprintet bzw angezeigt
    print(titel.text)      
    print(href)      
    aufruf_google = webbrowser.get("https://www.google.com/")   
    #Browser wird geschlossen
webbrowser.quit()

