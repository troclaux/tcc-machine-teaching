import os
import pandas as pd
from tqdm import tqdm
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

# Connect to the MySQL server
#cnx = mysql.connector.connect(user='root', password='RootSenha', host='127.0.0.1', database='tcc_machine_teaching')
#cnx = mysql.connector.connect(user='root', password='RootSenha', host='127.0.0.1')
url_object = db.URL.create(
    "mysql+pymysql",
    username="root",
    password="RootSenha",  # plain (unescaped) text
    host="127.0.0.1",
    database="tcc_machine_teaching",
)
engine = db.create_engine(url_object)
#engine = db.create_engine("mysql://root:RootSenha@127.0.0.1/tcc_machine_teaching")

Session = sessionmaker(engine)

#cnx.autocommit = True

# Create a cursor to execute SQL statements
#cursor = cnx.cursor(buffered=True)

# Connect to the MySQL Database
#cursor.execute("USE tcc_machine_teaching")

directory = os.getcwd()
path_csv = os.path.join(directory, "CSV")
pwd_list = sorted(os.listdir(path_csv))
with Session() as session:
	for i, filename in enumerate(tqdm(pwd_list)):
		#if "solution" in filename:
		#	problem_id = filename[9:-3]
		path = os.path.join(path_csv, filename)
		df = pd.read_csv(path)
		filename = filename[:-4]
		df.to_sql(con=engine, name=filename, if_exists='replace', method='multi', index=False)
		#elif "test" in filename:
		#	problem_id = filename[5:-3]
		session.commit()

#save_tests_output("input",820)