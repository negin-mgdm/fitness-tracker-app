# Import necessary modules
from DataAccess.ExerciseStoreManager import ExerciseStoreManager
from abc import abstractmethod


# Define a base class for managing database tables.
class BaseTableManager:
    def __init__(self, db_manager) -> None:
        # Initialise the BaseTableManager with a database manager.
        self.db_manager = db_manager
        # Create an ExerciseStoreManager instance using the database connection.
        self.store_manager = ExerciseStoreManager(db_manager.conn)
        # Store the database connection.
        self.conn = db_manager.conn

    @abstractmethod
    def _create_table(self):
        # Define an abstract method for creating a database table.
        pass

    @abstractmethod
    def _populate_table(self):
        # Define an abstract method for populating a database table.
        pass

    def run(self):
        # Method to create and populate the database table.
        self._create_table()
        self._populate_table()