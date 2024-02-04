
# Import the base table manager class.
from DataAccess.TableManagers.BaseTableManager import BaseTableManager

# Define a WorkoutRoutineManager class that inherits from BaseTableManager.
class WorkoutRoutineManager(BaseTableManager):
    def __init__(self, db_manager):
        # Initialise WorkoutRoutineManager with a database manager.
        super().__init__(db_manager)

    # Function to create the workout routine table.
    def _create_table(self):
        # Create workout routine table query.
        query = """ CREATE TABLE IF NOT EXISTS workout_routine (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            exercise_plans text NOT NULL,
                                            goal boolean NOT NULL
                                        ); """

        if self.conn is not None:
            # Create workout routine table.
             self.db_manager._create_table(query)
        else:
            print("Error! cannot create the database connection.")

    # Function to populate workout routines table with dummy data.
    def _populate_table(self):
        # List of workout routine data (name, exercise_plans, goal).
        routines = [
            ('Goal', '1 3 5 6 7 8', True),
            ('Light', '2 3 5', False),
            ('Intermediate', '2 3 5 6', False),
            ('Advanced', '1 4 5 6 7 8', False),
            ]
        for routine in routines:
            # Insert each workout routine into the database using the store manager.
            self.store_manager.insert_workout_routine(routine, True)