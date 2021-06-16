from restcrest.elements.user.user import User
from restcrest import db
import json

from bson import json_util
class UserDatabase():
    


    def test(self):
        db.test.insert_one({'info':'success'})

    def getById(self, id:str):
        return db.userD.find_one({'_id': id})

    def addUser(self, username:str, password:str, pfp = "https://www.seekpng.com/png/detail/143-1435868_headshot-silhouette-person-placeholder.png"):
        userdata = {'username':username, 'pfp':pfp, 'friends': [], 'validated': False, 'password': password}
        db.userD.insert_one(userdata)

    def checkUserNameAvailability(self, username:str):
        if(db.userD.find_one({'username': username})):
            return {'isAvailable': False, 'errorLog': "Username is already Taken"}

    def checkEmailAvailability(self, email:str):
        if(db.userD.find_one({'email': email})):
            return {'isAvailable': False, 'errorLog': "Email is already Taken"}

    def checkUserAvailability(self, username:str, email:str):
        if(db.userD.find_one({'username': username})):
            return {'isAvailable': False, 'errorLog': "Username is already Taken"}
        elif(db.userD.find_one({'email': email})):
            return {'isAvailable': False, 'errorLog': "Email is already Taken"}
        else:
            return {'isAvailable': True}

    def __getUserData(self, username:str, password:str):
        try:
            return db.userD.find_one({'username': username, 'password': password})
        except:
            return {'errorLog': 'Server Error'}



    def verifyUserDetails(self, username:str, password:str):
        isUser = self.__getUserData(username, password)
        if(isUser):
            return {'isAvailable': True ,'userData': json.loads(json_util.dumps(isUser))}
        
        else:
            return {'isAvailable': False, 'errorLog': "User details not verfied"}

    
