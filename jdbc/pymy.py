import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='ctedb',
    cursorclass=pymysql.cursors.DictCursor
)
try:
    with connection.cursor() as cursor:

        create_query = """
                CREATE TABLE IF NOT EXISTS employee1(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(45),
                    department VARCHAR(100));
        """
        cursor.execute(create_query)

        #insert data

        insert_query = """
                INSERT INTO employee1 (name,department) VALUES (%s,%s)
        """
        values = [("JOhn","IT"),("Alice","HR"),("Bob","Finance")]
        cursor.executemany(insert_query,values)
        connection.commit()

        select_query = "select * from employee1"
        cursor.execute(select_query)

        result = cursor.fetchall()

        for row in result:
            print(row)
finally:
    connection.close()