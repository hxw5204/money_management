from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from backend.main.api import User, CreditCardInfo, Transaction, CategoryRatio, CurrentTime,test,Prediction,AveMonthlyExp,CategoryPredict 
from .main.database import db

def create_app():
    app = Flask(__name__)

    # avoid cross-site request forgery(CSRF)
    CORS(app)
    app.config.from_object('backend.config.setting.ProductionConfig')
    #app.config.from_object('backend.config.secure')
    db.init_app(app)
    api = Api(app)
    api.add_resource(User,'/<int:UID>/userInfo')
    api.add_resource(CreditCardInfo,'/<int:UID>/creditCardInfo')
    api.add_resource(Transaction,'/<int:UID>/transactions')
    api.add_resource(CategoryRatio,'/<int:UID>/categoryRatio')
    api.add_resource(CurrentTime,'/currentTime')
    api.add_resource(test,'/test')
    api.add_resource(Prediction,'/<int:UID>/prediction')
    api.add_resource(AveMonthlyExp,'/<int:UID>/aveMonthlyExp')
    api.add_resource(CategoryPredict,'/<int:UID>/categoryPredict')

    return app