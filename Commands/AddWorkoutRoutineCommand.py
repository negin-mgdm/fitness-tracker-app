# Import the base Command class for command implementation.
from Commands.Command import Command
from Commands.ViewWorkoutRoutineCommand import ViewWorkoutRoutineCommand

# Class to capture a user request command to add a new Exercise, Exercise plan and Workout routine to the database.
class AddWorkoutRoutineCommand(Command):
    def __init__(self, exercise_store_manager) -> None:
        super().__init__(exercise_store_manager)

    # Add a new exercise to the database based on user input.        
    def _enter_exercise(self):
        try:      
            cmd = ViewWorkoutRoutineCommand(self.exercise_store_manager)
            print('Available exercise categories to pick from:')
            cmd.view_all_categories()
                    
            user_input = input('''\nEnter a new exercise to be added by providing the name, muscle group and category ID:
For example: Biceps Curls, Gluteus Maximus - Quadriceps - Hamstrings, 3\n''')
            
            exercise = list(map(lambda x: x.strip(), user_input.split(',')))
            self.exercise_store_manager.insert_exercise(exercise)
            print(f'''\'{user_input}\' is added to the exercise table.''')
        # Error handling for exercise addition.
        except Exception as e:
            print('An error occurred while adding the exercise to the table. Please ensure you enter the required values in the correct format.')        

    # Add a new exercise plan to the database based on user input.    
    def _enter_exercise_plan(self):      
        try:  
            cmd = ViewWorkoutRoutineCommand(self.exercise_store_manager)
            print('Available exercises to pick from:')
            cmd.view_all_exercise()
            
            user_input = input('''\nEnter a new exercise plan to be added by providing the number of sets, repetition, rest period and the exercise ID.
For example: 3, 10, 30, 1:\n''')     
            
            plan = list(map(lambda x: x.strip(), user_input.split(',')))
            self.exercise_store_manager.insert_exercise_plan(plan)
            print(f'''\'{user_input}\' is added to the exercise plan table.''')
        # Error handling for exercise plan addition.
        except Exception as e:
            print('An error occurred while adding the exercise plan to the table. Please ensure you enter the required values in the correct format.')
        
    # Add a new workout routine to the database based on user input.
    def _enter_workout_routine(self):
        try:
            cmd = ViewWorkoutRoutineCommand(self.exercise_store_manager)
            print('Available exercise plans to pick from:')
            cmd.view_all_exercise_plan()
            
            user_input = input('''\nEnter a new workout routine to be added by providing the name and exercise plan IDs with space delimited.
For example: Intermediate, 2 3 5 6:\n''')    
            
            routine = list(map(lambda x: x.strip(), user_input.split(','))) + [False]
            self.exercise_store_manager.insert_workout_routine(routine)            
        # Error handling for workout routine addition.
        except Exception as e:
            print('An error occurred while adding the workout routine to the table. Please ensure you enter the required values in the correct format.')
    
    # Perform the action based on the user's selection to add new exercises, exercise plans, or workout routines.    
    def run(self):
        options = '''Which of the following would you like to add?
1. Add a new exercise
2. Add an exercise plan
3. Add a new exercise routine
'''
        choice =int(input(options))
        match choice:
            case 1:
                self._enter_exercise()
            case 2:
                self._enter_exercise_plan()
            case 3:
                self._enter_workout_routine()
                
                