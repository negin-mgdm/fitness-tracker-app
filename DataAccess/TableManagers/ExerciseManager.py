# Import the base table manager class.
from DataAccess.TableManagers.BaseTableManager import BaseTableManager

# Define an ExerciseManager class that inherits from BaseTableManager.
class ExerciseManager(BaseTableManager):
    def __init__(self, db_manager):
        # Initialise ExerciseManager with a database manager.
        super().__init__(db_manager)

    # Function to create the exercise table.
    def _create_table(self):
        # Create exercise table query.
        query = """ CREATE TABLE IF NOT EXISTS exercise (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            muscle_group text NOT NULL,
                                            category_id integer not null references exercise_category(id)
                                        ); """

        if self.conn is not None:
            # Create exercise table.
             self.db_manager._create_table(query)
        else:
            print("Error! cannot create the database connection.")

    # Function to populate exercises table with dummy data.
    def _populate_table(self):
        # List of exercise data (name, muscle_group, category_id).
        exercises = [
            ('Squats', 'Gluteus Maximus - Quadriceps - Hamstrings', 3),
            ('Leg Extensions','Quadriceps', 3),
            ('Biceps Curls', 'Biceps Brachii', 3),
            ('Lat Pulldown', 'Latissimus Dorsi', 3),
            ('Plank', 'Rectus Abdominus - Transverse Abdominus', 3),
            ('Side Plank', 'Internal Obliques - External Obliques', 3),
            ]
        for exercise in exercises:
            # Insert each exercise into the database using the store manager.
            self.store_manager.insert_exercise(exercise, True)