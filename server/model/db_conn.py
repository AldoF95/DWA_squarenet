from pony.orm import *
from config import db_params as par

db = Database()
db.bind(provider= par["provider"], user=par["user"], password=par["password"], host=par["host"], database=par["database"])
