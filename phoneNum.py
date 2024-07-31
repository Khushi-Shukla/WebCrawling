# import requests      # Default
# import os            # Default
# import sys           # Default
# import random        # Default
# import time          # Default
import re            # Default
# import uuid          # Default
# import socket        # Default
# import platform      # Default
# import getpass       # Default
# import psutil        # pip install psutil
# import bs4           # pip install beautifulsoup4
import phonenumbers  # pip install phonenumbers
# import snscrape.modules.twitter as sntwitter
# import pandas as pd
# import trial

# checking phone numbers validity

p_op = ''
phonelookupURL = "www.truecaller.com/search/in/"
pData = {}

def number_lookup(phone_number):
    from phonenumbers import timezone
    from phonenumbers import carrier
    from phonenumbers import geocoder
    
    # Global variables
    global p_op
    p_op = '' # Resetting previous output

    # Information gathering about the number
    print(f'    [+] Gathering information about {phone_number}'.format(phone_number))
    p_op += f'\n    Reverse phone number lookup for {phone_number}'.format(phone_number)+'\n\n'

    # Check if the number is valid or not (regex)
    if not re.match(r'^\+[1-9]\d{1,14}$', phone_number):
        print('    > Invalid phone number format! (Example: +44xxxxxxxxxx)')
        return False
    
    # Country code check
    try:
        # Phone number format: (+Countrycode)xxxxxxxxxx
        phone_number_details = phonenumbers.parse(phone_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        print('    > Missing Country Code! (Example: +91, +44, +1)')
        return False

    # extract country_code & only_number from "Country Code: xx National Number: xxxxxxxxxx"
    country_code = str(phone_number_details).split('Country Code:', 1)[1].split('National Number:', 1)[0].strip()
    only_number = str(phone_number_details).split('Country Code:', 1)[1].split('National Number:', 1)[1].strip()
    
    # Validating a phone number
    valid = phonenumbers.is_valid_number(phone_number_details)

    # Checking possibility of a number
    possible = phonenumbers.is_possible_number(phone_number_details)

    if valid and possible:
        # Creating a phone number variable for country
        counrty_number = phonenumbers.parse(phone_number,'CH')

        # Gives mobile number's location (Region)
        region_code = phonenumbers.region_code_for_number(phone_number_details)

        # Gives mobile number's location (Country)
        country = geocoder.description_for_number(counrty_number, 'en')

        # Creating a phone number variable for service provider
        service_number = phonenumbers.parse(phone_number,'RO')

        # Gives mobile number's service provider (Airtel, Idea, Jio)
        service_provider = carrier.name_for_number(service_number, 'en')

        # Gives mobile number's timezone
        timezone_details_unfiltered = str(timezone.time_zones_for_number(phone_number_details))
        timezone_details = timezone_details_unfiltered.replace('[', '').replace(']', '').replace("'", '').replace('(', '').replace(')', '').replace(',', '').replace(' ', '')
        
        # RFC3966 Format
        r_format = phonenumbers.format_number(phone_number_details, phonenumbers.PhoneNumberFormat.RFC3966).replace('tel:', '')

        # Reconfiguring variables
        possible = str(possible)+' '*int(30-len(str(possible)))
        valid = str(valid)+' '*int(30-len(str(valid)))
        country_code = str(country_code)+' '*int(30-len(str(country_code)))
        country = str(country)+' '*int(30-len(str(country)))
        region_code = str(region_code)+' '*int(30-len(str(region_code)))
        service_provider = str(service_provider)+' '*int(30-len(str(service_provider)))
        timezone_details = str(timezone_details)+' '*int(30-len(str(timezone_details)))
        phone_number = str(phone_number)+' '*int(30-len(str(phone_number)))
        only_number = str(only_number)+' '*int(30-len(str(only_number)))
        r_format = str(r_format)+' '*int(30-len(str(r_format)))

        # pData.append(possible)
        # pData.append(valid)
        # pData.append(country_code)
        # pData.append(country)
        # pData.append(region_code)
        # pData.append(service_provider)
        # pData.append(timezone_details)
        # pData.append(phone_number)
        # pData.append(only_number),
        # pData.append(r_format)
        pData={
            "Possible" : possible.strip(),
            "Valid" :valid.strip(),
            "Country Code": country_code.strip(),
            "Country" :country.strip(),
            "region_code" :region_code.strip(),
            "Service Provider" :service_provider.strip(),
            "Timezone Details" :timezone_details.strip(),
            "Phone Number" :phone_number.strip(),
            "Only Number" :only_number.strip()
        }
        return pData

#def main():

    
# if __name__ == "__main__":
#    main()
# phone_number = input("Enter phone number: ")
# phone_number="+916000982561"

# data=number_lookup(phone_number)
# print(data)
# number = number_lookup(phone_number)
#print(trial.request_data(phonelookupURL, number))
    
