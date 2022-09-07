from sqlalchemy import create_engine, MetaData

engine =create_engine("mysql+pymysql://root:AFern1091#@localhost/datapath_project")
meta = MetaData()
conn = engine.connect()