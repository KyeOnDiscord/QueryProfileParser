import requests
from ProfileTypes import ProfileType
BASE_URL = 'https://fngw-mcp-gc-livefn.ol.epicgames.com'
BASE_MCP_URL = f'{BASE_URL}/fortnite/api/game/v2/profile'


def get_profile(account_id: str, bearer_token: str, profile_type: ProfileType):
    match profile_type:
        case ProfileType.Athena:
            from AthenaQueryProfile import AthenaQueryProfile
            return AthenaQueryProfile(account_id=account_id, bearer_token=bearer_token)
        case _:
            raise Exception("Invalid Profile Type")


class BaseQueryProfile:
    def __init__(self, bearer_token: str = None, account_id: str = None, download_profile: bool = True):
        if download_profile:
            self.bearer_token = bearer_token
            self.account_id = account_id
            self.profile = self.__download_profile()

        # global for all profiles
        self.profileRevision = self.profile['profileRevision']
        self.profileId = self.profile['profileId']
        self.profileChangesBaseRevision = self.profile['profileChangesBaseRevision']
        self.profileCommandRevision = self.profile['profileCommandRevision']
        self.serverTime = self.profile['serverTime']
        self.responseVersion = self.profile['responseVersion']

        self.__get_template_ids()
        print("\n".join(self.__get_template_ids()))

    def __download_profile(self):
        url = BASE_MCP_URL + \
            f"/{self.account_id}/client/QueryProfile?profileId={self.account_id}"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.bearer_token}'
        }
        response = requests.request(
            "POST", url, headers=headers, data="{}", timeout=60)
        return response.json()

    def get_items_by_id(self, template_id: str):
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
