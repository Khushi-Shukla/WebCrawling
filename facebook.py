from facebook_scraper import get_profile
import logging

#Extracting username from urls received after dorking
def extract_username_from_url(profile_url):
    # Remove any leading or trailing whitespace and ensure the URL is in lower case
    profile_url = profile_url.strip().lower()

    # Check if the URL starts with the expected format
    if profile_url.startswith("https://www.facebook.com/"):
        # Remove the starting part of the URL
        username_part = profile_url[len("https://www.facebook.com/"):]

        username=""
        if not (username_part.startswith("groups/")
        or username_part.startswith("p/")
        or username_part.startswith("permalink.php")
        or username_part.startswith("photo")):
            # Extract username until next slash or end of string
            username = username_part.split('/')[0]

        # Validate the extracted username
        if username:
            return username
        else:
            return None
    else:
        return None


def fbScraping(username):

    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Replace 'your_c_user_cookie' and 'your_xs_cookie' with the actual cookie values from your logged-in session
    cookies = {
        "c_user": "61561835009153",
        "xs": "9%3A5meeKgq-Pqk1yQ%3A2%3A1720978737%3A-1%3A-1"
    }

    try:
        # Scrape the profile
        profile = get_profile(username, cookies=cookies)

        # Handle missing fields gracefully and store in variables
        friend_count = profile.get('Friend_count', 'N/A')
        follower_count = profile.get('Follower_count', 'N/A')
        following_count = profile.get('Following_count', 'N/A')
        cover_photo = profile.get('cover_photo', 'N/A')
        profile_picture = profile.get('profile_picture', 'N/A')
        name = profile.get('Name', 'N/A')
        work = profile.get('Work', 'N/A')
        education = profile.get('Education', 'N/A')
        places_lived = profile.get('Places lived', 'N/A')
        contact_info = profile.get('Contact Info', 'N/A')
        basic_info = profile.get('Basic info', 'N/A')
        relationship = profile.get('Relationship', 'N/A')
        about = profile.get('About', 'N/A')
        life_events = profile.get('Life events', 'N/A')
        favourite_quotes = profile.get('Favourite Quotes', 'N/A')

        # Print the scraped profile information
        print(f"Friend Count: {friend_count}")
        print(f"Follower Count: {follower_count}")
        print(f"Following Count: {following_count}")
        print(f"Cover Photo: {cover_photo}")
        print(f"Profile Picture: {profile_picture}")
        print(f"Name: {name}")
        print(f"Work: {work}")
        print(f"Education: {education}")
        print(f"Places Lived: {places_lived}")
        print(f"Contact Info: {contact_info}")
        print(f"Basic Info: {basic_info}")
        print(f"Relationship: {relationship}")
        print(f"About: {about}")
        print(f"Life Events: {life_events}")
        print(f"Favourite Quotes: {favourite_quotes}")
    # except AssertionError:
    #     print("No more posts to get")
    except Exception as e:
        logging.error(f"Pareshani: {e}")

def gettingScrapedData(urls):
    users=[]
    print(type(users))
    for url in urls: #list of urls
        if url.startswith("https://www.facebook.com/"):
            username = extract_username_from_url(url)
            if username:
                users.append(username)

    print(users)

    for user in users:
        print(f'---------Extracting info of {user}:---------')
        fbScraping(user)
        
urls=[
'https://www.facebook.com/profile.php?id=100082664051399', 
# 'https://www.facebook.com/groups/PUNJABI.ADAB/?locale=ru_RU', 
# 'https://www.facebook.com/groups/1618658868232832/?locale=eo_EO', 
# 'https://www.facebook.com/groups/651402995529635/?locale=az_AZ',
# 'https://www.facebook.com/agnes.artpage/videos/a-panorama-of-the-works-of-agnes-dcruz-rajesh/10153482209128191/?locale=ms_MY',
# 'https://www.facebook.com/florentinoplayschool/',
# 'https://www.facebook.com/gomantakpune/', 
# 'https://www.facebook.com/seotoolover/'
]

gettingScrapedData(urls)