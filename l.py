from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv
import requests

start_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser  = webdriver.Chrome("C:/Users/Jackson/OneDrive/Desktop/New folder (3)/chromedriver.exe")
browser.get(start_url)
time.sleep(10)
headers = ["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date","hyperlink","planet_type","planet_radius","orbital_radius","orbital_periot","eccentricity"]
planet_data = []

def scrape():
    for i in range(1,5):
        while True:
            time.sleep(2)
            soup = BeautifulSoup(browser.page_source, "html.parser")
            current_page_number = int(soup.find_all("input", attrs = {"class", "page_num"})[0].get("value"))
            if current_page_number < i:
                browser.find_element(By.XPATH, value = '//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a')
            elif current_page_number > i:
                browser.find_element(By.XPATH, value = '//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[1]/a')
            else:
                break
        for ul_tag in soup.find_all("ul",attrs = {"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            hyperlink_li_tag = li_tags[0]
            temp_list.append("https://exoplanets.nasa.gov"+hyperlink_li_tag.find_all("a", href = True)[0]["href"])
            planet_data.append(temp_list)
        browser.find_element(By.XPATH, value = '//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a')
        print(f"page {i} scarping completed")

   # with open("scarper.csv", "w") as f:
    #    writer = csv.writer(f)
     #   writer.writerow(headers)
      #  writer.writerows(planet_data)
scrape()
new_planet_data = []
def scarpe_more_data(hyperlink):
    try: 
        page = requests.get(hyperlink)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        temp_list = []
        for tr_tag in soup.find_all("tr",attrs = {"class" : "fact_row"}):
            td_tags = tr_tag.find_all("td")
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div", attrs = {"class" : "value"})[0].contents[0])
                except:
                    temp_list.append("")
        new_planet_data.append[temp_list]
    except:
        time.sleep(1)
        scarpe_more_data(hyperlink)
for index, data in enumerate(planet_data):
    scarpe_more_data(data[5]) 
    print(f"scraping at hyperlink {index+1} is completed.")
print(new_planet_data[0:10])
final_planet_data = []
for index, data in enumerate(planet_data):
     new_planet_data_element = new_planet_data[index]
     new_planet_data_element = [elem.replace("\n", "") for elem in new_planet_data_element]
     new_planet_data_element = new_planet_data_element[:7] 
     final_planet_data.append(data + new_planet_data_element) 
with open("scraper1.csv", "w") as f: 
    csvwriter = csv.writer(f) 
    csvwriter.writerow(headers) 
    csvwriter.writerows(final_planet_data)

