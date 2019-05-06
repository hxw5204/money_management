from .database import db

# database


class Categories(db.Model):
    __tablename__ = 'categories'
    categories_id = db.Column(db.Integer, primary_key=True)
    categories = db.Column(db.String(32))


class Company(db.Model):
    __tablename__ = 'company'
    company_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(32))
    location = db.Column(db.String(100))


class CreditCard(db.Model):
    __tablename__ = 'credit_card'
    UID = db.Column(db.Integer)
    card_num = db.Column(db.Integer, primary_key=True)
    cvv = db.Column(db.Integer)
    exp_date = db.Column(db.String(16))


class TransactionInfo(db.Model):
    __tablename__ = 'transaction_info'
    TID = db.Column(db.Integer, primary_key=True)
    UID = db.Column(db.Integer)
    amount = db.Column(db.Float)
    categories_id = db.Column(db.Integer)
    T_date = db.Column(db.String(10))
    T_time = db.Column(db.String(10))
    campany_id = db.Column(db.Integer)
    type_id = db.Column(db.Integer)


class TransType(db.Model):
    __tablename__ = 'trans_type'
    type_id = db.Column(db.Integer, primary_key=True)
    trans_type = db.Column(db.String(32))


class UserInfo(db.Model):
    __tablename__ = 'user_info'
    UID = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(32))
    lastname = db.Column(db.String(32))
    type_id = db.Column(db.Integer)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(1))



