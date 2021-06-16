from restcrest import db

class PostDatabase():

    def addPost(self, user:str, content:str, dateTime:str):
        postdata = {'user':user, 'content':content, 'date':dateTime}
        db.postD.insert_one(postdata)

