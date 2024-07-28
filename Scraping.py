from googledorking import google_dorking_email
from linkedin import gettingLinkedinData
from facebook import gettingScrapedData
from instagram import getInstaInfo

# email=input("Enter email: ")
def Scraping(email, contact_type):
    data=[]
    # urls=google_dorking_email(email)

    # facebook_urls = [url for url in urls if url.startswith("https://www.facebook.com")]

    # linkedin_urls = [url for url in urls if "linkedin.com/in/" in url and "/posts" not in url and "/pub" not in url]
    # print(linkedin_urls)
    # gettingLinkedinData(linkedin_urls)
    # gettingScrapedData(facebook_urls)
    
    print("Hi this is test")
    if(contact_type=='email'):
        urls=google_dorking_email(email)
        facebook_urls = [url for url in urls if url.startswith("https://www.facebook.com")]
        
        insta_urls = [url for url in urls if url.startswith("https://www.instagram.com")]
        

        linkedin_urls = [url for url in urls if "linkedin.com/in/" in url and "/posts" not in url and "/pub" not in url]

        linkedindata=gettingLinkedinData(linkedin_urls)
        fbdata=gettingScrapedData(facebook_urls)
        instadata=getInstaInfo(insta_urls)
        data.append(linkedindata)
        data.append(fbdata)
        data.append(instadata)
        
        print("The data is : ",data)
        return data

# print(linkedin_urls)
# gettingLinkedinData(linkedin_urls)
# gettingScrapedData(facebook_urls)
