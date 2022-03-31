from models.user import UserModel


def authenticate(uname, passwd):
    user = UserModel.find_by_uname(uname)
    if user and user.passwd == passwd:
        return user


def identity(payload):
    uid = payload['identity']
    return UserModel.find_by_id(uid)
