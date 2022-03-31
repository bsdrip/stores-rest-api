from database import db


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(80))
    passwd = db.Column(db.String(255))

    def __init__(self, uname, passwd):
        self.uname = uname
        self.passwd = passwd

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_uname(cls, uname):
        return cls.query.filter_by(uname=uname).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
