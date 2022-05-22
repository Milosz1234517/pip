import requests


class CityRequests:
    headers = {
        "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com",
        "X-RapidAPI-Key": "d68c0b02c5mshf5355976d62ad0fp1c22ecjsn4938b96acbf7"
    }

    def getCity(self, location):
        url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
        querystring = {"location": str(location), "limit": "9"}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        return response.text

    def getNearbyCities(self, radius, cityCode):
        url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/" + str(cityCode) + "/nearbyCities"
        querystring = {"radius": str(radius), "limit": "9"}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        return response.text

    def getCityDetails(self, asciiMode, city):
        url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/" + city
        querystring = {"asciiMode": asciiMode}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        return response.text

    def getCityLocatedIn(self, cityCode):
        url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/" + str(cityCode) + "/locatedIn"
        response = requests.request("GET", url, headers=self.headers)
        return response.text
