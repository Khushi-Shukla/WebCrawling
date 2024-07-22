from googlesearch import search


def google_dorking_email(email):
    social_media_sites = ["https://www.linkedin.com", "https://www.facebook.com"]
    urls = []

    for site in social_media_sites:
        query = f'"{email}" site:{site}'
        print(f"Searching for email: {email} on {site}")
        site_results = [result for result in search(query,num_results=30, lang="en")]
        urls.extend(site_results)
    print(urls)
    return urls

# google_dorking_email("Khushi@gmail.com")