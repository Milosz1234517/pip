import json

from requestsHttp import CityRequests, CountryRequests


def getManyCityResult(list1):
    result = ""
    for info in list1:
        result += str(info['city']) + ", "
        result += str(info['country']) + ", "
        result += str(info['countryCode']) + ", "
        result += str(info['region']) + ", "
        result += str(info['regionCode']) + ", "
        result += str(info['population']) + ", "
        result += "\n"
    return result


def getOneCityResult(httpResult):
    result = str(json.loads(httpResult)['data']['city']) + ", "
    result += str(json.loads(httpResult)['data']['country']) + ", "
    result += str(json.loads(httpResult)['data']['countryCode']) + ", "
    result += str(json.loads(httpResult)['data']['region']) + ", "
    result += str(json.loads(httpResult)['data']['regionCode']) + ", "
    result += str(json.loads(httpResult)['data']['population']) + ", "
    result += "\n"
    return result


class ConvertToString:
    country = CountryRequests()
    city = CityRequests()

    def getCountryFromCurrency(self, currency):
        result = "Not avaliable"
        # httpResult = self.country.getCountry(str(currency))
        # result = ""
        # list1 = json.loads(httpResult)['data']
        # for info in list1:
        #     result += str(info['name']) + ", "
        #     result += str(info['currencyCodes']) + ", "
        #     result += str(info['code'])
        #     result += "\n"
        return result

    def getCountryDetailsFromCountry(self, asciiCode, countryCode):
        httpResult = self.country.getCountryDetails(asciiCode, countryCode)
        result = ""
        result += str(json.loads(httpResult)['data']['name']) + ", "
        result += str(json.loads(httpResult)['data']['capital']) + ", "
        result += str(json.loads(httpResult)['data']['currencyCodes']) + ", "
        result += str(json.loads(httpResult)['data']['code'])
        result += "\n"
        return result

    def getRegionsDetailsFromCountryAndRegionCode(self, asciiCode, languageCode, countryCode, regionCode):
        httpResult = self.country.getCountryRegionsDetails(asciiCode, languageCode, countryCode, regionCode)
        result = ""
        result += str(json.loads(httpResult)['data']['name']) + ", "
        result += str(json.loads(httpResult)['data']['capital']) + ", "
        result += str(json.loads(httpResult)['data']['countryCode'])
        result += "\n"
        return result

    def CountryRegionsCitiesFromCountryAndRegionCode(self, asciiCode, languageCode, countryCode, regionCode):
        httpResult = self.country.getCountryRegionsCities(asciiCode, languageCode, countryCode, regionCode)
        result = ""
        list1 = json.loads(httpResult)['data']
        for info in list1:
            result += str(info['name']) + ", "
            result += str(info['city']) + ", "
            result += str(info['population'])
            result += "\n"
        return result

    def getCityList(self, location):
        httpResult = self.city.getCity(location)
        list1 = json.loads(httpResult)['data']
        return getManyCityResult(list1)

    def getNearbyCitiesList(self, radius, cityCode):
        httpResult = self.city.getNearbyCities(radius, cityCode)
        list1 = json.loads(httpResult)['data']
        return getManyCityResult(list1)

    def getCityDetailsList(self, asciiMode, cityID):
        httpResult = self.city.getCityDetails(asciiMode, cityID)
        return getOneCityResult(httpResult)

    def getCityLocatedInList(self, cityCode):
        httpResult = self.city.getCityLocatedIn(cityCode)
        return getOneCityResult(httpResult)
