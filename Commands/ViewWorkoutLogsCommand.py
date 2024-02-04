# Import the base Command class for command implementation.
from Commands.Command import Command
from Commands.ViewWorkoutRoutineCommand import ViewWorkoutRoutineCommand

# Class to capture a user's request command to view exercise logs.
class ViewWorkoutLogsCommand(Command):
    def __init__(self, exercise_store_manager) -> None:
        super().__init__(exercise_store_manager)

    def view_all_exercise_logs(self):
        """
        Display all exercise logs.

        This function retrieves and prints information about all exercise logs stored in the database.
        """
        logs = self.exercise_store_manager.search_exercise_logs()
       
        if len(logs) == 0:
            print(f'Could not find any exercise logs.')
            return

        print(f'''Exercise logs found:''')

        for log in logs:
            self.console_writer.print_workout_log(log)
    
        # Add a new workout log to the database based on user input.
    def _enter_log(self):
        try:
            cmd = ViewWorkoutRoutineCommand(self.exercise_store_manager)
            print('Available workout routine IDs to pick from:')
            cmd.view_all_workout_routine()
                        
            user_input = input('''\nEnter a new workout log to be added to the table by providing the routine ID.
For example: 29-10-2023, 2
''')
            log = list(map(lambda x: x.strip(), user_input.split(',')))
            self.exercise_store_manager.insert_logs(log)
            print(f'''\'{user_input}\' is added to the exercise logs table.''')
        # Error handling for exercise log addition.
        except Exception as e:
            print('An error occurred while adding the exercise log to the table. Please ensure you enter the required values in the correct format.')

    # Function serving as the entry point for handling a user's request to view exercise logs.6
    def run(self):
        """
        Execute the view exercise logs command.

        This function is the entry point for handling a user's request to view all exercise logs.
        """
        options = '''Please enter your choice:
1. View all Workout logs
2. Add a new Workout log
'''
        choice = int(input(options))
        match choice:
            case 1:
                self.view_all_exercise_logs()
            case 2:
                self._enter_log()
       

        