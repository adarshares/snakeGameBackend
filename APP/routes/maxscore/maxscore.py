from flask import Blueprint,request,jsonify,make_response
from sqlalchemy import func
from ...models import User
from ...models import db
from ...utils import JWT

mxscore_bp = Blueprint('mxscore',__name__,url_prefix='/mxscore')

@mxscore_bp.route("/")
@mxscore_bp.route("")
def mxscore():
    token = request.cookies.get("token")
    user = JWT.validator(token)
    if not user:
        resp = make_response((jsonify(message="incorrect request")))
        resp.headers.add("Content-Type","application/json")
        resp.status_code = 401
        return resp

    amscore = db.session.query(func.max(User.maxscore)).scalar()
    username = db.session.query(User).filter(User.maxscore == amscore).first().username
    if(user.maxscore == amscore):
        username = user.username 

    resp = make_response(jsonify({"username":username,"maxscore":amscore}))
    resp.headers.add("Content-Type","application/json")
    return resp

    #user = JWT.validator(token)

#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJhYmNkZWYifQ.HNw8jOMDkdxIbm-llAxym7GSHiMBA21liJ0JPCkhjAE