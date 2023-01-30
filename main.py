import json
import requests

# GET request to obtain all ad_units
try:
    auth = {'Api-Key': 'flow like a waterfull'}
    url = 'https://o.applovin.com/mediation/v1/ad_units/'

    max_units = requests.get(url=url, auth=auth)

# try clause fails (API key is dummy); randomly generated MAX API ad units obtained from json file instead
except:
    with open('max_units.json') as max_units:
        max_units = json.load(max_units)



# function to save new ad units to master database
def save_new_units(max_units):

    # load master database
    with open('adunits/master_units.json', 'r+') as master_json:
        master_units = json.load(master_json)

        # generate list of existing ad unit IDs
        existing_unit_ids = [unit['ad_unit_id'] for unit in master_units]

        # generate list of new ad units
        new_units = [unit for unit in max_units if unit['ad_unit_id'] not in existing_unit_ids]

        # append *new* MAX API ad units to master database
        for unit in new_units:
            master_units.append(unit)

        master_json.seek(0)
        json.dump(master_units, master_json, indent=2)


# get active ios ad units
def get_active_ios():
    with open('adunits/master_units.json', 'r') as master_units:
        master_units = json.load(master_units)
        active_units = [unit for unit in master_units if not unit['disabled']]
        active_ios_units = [unit for unit in active_units if unit['platform'] == 'ios']
    return active_ios_units

# get active android ad units
def get_active_android():
    with open('adunits/master_units.json', 'r') as master_units:
        master_units = json.load(master_units)
        active_units = [unit for unit in master_units if not unit['disabled']]
        active_android_units = [unit for unit in active_units if unit['platform'] == 'android']
    return active_android_units

# get disabled ad units
def get_disabled():
    with open('adunits/master_units.json', 'r') as master_units:
        master_units = json.load(master_units)
        disabled_units  = [unit for unit in master_units if unit['disabled']]
    return disabled_units


save_new_units(max_units)
# get_disabled()
# get_active_ios()
# get_active_android()
