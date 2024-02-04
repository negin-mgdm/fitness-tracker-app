# Import the base Command class for command implementation.
from Commands.Command import Command

# Class to handle a user's request to search exercise records by category.
class SearchExerciseByCategoryCommand(Command):
    def __init__(self, exercise_store_manager) -> None:
        super().__init__(exercise_store_manager)

    # Fetch exercise records based on a specified category provided by the user.
    def _search_exercises_by_category(self):
        user_input = input('''Enter a workout category to search exercises for.
for example: \'Running\'
''')
        exercises = self.exercise_store_manager.search_exercises_by_category(user_input)

        if len(exercises) == 0:
            print(f'Could not find any exercises with the specified category: \'{user_input}\'')
            return

        print(f'''Exercises found for category \'{user_input}\':''')

        for exercise in exercises:
            self.console_writer.print_exercise_info(exercise, user_input)

    # Execute the command to search exercises based on a category.
    def run(self):
        self._search_exercises_by_category()