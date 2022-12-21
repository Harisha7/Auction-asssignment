
# Create Environment
# pip install flask
# pip install pymysql
# pip install flask-mysql

from flask import Flask, jsonify, request, session
import pymysql
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY="secret_sauce",
    SESSION_COOKIE_HTTPONLY=True,
    REMEMBER_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Strict",
)

# connect database
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Ayukta@Rithika2'
app.config['MYSQL_DATABASE_DB'] = 'assignment'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)


# login
@app.route("/app/login", methods=["POST"])
def login():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        bind = (request.json['email'], request.json['password'])
        cursor.execute(query, bind)
        user = cursor.fetchone()        
        if user['email']:
            session['user'] = user
            return jsonify({"login": True})
    except Exception as e:
        return jsonify({"login": False})
    finally:
        cursor.close()
        conn.close()

@app.route("/app/users",methods=["POST"])
def insert_users():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        query = "INSERT INTO users set firstname = %s, lastname = %s, email = %s, password = %s"
        bind = (request.json['firstname'], request.json['lastname'], request.json['email'], request.json['password'])
        cursor.execute(query, bind)
        conn.commit()
        user = cursor.fetchall()
        # user = cursor.fetchone() 
        # if user['email']:
        #     session['user'] = user
        return jsonify({"data": cursor.lastrowid})
    except Exception as e:
        print(e)
        return jsonify({"error couldnot type user"})
    finally:
        cursor.close()
        conn.close()
       


# check if logged in
@app.route("/app/login", methods=["GET"])
def check_session():
    if session.get('user'):
        return jsonify({"login": True})

    return jsonify({"login": False})


# logout
@app.route("/app/login", methods=["DELETE"])
def logout():
    session['user'] = {}
    return jsonify({"logout": True})


# get current user
@app.route("/app/users", methods=["GET"])
def user_data():
    if session.get('user'):
        return jsonify(session['user'])

    return jsonify({"login": False})


# this route should only work if logged in
@app.route("/app/protected-data", methods=["GET"])
def protected_data():
    if session.get('user'):
        return jsonify({"get-this-data": "Only if logged in"})

    return jsonify({"login": False})


# login
@app.route("/app/updatebid", methods=["POST"])
def update_bid():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try: 
        query ="SELECT price, id FROM bids WHERE auction_item = %s ORDER BY price LIMIT 1"
        bind = (request.json['auction_item'])
        cursor.execute(query, bind)
        biditem = cursor.fetchone()
        if not (biditem["id"] == request.json["id"]):
            if biditem["price"] < request.json["price"]:
                query = "UPDATE bids SET price = %s WHERE auction_item = %s"
                bind = (request.json['price'],request.json['auction_item'])
                cursor.execute(query, bind)
                conn.commit()
                return jsonify({"updated": "your bid have been registred! " })
            else: 
                return jsonify({"updated": "you need to have a higher bid! " })
        else:
            return jsonify({"updated": "you cannot bid on your own items" })
    except Exception as e:
        return jsonify({"update": str(e)})
    finally:
        cursor.close()
        conn.close()    


@app.route("/app/additem", methods=["POST"])
def add_item():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        query = "INSERT INTO auction_items(name, description, start_time, end_time) VALUES (%s, %s, %s, %s)"
        bind = (request.json['name'],request.json['description'],request.json['start_time'],request.json['end_time'])
        cursor.execute(query, bind)
        conn.commit()    
        return jsonify({"additem": True })
    except Exception as e:
        return jsonify({"additem": str(e)})
    finally:
        cursor.close()
        conn.close()

@app.route('/api/getlistitem', methods=['GET'])
def get_List_Item():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        query = "SELECT id, name, SUBSTRING(description, 1,18) FROM auction_items"
        cursor.execute(query)
        rows = cursor.fetchall()
        return jsonify({"data":rows})
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/api/getitem', methods=['GET'])
def get_Item():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        query = "SELECT * FROM auction_items WHERE id =%s"
        bind = (request.json['id'])
        cursor.execute(query, bind)
        rows = cursor.fetchall()
        return jsonify({"data":rows})
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/api/getitemwithpicture', methods=['GET'])
def get_Item_With_Picture():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        query = "SELECT name, description, start_time, end_time, images.url FROM auction_items left join images on images.auction_item = auction_item"
        cursor.execute(query)
        rows = cursor.fetchall()
        return jsonify({"AUCTIONITEMWITHIMAGES":rows})
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/api/getcurrentbid', methods=['GET'])
def get_Current_Bid():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        query = "SELECT start_time, end_time, bids.price, auction_item.id FROM auction_items LEFT JOIN bids ON bids.user = bids.id"
        cursor.execute(query)
        rows = cursor.fetchall()
        return jsonify({"CURRENTBID":rows})
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/api/getfivelatestbids', methods=['GET'])
def get_Five_LatestBids():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        query = "SELECT * FROM bids JOIN item ON auction_item = auction_item.id WHERE item.id = 1 ORDER BY price DESC LIMIT 5"
        cursor.execute(query)
        rows = cursor.fetchall()
        return jsonify({"getfivelatestbids":rows})
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# this route should work even if you are not logged in
@app.route("/api/unprotected-data", methods=["GET"])
def unprotected_data():
    return jsonify({"get-this-data": "Even if you are logged out"})





if __name__ == "__main__":
    app.run(debug=True, load_dotenv=True)
