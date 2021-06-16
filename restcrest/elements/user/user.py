from flask_login import UserMixin
from restcrest import db
class User(UserMixin):
    def __init__(self, userdata:dict):
        self.__id = userdata["_id"]
        self.__username = userdata['username']
        self.__pfp = userdata['pfp']
        self.__password = userdata['password']
        self.__validated = userdata['validated']
        self.__friends = userdata['friends']

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.__id

    @classmethod
    def get_by_id(self, id):
        data = db.userD.find_one({"_id":id})
        if(data):
            return data
        else:
            return None

    def getInfo(self):
        return {
            'id': str(self.__id),
            'username': str(self.__username), 
            'pfp': str(self.__pfp),
            'friends': self.__friends,
            'validated': str(self.__validated), 
            'password': str(self.__password), 
            # 'validation': str(self.__validated)
        }

    def getUserName(self):
        return self.__username

    def getProfilePhotoPath(self):
        return self.__pfp

    def getValidation(self):
        return self.__validation

    def setUserName(self, newUserName:str):
        self.__username = newUserName

    def setProfilePhotoPath(self, newpfp:str):
        self.__pfp = newpfp

    def setValidated(self):
        self.__validated = True

    def getId(self):
        return self.__id

    def checkUser(self, password:str):
        return password == self.__password  

    



