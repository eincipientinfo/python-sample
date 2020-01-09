from pymongo import MongoClient # import mongo client to connect  
import pprint  
# Creating instance of mongoclient  
client = MongoClient()  
# Creating database  
db = client.javatpoint  
employee = {"id": "101",  
"name": "Peter",  
"profession": "Software Engineer",  
}  
# Creating document  
employees = db.employees  
# Inserting data  
employees.insert_one(employee)  
# Fetching data  
pprint.pprint(employees.find_one())  