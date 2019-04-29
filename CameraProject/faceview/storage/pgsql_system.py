#!/usr/bin/python3

import psycopg2

#from .db_config import sql_connect_info
#from .db_config import create_connection
# from . import sql_connect_info
# from . import create_connection

# connect to the db
def create_connection():
    try:
        conn = psycopg2.connect("dbname='datahead' user='postgres' host='localhost' password='datahead'")
    except:
        print("I am unable to connect to the database")
    return conn



system_db = "system"

table_systemconfig = "face_system_config"      # name for config table
table_systemuser = "face_system_users"      # name for config table
table_customer = "customer"         # name for customer's table
table_customer_user = "face_customer_users"         # name for customer's users table
table_app_service = "app_service"   # name for customer's service/appkey table


'''
# ------------------------------------------------------------------------------
def check_table_system(tbl=table_systemconfig):
    cd = sql_connect_info(system_db)
    conn = create_connection(cd[0], cd[1], cd[2], cd[3], cd[4])
    cursor = conn.cursor()

    #SELECT EXISTS (SELECT table_name FROM information_schema.tables WHERE table_name = 'table_name');

    cursor.execute("SELECT relname FROM pg_class WHERE relname = %s", (tbl,))
    tbl_data = cursor.fetchone()

    # save the changes and cose the connection
    cursor.close()
    conn.commit()
    conn.close()

    return tbl_data

#test = check_systable()
#print("table info: ", test)


# ------------------------------------------------------------------------------
# insert new config
def add_sysconfig(field, def_value, sys_value=None, value_a=None, value_b=None, value_c=None, value_d=None, value_e=None):
    cd = sql_connect_info(system_db)
    conn = create_connection(cd[0], cd[1], cd[2], cd[3], cd[4])
    cursor = conn.cursor()

    if not sys_value:
        sys_value = def_value
    cursor.execute("INSERT INTO {tn} (config_item, default_value, system_value, custom_value_a, custom_value_b, \
                   custom_value_c, custom_value_d, custom_value_e) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                   .format(tn=table_systemconfig), (field, def_value, sys_value, value_a, value_b, value_c, value_d, value_e))

    # save the changes and cose the connection
    cursor.close()
    conn.commit()
    conn.close()

#add_sysconfig("xpath", "/home/liroy")


# ------------------------------------------------------------------------------
# update data in config table
def update_sysconfig(field, value=None):
    cd = sql_connect_info(system_db)
    conn = create_connection(cd[0], cd[1], cd[2], cd[3], cd[4])
    cursor = conn.cursor()

    cursor.execute("UPDATE {tn} SET system_value=%s WHERE config_item=%s".format(tn=table_systemconfig), (value, field))

    # save the changes and cose the connection
    cursor.close()
    conn.commit()
    conn.close()

#update_sysconfig("xpath", "/home/panshi/test")


# ------------------------------------------------------------------------------
# get config
def get_sysconfig(field, value="system_value"):
    cd = sql_connect_info(system_db)
    conn = create_connection(cd[0], cd[1], cd[2], cd[3], cd[4])
    cursor = conn.cursor()

    cursor.execute("SELECT {col} FROM {tn} WHERE config_item=%s".format(col=value, tn=table_systemconfig), (field,))
    row_data = cursor.fetchone()

    cursor.close()
    conn.close()

    if row_data:
        return row_data[0]
    else:
        return

#test = get_sysconfig("face_gallery_root", "custom_value_a")
#test = get_sysconfig("xpath")
#print(test)


# ------------------------------------------------------------------------------
# add new system-user
def add_sysuser(userID, userSecret, createdAt, userTz=1, userStatus=1, userType=1, authVer=1, Notes=None):
    cd = sql_connect_info(system_db)
    conn = create_connection(cd[0], cd[1], cd[2], cd[3], cd[4])
    cursor = conn.cursor()

    cursor.execute("INSERT INTO {tn} (user_id, user_secret, user_status, user_type, user_tz, created_at, \
                   auth_ver, notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" \
                   .format(tn=table_systemuser), (userID, userSecret, userStatus, userType,
                                                  userTz, createdAt, authVer, Notes))

    conn.commit()
    conn.close()


# ------------------------------------------------------------------------------
# get system-user details
def get_sysuser(userID):
    cd = sql_connect_info(system_db)
    conn = create_connection(cd[0], cd[1], cd[2], cd[3], cd[4])
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM {tn} WHERE user_id=%s".format(tn=table_systemuser), (userID,))
    row_data = cursor.fetchone()

    cursor.close()
    conn.close()

    return row_data

'''
# ------------------------------------------------------------------------------
# add customer
def add_customer(cusID=None, name=None, email=None, createdAt=None, rowID=None, tz=1, status=1, cusType=1,
                 company=None, phone=None, address1=None, address2=None, state=None, country=None,
                 last_access=None, Notes=None):

    # cd = sql_connect_info(system_db)
    # conn = create_connection(cd[0], cd[1], cd[2], cd[3], cd[4])
    conn = create_connection()
    cursor = conn.cursor()

    if rowID:
        cursor.execute("INSERT INTO {tn} (id, cus_id, cus_name, cus_email, cus_org, cus_phone, \
                       cus_address_1, cus_address_2, cus_state, cus_country, cus_tz, cus_enroll, \
                       cus_last_access, cus_status, cus_type, notes) \
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" \
                       .format(tn=table_customer), (rowID, cusID, name, email, company, phone,
                                                    address1, address2, state, country, tz, createdAt,
                                                    last_access, status, cusType, Notes))

    else:
        cursor.execute("INSERT INTO {tn} (cus_id, cus_name, cus_email, cus_org, cus_phone, \
                       cus_address_1, cus_address_2, cus_state, cus_country, cus_tz, cus_enroll, \
                       cus_last_access, cus_status, cus_type, notes) \
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" \
                       .format(tn=table_customer), (cusID, name, email, company, phone,
                                                    address1, address2, state, country, tz, createdAt,
                                                    last_access, status, cusType, Notes))

    cursor.close()
    conn.commit()
    conn.close()

    return "ok"

'''
# ------------------------------------------------------------------------------
# add user for customer
def add_customer_user(cusId, userId, userSecret, name, createdAt, email=None, mobile=None,
                      status=1, userType=1, authVer=1,  lastAccess=None, Notes=None):

    cd = sql_connect_info(system_db)
    conn = create_connection(cd[0], cd[1], cd[2], cd[3], cd[4])
    cursor = conn.cursor()

    cursor.execute("INSERT INTO {tn} (cus_id, user_id, user_secret, user_name, user_email, \
                   user_mobile, user_enroll, last_access, user_status, user_type, \
                   auth_ver, notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                   .format(tn=table_customer_user), (cusId, userId, userSecret, name, email, mobile,
                                                     createdAt, lastAccess, status, userType, authVer, Notes))

    cursor.close()
    conn.commit()
    conn.close()

    return "ok"


# ------------------------------------------------------------------------------
# update user profile of the customer
def update_customer_user(cusId, userId, userSecret=None, status=1, userType=1, name=None,
                         email=None, mobile=None, Notes=None):

    cd = sql_connect_info(system_db)
    conn = create_connection(cd[0], cd[1], cd[2], cd[3], cd[4])
    cursor = conn.cursor()

    if userSecret:
        cursor.execute("UPDATE {tn} SET user_status=%s, user_type=%s, user_secret=%s, user_name=%s, user_email=%s, \
                   user_mobile=%s WHERE cus_id=%s AND user_id=%s".format(tn=table_customer_user),
                       (status, userType, userSecret, name, email, mobile, cusId, userId))
    else:
        cursor.execute("UPDATE {tn} SET user_status=%s, user_type=%s, user_name=%s, user_email=%s, \
                   user_mobile=%s WHERE cus_id=%s AND user_id=%s".format(tn=table_customer_user),
                       (status, userType, name, email, mobile, cusId, userId))

    cursor.close()
    conn.commit()
    conn.close()

    return "ok"


# ------------------------------------------------------------------------------
# get customer details
def get_customer(cusID):
    cd = sql_connect_info(system_db)
    conn = create_connection(cd[0], cd[1], cd[2], cd[3], cd[4])
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM {tn} WHERE cus_id=%s".format(tn=table_customer), (cusID,))
    row_data = cursor.fetchone()

    cursor.close()
    conn.close()

    return row_data


# ------------------------------------------------------------------------------
# get customer list
def get_customer_list(per_page=0, start_from=0, sort_by="ASC"):
    cd = sql_connect_info(system_db)
    conn = create_connection(cd[0], cd[1], cd[2], cd[3], cd[4])
    cursor = conn.cursor()

    if per_page:
        cursor.execute("SELECT cus_id, cus_org FROM {tn} ORDER BY cus_org {sort} LIMIT {pp} \
        OFFSET {sf}".format(tn=table_customer, sort=sort_by, pp=per_page, sf=start_from))
    else:
        cursor.execute("SELECT cus_id, cus_org FROM {tn} ORDER BY cus_org {sort}"
                       .format(tn=table_customer, sort=sort_by))

    row_data = cursor.fetchall()

    #print("customer list: ", row_data)
    #print("customer count: ", count)
    #print("customer id 1: ", row_data[1][0])

    cursor.close()
    conn.close()

    return row_data


# ------------------------------------------------------------------------------
# get customer-user details
def get_customer_user(cusID, userID):
    cd = sql_connect_info(system_db)
    conn = create_connection(cd[0], cd[1], cd[2], cd[3], cd[4])
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM {tn} WHERE cus_id=%s AND user_id=%s".format(tn=table_customer_user), (cusID, userID,))
    row_data = cursor.fetchone()

    cursor.close()
    conn.close()

    if row_data:
        return row_data
    else:
        return False



# ------------------------------------------------------------------------------
# generate new customer id
def gen_customer_id():
    config_start_id = int(get_sysconfig("app_customer_start_id"))

    cd = sql_connect_info(system_db)
    conn = create_connection(cd[0], cd[1], cd[2], cd[3], cd[4])
    cursor = conn.cursor()

    cursor.execute("SELECT max(id) from {tn}".format(tn=table_customer))
    row_id = cursor.fetchone()[0]

    if row_id:
        row_id = int(row_id)
        if row_id < config_start_id:
            cus_id = config_start_id
        elif row_id == config_start_id:
            cus_id = config_start_id + 1
        else:
            cus_id = row_id + 1
    else:
        cus_id = config_start_id

    cursor.close()
    conn.close()

    #print("row_id: ", row_id)
    #print("cus_id: ", cus_id)

    return int(cus_id)


# ------------------------------------------------------------------------------
# generate new app service-id
def gen_app_id():
    config_start_id = int(get_sysconfig("app_service_start_id"))

    cd = sql_connect_info(system_db)
    conn = create_connection(cd[0], cd[1], cd[2], cd[3], cd[4])
    cursor = conn.cursor()

    cursor.execute("SELECT max(id) from {tn}".format(tn=table_app_service))
    row_id = cursor.fetchone()[0]

    if row_id:
        row_id = int(row_id)
        if row_id < config_start_id:
            app_id = config_start_id
        elif row_id == config_start_id:
            app_id = config_start_id + 1
        else:
            app_id = row_id + 1
    else:
        app_id = config_start_id

    cursor.close()
    conn.close()

    #print("row_id: ", row_id)
    #print("app_id: ",app_id)

    return int(app_id)


# ------------------------------------------------------------------------------
# add new app id/key
def add_app_service(cusId=None, appId=None, appKey=None, createdAt=None, appExpire=None, appRenewable=0,
                    rowId=0, authVer=1, status=1, lastAccess=None, notes=None):

    cd = sql_connect_info(system_db)
    conn = create_connection(cd[0], cd[1], cd[2], cd[3], cd[4])
    cursor = conn.cursor()

    if rowId:
        cursor.execute("INSERT INTO {tn} (id, cus_id, app_id, app_key, app_created, app_expire, app_renewable, \
                       last_access, app_status, auth_ver, notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                       .format(tn=table_app_service), (rowId, cusId, appId, appKey, createdAt, appExpire,
                                                       appRenewable, lastAccess, status, authVer, notes))

    else:
        cursor.execute("INSERT INTO {tn} (cus_id, app_id, app_key, app_created, app_expire, app_renewable, \
                       last_access, app_status, auth_ver, notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                       .format(tn=table_app_service), (cusId, appId, appKey, createdAt, appExpire, appRenewable,
                                                       lastAccess, status, authVer, notes))

    cursor.close()
    conn.commit()
    conn.close()

    return "ok"

# ------------------------------------------------------------------------------
# get app-id/key details
def get_app_service(appID):
    row_data = None
    cd = sql_connect_info(system_db)
    conn = create_connection(cd[0], cd[1], cd[2], cd[3], cd[4])
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM {tn} WHERE app_id=%s".format(tn=table_app_service), (appID,))
    row_data = cursor.fetchone()

    cursor.close()
    conn.close()

    return row_data


# ------------------------------------------------------------------------------
# create table
def create_config_db_table():
    cd = sql_connect_info(system_db)
    conn = create_connection(cd[0], cd[1], cd[2], cd[3], cd[4])
    cursor = conn.cursor()

    # create table for app-service
    cursor.execute("CREATE TABLE IF NOT EXISTS {tn} \
              (id  SERIAL PRIMARY KEY, \
               config_item  VARCHAR(50)  NOT NULL, \
               default_value  VARCHAR(100), \
               system_value  VARCHAR(100), \
               custom_value_a  VARCHAR(100), \
               custom_value_b  VARCHAR(100), \
               custom_value_c  VARCHAR(100), \
               custom_value_d  VARCHAR(100), \
               custom_value_e  VARCHAR(100))"
               .format(tn=table_systemconfig))

    # create table for system users
    cursor.execute("CREATE TABLE IF NOT EXISTS {tn} \
              (id  SERIAL PRIMARY KEY, \
               user_id  VARCHAR(50)  NOT NULL, \
               user_secret  VARCHAR(128)  NOT NULL, \
               user_status  INTEGER  NOT NULL, \
               user_type  INTEGER  NOT NULL, \
               user_tz  INTEGER  NOT NULL, \
               created_at  TIMESTAMP  NOT NULL, \
               auth_ver  INTEGER  NOT NULL, \
               notes  TEXT)"
               .format(tn=table_systemuser))

    # create table for customers
    cursor.execute("CREATE TABLE IF NOT EXISTS {tn} \
              (id  SERIAL PRIMARY KEY, \
               cus_id  VARCHAR(10) NOT NULL, \
               cus_name  VARCHAR(50) NOT NULL, \
               cus_email  VARCHAR(50) NOT NULL, \
               cus_org  VARCHAR(100), \
               cus_phone  VARCHAR(20), \
               cus_address_1  VARCHAR(100), \
               cus_address_2  VARCHAR(100), \
               cus_state  VARCHAR(50), \
               cus_country  VARCHAR(50), \
               cus_tz  INTEGER  NOT NULL, \
               cus_enroll  TIMESTAMP  NOT NULL, \
               cus_last_access  TIMESTAMP, \
               cus_status  INTEGER  NOT NULL, \
               cus_type  INTEGER  NOT NULL, \
               notes  TEXT)"
               .format(tn=table_customer))

    cursor.execute("CREATE TABLE IF NOT EXISTS {tn} \
              (id  SERIAL PRIMARY KEY, \
               cus_id  VARCHAR(12) NOT NULL, \
               user_id  VARCHAR(20) NOT NULL, \
               user_secret  VARCHAR(128) NOT NULL, \
               user_name  VARCHAR(50) NOT NULL, \
               user_email  VARCHAR(50), \
               user_mobile  VARCHAR(20), \
               user_enroll  TIMESTAMP  NOT NULL, \
               last_access  TIMESTAMP, \
               user_status  INTEGER  NOT NULL, \
               user_type  INTEGER  NOT NULL, \
               auth_ver  INTEGER  NOT NULL, \
               notes  TEXT)"
               .format(tn=table_customer_user))

    cursor.execute("CREATE TABLE IF NOT EXISTS {tn} \
              (id  SERIAL PRIMARY KEY, \
               cus_id  VARCHAR(12) NOT NULL, \
               app_id  VARCHAR(12) NOT NULL, \
               app_key  VARCHAR(128) NOT NULL, \
               app_created  TIMESTAMP  NOT NULL, \
               app_expire  TIMESTAMP  NOT NULL, \
               app_renewable  INTEGER  NOT NULL, \
               last_access  TIMESTAMP, \
               app_status  INTEGER  NOT NULL, \
               auth_ver  INTEGER  NOT NULL, \
               notes  TEXT)"
               .format(tn=table_app_service))

    # close communication with the PostgreSQL database server
    cursor.close()

    # save the changes
    conn.commit()
    conn.close()


#create_config_db_table()

'''
