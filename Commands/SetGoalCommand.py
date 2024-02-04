# Import the base Command class for command implementation.
from Commands.Command import Command

# Class to capture a user's update command for setting workout goals.
class SetGoalCommand(Command):
    def __init__(self, ebookstore_manager) -> None:
        super().__init__(ebookstore_manager)

    def _print_workout_routines(self):
        """
        Display a list of available workout routines.

        This function retrieves and prints information about workout routines stored in the database.
        """
        routines = self.exercise_store_manager.search_workout_routines()
        if len(routines) == 0:
            print(f'Could not find any routines.')
            return

        print(f'''Routines found:''')

        for routine in routines:
            self.console_writer.print_routine_info(routine, self.exercise_store_manager)

    def _set_goal(self):
        """
        Set a workout routine as a user's goal.

        This function allows the user to choose a workout routine by its ID and set it as their goal.
        """
        self._print_workout_routines()
        id = input('''Enter the id of a workout routine to set as your goal:''')
        self.exercise_store_manager.update_workout_routine_set_goal(id)
 
    def run(self):
        """
        Execute the set goal command.

        This function is the entry point for handling a user's request to set a workout routine as their goal.
        """
        self._set_goal()