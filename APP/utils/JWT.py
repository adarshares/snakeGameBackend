from ..models import User
import jwt

 
class JWT:
    def tokenizer(data):
        encoded_jwt = jwt.encode(data, "secret", algorithm="HS256")
        return encoded_jwt
    def validator(data):
        try:
            info = jwt.decode(data, "secret", algorithms=["HS256"])
        except:
            return None
        username = info.get("username") 
        password = info.get("password")
        user =  User.query.filter_by(username=username).first()
        if not user:
            return None
        
        if user.password != password:
            return None

        return user