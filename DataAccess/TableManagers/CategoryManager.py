# Import the base table manager class.
from DataAccess.TableManagers.BaseTableManager import BaseTableManager

# Define a CategoryManager class that inherits from BaseTableManager.
class CategoryManager(BaseTableManager):
    def __init__(self, db_manager):
        # Initialise CategoryManager with a database manager.
        super().__init__(db_manager)

       # Function to create the exercise_category table.
    def _create_table(self):
        # SQL query to create the exercise_category table.
        query = """ CREATE TABLE IF NOT EXISTS exercise_category(
                                            id integer PRIMARY KEY,
                                            name text NOT NULL
                                        ); """

        if self.conn is not None:
            # Create the exercise_category table if the database connection exists.
             self.db_manager._create_table(query)
        else:
            print("Error! cannot create the database connection.")

    # Function to populate the exercise categories table with dummy data.
    def _populate_table(self):
        # List of exercise categories.
        categories = [
            'Running',
            'Cycling',
            'Weightlifting',
            'Yoga',
            ]
        # Insert each category into the database using the store manager.
        for category in categories:
            self.store_manager.insert_categories(category, True)