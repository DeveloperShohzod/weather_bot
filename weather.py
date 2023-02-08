import requests
import json




class Today:
    def __init__(self):
        self.url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
        self.querystring = {"q": "", "days": "3", "lang": "uz"}
        self.headers = {
            "X-RapidAPI-Key": "b0c9fc13damsh20553890e97132ep1594e1jsn1a9aaf8982c3",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        self.response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
        self.xabar = (self.response.json())

    def get_shahar(self):
        self.shahar = f"Shahar: {self.xabar['location']['region']}"
        return self.shahar

    def get_harorat(self):
        self.harorat = f"Harorat: {self.xabar['current']['temp_c']} C"
        return self.harorat

    def get_shamol(self):
        self.shamol = f"Shamol tezligi: {self.xabar['current']['wind_mph']} m/s"
        return self.shamol

    def get_havo(self):
        self.havo = f"{self.xabar['current']['condition']['text']}"
        if self.havo == "Partly cloudy":
            self.havo = "Kam bulutli"
        elif self.havo == "Cloudy":
            self.havo = "Bulutli"
        elif self.havo == "Mist":
            self.havo = "Tuman"
        elif self.havo == "Sunny":
            self.havo = "Quyoshli"
        elif self.havo == "Light rain shower":
            self.havo = "Yengil yomg'ir"

        return self.havo
# def __repr__(self):
# 	return f"""
# 			{self.shahar}
# 			{self.harorat}
# 			{self.shamol}
# 			{self.havo}"""
