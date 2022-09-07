from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer, String, Date, DECIMAL
from config.db import meta,engine,conn
import pandas as pd

answer1 = Table(
    "answer1",
    meta,
    Column("department_name", String(255)),
    Column("order_item_subtotal", DECIMAL)
)

answer2 = Table(
    "answer2",
    meta,
    Column("category_name", String(255)),
    Column("order_item_quantity", Integer)
)

answer3 = Table(
    "answer3",
    meta,
    Column("customer_id", Integer),
    Column("customer_fname", String(255)),
    Column("customer_lname", String(255)),
    Column("order_item_quantity", Integer)
)

answer4 = Table(
    "answer4",
    meta,
    Column("order_date", Date),
    Column("order_item_quantity", Integer)
)

meta.create_all(engine)

# Load data results to my tables

df = pd.read_sql('SELECT * FROM order_items INNER JOIN products ON order_items.order_item_product_id=products.product_id INNER JOIN categories ON products.product_category_id=categories.category_id INNER JOIN departments ON categories.category_department_id=departments.department_id INNER JOIN orders ON order_items.order_item_order_id=orders.order_id INNER JOIN customers ON customers.customer_id=orders.order_customer_id', con=conn)

# Answer1: Load data

q1 = df.groupby('department_name')[["order_item_subtotal"]].sum().reset_index().sort_values(by="order_item_subtotal",ascending=False)
q1.to_sql('answer1', conn, if_exists='replace', index = False)

# Answer2: Load data

q2 = df.groupby('category_name')[["order_item_quantity"]].sum().sort_values(by="order_item_quantity",ascending=False).reset_index()
q2.to_sql('answer2', conn, if_exists='replace', index = False)

# Answer3: Load data

q3 = df.groupby(['customer_id','customer_fname','customer_lname'])[['order_item_quantity']].sum().sort_values(by='order_item_quantity',ascending=False).reset_index()[:10]
q3.to_sql('answer3', conn, if_exists='replace', index = False)

# Answer4: Load data

q4 = df.groupby('order_date')[['order_item_quantity']].sum().reset_index()
q4["order_date"] = pd.to_datetime(q4["order_date"])
q4 = q4.sort_values(by='order_date')
q4.to_sql('answer4', conn, if_exists='replace', index = False)