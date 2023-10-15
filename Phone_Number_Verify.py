import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder, carrier


Phone_num=input("Enter a number with Country Code Ex. +120325678987 : ")
P_num=phonenumbers.parse(Phone_num)

#CountryCode, NationalNumber ,LocalFormat, InternationalFormat

Country_code=P_num.country_code
Nation_number=P_num.national_number

Local_Format="0"+str(Nation_number)
International_Format="+"+str(Country_code)+" "+str(Nation_number)


#check if phone number is valid or not
try:
    Is_Valid=phonenumbers.is_valid_number(P_num)
except:
    Is_Valid="False"


#Location
loc=[]
Loc=str(timezone.time_zones_for_number(P_num))
for i in Loc.split("/"):
    loc.append(i)
Location=loc[1].replace("'","").replace(",","").replace(")","")


Carrier=carrier.name_for_number(P_num,"en")

Country=geocoder.country_name_for_number(P_num,"en")

Details={"PhoneNumber":Phone_num, "Valid":Is_Valid, "Local Format":Local_Format, "International Format":International_Format, "Country Prefix": Country_code, "Country": Country, "Location":Location, "Carrier":Carrier}
print(Details)