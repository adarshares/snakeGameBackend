from flask import Blueprint,request,jsonify,make_response
from .login import login_bp
from .logout import logout_bp
from .maxscore import score_bp
from .userinfo import uinfo_bp

base_bp = Blueprint('base',__name__,url_prefix="/api")

base_bp.register_blueprint(login_bp)
base_bp.register_blueprint(logout_bp)
base_bp.register_blueprint(score_bp)
base_bp.register_blueprint(uinfo_bp)


@base_bp.route("")
@base_bp.route("/")
def userinfo():
    print(uinfo_bp._blueprints)
    resp = make_response(jsonify(message="dekhojara"))
    resp.headers.add("Content-Type","application/json")
    return resp
