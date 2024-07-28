from googlesearch import search


def google_dorking_email(email):
    social_media_sites = ["https://www.linkedin.com", "https://www.facebook.com", "https://www.instagram.com"]
    urls = []
    
    for site in social_media_sites:
        query = f'"{email}" site:{site}'
        print(f"Searching for email: {email} on {site}")
     
        for _ in range(5):  # limiting the number of attempts per site
            try:
                site_results = search(query, sleep_interval=20, num_results=5, lang="en", )
                urls.extend(site_results)
                break  # Break if successful
            except Exception as e:
                print(f"Error : {e}")
                continue  # Try the next proxy if failed
        
    print(urls)
    return urls



# google_dorking_email("Khushi@gmail.com")