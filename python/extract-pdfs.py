import pandas as pd
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

metadata = pd.read_csv(r'Data\metadata.csv')

# Here, we're just importing both Beautiful Soup and the Requests library
page_link = "https://www.ncbi.nlm.nih.gov/pmc/"
# this is the url that we've already determined is safe and legal to scrape from.
page_response = requests.get(page_link, timeout=5)
# here, we fetch the content from the url, using the requests library
soup = BeautifulSoup(page_response.content, "html.parser")

PMC_papers = list(metadata[metadata.source_x=='PMC'].pmcid.values)
browser = webdriver.Chrome(r'chromedriver.exe')

chromeOptions = webdriver.ChromeOptions()
prefs = {"plugins.plugins_disabled" : ["Chrome PDF Viewer"],"plugins.always_open_pdf_externally": True, "download.default_directory" : "Data\Covid_papers\PCM_papers_scrapped"} # Here should be a list
download_dir = r'Data/Covid_papers/PCM_papers_scrapped'
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = r'chromedriver.exe'
download_driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)

def get_pdf_url(query):
    browser.get(page_link)
    sbox = browser.find_element_by_id("term")
    sbox.send_keys(query)
    submit = browser.find_element_by_id("search")
    submit.click()
    pdf_link = browser.find_element_by_xpath(u"//a[contains(text(), 'PDF')]")
    pdf_link.click()
    pdf_url = browser.current_url
    return pdf_url

def download_paper(pdf_url):  
    download_driver.get(pdf_url)
    #download_driver.close()
    return 1

dictNames = {}
for query in PMC_papers:
    
    print(query)
    pdf_url = ''
    try :
        pdf_url = get_pdf_url(query)
    except:
        print("couldn't find the url")
    try :
        download_paper(pdf_url)
    except:
        print("couldn't download the paper")
    
    dictNames[pdf_url.split('/')[-1]] = query
        