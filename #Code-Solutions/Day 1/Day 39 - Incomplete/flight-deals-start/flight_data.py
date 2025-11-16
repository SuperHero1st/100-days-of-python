#This class is responsible for structuring the flight data.
class FlightData:
    def __init__(self) -> None:
        pass

    def struct_offers(self, offers):
        prices = []
        for offer in offers:
            price = (offer['price']['total']) 
            GBP_price = round(float(price) * 0.85, 2)
            prices.append(GBP_price)
        if prices:
            min_price = min(prices)
            print(f"£{min_price}")
            return min_price
        else:
            print("N/A")