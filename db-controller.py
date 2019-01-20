import psycopg2
try:
    connection = psycopg2.connect(user = "mnaoikjnojorsv",
                                  password = "dd47b86a853ec65e1a76a003a07d717ecfc20af547721d750042bafdfbf37520",
                                  host = "ec2-54-75-245-94.eu-west-1.compute.amazonaws.com",
                                  port = "5432",
                                  database = "df87fg6nok0dv8")
    cursor = connection.cursor()
    id = 1
    #insert_data = 'DO $$ BEGIN IF (SELECT has_come from qr_students WHERE id = '+ id + ') THEN RAISE NOTICE "has_come";ELSE IF ((SELECT COUNT(*) from qr_students WHERE id = '+ id + ') > 0) THEN UPDATE qr_students SET has_come = "t" WHERE id = '+ id + '; RAISE NOTICE "true"; ELSE RAISE NOTICE "no"; END IF; END IF; END $$;'
    ins_data = '''SELECT has_come from qr_students WHERE id = {};'''.format(id)
    cursor.execute(ins_data)
    connection.commit()
    response = cursor.fetchall()[0][0]

except (Exception, psycopg2.Error) as error :
    print ('ERR:', error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")