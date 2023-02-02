from faker import Faker
import pandas as pd
import random

fake=Faker()

def make_employees():
    first_name=fake.first_name()
    last_name=fake.last_name()
    empdata= {}
    empdata["emp_id"] = fake.unique.bothify(text="??####", letters="ABCDEFGHJKMNPQRSTUVWXYZ")
    empdata["emp_name"] = first_name+" "+last_name
    empdata["emp_email"] = str.lower(first_name[0]+first_name[-1] + "." + last_name + "@qtan.com")
    empdata["years_worked"] = random.randint(0,15)
    empdata["salary"] = random.randint(50000,80000)
    empdata["salary"] = empdata["salary"] + empdata["salary"]*.05*empdata["years_worked"]
    return empdata

employees=[make_employees() for i in range (30)]

empdf=pd.DataFrame.from_dict(employees)

position = ['CEO', 'Sales Manager', 'Purchasing Manager', 'Tech Manager', 'Finance Manager', 'Warehouse Manager',
            'salesperson', 'salesperson', 'salesperson', 'salesperson', 'sales assistant', 'customer support',
            'purchaser', 'purchaser', 'purchaser', 'purchaser', 'purchasing assistant',
            'website developer', 'IT', 'tech assistant', 'tech assistant',
            'accountant', 'accountant', 'accounting assistant',
            'warehouse worker', 'warehouse worker', 'warehouse worker',
            'executive assistant', 'executive assistant', 'human resources']

department = ['management', 'sales', 'purchasing', 'tech', 'finance', 'warehouse',
              'sales', 'sales', 'sales', 'sales', 'sales', 'sales',
              'purchasing', 'purchasing', 'purchasing', 'purchasing', 'purchasing',
              'tech', 'tech', 'tech', 'tech',
              'finance', 'finance', 'finance',
              'warehouse', 'warehouse', 'warehouse',
              'general office', 'general office', 'general office']
empdf['position']=position
empdf['department']=department
print(empdf)
empdf.to_csv('employees.csv')

