# Notes
- First run 'generate_adunits.py' to create json file of randomly generated ad_units. Necessary since we have no real api key to use in GET request. Then run 'main.py', read comments in file.
- Couldn't figure out how to append list of dicts to json file without having to read json to list, append to list, then overwrite json old file.
- There might be a quicker way of checking if ad unit already exists using hash maps instead of iterating over existing ad unit ids. Not enough time to implement.
- Wrote some basic sorting functions to put ad units into different categories but idk how useful this is.
- Important to open master database each time we want to interact with our data to ensure it is up to date.
