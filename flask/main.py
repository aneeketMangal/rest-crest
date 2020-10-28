from flask import Flask, request, render_template
from flask_restful import Api, Resource, reqparse, abort, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# below command wraps app as an api.
api = Api(app)
# creating a directory for SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.datab'
# below mentioned commands create a alchemy database
datab = SQLAlchemy(app)

class Models(datab.Model):
	id = datab.Column(datab.Integer, primary_key = True)
	name = datab.Column(datab.String(100), nullable = False)
	views = datab.Column(datab.Integer, nullable = False)
	likes = datab.Column(datab.Integer, nullable = False) 

	def __repr__(self):
		return f"Video(name = {name}, likes = {likes}, views = {views})"

# datab.create_all()
videoPutArgs = reqparse.RequestParser()
videoPutArgs.add_argument("name", type =str, help = "Error", required = True)
videoPutArgs.add_argument("views", type =int, help = "Error", required = True)
videoPutArgs.add_argument("likes", type =int, help = "Error", required = True)


videoUpdateArgs = reqparse.RequestParser()
videoUpdateArgs.add_argument("name", type =str, help = "Error")
videoUpdateArgs.add_argument("views", type =int, help = "Error")
videoUpdateArgs.add_argument("likes", type =int, help = "Error")

resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'views': fields.Integer,
	'likes': fields.Integer
}
datab.create_all()
# def videoDoesNotExists(video_id):
# 	if video_id not in videos:
# 		abort(404, message = "Video id is not valid try another")

# def videoDoesExists(video_id):
# 	if video_id in videos:
# 		abort(409, message = "Video already exists")



class Video(Resource):
	@marshal_with(resource_fields)
	# this is what happens when a get request is sent to a server
	def get(self, video_id):
		result = Models.query.filter_by(id = video_id).first()
		if not result:
			abort(404, message = "nothing found")
		return result

	@marshal_with(resource_fields)
	def put(self, video_id):
		
		args = videoPutArgs.parse_args()
		result = Models.query.filter_by(id = video_id).first()
		if result:
			abort(409, message = "pehle se hi hai yaar doosri try kar")
		video= Models(id = video_id, name = args["name"], views = args["views"], likes = args["likes"])
		
		datab.session.add(video)
		datab.session.commit()
		return video, 201

	@marshal_with(resource_fields)
	def patch(self, video_id):
		
		args = videoUpdateArgs.parse_args()
		result = Models.query.filter_by(id = video_id).first()
		if not result:
			abort(404, message = "video not founded")
		if args['name']:
			result.name = args['name']
		if args['views']:
			result.views = args['views']
		if args['likes']:
			result.likes = args['likes']

		datab.session.commit()
		return result

	def delete(self, video_id):
		videoDoesNotExists(video_id)
		del videos[video_id]
		return "", 204





	# def  put(self, video_id):
	# 	print()
    # GET  : to request data from the server.
	# PUT  : is a request method supported by HTTP used by the World Wide Web. The PUT method requests that the enclosed entity be stored under the supplied URI.
    # POST : to submit data to be processed to the server.

	# def post(self):
	# 	return {"data":"jio"}
api.add_resource(Video, "/video/<int:video_id>")

@app.route("/")
def home():
    return render_template("home.html")



# this is to know errors it is almost similar as we did in dart
if __name__ == '__main__':
    app.run(debug=True)



