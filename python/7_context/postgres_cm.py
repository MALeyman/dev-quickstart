import psycopg2 as pgadmin

# https://github.com/ilystsov/postgres-db-interaction/blob/main/src/cursor.py
class OpenPostgres:
    def __init__(self, dbname, user, password, host):
        # Data to access the database
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password

        # Making a connection
        self.connection = pgadmin.connect(
            host=self.host,
            dbname=self.dbname,
            user=self.user,
            password=self.password
        )

        # Creating the cursor
        self.cursor = self.connection.cursor()

    def __enter__(self):
        # Returning the cursor to the context manager
        return self.cursor

    def __iter__(self):
        # Returning the items fetched by select statements
        for item in self.cursor:
            yield item

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Closing the cursor
        self.cursor.close()
        if isinstance(exc_val, Exception):
            # Rollback if any errors occur
            self.connection.rollback()
        else:
            # Committing the changes if doesn't occur any errors
            self.connection.commit()
        # Closing the connection
        self.connection.close()
