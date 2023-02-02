from faker import Factory
from faker import Faker
import pinyin
import pandas as pd

fake = Factory.create('zh-CN')
f = Faker()

# Creates a supplier
def generate_supplier():
    name = fake.name()
    translatename = pinyin.get(name, format="strip", delimiter=" ")
    initials = pinyin.get_initial(name)
    company_prefix = fake.company_prefix()
    company_suffix = fake.company_suffix()
    company = company_prefix + company_suffix
    translated_company_prefix = pinyin.get(company_prefix, format= "strip", delimiter=" ")
    translated_company_suffix = pinyin.get(company_suffix, format="strip", delimiter=" ")
    company_translated = translated_company_prefix + translated_company_suffix
    email = initials.replace(" " , "") + "@" + translated_company_prefix.replace(" ", "") + ".com"

    # Creates a dictionary supdata to put the data in

    supdata = {}
    supdata["sup_id"] = f.unique.bothify(text="??####?", letters="ABCDEFGHJKMNPQRSTUVWXYZ")
    supdata["chinese_name"] = name
    supdata["translated_name"] = translatename
    supdata["company"] = company
    supdata["translated_company"] = company_translated
    supdata["sup_email"] = email
    supdata["sup_phone"] = fake.phone_number()
    return supdata

# Runs generate supplier 100 times to generate data
suppliers = [generate_supplier() for i in range(100)]

# Converts data into DataFrame, prints it to test it
supdf = pd.DataFrame(suppliers)
print(supdf)

# Creats a CSV file with the data
supdf.to_csv('suppliers.csv')