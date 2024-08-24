from QueryProfile import BaseQueryProfile
from ProfileTypes import ProfileType

class AthenaQueryProfile(BaseQueryProfile):
    def __init__(self, bearer_token: str = None, account_id: str = None, profile=None) -> None:
        self.profile_id = ProfileType.Athena
        if profile:
            self.profile = profile
            super().__init__(download_profile=False)
        else:
            super().__init__(bearer_token, account_id)

    def get_skins(self):
        """Gets skins"""
        return self.get_items_by_id("AthenaCharacter")

    def get_backpacks(self):
        """Gets backpacks"""
        return self.get_items_by_id("AthenaBackpack")

    def get_pickaxes(self):
        """Gets pickaxes"""
        return self.get_items_by_id("AthenaPickaxe")

    def get_emotes(self):
        """Gets emotes"""
        return self.get_items_by_id("AthenaDance")
