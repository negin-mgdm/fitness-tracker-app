# Helper class to enable formatted console prints. 
from DataAccess.ExerciseStoreManager import ExerciseStoreManager


class ConsoleWriter:
    
    def print_routine_lite_info(self, routine):
        """
        Print formatted information about a workout routine.

        Args:
            routine (tuple): A tuple containing routine information.

        Example:
            print_routine_info((1, 'Beginner Full Body Workout', 'Push-ups, Squats, Planks', True))
        """
        print_message = f'''Id: \'{routine[0]}\', Name: \'{routine[1]}\', Exercise Plans: \'{routine[2]}\', Is Your Goal: \'{True if routine[3] == 1 else False}\''''
        print(print_message)

    def print_workout_log(self, log):
        """
        Print formatted information about a workout log entry.

        Args:
            log (tuple): A tuple containing log entry information.

        Example:
            print_workout_log((1, '2023-11-07', 1))
        """
        print_message = f'''Id: \'{log[0]}\', Routine Id: \'{log[2]}\', Date: \'{log[1]}\''''
        print(print_message)

    def print_exercise_info(self, exercise: list[str], category : str):
        """
        Print formatted information about an exercise.

        Args:
            exercise (tuple): A tuple containing exercise information.

        Example:
            print_exercise_info((1, 'Push-ups', 'Chest and Arms'))
        """
        print_message = f'''Id: \'{exercise[0]}\', Name: \'{exercise[1]}\', Muscle Group: \'{exercise[2]}\', Category: \'{category}\''''
        print(print_message)
        
    def print_routine_info(self, routine, exercise_store_manager : ExerciseStoreManager):
        """
        Print detailed information about a routine.

        Args:
            routine (tuple): Contains routine details.
            exercise_store_manager (ExerciseStoreManager): Manages exercise data.

        Example:
            print_routine_info(routine_data, exercise_store_manager_instance)
        """
        self.print_routine_lite_info(routine)
        
        plans_ids = routine[2].split(' ')
        
        print(f'\tRoutine breakdown:')
        for id in plans_ids:    
            plan = exercise_store_manager.search_exercise_plan_by_id(id)
            self.print_exercise_plan_info(plan, exercise_store_manager)
            
    def print_exercise_plan_info(self, plan, exercise_store_manager):
        """
        Print detailed information about an exercise plan.

        Args:
            plan (tuple): Contains plan details.
            exercise_store_manager (ExerciseStoreManager): Manages exercise data.

        Example:
            print_exercise_plan_info(plan_data, exercise_store_manager_instance)
        """
        exercise = exercise_store_manager.search_exercise_by_id(plan[4])
        print(f'\t\tPlan id: {plan[0]} - {exercise[1]}, sets: {plan[1]}, reps: {plan[2]}, rest period: {plan[3]} seconds.')
    
    def print_exercise_category_info(self, category : list[str]):
        """
        Print category information.

        Args:
            category (list[str]): Contains category details (ID, Category).

        Example:
            print_exercise_category_info([1, 'Strength Training'])
        """
        print(f'''Id: \'{category[0]}\', Category: \'{category[1]}\'''')
       
        