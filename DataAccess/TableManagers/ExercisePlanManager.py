# Import the base table manager class.
from DataAccess.TableManagers.BaseTableManager import BaseTableManager

# Define an ExercisePlanManager class that inherits from BaseTableManager.  
class ExercisePlanManager(BaseTableManager):
    def __init__(self, db_manager):
        # Initialise ExercisePlanManager with a database manager.
        super().__init__(db_manager)

    # Function to create the exercise_plan table.
    def _create_table(self):
        # Create exercise table query.
        query = """ CREATE TABLE IF NOT EXISTS exercise_plan (
                                            id integer PRIMARY KEY,
                                            'set' integer NOT NULL,
                                            rep integer NOT NULL,
                                            rest_period integer NOT NULL,
                                            exercise_id integer not null references exercise(id)
                                        ); """

        if self.conn is not None:
            # Create exercise_plan table.
             self.db_manager._create_table(query)
        else:
            print("Error! cannot create the database connection.")

    # Function to populate exercise plans table with dummy data.
    def _populate_table(self):
        # List of exercise plan data ('set', rep, rest_period, exercise_id).
        exercise_plans = [
            (1, 3, 10, 30, 1),
            (2, 3, 8, 30, 1),
            (3, 3, 6, 30, 2),
            (4, 2, 10, 30, 2),
            (5, 3, 8, 30, 3),
            (6, 3, 10, 30, 4),
            (7, 3, 6, 30, 5),
            (8, 3, 6, 30, 6),
            ]
        for plan in exercise_plans:
            # Insert each exercise plan into the database using the store manager.
            self.store_manager.insert_exercise_plan_startup(plan, True)