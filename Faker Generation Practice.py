from faker import Faker
import pandas as pd
import random

f = Faker()
# for chinese stuff -- f = Faker(["zh_CN"])


####  Print 10 random names
# for i in range(10):
#    print(f.name())

#### Print Random address, phone number, company
# print(f.address())
# print(f.phone_number())
# print(f.company())

####  Print 5 unique alpha-numeric codes that follow letter-letter-num-num-num-num
#  for i in range (5):
#    print(f.unique.bothify(text="??#####", letters="ABCDEFGHJKMNPQRSTUVWXYZ"))

####  Print 5 unique numbers in a range so that it will always be 4 digits
# for i in range (5):
#     print(f.unique.random_int(min=1000, max=9999))

#   List of states to choose from
states = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]

#   columns for customers dataframe
def generate_customers():
    return {
        'customer_id': f.unique.bothify(text="??#####", letters="ABCDEFGHJKMNPQRSTUVWXYZ"),
        'company': f.company(),
        'contact_firstname': f.first_name(),
        'contact_lastname': f.last_name(),
        'contact_email': f.company_email(),
        'contact_phone': f.phone_number(),
        'street_address': f.street_address(),
        'city': f.city(),
        'state': random.choice(states),
        'zip_code': f.postcode()
    }

#   Generates 100 customers
customers = [generate_customers() for i in range(250)]

#   puts generated customers to a dataframe
custdf=pd.DataFrame(customers)
print(custdf)

#   exports dataframe to csv file
custdf.to_csv('customers.csv')