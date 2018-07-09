from flask import *
import datetime
import time
from models import connection,cur
from functools import wraps
import jwt
import pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'brybzlee'

@app.route ('/',methods=['GET'])
def home():
    return jsonify({'message' : 'welcome home techies'})

@app.route ('/register',methods=['POST'])
def register():
    name=request.get_json()["name"]
    username=request.get_json()["username"]
    email=request.get_json()["email"]
    password=request.get_json()["password"]
    try:
        with connection.cursor() as cursor:
            sql ="INSERT INTO `users`(`name`,`username`,`email`,`password`)VALUES(%s, %s, %s, %s)"
            try:
                cursor.execute("SELECT * FROM users WHERE username = %s;", username)
                if cursor.fetchone() is not None:
                    return jsonify({'message':'username exists'})
                else:
                    cursor.execute(sql, (name, username, email, password))
                    #return jsonify({'message' : 'you are succesfully registered'})
            except:
                return jsonify({'meassage' : 'you are not succesfully registered'})
        connection.commit()
    except:
        pass
    return jsonify({'message' : 'you are succesfully registered'})

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token') 

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 403

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message' : 'Token is invalid!'}), 403

        return f(*args, **kwargs)

    return decorated



@app.route('/login',methods=['POST'])
def log_in():
    username=request.get_json()["username"]
    password=request.get_json()["password"]
    cur.execute("SELECT COUNT(1) FROM users WHERE username = %s;", username) # CHECKS IF USERNAME EXSIST
    if cur.fetchone()[0]:
        cur.execute("SELECT password FROM users WHERE username = %s;", username) # FETCH THE PASSWORD
        for row in cur.fetchall():
            if password == row[0]:
                token = jwt.encode({'username' : username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
                return jsonify({'message' : 'Login successful','token' : token.decode('UTF-8')})
            else:
                return jsonify({'message' : 'wrong password'})
    else:
        return jsonify({'message' : 'Username does not exist'})
    cur.close()


@app.route ('/comments',methods=['POST','GET'])
@token_required
def comments():
    comment=request.get_json()["comment"]
    username=request.get_json()["username"]
    try:
        with connection.cursor() as cursor:
            sql ="INSERT INTO `comments`(`username`,`comment`)VALUES(%s, %s)"
            try:
                cursor.execute("SELECT * FROM users WHERE username = %s;", username)
                if cursor.fetchone() is not None:
                    cursor.execute(sql, (username, comment))
                else:
                    return jsonify({'message' : 'you are not a registered user'})
            except:
                return jsonify({'message' : 'comment not posted'})
        connection.commit()
    finally:
        pass
    return jsonify({'message' : 'your comment is succesfully posted'})


@app.route ('/get_comments', methods=['GET'])
@token_required
def get_comments():
    cur.execute("SELECT * FROM comments")
    rows=cur.fetchall()
    return jsonify(rows)

    

@app.route ('/delete_comments/<int:commentID>', methods=['DELETE','POST'])
@token_required
def delete_comments(commentID):
    username=request.get_json()["username"]
    try:
        with connection.cursor() as cursor:
            sql="DELETE FROM `comments` WHERE `comments`.`commentID`="+str(commentID)+"and `comments`.`username`= '"+username+"'"
            try:
                if username == commentID:
                    cursor.execute(sql)
                else:
                   return jsonify({'message' : 'you are not authorised to delete this message'})
            except:
                return jsonify({'message' : 'you are not a registered user'})
        connection.commit()
    except:
        pass
    return jsonify({'message' : 'comment deleted'})

@app.route ('/get_users', methods=['GET'])
@token_required
def get_users():
    cur.execute("SELECT * FROM users")
    rows=cur.fetchall()
    return jsonify(rows)

if __name__== '__main__':
    app.run(debug=True)