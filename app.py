from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into country (name) values (:name)",hey)
        user = query_db('select * from country')

        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")


    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_city", methods=["GET","POST"])
def add_one_city():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into city (name,country_id) values (:name,:country_id)",hey)
        user = query_db('select * from city')

        return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from city')
    one_user = query_db("select * from city limit 1", one=True)
    return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)

@app.route("/add_one_sql_girl_not_part", methods=["GET","POST"])
def add_one_sql_girl_not_part():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslessql_query_controller= query_db("select * from sql_query_controller")

        one_user = query_db("insert into sql_girl_not_part (not_condition,is_not_applied,sql_query_controller_id) values (:not_condition,:is_not_applied,:sql_query_controller_id)",hey)
        user = query_db('select * from sql_girl_not_part')

        return render_template("sql_girl_not_partform.html", sql_girl_not_parts=user, one_user=one_user, the_title="add new sql_girl_not_part", touslessql_query_controller=touslessql_query_controller)


    touslessql_query_controller= query_db("select * from sql_query_controller")

    user = query_db('select * from sql_girl_not_part')
    one_user = query_db("select * from sql_girl_not_part limit 1", one=True)
    return render_template("sql_girl_not_partform.html", sql_girl_not_parts=user, one_user=one_user, the_title="add new sql_girl_not_part", touslessql_query_controller=touslessql_query_controller)

@app.route("/add_one_sql_boy_part", methods=["GET","POST"])
def add_one_sql_boy_part():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslessql_query_controller= query_db("select * from sql_query_controller")

        one_user = query_db("insert into sql_boy_part (positive_conditions,select_clause,sql_query_controller_id) values (:positive_conditions,:select_clause,:sql_query_controller_id)",hey)
        user = query_db('select * from sql_boy_part')

        return render_template("sql_boy_partform.html", sql_boy_parts=user, one_user=one_user, the_title="add new sql_boy_part", touslessql_query_controller=touslessql_query_controller)


    touslessql_query_controller= query_db("select * from sql_query_controller")

    user = query_db('select * from sql_boy_part')
    one_user = query_db("select * from sql_boy_part limit 1", one=True)
    return render_template("sql_boy_partform.html", sql_boy_parts=user, one_user=one_user, the_title="add new sql_boy_part", touslessql_query_controller=touslessql_query_controller)

@app.route("/add_one_rails_view_guard", methods=["GET","POST"])
def add_one_rails_view_guard():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesrails_controller= query_db("select * from rails_controller")

        one_user = query_db("insert into rails_view_guard (view_template_path,layout_format,is_rendered,rails_controller_id) values (:view_template_path,:layout_format,:is_rendered,:rails_controller_id)",hey)
        user = query_db('select * from rails_view_guard')

        return render_template("rails_view_guardform.html", rails_view_guards=user, one_user=one_user, the_title="add new rails_view_guard", touslesrails_controller=touslesrails_controller)


    touslesrails_controller= query_db("select * from rails_controller")

    user = query_db('select * from rails_view_guard')
    one_user = query_db("select * from rails_view_guard limit 1", one=True)
    return render_template("rails_view_guardform.html", rails_view_guards=user, one_user=one_user, the_title="add new rails_view_guard", touslesrails_controller=touslesrails_controller)

@app.route("/add_one_rails_controller", methods=["GET","POST"])
def add_one_rails_controller():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesweb_development_route= query_db("select * from web_development_route")

        one_user = query_db("insert into rails_controller (controller_name,action_name,before_action_filters,web_development_route_id) values (:controller_name,:action_name,:before_action_filters,:web_development_route_id)",hey)
        user = query_db('select * from rails_controller')

        return render_template("rails_controllerform.html", rails_controllers=user, one_user=one_user, the_title="add new rails_controller", touslesweb_development_route=touslesweb_development_route)


    touslesweb_development_route= query_db("select * from web_development_route")

    user = query_db('select * from rails_controller')
    one_user = query_db("select * from rails_controller limit 1", one=True)
    return render_template("rails_controllerform.html", rails_controllers=user, one_user=one_user, the_title="add new rails_controller", touslesweb_development_route=touslesweb_development_route)

@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into user (username,phone,email,password,country_id) values (:username,:phone,:email,:password,:country_id)",hey)
        user = query_db('select * from user')

        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['username','phone','email','password','country_id']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['username','phone','email','password','country_id']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['username','phone','email','password','country_id']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_street", methods=["GET","POST"])
def add_one_street():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescity= query_db("select * from city")

        one_user = query_db("insert into street (name,city_id) values (:name,:city_id)",hey)
        user = query_db('select * from street')

        return render_template("streetform.html", streets=user, one_user=one_user, the_title="add new street", touslescity=touslescity)


    touslescity= query_db("select * from city")

    user = query_db('select * from street')
    one_user = query_db("select * from street limit 1", one=True)
    return render_template("streetform.html", streets=user, one_user=one_user, the_title="add new street", touslescity=touslescity)

@app.route("/add_one_station", methods=["GET","POST"])
def add_one_station():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescity= query_db("select * from city")

        one_user = query_db("insert into station (city_id,name) values (:city_id,:name)",hey)
        user = query_db('select * from station')

        return render_template("stationform.html", stations=user, one_user=one_user, the_title="add new station", touslescity=touslescity)


    touslescity= query_db("select * from city")

    user = query_db('select * from station')
    one_user = query_db("select * from station limit 1", one=True)
    return render_template("stationform.html", stations=user, one_user=one_user, the_title="add new station", touslescity=touslescity)

@app.route("/add_one_display_rule", methods=["GET","POST"])
def add_one_display_rule():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesweb_development_route= query_db("select * from web_development_route")

        one_user = query_db("insert into display_rule (display_mode,title,description,web_development_route_id) values (:display_mode,:title,:description,:web_development_route_id)",hey)
        user = query_db('select * from display_rule')

        return render_template("display_ruleform.html", display_rules=user, one_user=one_user, the_title="add new display_rule", touslesweb_development_route=touslesweb_development_route)


    touslesweb_development_route= query_db("select * from web_development_route")

    user = query_db('select * from display_rule')
    one_user = query_db("select * from display_rule limit 1", one=True)
    return render_template("display_ruleform.html", display_rules=user, one_user=one_user, the_title="add new display_rule", touslesweb_development_route=touslesweb_development_route)

@app.route("/add_one_pedestrian_route", methods=["GET","POST"])
def add_one_pedestrian_route():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesstreet= query_db("select * from street")

        touslesuser= query_db("select * from user")

        one_user = query_db("insert into pedestrian_route (lat,lon,street_id,user_id) values (:lat,:lon,:street_id,:user_id)",hey)
        user = query_db('select * from pedestrian_route')

        return render_template("pedestrian_routeform.html", pedestrian_routes=user, one_user=one_user, the_title="add new pedestrian_route", touslesstreet=touslesstreet, touslesuser=touslesuser)


    touslesstreet= query_db("select * from street")

    touslesuser= query_db("select * from user")

    user = query_db('select * from pedestrian_route')
    one_user = query_db("select * from pedestrian_route limit 1", one=True)
    return render_template("pedestrian_routeform.html", pedestrian_routes=user, one_user=one_user, the_title="add new pedestrian_route", touslesstreet=touslesstreet, touslesuser=touslesuser)

@app.route("/add_one_sql_query_controller", methods=["GET","POST"])
def add_one_sql_query_controller():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesweb_development_route= query_db("select * from web_development_route")

        one_user = query_db("insert into sql_query_controller (web_development_route_id,query,description) values (:web_development_route_id,:query,:description)",hey)
        user = query_db('select * from sql_query_controller')

        return render_template("sql_query_controllerform.html", sql_query_controllers=user, one_user=one_user, the_title="add new sql_query_controller", touslesweb_development_route=touslesweb_development_route)


    touslesweb_development_route= query_db("select * from web_development_route")

    user = query_db('select * from sql_query_controller')
    one_user = query_db("select * from sql_query_controller limit 1", one=True)
    return render_template("sql_query_controllerform.html", sql_query_controllers=user, one_user=one_user, the_title="add new sql_query_controller", touslesweb_development_route=touslesweb_development_route)

@app.route("/add_one_afficher", methods=["GET","POST"])
def add_one_afficher():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into afficher (affichage,web_development_route,title,description) values (:affichage,:web_development_route,:title,:description)",hey)
        user = query_db('select * from afficher')

        return render_template("afficherform.html", affichers=user, one_user=one_user, the_title="add new afficher")


    user = query_db('select * from afficher')
    one_user = query_db("select * from afficher limit 1", one=True)
    return render_template("afficherform.html", affichers=user, one_user=one_user, the_title="add new afficher")

@app.route("/add_one_webapp", methods=["GET","POST"])
def add_one_webapp():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into webapp (name,user_id,description) values (:name,:user_id,:description)",hey)
        user = query_db('select * from webapp')

        return render_template("webappform.html", webapps=user, one_user=one_user, the_title="add new webapp", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from webapp')
    one_user = query_db("select * from webapp limit 1", one=True)
    return render_template("webappform.html", webapps=user, one_user=one_user, the_title="add new webapp", touslesuser=touslesuser)

@app.route("/add_one_waypoint", methods=["GET","POST"])
def add_one_waypoint():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslespedestrian_route= query_db("select * from pedestrian_route")

        one_user = query_db("insert into waypoint (lat,lon,sequence_order,pedestrian_route_id) values (:lat,:lon,:sequence_order,:pedestrian_route_id)",hey)
        user = query_db('select * from waypoint')

        return render_template("waypointform.html", waypoints=user, one_user=one_user, the_title="add new waypoint", touslespedestrian_route=touslespedestrian_route)


    touslespedestrian_route= query_db("select * from pedestrian_route")

    user = query_db('select * from waypoint')
    one_user = query_db("select * from waypoint limit 1", one=True)
    return render_template("waypointform.html", waypoints=user, one_user=one_user, the_title="add new waypoint", touslespedestrian_route=touslespedestrian_route)

@app.route("/add_one_web_development_route", methods=["GET","POST"])
def add_one_web_development_route():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        tousleswebapp= query_db("select * from webapp")

        one_user = query_db("insert into web_development_route (name,webapp_id,description) values (:name,:webapp_id,:description)",hey)
        user = query_db('select * from web_development_route')

        return render_template("web_development_routeform.html", web_development_routes=user, one_user=one_user, the_title="add new web_development_route", tousleswebapp=tousleswebapp)


    tousleswebapp= query_db("select * from webapp")

    user = query_db('select * from web_development_route')
    one_user = query_db("select * from web_development_route limit 1", one=True)
    return render_template("web_development_routeform.html", web_development_routes=user, one_user=one_user, the_title="add new web_development_route", tousleswebapp=tousleswebapp)

@app.route("/add_one_train_conductor", methods=["GET","POST"])
def add_one_train_conductor():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslespublic_transportation_route= query_db("select * from public_transportation_route")

        one_user = query_db("insert into train_conductor (name,fm,public_transportation_route_id,pic) values (:name,:fm,:public_transportation_route_id,:pic)",hey)
        user = query_db('select * from train_conductor')

        return render_template("train_conductorform.html", train_conductors=user, one_user=one_user, the_title="add new train_conductor", touslespublic_transportation_route=touslespublic_transportation_route)


    touslespublic_transportation_route= query_db("select * from public_transportation_route")

    user = query_db('select * from train_conductor')
    one_user = query_db("select * from train_conductor limit 1", one=True)
    return render_template("train_conductorform.html", train_conductors=user, one_user=one_user, the_title="add new train_conductor", touslespublic_transportation_route=touslespublic_transportation_route)

@app.route("/add_one_public_transportation_route", methods=["GET","POST"])
def add_one_public_transportation_route():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesweb_development_route= query_db("select * from web_development_route")

        touslespedestrian_route= query_db("select * from pedestrian_route")

        touslesdeparture_station= query_db("select * from departure_station")

        one_user = query_db("insert into public_transportation_route (mean_of_transportation,web_development_route_id,pedestrian_route_id,destination,departure_station_id) values (:mean_of_transportation,:web_development_route_id,:pedestrian_route_id,:destination,:departure_station_id)",hey)
        user = query_db('select * from public_transportation_route')

        return render_template("public_transportation_routeform.html", public_transportation_routes=user, one_user=one_user, the_title="add new public_transportation_route", touslesweb_development_route=touslesweb_development_route, touslespedestrian_route=touslespedestrian_route, touslesdeparture_station=touslesdeparture_station)


    touslesweb_development_route= query_db("select * from web_development_route")

    touslespedestrian_route= query_db("select * from pedestrian_route")

    touslesdeparture_station= query_db("select * from departure_station")

    user = query_db('select * from public_transportation_route')
    one_user = query_db("select * from public_transportation_route limit 1", one=True)
    return render_template("public_transportation_routeform.html", public_transportation_routes=user, one_user=one_user, the_title="add new public_transportation_route", touslesweb_development_route=touslesweb_development_route, touslespedestrian_route=touslespedestrian_route, touslesdeparture_station=touslesdeparture_station)

@app.route("/add_one_query_log", methods=["GET","POST"])
def add_one_query_log():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslessql_query_controller= query_db("select * from sql_query_controller")

        one_user = query_db("insert into query_log (executed_query,executed_at,sql_query_controller_id) values (:executed_query,:executed_at,:sql_query_controller_id)",hey)
        user = query_db('select * from query_log')

        return render_template("query_logform.html", query_logs=user, one_user=one_user, the_title="add new query_log", touslessql_query_controller=touslessql_query_controller)


    touslessql_query_controller= query_db("select * from sql_query_controller")

    user = query_db('select * from query_log')
    one_user = query_db("select * from query_log limit 1", one=True)
    return render_template("query_logform.html", query_logs=user, one_user=one_user, the_title="add new query_log", touslessql_query_controller=touslessql_query_controller)

