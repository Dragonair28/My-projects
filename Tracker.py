import phonenumbers
#from num import number
number = input("Enter the number with country code: ")

from phonenumbers import geocoder 
ch_number = phonenumbers.parse(number,"CH")
print(f'Location: {geocoder.description_for_number(ch_number,"en")}')

from phonenumbers import carrier
service_number = phonenumbers.parse(number,"RO")
print(f'Carrier: {carrier.name_for_number(service_number,"en")}')