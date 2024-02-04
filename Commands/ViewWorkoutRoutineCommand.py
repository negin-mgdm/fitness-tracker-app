# Import the base Command class for command implementation.
from Commands.Command import Command

# Class to capture a user's request command to view workout routines.
class ViewWorkoutRoutineCommand(Command):
    def __init__(self, exercise_store_manager) -> None:
        super().__init__(exercise_store_manager)
                       
    def view_workout_routine(self):
        """
        View a specific workout routine by its ID.

        This function allows the user to enter a routine ID and displays information about the selected workout routine.
        """
        id = input('''Enter the routine id you wish to see:''')
        routine = self.exercise_store_manager.search_workout_routine_by_id(id)

        self.console_writer.print_routine_info(routine, self.exercise_store_manager)

    def view_all_workout_routine(self):
        """
        View all workout routines.

        This function retrieves and prints information about all workout routines stored in the database.
        """
        routines = self.exercise_store_manager.search_workout_routines()
        if len(routines) == 0:
            print(f'Could not find any routines.')
            return

        print(f'''Routines found:''')

        for routine in routines:
            self.console_writer.print_routine_info(routine, self.exercise_store_manager)

    def view_all_exercise_plan(self):
        """
        View all exercise plans.

        This function retrieves and prints information about all exercise plans stored in the database.
        """
        plans = self.exercise_store_manager.search_exercise_plans()
        if len(plans) == 0:
            print(f'Could not find any exercise plans.')
            return

        print(f'''Exercise plans found:''')

        for plan in plans:
            self.console_writer.print_exercise_plan_info(plan, self.exercise_store_manager)
            
    def view_all_exercise(self):
        """
        View all exercises.

        This function retrieves and prints information about all exercises stored in the database.
        """
        exercises = self.exercise_store_manager.search_exercises()
        if len(exercises) == 0:
            print(f'Could not find any exercises.')
            return

        print(f'''Exercises found:''')

        for exercise in exercises:
            category_id = exercise[3]
            category = self.exercise_store_manager.search_category_by_id(category_id)
            self.console_writer.print_exercise_info(exercise, category[1])
    
    def view_all_categories(self):
        """
        View all exercise categories.

        This function retrieves and prints information about all exercise categories stored in the database.
        """
        categories = self.exercise_store_manager.search_category()
        if len(categories) == 0:
            print(f'Could not find any exercise categories.')
            return
        
        print(f'''Exercise categories found:''')
        for category in categories:
            self.console_writer.print_exercise_category_info(category)
        
            
    # Function serving as the entry point for handling a user's request to view workout routines.
    def run(self):
        """
        Execute the view workout routines command.

        This function is the entry point for handling a user's request to view workout routines, exercise plans, exercises and exercise categories.
        """
        options = '''Please enter the option number you wish to view:
1. View Workout Routine by ID
2. View all Workout Routines
3. View all exercise plans
4. View all exercises
5. View all exercise categories
'''
        choice = int(input(options))
        match choice:
            case 1:
                self.view_workout_routine()
            case 2:
                self.view_all_workout_routine()
            case 3:
                self.view_all_exercise_plan()
            case 4:
                self.view_all_exercise()
            case 5:
                self.view_all_categories()

        