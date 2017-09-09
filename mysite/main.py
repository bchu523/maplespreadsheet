from flask import Flask, request, redirect, jsonify, session,render_template,url_for
import os
from werkzeug.utils import secure_filename
from flask import Flask, session
#from flask.ext.session import Session
from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
import json
from flask import Flask, render_template, request, flash, session, redirect, url_for, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
#from flask_migrate import Migrate
from models import *

#engine = create_engine('sqlite:///test.db', echo=True)
#app = Flask(__name__)
#app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
#SESSION_TYPE = 'filesystem'
#app.config.from_object(__name__)
#Session(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#db = SQLAlchemy(app)
#from table import User
#class User(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(80), unique=True)
#I    password = db.Column(db.String(120), unique=True)

 #   def __init__(self, username, email):
 #j       self.username = username
  #      self.password = password

# Check Configuration section for more details
#SESSION_TYPE = 'sqlalchemy'
#app.config.from_object(__name__)
#Session(app)

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="maplespreadsheet",
    password="mewmew79",
    hostname="maplespreadsheet.mysql.pythonanywhere-services.com",
    databasename="maplespreadsheet$votr",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
db.create_all(app=app)
# load config from the config file we created earlier
#votr.config.from_object('config')

#db = SQLAlchemy(votr)


@app.route("/addlink",methods=['POST'])
def add_link():
    if request.method == 'POST':
        # get the poll and save it in the database
        entry = request.get_json(force=True)



        spritename = entry['sprite']['name'][0]
        spritetitle = entry['sprite']['title'][0]
        spritenamestatus = int(entry['sprite']['name'][1])
        spritetitlestatus = int(entry['sprite']['title'][1])



        spritequery = Sprite.query.filter_by(title=spritetitle)
        if spritequery.count() == 0 and spritenamestatus == -1 and not spritename == "":
            new_sprite = Sprite(name=spritename,title=spritetitle)
            db.session.add(new_sprite)
            db.session.commit()
        elif not spritenamestatus == -1:
             new_sprite = spritequery.first()
             spritequery = Sprite.query.filter_by(id = spritenamestatus).first();
             if not spritename =="":
                spritequery.name = spritename
             if not spritetitle == "":
                spritequery.title = spritetitle

             db.session.commit()
        else:
            new_sprite = spritequery.first()








        equip = entry['equip']
        equiptooltip = equip['tooltip']
        equipicon = equip['icon']
        equiptooltipstatus = equiptooltip[1]
        equipiconstatus = equipicon[1]
        tooltipquery = Tooltip.query.filter_by(id = equiptooltipstatus).first()
        iconquery = Icon.query.filter_by(id = equipiconstatus,sprite_id= new_sprite.id).first()
        if tooltipquery is None :
               tooltipquery = Tooltip(name = equiptooltip[0])
               db.session.add(tooltipquery)
               db.session.commit()
        else:
               tooltipquery.name = equiptooltip[0]
               db.session.commit()

        if iconquery is None :
                iconquery = Icon(name=equipicon[0],sprite_id=new_sprite.id,tooltip_id=tooltipquery.id)
                db.session.add(iconquery)
                db.session.commit()
        else :
                iconquery.name = equipicon[0]
                db.session.commit()




    result ={"sprite": {"id":new_sprite.id},"tooltip": {"id": tooltipquery.id},"icon":{"id": iconquery.id }}

    print(result)
    return jsonify(result)



@app.route("/deletelink",methods=["POST"])
def delete_link():
        entry = request.get_json()

        equipicon = int(entry['id'])
        iconquery = Icon.query.filter_by(id= equipicon).first();

        #iconquery = Icon.query.first();
        tooltipquery = Tooltip.query.filter_by(id = iconquery.tooltip_id).first();



        db.session.delete(iconquery)
        if tooltipquery is not None:
            db.session.delete(tooltipquery)
        db.session.commit()

        return jsonify({'message': 'Deleted succesfully'})

@app.route("/updatetooltip",methods=["Post"])
def update_tooltip():
        entry = request.get_json()
        id = entry['id']
        name = entry['name']
        tooltipquery = Tooltip.query.filter_by(id = id).first();
        tooltipquery.name = name
        db.session.commit()
        return jsonify({'message': 'Tooltip updated succesfully'})





@app.route("/readlink",methods=["GET"])
def read_link():
        spritequery = Sprite.query.all()
        #result ={rows:[{"sprite": {"name":"sprite","title":"title"},"equip": [{"tooltip": "tooltip", "icon":"icon" }]} ]}
        result = {"rows":[]}
        row={"sprite": {"name":None,"title":None},"equip": []}
        for sprite in spritequery:

            iconquery = Icon.query.filter_by(sprite_id=sprite.id).all();

            row1 = {"sprite": {"id":None,"name":None,"title":None},"equip": []}
            if not sprite.name == "":

                    row1["sprite"]["name"] = sprite.name
                    row1["sprite"]["title"] = sprite.title
                    row1["sprite"]["id"] = sprite.id

            for icon in iconquery:
                    if not icon.tooltip is None:

                        row1["equip"].append({"tooltip_id":icon.tooltip.id, "tooltip_name":icon.tooltip.name,"icon_id":icon.id,"icon_name":icon.name})
                    else:

                        row1["equip"].append({"tooltip_id":"", "tooltip_name":"","icon_id":icon.id,"icon_name":icon.name})


            result["rows"].append(row1)

        return jsonify(result)




@app.route("/")
def index():
    return redirect("/static/index.html")










