# Import necessary module for database interactions.
import sqlite3
from DataAccess.TableManagers.CategoryManager import CategoryManager
from DataAccess.TableManagers.ExerciseLogsManager import ExerciseLogsManager
from DataAccess.TableManagers.ExerciseManager import ExerciseManager
from DataAccess.TableManagers.ExercisePlanManager import ExercisePlanManager
from DataAccess.TableManagers.WorkoutRoutineManager import WorkoutRoutineManager

# Class used for general database interactions. 
class DatabaseManager:
    
    def __init__(self):
        # Initialise the DatabaseManager with a database connection.   
        self.conn = self.setup_db()
        self._build_tables_on_startup()

    # Function used to create a table.
    def _create_table(self, create_table_sql):
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Exception as e:
            print(e)

    # Function to create and populate required tables on startup. 
    def _build_tables_on_startup(self):
        # Create and populate various tables on application startup.
        managers = [
            CategoryManager(self),
            ExerciseManager(self),
            ExercisePlanManager(self),
            WorkoutRoutineManager(self),
            ExerciseLogsManager(self)
        ]
        
        for manager in managers:
            manager.run()
    # Function to create a database connection.    
    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Exception as e:
            print('Following error occurred while connecting to the local sqlite database.')
            print(e)

    # Function to close connection to the database.        
    def close_connection(self):
        self.conn.close()

    # Function to setup the database on application startup.
    def setup_db(self):
        database = r"database.db"

        # Create a database connection.
        conn = self.create_connection(database)
    
        return conn
    