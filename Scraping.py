from googledorking import google_dorking_email
from linkedin import gettingLinkedinData
from facebook import gettingScrapedData


email=input("Enter email: ")
urls=google_dorking_email(email)

facebook_urls = [url for url in urls if url.startswith("https://www.facebook.com")]

linkedin_urls = [url for url in urls if "linkedin.com/in/" in url and "/posts" not in url and "/pub" not in url]

print(linkedin_urls)
gettingLinkedinData(linkedin_urls)
gettingScrapedData(facebook_urls)
