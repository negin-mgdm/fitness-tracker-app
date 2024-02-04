# Import necessary modules for various commands and data access.
from Commands.AddWorkoutRoutineCommand import AddWorkoutRoutineCommand
from Commands.DeleteExerciseByCategoryCommand import DeleteExerciseByCategoryCommand
from Commands.AddCategoryCommand import AddCategoryCommand
from Commands.GetProgressTowardsGoalCommand import GetProgressTowardsGoalCommand
from Commands.SearchExerciseByCategoryCommand import SearchExerciseByCategoryCommand
from Commands.SetGoalCommand import SetGoalCommand
from Commands.ViewWorkoutLogsCommand import ViewWorkoutLogsCommand
from Commands.ViewWorkoutRoutineCommand import ViewWorkoutRoutineCommand
from DataAccess.ExerciseStoreManager import ExerciseStoreManager

class UserInputs:
    # Initialize the UserInputs class with a database connection.
    def __init__(self, conn):
        self.exercise_store_manager = ExerciseStoreManager(conn)

#region insert
    def add_new_workout_category(self):
        # Execute the command to add a new workout category.
        command = AddCategoryCommand(self.exercise_store_manager)
        command.run()
    
    def add_new_workout_routine(self):
        # Execute the command to add a new workout routine.
        command = AddWorkoutRoutineCommand(self.exercise_store_manager)
        command.run()    
#endregion

#region search
    def view_exercise_by_category(self):
        # Execute the command to view exercises by category.
        command = SearchExerciseByCategoryCommand(self.exercise_store_manager)
        command.run()

    def view_workout_routine(self):
        # Execute the command to view workout routines.
        command = ViewWorkoutRoutineCommand(self.exercise_store_manager)
        command.run()

    def view_workout_progress(self):
        # Execute the command to view exercise progress.
        command = ViewWorkoutLogsCommand(self.exercise_store_manager)
        command.run()

    def view_progress_towards_goal(self):
        # Execute the command to view progress towards fitness goals.
        command = GetProgressTowardsGoalCommand(self.exercise_store_manager)
        command.run()
#endregion

#region update
    def set_goal(self):
        # Execute the command to set fitness goals.
        command = SetGoalCommand(self.exercise_store_manager)
        command.run()
#endregion

#region delete
    def delete_exercise_by_category(self):
        # Execute the command to delete exercises by category.
        command = DeleteExerciseByCategoryCommand(self.exercise_store_manager)
        command.run()
#endregion