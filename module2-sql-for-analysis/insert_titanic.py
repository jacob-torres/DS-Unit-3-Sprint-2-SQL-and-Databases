"""
    This module uses psycopg2 to connect to a remote PostgreSQL database,
    and insert data from the titanic csv file.
"""

import psycopg2

# Credentials for ElephantSQL database
DB_NAME = 'jojzcyqd'
DB_USER = 'jojzcyqd'
DB_PASSWORD = 'f-PptvD0r84jKBo0ecoTlXoay8n3_fei'
DB_HOST = 'otto.db.elephantsql.com'


def insert_titanic():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )

        print("Successfully connected to database!")

        cur = conn.cursor()

        # Queries
        create_sex_enum = "create type sex as enum ('female', 'male');"

        create_table = """create table titanic (
            Survived int,
            Pclass int,
            Name varchar (110) not null,
            Sex sex,
            Age real,
            Siblings_and_Spouses int,
            Parents_and_Children int,
            Fare real);
        """

        # Create sex type and empty titanic table
        cur.execute(create_sex_enum)
        cur.execute(create_table)
        print("Successfully created 'titanic' table!")

        # Insert data from csv
        with open('titanic.csv', 'r') as f:
            next(f)
            cur.copy_from(f, 'titanic', sep=',')
        print("Successfully inserted data from 'titanic.csv' into the table!")

        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print("Closing the connection. Bye for now!")


insert_titanic()
