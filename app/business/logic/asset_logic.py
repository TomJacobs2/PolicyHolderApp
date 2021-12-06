#  Copyright (c) Thomas Jacobs. All Rights Reserved.

class AssetLogic():
    def __init__(self):
        pass

    def process_get_all(self):
        print("Asset Logic: get all called")

    def process_get_asset(self, asset_id: int):
        print(f"Asset Logic: get asset with id of {asset_id}")

    def process_post(self):
        print("Asset Logic: post request called")