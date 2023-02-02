import pandas as pd

empdf = pd.read_csv(r'C:\Users\toddm\Desktop\Programming\Python Projects\Promineo Capstone\employees.csv')

deptid = ['mgmt', 'sales', 'purch', 'tech', 'finan', 'ware'] + ['sales']*6+['purch']*5+['tech']*4+['finan']*3+['ware']*3+['office']*3

deptdf = pd.DataFrame(empdf, columns=['emp_id'])

deptdf['deptid']=deptid

print(deptdf)