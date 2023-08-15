from app import app
from dotenv import load_dotenv
import os
import psycopg2
import psycopg2.extras

load_dotenv()

config = {
    "host": os.getenv("YUGABYTE_HOST"),
    "port": os.getenv("YUGABYTE_PORT"),
    "dbName": os.getenv("YUGABYTE_DATABASE"),
    "dbUser": os.getenv("YUGABYTE_USER"),
    "dbPassword": os.getenv("YUGABYTE_PASSWORD"),
    "sslMode": "",
    "sslRootCert": os.getenv("CRT_ADDR"),
}


def main(conf):
    print(">>>> Connecting to YugabyteDB!")

    try:
        if conf["sslMode"] != "":
            yb = psycopg2.connect(
                host=conf["host"],
                port=conf["port"],
                database=conf["dbName"],
                user=conf["dbUser"],
                password=conf["dbPassword"],
                sslmode=conf["sslMode"],
                sslrootcert=conf["sslRootCert"],
                connect_timeout=10,
            )
        else:
            yb = psycopg2.connect(
                host=conf["host"],
                port=conf["port"],
                database=conf["dbName"],
                user=conf["dbUser"],
                password=conf["dbPassword"],
                connect_timeout=10,
            )
    except Exception as e:
        print("Exception while connecting to YugabyteDB")
        print(e)
        exit(1)

    print(">>>> Successfully connected to YugabyteDB!")
    # bulk_insert(yb)
    # insert_user(yb)
    # update_user(yb)
    # select_users(yb)
    # delete_user(yb)
    # select_users(yb)
    yb.close()


def select_users(yb):
    print(">>>> Selecting users")

    with yb.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as yb_cursor:
        yb_cursor.execute("SELECT * FROM users where user_id < 20")

        results = yb_cursor.fetchall()
        for row in results:
            print(
                "first name = {first_name}, last name = {last_name}, email = {email}".format(
                    **row
                )
            )


# def bulk_insert(yb):
#     data = """

# """
#     data = data.replace("'", "")
#     lines = data.strip().split("\n")
#     data_list = [line.split(",") for line in lines]

#     try:
#         with yb.cursor() as yb_cursor:
#             for d in data_list:
#                 stmt = f"INSERT INTO users (user_id, first_name, middle_name, last_name, email, phone_number, iscandidate) VALUES ({d[0]},'{d[1]}', '{d[2]}','{d[3]}','{d[4]}','{d[5]}',{d[6]})"

#                 yb_cursor.execute(stmt)
#         yb.commit()
#         print(">>>> Successfully inserted into the table")
#     except Exception as e:
#         print(e)


def insert_user(yb):
    try:
        with yb.cursor() as yb_cursor:
            stmt = "INSERT INTO users (user_id, first_name, middle_name, last_name, email, phone_number, iscandidate) VALUES (6, 'Yash', 'Gandhi','yash@test.com', '12345677890', 'www.yashgandhi.com')"

            yb_cursor.execute(stmt)
            print(">>>> Successfully inserted into the table")
    except Exception as e:
        print(e)


def update_user(yb):
    stmt = "UPDATE users SET email = 'newemail@example.com', phone_number = '9876543210' WHERE user_id = 1;"
    try:
        with yb.cursor() as yb_cursor:
            yb_cursor.execute(stmt)
            print(">>>> Successfully Updated")
    except Exception as e:
        print("Error occured while update")
        print(e)


def delete_user(yb):
    stmt = "DELETE FROM users WHERE user_id = 6"
    try:
        with yb.cursor() as yb_cursor:
            yb_cursor.execute(stmt)
            print(">>>> Successfully deleted")
    except Exception as e:
        print("Error occured while performing delete")
        print(e)


if __name__ == "__main__":
    main(config)
    app.run(debug=True)
