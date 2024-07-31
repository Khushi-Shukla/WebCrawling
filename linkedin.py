# Using selenium

# imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from parsel import Selector
import time
import csv
import random
import pickle
import subprocess

# def changeIP():
    
#     # Define the new IP address, subnet mask, and gateway
#     new_ip = "192.168.1."+str(random.randint(3,100))
#     subnet_mask = "255.255.255.0"
#     gateway = "192.168.1.1"
#     interface = "Wi-Fi"  # The name of the network interface you want to change

#     # Construct the netsh command
#     command = f"netsh interface ip set address name={interface} static {new_ip} {subnet_mask} {gateway}"

#     # Run the command
#     result = subprocess.run(command, shell=True, capture_output=True, text=True)

#     # Check the result
#     if result.returncode == 0:
#         print("IP address changed successfully to: ", new_ip)
#     else:
#         print("Failed to change IP address.")
#         print(result.stderr)
        

with open('linkedin_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        'Name', 'Job Title', 'Company', 'College', 'Location', 'URL'
    ])


# Configuration
linkedin_username = 'tzw57355@tccho.com'
# 'tzw57355@tccho.com' 'vBAEqMvPYfSG27!'
linkedin_password = 'vBAEqMvPYfSG27!'
# 'faemlfpqvpnxrevjei@ckptr.com' 'Abcd@1234'


def get_fake_user_agent():
    ua = UserAgent()
    return ua.random

# Set up Chrome options
# chrome_options = Options()
# # chrome_options.add_argument("--headless")  # Run in headless mode
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument(f"user-agent={get_fake_user_agent()}")    
# service = Service(ChromeDriverManager().install())
# chrome_options.add_argument("--disable-gpu") 
# chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
# # Set up ChromeDriver
# # driver = webdriver.Chrome()
# driver = webdriver.Chrome(service=service, options=chrome_options)


# Set up Chrome options
driver = None
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument(f"user-agent={get_fake_user_agent()}")    
chrome_options.add_argument("--disable-gpu") 
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome()
driver = webdriver.Chrome(service=service, options=chrome_options)


def main():
    urls = [
        # 'https://in.linkedin.com/in/rajeshpremchandran', 
        # 'https://in.linkedin.com/in/rajesh-uppalapati-1368a91', 
        # 'https://in.linkedin.com/in/rajeshshah910', 
        # 'https://in.linkedin.com/in/rajeshrajgor', 
        # 'https://www.linkedin.com/in/rajeshahuja12', 
        # 'https://in.linkedin.com/in/thyagar'
    ]
    
    # gettingLinkedinData(urls)

# function to ensure all key data fields have a value
def validate_field(field):# if field is present pass 
    if field:pass
    else:
       field = 'No results'
    return field

def login_to_linkedin(username, password):
    global driver
    driver.get('https://www.linkedin.com/login')
    time.sleep(random.uniform(3,6))  # Wait for the page to load

    # Find and fill the email field
    email_field = driver.find_element(By.ID, 'username')
    email_field.send_keys(username)

    # Find and fill the password field
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(password)

    # Submit the login form
    password_field.send_keys(Keys.RETURN)
    time.sleep(random.uniform(3,6))  # Wait for the page to load
    # Wait for the login process to complete
    
    # Save cookies to a file
    with open("cookies.pkl", "wb") as cookies_file:
        pickle.dump(driver.get_cookies(), cookies_file)

def load_cookies(driver):
    with open("cookies.pkl", "rb") as cookies_file:
        cookies = pickle.load(cookies_file)
        for cookie in cookies:
            driver.add_cookie(cookie)


# login_to_linkedin(linkedin_username, linkedin_password)
# load_cookies(driver) 


def linkedinScraper(username):   
    global driver
    url = "https://uk.linkedin.com/in/"+username
    driver.get(url)
    time.sleep(random.uniform(3,6))  # Wait for the page to load
    
    # Reload the page to ensure cookies are used
    driver.refresh()
    time.sleep(random.uniform(3, 6))  # Wait for the page to load
    
    # assigning the source code for the webpage to variable sel
    sel = Selector(text=driver.page_source) 
    # xpath to extract the text from the class containing the name
    name = sel.xpath('//*[starts-with(@class, "top-card-layout__title font-sans")]/text()').extract_first() 
    

    if name:
        name = name.strip()


    # xpath to extract the text from the class containing the job title
    job_title = sel.xpath('//*[starts-with(@class, "top-card-layout__headline")]/text()').extract_first() #or ''
    

    if job_title:
        job_title = job_title.strip()


    # xpath to extract the text from the class containing the company
    company = sel.xpath('//*[starts-with(@class, "top-card-link__description line-clamp-2")]/text()').extract_first() 
    

    if company:
        company = company.strip()


    # xpath to extract the text from the class containing the college
    college = sel.xpath('//div[@data-section="educationsDetails"]//a//span[@class="top-card-link__description line-clamp-2"]/text()').extract_first()
     
   

    if college:
        college = college.strip()


    # xpath to extract the text from the class containing the location
    location = sel.xpath('//div[@class="not-first-middot"]/span[1]/text()').extract_first() 
    
    if location:
        location = location.strip()
    linkedin_url = driver.current_url
    
    # validating if the fields exist on the profile
    name = validate_field(name)
    job_title = validate_field(job_title)
    company = validate_field(company)
    college = validate_field(college)
    location = validate_field(location)
    linkedin_url = validate_field(linkedin_url)
    
    # printing the output to the terminal
    # print('\n')
    # print('Name: ' + name)
    # print('Job Title: ' + job_title)
    # print('Company: ' + company)
    # print('College: ' + college)
    # print('Location: ' + location)
    # print('URL: ' + linkedin_url)
    # print('\n')    
    
        
    data = {
        'Name': name,
        'Job Title': job_title,
        'Company': company,
        'College': college,
        'Location': location,
        'URL': linkedin_url
    }
    
    with open('linkedin_data.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([name,job_title, company, college, location, linkedin_url])
    
    print('\nScraped data:')
    for key, value in data.items():
        print(f'{key}: {value}')
    
    print(type(data), " --Info type")
    return data

          
def extractingUsername(linkedin_urls):
    linkedin_usernames = []
    for url in linkedin_urls:
        # Extract username from LinkedIn URL
        if "/in/" in url:
            username = url.split("/in/")[1].split("/")[0]
            linkedin_usernames.append(username)
        elif "/pub/dir/" in url:
            username = url.split("/pub/dir/")[1].split("/")[0]
            linkedin_usernames.append(username)
        
    return linkedin_usernames

def allGood(info):
    #checks if not all the values have no result
    if all(value == 'No results' for key, value in info.items() if key != 'URL'):
        # login_to_linkedin(linkedin_username, linkedin_password)
        # load_cookies(driver)
        return False
    return True

def gettingLinkedinData(urls):
    global driver    
    if driver:
        try:  
            # changeIP()      
            # Login to LinkedIn
            login_to_linkedin(linkedin_username, linkedin_password)
            load_cookies(driver) 
            linkedinInfo = []
            print("Inside linkedin scrapper")
            users=[]
            users = extractingUsername(urls)
            print(users)

            for user in users:
                print(f'---------Extracting info of {user}:---------')
                print(type(linkedinInfo), " linkddd ", type(users) )
                info=linkedinScraper(user)
                if(not allGood(info)): 
                    time.sleep(10)                
                if info and allGood(info): 
                    linkedinInfo.append(info)
                else:
                    print("Data not returned properly")
                time.sleep(random.uniform(5,10))  # Wait for the page to load
            return linkedinInfo
        except Exception as e:
            print(f"Error during data scraping: {e}")
            return None
        finally:
            driver.quit()
                        
    else:
        return "Failed to initialize WebDriver"



if __name__ == "__main__":
    main()
    
    
# gettingLinkedinData([ 'https://in.linkedin.com/in/rajesh-ramakrishnan-2bb33b22', 'https://www.linkedin.com/in/arvindakshanrajesh', 'https://uk.linkedin.com/in/pauljgarner' , 'https://www.linkedin.com/in/tawny-rodriguez'])

# https://www.linkedin.com/in/arvindakshanrajesh
# https://uk.linkedin.com/in/pauljgarner
# https://www.linkedin.com/in/tawny-rodriguez
# terminates the application
# driver.quit()


# OBSERVATIONS
# 1. Scrapped data even while password was incorrect
# 2. inspect element different for urls starting with uk and www
# 3. unable to scrape urls starting with www
# 4. Repeated requests results in no scrapping 
    # Output
    # Name: No results
    # Job Title: No results
    # Company: No results
    # College: No results
    # Location: No results
    # URL: https://www.linkedin.com/authwall?trk=qf&original_referer=&sessionRedirect=https%3A%2F%2Fuk.linkedin.com%2Fin%2Farvindakshanrajesh    



