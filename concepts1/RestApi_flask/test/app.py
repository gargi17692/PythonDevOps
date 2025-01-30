from flask import Flask
from flask_restful import Resource, Api

app=Flask(__name__)
api=Api(app)

employee_info ={
              "Radha": {
              "salary": "100k",
              "Technology": "Linux Admin"
                },
              "Krishnan": {
              "salary":"8k",
              "Technology": "Web Developer",
               }
             }

class Help(Resource):
     def get(self):
         help={
            "All Endpoints" : ["/api/v1/esinfo","/api/v1/esinfo/:ename"]
              }
         return help

class Employess(Resource):
     def get(self,ename=None):
         if ename:
              if ename in employee_info.keys():
                 return employee_info.get(ename)
              else:
                     message={
                      "message" : "Employee_Name not found"
                       }
                     return message
         return employee_info
     
api.add_resource(Help,"/")
api.add_resource(Employess,"/api/v1/esinfo","/api/v1/esinfo/<string:ename>")

app.run(port=5000,host="localhost")