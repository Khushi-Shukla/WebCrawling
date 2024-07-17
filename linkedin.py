# Using selenium

# imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from parsel import Selector
import time
import csv
import parameters

# # defining new variable passing two parameters
# writer = csv.writer(open("linkedin", 'wb'))

# # writerow() method to the write to the file object
# writer.writerow(['Name', 'Job Title', 'Company', 'College', 'Location', 'URL'])

with open(parameters.file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    # writerow() method to write to the file object
    writer.writerow(['Name', 'Job Title', 'Company', 'College', 'Location', 'URL'])


# Configuration
linkedin_username = 'tzw57355@tccho.com'
# faemlfpqvpnxrevjei@ckptr.com
linkedin_password = 'Abcd@1234'

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up ChromeDriver
driver = webdriver.Chrome()

# function to ensure all key data fields have a value
def validate_field(field):# if field is present pass 
    if field:pass
# if field is not present print text 
    else:
       field = 'No results'
    return field

def login_to_linkedin(username, password):
    driver.get('https://www.linkedin.com/login')
    time.sleep(5)  # Wait for the page to load

    # Find and fill the email field
    email_field = driver.find_element(By.ID, 'username')
    email_field.send_keys(username)

    # Find and fill the password field
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(password)

    # Submit the login form
    password_field.send_keys(Keys.RETURN)
    time.sleep(5)  # Wait for the login process to complete
    
    
def linkedinScraper(url):    
    driver.get(url)
    time.sleep(5)
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
    college = sel.xpath('//*[starts-with(@class, "zbVqLUrOFbAINNXOmmqyRHDofCKFHjSE inline-show-more-text--is-collapsed")]/text()').extract_first() 

    if college:
        college = college.strip()


    # xpath to extract the text from the class containing the location
    location = sel.xpath('//*[starts-with(@class, "text-body-small inline t-black--light break-words")]/text()').extract_first() 
    
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
    print('\n')
    print('Name: ' + name)
    print('Job Title: ' + job_title)
    print('Company: ' + company)
    print('College: ' + college)
    print('Location: ' + location)
    print('URL: ' + linkedin_url)
    print('\n')
    
    # writer.writerow([name.encode('utf-8'),job_title.encode('utf-8'),
    #                 company.encode('utf-8'),
    #                 college.encode('utf-8'),
    #                 location.encode('utf-8'),
    #                 linkedin_url.encode('utf-8')])

# Login to LinkedIn
login_to_linkedin(linkedin_username, linkedin_password)
linkedinScraper('https://uk.linkedin.com/in/pauljgarner')

# https://www.linkedin.com/in/arvindakshanrajesh
# https://uk.linkedin.com/in/pauljgarner
# https://www.linkedin.com/in/tawny-rodriguez
# terminates the application
driver.quit()