# Import the base Command class for command implementation.
from Commands.Command import Command

# Class to capture user's delete commands for exercises by category.
class DeleteExerciseByCategoryCommand(Command):
    def __init__(self, exercise_store_manager) -> None:
        super().__init__(exercise_store_manager)
    
    # Function to delete exercises by a specified category.
    def _delete_exercise_by_category(self):
        category = input('Enter category of exercises to be deleted: ')

        exercises = self.exercise_store_manager.search_exercises_by_category(category)
        if(len(exercises) == 0):
            print(f'No exercises found for the given category \'{category}\'.')
            return
        
        self.exercise_store_manager.delete_exercises_by_category(category)
        print(f'All exercises of the \'{category}\' category are deleted.')

    # Function serving as the entry point for handling various deletion requests by the user.
    def run(self):
        self._delete_exercise_by_category()