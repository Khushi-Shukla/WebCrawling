# import asyncio
# from playwright.async_api import async_playwright
# import jmespath
#
# async def scrape_twitter(username):
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=True)
#         context = await browser.new_context()
#         page = await context.new_page()
#
#         profile_url = f"https://twitter.com/{username}"
#         await page.goto(profile_url)
#
#         try:
#             # Wait for the tweets to load with an increased timeout
#             await page.wait_for_selector("[data-testid='tweet']", timeout=60000)  # Timeout set to 60 seconds
#
#             # Scroll the page to load more tweets
#             num_scrolls = 5
#             for _ in range(num_scrolls):
#                 await page.evaluate('window.scrollTo(0, document.body.scrollHeight);')
#                 await asyncio.sleep(2)
#
#             # Get the tweet elements
#             tweet_elements = await page.query_selector_all('article')
#
#             tweets = []
#             for element in tweet_elements:
#                 tweet_html = await element.inner_html()
#                 tweets.append(tweet_html)
#
#         except Exception as e:
#             print(f"An error occurred: {e}")
#
#         await browser.close()
#         return tweets
#
# def extract_tweet_data(tweets_html):
#     # Extract tweet text using JMESPath or any other method
#     extracted_data = []
#     for html in tweets_html:
#         # Example: Using JMESPath to extract tweet text
#         tweet_text = jmespath.search("** | [0]", html)  # Adjust the JMESPath expression as needed
#         extracted_data.append(tweet_text)
#     return extracted_data
#
# username = 'GhoshShankhanil'  # Replace with the desired Twitter username
# tweets_html = asyncio.run(scrape_twitter(username))
# tweet_data = extract_tweet_data(tweets_html)
#
# for data in tweet_data:
#     print(data)

from playwright.sync_api import sync_playwright
import json

def scrape_profile(url: str, username: str, password: str) -> list:
    """
    Scrape a X.com profile details e.g.: https://x.com/Scrapfly_dev
    """
    _xhr_calls = []

    def intercept_response(response):
        """capture all background requests and save them"""
        # we can extract details from background requests
        if response.request.resource_type == "xhr":
            _xhr_calls.append(response)
        return response

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        # enable background request intercepting:
        page.on("response", intercept_response)
        # go to url and wait for the page to load
        page.goto("https://twitter.com/login", timeout=100000)

        # Wait for the username input field to be available
        #page.wait_for_selector("#react-root > div > div > div > main > div > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox > div.css-175oi2r.r-16y2uox.r-f8sm7e.r-13qz1uu > div > div.css-175oi2r.r-1mmae3n.r-1e084wi.r-13qz1uu > label > div > div.css-175oi2r.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-is05cd.r-ttdzmv > div > input", timeout=100000)
        #//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[4]/label/div/div[2]/div/input
        # Log in to Twitter
        page.fill("input[autocomplete=username]", username)
        page.locator('"Next"').click()
        page.type('[autocomplete="current-password"]', password);
        page.locator('"Log in"').click()
        # Wait for the home page to load to ensure the login is successful
        page.wait_for_selector("[data-testid='SideNav_AccountSwitcher_Button']", timeout=60000)

        # Go to the profile URL and wait for the page to load
        page.goto(url)
        page.wait_for_selector("[data-testid='primaryColumn']", timeout=60000)

        # Give it some time to load more tweets
        page.wait_for_timeout(10000)  # Wait for 10 seconds to load more tweets
        # find all tweet background requests:
        tweet_calls = [f for f in _xhr_calls if "UserBy" in f.url]
        for xhr in tweet_calls:
            try:
                data = json.loads(xhr.body())
                return data['data']['user']['result']
            except Exception as e:
                print(f"Error processing XHR response: {e}")
                continue

    return None


if __name__ == "__main__":
    username = "MukherjeeSoumee"
    password = "So877759430"

    profile_data = scrape_profile("https://x.com/Scrapfly_dev", username, password)
    print(profile_data)
