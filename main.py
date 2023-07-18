import uuid
from flask import *
from flask_cors import CORS
import sqlite3
import random
import os
app = Flask(__name__)
cors = CORS(app)

conn = sqlite3.connect('phone_numbes.db')

c = conn.cursor()



c.execute('''CREATE TABLE IF NOT EXISTS people (
            id integer primary key autoincrement,
            username text unique,
            password varchar
            ) ''')

c.execute('''CREATE TABLE IF NOT EXISTS posts (
            id integer primary key autoincrement,
            user_id integer ,
            title text,
            text text
            ) ''')

c.execute('''CREATE TABLE IF NOT EXISTS products (
            id integer primary key autoincrement,
            user_id integer,
            product_name text,
            product_price integer,
            image1 varchar,
            image2 varchar,
            image3 varchar
            ) ''')

c.execute('''CREATE TABLE IF NOT EXISTS ids (
            id integer,
            token integer
            ) ''')




c.execute('''CREATE TABLE IF NOT EXISTS details (
            name varchar primary key,
            slogan text ,
            banner text

            ) ''')





@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/myHome', methods=['GET'])
def myHome():
    conn = sqlite3.connect('phone_numbes.db')
    c = conn.cursor()
    token = request.cookies.get('token')
    print(token)
    c.execute(f'select id from ids where token={token}')
    user_id = c.fetchall()[0][0]
    print(user_id) 
    c.execute(f'select username from people where id = {user_id}')
    name = c.fetchall()[0][0]
    print(f"{name=}")

    c.execute(f'select id,product_name, product_price, image1 from products where user_id = {user_id}')
    products_raw = c.fetchall()
    print(f"{products_raw=}")
    products = []
    # print(user_id)
    # if 
    if len(products_raw):
        for i in products_raw:
            product_id = i[0]
            product_name = i[1]
            product_price = i[2]
            product_image = f"/static/imgs/{i[3]}.jpg"
            product_tuple = ( product_name, product_price, product_image, product_id)
            products.append(product_tuple)


    # if 
    slogan = 'slogan'
    url = 'url'



    c.execute(f'select slogan, banner from details where name = "{name}"')
    details = c.fetchall()
    if len(details):
        slogan = details[0][1]
        url = details[0][0]

    print(f'{products=}')
    conn.commit()
    c.close()
    conn.close()
    print(url)
    print(slogan)
    return render_template('myHome.html', name=name, slogan=slogan, logo_url=url, products=products)


@app.route('/product/<int:number>', methods=['GET'])
def product_overview(number):
    conn = sqlite3.connect('phone_numbes.db')
    c = conn.cursor()

    c.execute(f'select image1, image2, image3 from products where id = {number} ')
    images_raw = c.fetchall()
    if not len(images_raw):
        conn.commit()
        c.close()
        conn.close()
        return render_template('noProduct.html')
        


    c.execute(f'select product_name, product_price from products where id = {number}')
    product_info = c.fetchall()[0]
    

    images_raw = images_raw[0]
    images = []
    for i in images_raw:
        images.append(f'/static/imgs/{i}.jpg')

    conn.commit()
    c.close()
    conn.close()

    print(f"{images=}")
    print(f"{product_info=}")
    return render_template('productView.html', images=images, name_price = product_info)




@app.route('/home/<name>', methods=['GET'])
def userHome(name):
    conn = sqlite3.connect('phone_numbes.db')
    c = conn.cursor()

    c.execute(f'select id from people where username = "{name}" ')
    user_id = c.fetchall()
    if not len(user_id):
        conn.commit()
        c.close()
        conn.close()
        return render_template('noUser.html')
    user_id = user_id[0][0]
    c.execute(f'select id, product_name, product_price, image1 from products where user_id = {user_id}')
    products_raw = c.fetchall()
    products = []
    # print(user_id)
    # if 
    if len(products_raw):
        for i in products_raw:
            product_name = i[1]
            product_price = i[2]
            product_image = f"/static/imgs/{i[3]}.jpg"
            product_id = i[0]
            product_tuple = (product_name, product_price, product_image, product_id)
            print(f"{product_tuple=}")
            products.append(product_tuple)
            

    slogan = 'slogan'
    url = 'url'
    c.execute(f'select slogan, banner from details where name = "{name}"')
    details = c.fetchall()
    if len(details):
        slogan = details[0][0]
        url = details[0][1]
    

    conn.commit()
    c.close()
    conn.close()

    if url != "banner":
        return render_template('userHome.html', name=name, slogan=slogan, logo_url=f"/static/imgs/{url}.jpg", products = products)
    else:
        return render_template('userHome.html', name=name, slogan=slogan, logo_url="/static/banner.png", products = products)







# *****************************************************************
@app.route('/home', methods=['GET'])
def home():
    conn = sqlite3.connect('phone_numbes.db')
    c = conn.cursor()



    c.execute(f'select * from details')
    users_raw = c.fetchall()
    users = []
    for i in users_raw:
        name = i[0]
        slogan = i[1]
        if i[2] != "banner":
            banner = f"/static/imgs/{i[2]}.jpg"
        else:
            banner = "static/banner.png"

        users.append((name, slogan, banner))
        


    

    conn.commit()
    c.close()
    conn.close()

    print(users)
    return render_template('home.html',users = users)



# *****************************************************************







@app.route('/add', methods=['GET'])
def add():
    return render_template('add.html')

@app.route('/asdf', methods=['GET'])
def asdf():
    return render_template('asdf.html')


@app.route('/singin', methods=['GET'])
def singin():
    return render_template('singin.html')



@app.route('/login', methods=['GET'])
def login():
     return render_template('login.html')



@app.route("/signup", methods=['POST'])
def signup():
    conn = sqlite3.connect('phone_numbes.db')
    c = conn.cursor()
    json_info = request.get_json()
    to_add = json_info['to_add']
    # print(f'{to_add=}')
    username = to_add[0]
    password = to_add[1]

    # c.execute('select ')


    try:
        c.execute(f'''INSERT INTO people VALUES (NULL, "{username}", "{password}","{username}","https://i.pinimg.com/originals/1e/f8/15/1ef8156889dba99417ff2b3a6d99988d.jpg") ''')
    except:
            json_obj = jsonify({"added": 'unsuccefully'})
            resp = make_response(json_obj, 200) 
            conn.commit()
            c.close()
            conn.close()
            return resp
    
    # print(list_of_transactions)

     

    
    json_obj = jsonify({"added": 'succefully'})
    resp = make_response(json_obj, 200) 
    conn.commit()
    c.close()
    conn.close()
    return resp



@app.route("/homepage", methods=['POST'])
def homepage():
    conn = sqlite3.connect('phone_numbes.db')
    c = conn.cursor()
    cookie = request.cookies.get('token')
    print(f'{cookie=}')
    if cookie:
        print('there is cookie')
        
        token = request.cookies.get('token')
        print(token)    
        c.execute('SELECT * FROM ids')
        account = c.fetchall()
        acc_id = account
        token = account
        print(f"{acc_id=}")

        if len(acc_id):
            c.execute(f'SELECT username FROM PEOPLE WHERE id = {acc_id[0][0]}')
        else:
            c.execute('SELECT * FROM ids WHERE FALSE')
        name = c.fetchall()
        print(name)

        
        if len(name):
            json_obj = jsonify(name[0][0])
            resp = make_response(json_obj, 200)
            conn.commit()
            c.close()
            conn.close()
            return resp
        else:
            json_obj = jsonify("None")






@app.route("/singinFunction", methods=['POST'])
def singinfunc():
    conn = sqlite3.connect('phone_numbes.db')
    c = conn.cursor()
    json_info = request.get_json()
    password = json_info["password"]
    username = json_info["name"]
    try:
        c.execute(f'insert into people values (null, "{username}","{password}")')
        c.execute(f'insert into details values("{username}", "Blooming Beauty Delivered to Your Doorstep! ", "banner")')
        
        json_obj = "success"
    except:
        json_obj = "faliure"
    resp = make_response(json_obj, 200)
    conn.commit()
    c.close()
    conn.close()
    return resp





# @app.route("/homeProducts", methods=['POST'])
# def home_posts():
#     print('hello mir manera krutit mir')
#     conn = sqlite3.connect('phone_numbes.db')
#     c = conn.cursor()

#     args = request.args.get("name")
#     print(f"{args=}")
    


#     json_obj = "faliure"
#     resp = make_response(json_obj, 200)
#     conn.commit()
#     c.close()
#     conn.close()
#     return resp





@app.route("/update", methods=['POST'])
def update():
    conn = sqlite3.connect('phone_numbes.db')
    c = conn.cursor()
    request
    data = request.form['data']
    slogan = ''
    file = ''

    token = request.cookies.get('token')
    c.execute(f'select id from ids where token = {token}')
    user_id = c.fetchall()[0][0]

    c.execute(f'select username from people where id = {user_id}')
    name = c.fetchall()[0][0]

    if data:
        json_info = json.loads(data)
        slogan = json_info['slogan']

    # print(f"{slogan=}")
    file = request.files.get('file')
    # print(f"{file=}")+6

    token = request.cookies.get('token')
    c.execute(f'select id from ids where token = {token}')
    user_id = c.fetchall()[0][0]

    c.execute(f'select username from people where id = {user_id}')
    name = c.fetchall()[0][0]


    c.execute(f'select banner from details where name = "{name}"')
    old_file = c.fetchall()[0][0]
    print(old_file)
    file_path = f'./static/imgs/{old_file}.jpg'
    

    if file and slogan:
        unique_id = str(uuid.uuid4())[:8]
        file.save(f'./static/imgs/{unique_id}.jpg')
        c.execute('')


        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"The file {file_path} has been deleted.")
        else:
            print(f"The file {file_path} does not exist.")

        print(f"{name=}")
        print(f"{slogan=}")
        print(f"{unique_id=}")
        # c.execute('insert or ignore into details values')
        c.execute(f'update details set slogan = "{slogan}", banner = "{unique_id}" where name = "{name}"')
        json_obj = "updated"
        # c.execute(update )
    
    elif slogan and not file:
        c.execute(f'update details set slogan = "{slogan}" where name = "{name}"')
        json_obj = "updated slogan"
    
    elif file and not slogan:
        unique_id = str(uuid.uuid4())[:8]
        file.save(f'./static/imgs/{unique_id}.jpg')
       
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"The file {file_path} has been deleted.")
        else:
            print(f"The file {file_path} does not exist.")
       
        c.execute(f'update details set banner = "{unique_id}" where name = "{name}"')
        json_obj = "updated banner"
    
    else:
        json_obj = "failed to update"

    resp = make_response(json_obj, 200)
    conn.commit()
    c.close()
    conn.close()
    return resp




@app.route("/loginFunction", methods=['POST'])
def login_function  ():
    conn = sqlite3.connect('phone_numbes.db')
    c = conn.cursor()
    json_info = request.get_json()
    to_add = json_info['to_add']
    # print(f'{to_add=}')
    username = to_add[0]
    password = to_add[1]
    token = random.randrange(1000,9999)

    c.execute(f'SELECT id FROM people WHERE username="{username}" AND password = "{password}"')
    account = c.fetchall()
    c.execute('DELETE FROM ids')





    if len(account):    
        json_obj = jsonify('successfuly')
        resp = make_response(json_obj, 200)
        resp.set_cookie('token',f"{token}")
        c.execute(f'INSERT INTO ids VALUES ({account[0][0]},{token})')
        
    else:
        json_obj = jsonify('unsuccessfuly')
        resp = make_response(json_obj, 200)
        
    conn.commit()
    c.close()
    conn.close()
    return resp
         





@app.route("/logout", methods=['POST'])
def logout():
    print('hello world')
    conn = sqlite3.connect('phone_numbes.db')
    c = conn.cursor()
    cookie = request.cookies.get('token')
    print(cookie)
    if cookie:
        c.execute(f'delete from ids where token = {cookie}')
    conn.commit()
    c.close()
    conn.close()
    json_obj = jsonify('deleted')
    resp = make_response(json_obj,200)
    resp.delete_cookie('token')
    return resp



@app.route("/profilepage", methods=['POST'])
def profilepage():
    conn = sqlite3.connect('phone_numbes.db')
    c = conn.cursor()
    json_info = request.get_json()
    token = json_info['to_add'][6:]
    print(token)
    c.execute(f"select id from ids where token={token}")
    id = c.fetchall()[0][0]
    print(id)

    c.execute(f"select * from people where id = {id}")
    profile = c.fetchall()
    print(f'{profile=}')
    url = profile[0][4]
    name = profile[0][3]
    print(f"{url=}")
    json_obj = jsonify({"url": f'{url}',"name":f"{name}"})
    resp = make_response(json_obj,200)
    conn.commit()
    c.close()
    conn.close()
    return resp



@app.route('/upload', methods=["POST"])
def upload():
    conn = sqlite3.connect('phone_numbes.db')
    c = conn.cursor()
    files = request.files.getlist('files[]')
    json_data = request.form['data']
    json_info = json.loads(json_data)
    # json = jsonify(json)
    print(f"{json_info=}")
    price = json_info["price"]
    name = json_info["name"]
    token = request.cookies.get('token')
    c.execute(f'select id from ids where token = "{token}"')
    user_id = c.fetchall()[0][0]
    print(user_id)
    ids = []
    
    for i in range(len(files)):
        unique_id = str(uuid.uuid4())[:8]
        ids.append(unique_id)

    print(f"{ids=}")
    
    print(f"{name=}")
    print(f"{price=}")



    c.execute(f'insert into products values (NULL, {user_id}, "{name}", {price}, "{ids[2]}", "{ids[1]}", "{ids[0]}")')

    for i,file in enumerate(files):

        file.save(f'./static/imgs/{ids[i-1]}.jpg')
    conn.commit()
    c.close()
    conn.close()
    return 'File uploaded successfully!'






@app.route("/remove", methods=['POST'])
def remove():
    conn = sqlite3.connect('phone_numbes.db')
    c = conn.cursor()
    json_info = request.get_json()
    print(json_info)
    product_id = json_info["id"]
    try:
        c.execute(f'delete from products where id = {product_id}')
        resp = make_response("deleted", 200)
    except:
        resp = make_response('error',200)
    conn.commit()
    c.close()
    conn.close()
    return resp


app.run(debug=True)
conn.commit()
c.close()


