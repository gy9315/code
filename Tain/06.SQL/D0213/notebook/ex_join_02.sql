use sqlclass_db;
create table customer
(customer_id smallint unsigned,
first_name varchar(20),
last_name varchar(20),
birth_date date,
spouse_id smallint unsigned,
primary key(customer_id));
desc customer;

INSERT INTO customer (customer_id, first_name, last_name, birth_date, spouse_id)
VALUES
(1, 'John', 'Mayer', '1983-05-12', 2),
(2, 'Mary', 'Mayer', '1990-07-30', 1),
(3, 'Lisa', 'Ross', '1989-04-15', 5),
(4, 'Anna', 'Timothy', '1988-12-26', 6),
(5, 'Tim', 'Ross', '1957-08-15', 3),
(6, 'Steve', 'Donell', '1967-07-09', 4);

INSERT INTO customer (customer_id, first_name, last_name, birth_date)
VALUES (7, 'Donna', 'Trapp', '1978-06-23');

select * from customer;

# self-join
select
cust.customer_id,
cust.first_name,
cust.last_name,
cust.birth_date,
cust.spouse_id,
spouse.first_name spouse_first_name,
spouse.last_name spouse_last_name
from customer cust join customer spouse
on cust.spouse_id=spouse.customer_id;
