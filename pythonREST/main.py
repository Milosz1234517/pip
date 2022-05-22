from strToJson import ConvertToString
import os

convert = ConvertToString()


def mainMenu():
    while True:
        nl = "\n"
        options = "1. Find country by currency code" + nl
        options += "2. Get the details of country by country code" + nl
        options += "3. Get the details of a specific country region" + nl
        options += "4. Get the cities in a specific country region" + nl
        options += "5. Find cities by location code " + nl
        options += "6. Get cities near the given city" + nl
        options += "7. Get the details for a specific city" + nl
        options += "8.Get the details for the containing populated place" + nl
        options += "0. Exit" + nl
        choice = int(input(options))
        if choice == 0:
            break
        elif choice == 1:
            subMenu1()
        elif choice == 2:
            subMenu2()
        elif choice == 3:
            subMenu3()
        elif choice == 4:
            subMenu4()
        elif choice == 5:
            subMenu5()
        elif choice == 6:
            subMenu6()
        elif choice == 7:
            subMenu7()
        elif choice == 8:
            subMenu8()

    return


def subMenu1():
    choice = str(input("Wpisz kod waluty np \"GBP\"\n"))
    print(convert.getCountryFromCurrency(choice))
    os.system("pause")
    os.system('cls')


def subMenu2():
    choice = str(input("Wpisz kod kraju np \"US\"\n"))
    print(convert.getCountryDetailsFromCountry("true", choice))
    os.system("pause")
    os.system('cls')


def subMenu3():
    choice = str(input("Wpisz kod kraju np \"US\"\n"))
    choice1 = str(input("Wpisz kod regionu np \"CA\"\n"))
    print(convert.getRegionsDetailsFromCountryAndRegionCode("true", "EN", choice, choice1))
    os.system("pause")
    os.system('cls')


def subMenu4():
    choice = str(input("Wpisz kod kraju np \"US\"\n"))
    choice1 = str(input("Wpisz kod regionu np \"CA\"\n"))
    print(convert.CountryRegionsCitiesFromCountryAndRegionCode("true", "EN", choice, choice1))
    os.system("pause")
    os.system('cls')


def subMenu5():
    location = str(input("Insert location in ISO-6709 format np +38-097\n"))
    print(convert.getCityList(location))


def subMenu6():
    cityCode = str(input("Insert city id np Q60\n"))
    radius = str(input("Insert radius np 100\n"))
    print(convert.getNearbyCitiesList(radius, cityCode))


def subMenu7():
    cityCode = str(input("Insert city id np Q60\n"))
    print(convert.getCityDetailsList("true", cityCode))


def subMenu8():
    cityCode = str(input("Insert city id np Q65\n"))
    print(convert.getCityLocatedInList(cityCode))


if __name__ == '__main__':
    mainMenu()
