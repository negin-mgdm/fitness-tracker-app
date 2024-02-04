# Import the base table manager class.
from DataAccess.TableManagers.BaseTableManager import BaseTableManager

# Define an ExerciseLogsManager class that inherits from BaseTableManager.
class ExerciseLogsManager(BaseTableManager):
    def __init__(self, db_manager):
        # Initialise ExerciseLogsManager with a database manager.
        super().__init__(db_manager)

    # Function to create the exercise logs table.
    def _create_table(self):
        # SQL query to create the exercise_logs table.
        query = """ CREATE TABLE IF NOT EXISTS exercise_logs (
                                            id integer PRIMARY KEY,
                                            date datetime default current_timestamp,
                                            routine_id integer not null references workout_routine(id)
                                        ); """

        if self.conn is not None:
            # Create the exercise_logs table if the database connection exists.
             self.db_manager._create_table(query)
        else:
            print("Error! cannot create the database connection.")

    # Function to populate the exercise logs table with dummy data.
    def _populate_table(self):
        # List of exercise log data (id, date, routine_id).
        logs = [
            (1, '29-10-2023', 2),
            (2, '01-11-2023', 2),
            (3, '02-11-2023', 2),
            (4, '04-11-2023', 3),
            (5, '05-11-2023', 3),
        ]
        for log in logs:
            # Insert each exercise log into the database using the store manager.
            self.store_manager.insert_exercise_logs(log, True)