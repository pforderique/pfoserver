from flask import jsonify, request
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from bson.objectid import ObjectId
from pymongo import MongoClient
from .config import MONGO_URI

#cluster = MongoClient(MONGO_URI)
#airchat_db = cluster['airchat']

#users = airchat_db['users']

#? PARSE FORM! -- like parse_form() method in AirPiano I made, it does it easily
#user_put_args = reqparse.RequestParser()
#user_put_args.add_argument("name", type=str, help="Name is required", required=True)
#user_put_args.add_argument("age", type=int, help="Age is required", required=True)
#user_put_args.add_argument("followers", type=int, help="follower count is required", required=True) # else defaulted to None if not required

#? PARSE FORM! -- all optional paramaters -- 'None' if not given
#video_update_args = reqparse.RequestParser()
#video_update_args.add_argument("name", type=str, help="Name of the video is required")
#video_update_args.add_argument("views", type=int, help="Views of the video is required")
#video_update_args.add_argument("likes", type=int, help="Likes on the video is required") # else defaulted to None if not required

user_resource_fields = {
	'_id': fields.String,
	'name': fields.String,
   'age':fields.Integer,
   'followers':fields.Integer,
}

class User(Resource):
    # serialize this return value (object) using these resource fields: 
    # @marshal_with(user_resource_fields) 
    def get(self, id:str):
        return "nice! issue with mongo thens"
        # #result = users.find_one({"_id":ObjectId(id)})

        # if not result:
        #     abort(404, message="404 error - could not find user with that id")

        # return result, 200

    # #* PUT takes in identifier and creates or updates info based on it
    # @marshal_with(user_resource_fields) 
    # def put(self, id:str):
    #     args = user_put_args.parse_args()

    #     result = users.find_one({"_id":ObjectId(id)})

    #     if result:
    #         users.replace_one({'_id':ObjectId(id)}, args)
    #     else:
    #         users.insert_one(args)

    #     result = users.find_one({"_id":ObjectId(id)})
        
    #     return result, 201 # 201 means created

    # #* POST autogenerate an ID for em
    # @marshal_with(user_resource_fields) 
    # def post(self):
    #     args = user_put_args.parse_args()
    #     _id = users.insert_one(args).inserted_id # returns ObjectId("...")
        
    #     result = users.find_one({"_id":_id})

    #     return result, 201

    # @marshal_with(user_resource_fields)
    # def patch(self, video_id):
    #     args = video_update_args.parse_args()
    #     result = VideoModel.query.filter_by(id=video_id).first()
    #     if not result:
    #         abort(404, message="404 error - Video doesn't exist, cannot update")

    #     if args['name']:
    #         result.name = args['name']
    #     if args['views']:
    #         result.views = args['views']
    #     if args['likes']:
    #         result.likes = args['likes']

    #     db.session.commit() # commit the changes. we dont re"add" object.
    
    #     return result

    # @marshal_with(user_resource_fields)
    # def delete(self, video_id):
    #     result = VideoModel.query.filter_by(id=video_id).first_or_404(description=f"video with id {video_id} not found.")
    #     db.session.delete(result)
    #     db.session.commit()
    #     return '', 204 # 204 = No Content -- signifies deleted successfully 

