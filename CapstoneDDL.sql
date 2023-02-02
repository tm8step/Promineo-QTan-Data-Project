create table 'customer' (
	'customer_id' VARCHAR(255),
	'company' VARCHAR (255),
	'contact_first' VARCHAR (255),
	'contact_last' VARCHAR (255),
	'contact_email' VARCHAR (255),
	'address' VARCHAR (255),
	'city' VARCHAR (255),
	'state' VARCHAR (255)
)

create table 'orders' (
	'order_id' integer,
	'customer_id' integer,
	'product_id' integer,
	'order_date' date
)

create table 'payments' (
	'payment_id' integer,
	'customer_id' integer,
	'product_id' integer,
	'order_id' integer,
	'payment_date' date,
	'amount_paid' FLOAT
)

create table 'reports' (
	'report_id' INTEGER,
	'customer_id' INTEGER,
	'order_id' INTEGER,
	'product_id' INTEGER,
	'payment_id' INTEGER,
	'report_type' VARCHAR (255),
	'department_id' INTEGER
)

create table 'departments' (
	'department_id' INTEGER,
	'department_name' VARCHAR (255),
	'employee_id' VARCHAR (255)
)

create table 'employees' (
	'employee_id' INTEGER,
	'department' VARCHAR (255),
	'first_name' VARCHAR (255),
	'last_name' VARCHAR (255),
	'years_worked' INTEGER,
	'salary' FLOAT,
	'job_name' VARCHAR (255)
)

create table 'shipping' (
	'shipping_id' INTEGER,
	'customer_id' INTEGER,
	'order_id' INTEGER,
	'shippping_cost' FLOAT,
	'delivery_date' DATE
)

create table 'products' (
	'product_id' INTEGER,
	'category_id' INTEGER,
	'product_name' VARCHAR (255)
)

create table 'categories' (
	'category_id' INTEGER,
	'product_id' INTEGER,
	'category_name' VARCHAR (255)
)

create table 'suppliers' (
	'supplier_id' VARCHAR (255),
	'supplier_contact_firstname' = VARCHAR (255),
	'supplier_contact_lastname' = VARCHAR (255),
	'supplier_email' = VARCHAR (255),
	'supplier_phone' = INTEGER,
	'supplier_address' = VARCHAR(255)
	
)