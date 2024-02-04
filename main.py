# Import necessary modules for database management and user input handling.
from DataAccess.DatabaseManager import DatabaseManager
from UserInputHandler.UserInputs import UserInputs

# Main entry point of the application.
def main():
    # setup db access to handle database interactions.
    db_manager = DatabaseManager()

    # Continuously prompt the user for commands using a main menu.
    while True:
        options = '''
1. Add exercise category
2. View exercise by category
3. Delete exercise by category
4. Create Workout Routine, Plan and Exercises
5. View all Workout Routines, Plans, Exercises and Categories  
6. Manage Exercise Progress
7. Set Fitness Goals
8. View Progress towards Fitness Goals
9. Quit
'''
        # Get the user's choice as an integer input.
        choice = int(input(options))

        # Create a user input handler instance with the database connection.
        user_input_handler = UserInputs(db_manager.conn)
        
        # Match the user's choice and execute the corresponding action.
        match (choice):
            case 1:
                user_input_handler.add_new_workout_category()
            case 2:
                user_input_handler.view_exercise_by_category()
            case 3:
                user_input_handler.delete_exercise_by_category()
            case 4:
                user_input_handler.add_new_workout_routine()
            case 5:
                user_input_handler.view_workout_routine()
            case 6:
                user_input_handler.view_workout_progress()
            case 7:
                user_input_handler.set_goal()
            case 8:
                user_input_handler.view_progress_towards_goal()
            case 9:
                break
    
    # Close db connection and upon application termination. 
    db_manager.close_connection()
    exit()

# Call the main function to start the application.
main()


