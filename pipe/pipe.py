import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

import warnings
warnings.filterwarnings("ignore")

engine =create_engine("mysql+pymysql://root:AFern1091#@localhost/datapath_project")
conn = engine.connect()


def extract():
    # Load data results to my tables
    dataframe_db = pd.read_sql('SELECT * FROM order_items INNER JOIN products ON order_items.order_item_product_id=products.product_id INNER JOIN categories ON products.product_category_id=categories.category_id INNER JOIN departments ON categories.category_department_id=departments.department_id INNER JOIN orders ON order_items.order_item_order_id=orders.order_id INNER JOIN customers ON customers.customer_id=orders.order_customer_id', con=conn)
    return dataframe_db

def transform_group(data: pd.DataFrame,group: list[str],value: str,asc: bool,top_10: bool):
    question = data.groupby(group)[[value]].sum().sort_values(by=value,ascending=asc).reset_index()
    if top_10:
        return question.iloc[:10,:]
    else:
        return question

def transform_group_date(data: pd.DataFrame,group_date: str,value: str):
    question = data.groupby(group_date)[[value]].sum().reset_index()
    question[group_date] = pd.to_datetime(question[group_date])
    question = question.sort_values(by=group_date)
    return question

def load(data: pd.DataFrame,table: str):
    data.to_sql(table,conn,if_exists='replace',index=False)

def log(message: str):
    timestamp_format = '%H:%M:%S-%h-%d-%Y'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open('/home/aaron/Documentos/Data_Enginner_Program/Proyecto Data Engineering con Python/logs/dealership_logfile.txt','a') as f:
        f.write(timestamp + ', ' + message + '\n')

#####################################################
log("ETL Job started")

#####################################################
log("Extract phase started")
data_extract = extract()
log("Extract phase ended")

#####################################################
log("Transform phase by group started")
log("Transform phase answer1")
ans1 = transform_group(data_extract,['department_name'],"order_item_subtotal",False,False)
log("Transform phase answer2")
ans2 = transform_group(data_extract,['category_name'],"order_item_quantity",False,False)
log("Transform phase answer3")
ans3 = transform_group(data_extract,['customer_id','customer_fname','customer_lname'],"order_item_quantity",False,True)
log("Transform phase answer4")
ans4 =transform_group_date(data_extract,'order_date',"order_item_quantity")
log("Transform phase ended")
#####################################################
log("Load phase started")
log("Load phase answer1")
load(ans1,'answer1')
log("Load phase answer2")
load(ans2,'answer2')
log("Load phase answer3")
load(ans3,'answer3')
log("Load phase answer4")
load(ans4,'answer4')
log("Load phase Ended")
#####################################################
log("ETL Job ended")