from googledorking import google_dorking_email
from linkedin import gettingLinkedinData
from facebook import gettingScrapedData
from instagram import getInstaInfo
import phoneNum
import trial

phonelookupURL = "www.truecaller.com/search/in/"


# email=input("Enter email: ")
def Scraping(inp, contact_type):
    data=[]
    phonedata=[]
    print("Hi this is test")
    if(contact_type=='email'):
        # data.append(inp)
        urls=google_dorking_email(inp)
        facebook_urls = [url for url in urls if url.startswith("https://www.facebook.com")]
        
        insta_urls = [url for url in urls if url.startswith("https://www.instagram.com")]
        

        linkedin_urls = [url for url in urls if "linkedin.com/in/" in url and "/posts" not in url and "/pub" not in url]

        linkedindata=gettingLinkedinData(linkedin_urls)
        fbdata=gettingScrapedData(facebook_urls)
        instadata=getInstaInfo(insta_urls)
        data.append(linkedindata)
        data.append(fbdata)
        data.append(instadata)
        
    elif(contact_type=='phone'):
        print("Into the phonenum")
        phoneNumDetails = phoneNum.number_lookup(inp)
        phonedata.append(phoneNumDetails)
        print(phoneNumDetails)
        truecallerData = trial.request_data(phonelookupURL, phoneNumDetails['Phone Number'])
        print(truecallerData)
        email_info={'Email': truecallerData}
        phonedata.append(email_info)
        urls=google_dorking_email(truecallerData)
        print(urls)
        facebook_urls = [url for url in urls if url.startswith("https://www.facebook.com")]
        
        insta_urls = [url for url in urls if url.startswith("https://www.instagram.com")]
        

        linkedin_urls = [url for url in urls if "linkedin.com/in/" in url and "/posts" not in url and "/pub" not in url]

        linkedindata=gettingLinkedinData(linkedin_urls)
        fbdata=gettingScrapedData(facebook_urls)
        instadata=getInstaInfo(insta_urls)
        data.append(linkedindata)
        data.append(fbdata)
        data.append(instadata)
        
    print("The data is : ", data)
        
    print("The phonedata is : ", phonedata)
    return data,phonedata

# print(linkedin_urls)
# gettingLinkedinData(linkedin_urls)
# gettingScrapedData(facebook_urls)
# Scraping("+919393929291", 'phone')