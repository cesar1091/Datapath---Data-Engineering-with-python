from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer, String, Date, DECIMAL
from config.db import meta,engine


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