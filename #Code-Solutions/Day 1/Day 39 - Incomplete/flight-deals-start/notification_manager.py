from data_manager import DataManager
my_dm = DataManager()

class NotificationManager:
    def __init__(self) -> None:
        pass
    
    def check_price(self, price, index):
        data = my_dm.get_sheet_data()
        sheet_price = data['prices'][index]['lowestPrice']
        if price < sheet_price:
            return True
        return False

