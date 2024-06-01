from QueryProfile import BaseQueryProfile


class AthenaQueryProfile(BaseQueryProfile):
    ID = "athena"

    def __init__(self, bearer_token: str, account_id: str) -> None:
        super().__init__(bearer_token, account_id)

    def __init__(self, profile):
        self.profile = profile
        super().__init__(download_profile=False)

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
