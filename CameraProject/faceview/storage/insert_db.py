from .pgsql_system import create_connection, table_app_service

# ------------------------------------------------------------------------------
# add new app id/key
def app_service(cusId=None, appId=None, appKey=None, createdAt=None, appExpire=None, appRenewable=0,
                    rowId=0, authVer=1, status=1, lastAccess=None, notes=None):

    conn = create_connection()
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