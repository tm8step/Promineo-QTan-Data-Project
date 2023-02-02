from faker import Faker
import pandas as pd
import random

f = Faker()

#   List of states to choose from
states = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]

#   columns for customers dataframe
def generate_customers():
    first_name = f.first_name()
    last_name = f.last_name()
    company=f.company()
    email = company.replace(" ", "")
    email = email.replace(",", "")
    custdata = {}
    custdata["custid"] = f.unique.bothify(text="?#?###?#?", letters="ABCDEFGHJKMNPQRSTUVWXYZ")
    custdata["cust_first_name"]=first_name
    custdata["cust_last_name"]=last_name
    custdata["cust_company"]= company
    custdata["cust_email"] = first_name[0] + last_name + "@" + email + ".com"
    custdata["cust_phone"] = f.phone_number()
    return custdata

#   Generates 250 customers
customers = [generate_customers() for i in range(250)]

#   puts generated customers to a dataframe
custdf=pd.DataFrame(customers)
print(custdf)

#   exports dataframe to csv file
custdf.to_csv('customers.csv')