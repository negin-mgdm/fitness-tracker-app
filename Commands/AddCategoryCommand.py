# Import the base Command class for command implementation.
from Commands.Command import Command

# Class to capture a user request command to add a new workout category to the database.
class AddCategoryCommand(Command):
    def __init__(self, exercise_store_manager) -> None:
        super().__init__(exercise_store_manager)

    # Add a new workout category to the database based on user input.
    def _enter_category(self):
        try:
            user_input = input('''Enter a new exercise category to be added. Provide the category name.
For example: CrossFit
''')
            self.exercise_store_manager.insert_categories(user_input)
            
            print(f'{user_input} has been added to the categories table.')
        # Error handling for exercise category addition.         
        except Exception as e:
            print('An error occurred while adding the exercise category to the table. Please ensure you enter the required values in the correct format.')
    
    # Function serving as the entry point for handling a user's command request to add a new category.
    def run(self):
        self._enter_category()