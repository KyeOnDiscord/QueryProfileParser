import json
from QueryProfile import get_profile
from AthenaQueryProfile import AthenaQueryProfile

# read file as json
profile = json.load(open("profile.json"))
athena = AthenaQueryProfile(profile=profile)
# profile = get_profile("", "")
skins = athena.get_skins()
backpacks = athena.get_backpacks()
pickaxes = athena.get_pickaxes()
emotes = athena.get_emotes()

print(str(len(skins)) + " skins found")
print(str(len(backpacks)) + " backpacks found")
print(str(len(pickaxes)) + " pickaxes found")
print(str(len(emotes)) + " emotes found")

# json.dump(profile, open("profile.json", "w"))
# print("Profile: ", profile)
