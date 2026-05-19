import pandas as pd

def make_connection_with_db():
    import mysql.connector

    connection_mydb = mysql.connector.connect(
    host='localhost',
    port=3360,
    user='root',
    password='',
    database='wp_ecommerce')

    cursor = connection_mydb.cursor(dictionary=True)
    return connection_mydb,cursor


def get_users_profiles():
    df = pd.DataFrame(columns=['user_id','country','age','gender'])
    _,cursor = make_connection_with_db()

    sql='SELECT ID FROM wp_users'

    cursor.execute(sql)

    users_results = cursor.fetchall()

    for user in users_results:
        user_id = user['ID']

        sql = "SELECT meta_value FROM wp_usermeta WHERE user_id=(%s) and meta_key='country'"

        param = (user_id, )

        cursor.execute(sql, param)

        result = cursor.fetchall()

        if result != None and len(result) > 0:
            country = result[0]['meta_value']

        else:
            country='Unknown'

        sql = "SELECT meta_value FROM wp_usermeta WHERE user_id=(%s) and meta_key='age'"

        param = (user_id, )

        cursor.execute(sql, param)

        result = cursor.fetchall()

        if result != None and len(result) > 0:
            age = result[0]['meta_value']

        else:
            age='Unknown'

        sql = "SELECT meta_value FROM wp_usermeta WHERE  user_id=(%s) and meta_key='gender'"

        param = (user_id, )

        cursor.execute(sql, param)

        result = cursor.fetchall()

        if result != None and len(result) > 0:
            gender = result[0]['meta_value']

        else:
            gender='Unknown'

        obj = {
            'user_id':[user['ID']],
            'country':[country],
            'age':[age],
            'gender':[gender],
        }

        df_obj = pd.DataFrame(obj)

        df = pd.concat([df,df_obj], ignore_index=True)

    df.drop(df[df['country']=='Unknown'].index)
    df.drop(df[df['age']=='Unknown'].index)
    df.drop(df[df['gender']=='Unknown'].index)

    df['age']=pd.to_numeric(df['age'])

    return df

            