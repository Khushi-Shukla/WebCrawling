import instaloader
import re

def get_instagram_profile_info(username):
    # Create an instance of Instaloader
    L = instaloader.Instaloader()

    try:
        # Load the profile
        profile = instaloader.Profile.from_username(L.context, username)

        # Extract profile information
        profile_info = {
            "Username": profile.username,
            "Full Name": profile.full_name,
            "Bio": profile.biography,
            "Profile Picture URL": profile.profile_pic_url,
            "Followers": profile.followers,
            "Following": profile.followees,
            "Number of Posts": profile.mediacount,
            "Is Private": profile.is_private,
            "Is Verified": profile.is_verified
        }

        return profile_info

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile {username} does not exist.")
        return None
    except instaloader.exceptions.ConnectionException as e:
        print(f"Connection error: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None



def getInstaInfo(urls):
    
    #Extracting usernames
    instaData=[]
    usernames = []
    pattern = re.compile(r"https://www\.instagram\.com/([^/]+)/")
    for url in urls:
        match = pattern.search(url)
        if match:
            usernames.append(match.group(1))
    
    for username in usernames:
        info = get_instagram_profile_info(username)
        instaData.append(info)
        if info:
            print(f"Profile Information for {username}:")
            for key, value in info.items():
                print(f"{key}: {value}")
            print("\n")
        return instaData

# Example usage
# urls = [
#     'https://www.instagram.com/____khushi___/?hl=en',
#     'https://www.instagram.com/example_user/?hl=en',
#     'https://www.instagram.com/anotheruser/?hl=en'
# ]

# extract_usernames(urls)