from restcrest.elements.user.user import User
from restcrest.elements.post.post import Post
from restcrest import db
class FetchPost():
    
    
    def getGlobalPosts(self):
        collection = db.postD.find()
        postSet = []
        for i in collection:
            print(i)
            i['user'] = User(db.userD.find_one({'_id': i['user']}))
            
            a = Post(i)
            postSet.append(a.getPostData())

        return postSet

