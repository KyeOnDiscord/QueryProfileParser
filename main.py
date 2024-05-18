import requests
import json

BASE_URL = 'https://fngw-mcp-gc-livefn.ol.epicgames.com'
BASE_MCP_URL = f'{BASE_URL}/fortnite/api/game/v2/profile'


class QueryProfile:
    def __init__(self, bearer_token: str, account_id: str, profile_id: str = "athena"):
        self.bearer_token = bearer_token
        self.account_id = account_id
        self.profile_id = profile_id
        self.profile = self.__download_profile()
        self.__get_template_ids()
        print("\n".join(self.__get_template_ids()))

    def __download_profile(self):
        url = BASE_MCP_URL + \
            f"/{self.account_id}/client/QueryProfile?profileId={self.profile_id}"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.bearer_token}'
        }
        response = requests.request(
            "POST", url, headers=headers, data="{}", timeout=60)
        return response.json()

    def __get_items_by_id(self, template_id: str):
        """Gets all items from the profile that match the template_id

        Args:
            template_id (str): The template id to filter the items by

        Returns:
            _type_: Array of items that match the template_id
        """
        items = (self.profile['profileChanges'][0]['profile']['items']).items()
        filtered = {item_id: item_data for item_id,
                    item_data in items if item_data["templateId"].startswith(template_id)}
        result = []
        for item in filtered:
            result.append({
                "id": filtered[item]["templateId"].split(":")[1],
                "attributes": filtered[item]["attributes"],
            })
        return result

    def __get_template_ids(self):
        items = (self.profile['profileChanges'][0]['profile']['items']).items()
        result = []
        for item_id, item_data in items:
            result.append(item_data["templateId"].split(":")[0])
        return list(set(result))

    def get_skins(self):
        """Gets skins"""
        return self.__get_items_by_id("AthenaCharacter")

    def get_backpacks(self):
        """Gets backpacks"""
        return self.__get_items_by_id("AthenaBackpack")

    def get_pickaxes(self):
        """Gets pickaxes"""
        return self.__get_items_by_id("AthenaPickaxe")

    def get_emotes(self):
        """Gets emotes"""
        return self.__get_items_by_id("AthenaDance")


profile = QueryProfile("", "")
skins = profile.get_skins()
backpacks = profile.get_backpacks()
pickaxes = profile.get_pickaxes()
emotes = profile.get_emotes()

print(str(len(skins)) + " skins found")
print(str(len(backpacks)) + " backpacks found")
print(str(len(pickaxes)) + " pickaxes found")
print(str(len(emotes)) + " emotes found")

# json.dump(profile, open("profile.json", "w"))
# print("Profile: ", profile)
