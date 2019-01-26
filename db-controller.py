import psycopg2
import pandas as pd
try:
    connection = psycopg2.connect(user = "mnaoikjnojorsv",
                                  password = "dd47b86a853ec65e1a76a003a07d717ecfc20af547721d750042bafdfbf37520",
                                  host = "ec2-54-75-245-94.eu-west-1.compute.amazonaws.com",
                                  port = "5432",
                                  database = "df87fg6nok0dv8")
    cursor = connection.cursor()
    data = pd.read_csv('data.csv', header=0, index_col="№")
    for name in data["ФИО выпускника"]:
        ins_data = '''INSERT INTO qr_students(name, has_come) VALUES ('{}', 'f');'''.format(name)
        cursor.execute(ins_data)
        connection.commit()
        #response = cursor.fetchall()[0][0]

except (Exception, psycopg2.Error) as error :
    print ('ERR:', error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")