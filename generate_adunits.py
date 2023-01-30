from random_word import RandomWords
import random
import json

# method to randomly generate a single ad unit
def rand_unit():
    r = RandomWords()

    data = {
             "name": r.get_random_word(),
             "platform": random.choice(['ios', 'android']),
             "package_name": "com.my.test.app",
             "ad_format": random.choice(['INT', 'BANNER', 'REWARD']),
             "ad_unit_id": random.randint(0,16777215),
             "has_active_experiment": bool(random.getrandbits(1)), 
             "disabled": bool(random.getrandbits(1))
            }

    return data

# generate 20 random MAX API ad units
max_units = [rand_unit() for n in range(20)]

# save generated MAX API ad units to json file
with open("max_units.json", "w") as out:
   json.dump(max_units, out, indent=2)

# save 4 random MAX API ad units to master database as though we already have a record of them
with open("adunits/master_units.json", "w") as out:
   json.dump(random.sample(max_units, 4), out, indent=2)
