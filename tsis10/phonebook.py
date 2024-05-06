import psycopg2

try:

    connection = psycopg2.connect(
        database="postgres", 
        user="postgres", 
        password="12345", 
        host="127.0.0.1", 
        port="5432"
    )

    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")   

        print(f"Server version: {cursor.fetchone()}")

    # Создание таблицы
    aa = input("is table created? ")
    if aa == "no":
        with connection.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE phonebook(
                    name varchar NOT NULL,
                    phonenumber varchar NOT NULL PRIMARY KEY);"""
            )
    elif aa == 'yes':

        dd = input("add smt? ")
        if dd == "yes":
            # Добавление в таблицу из терминала
            x = str(input())
            y = str(input())
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""INSERT INTO phonebook (name, phonenumber) VALUES
                    ('{x}', '{y}');"""
                )

            # Добавление в таблицу из csv

            #with connection.cursor() as cursor:
                #cursor.execute("""COPY phonebook(name, phonenumber)
                                        #FROM 'C:\Users\Мирас\Desktop\KBTU\1 курс, 2 семестр\pp2\tsis10'
                                        #DELIMITER ','
                                        #CSV HEADER;""")
        elif dd == "no":
            bb = input('search smt? ')

            if bb == "yes":
                # Поиск 

                choice = str(input())
                if choice == "phonenumber":
                    x = str(input())
                    with connection.cursor() as cursor:
                        cursor.execute(
                            f"""SELECT * FROM phonebook WHERE phonenumber = '{x}';"""
                        )
                        print(cursor.fetchone())

                elif choice == "name":
                    x = str(input())
                    with connection.cursor() as cursor:
                        cursor.execute(f"""SELECT * FROM phonebook WHERE name = '{x}';""")
                        print(cursor.fetchone())
            elif bb == "no":
                cc = input("drop smt? ")
                if cc == "yes":
                    # Удаление

                    drop = str(input())
                    with connection.cursor() as cursor:
                        cursor.execute(f"""DELETE FROM phonebook WHERE name = '{drop}' OR phonenumber = '{drop}'""")                
                
except Exception as error:
    print("error:", error)

finally:
    if connection:
        connection.close()
        print("connection closed")