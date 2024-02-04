from Commands.Command import Command

# class to capture update command by user 
class GetProgressTowardsGoalCommand(Command):
    def __init__(self, exercise_store_manager) -> None:
        super().__init__(exercise_store_manager)

    # Method to fetch and calculate the user's progress towards their fitness goal.
    def _get_progress_towards_goal(self):
        # Retrieve user's fitness goal and the most recent workout routine log.
        goal = self.exercise_store_manager.search_goal()
        most_recent_log = self.exercise_store_manager.search_exercise_logs()[-1]
        routine_most_recent_workout = self.exercise_store_manager.search_workout_routine_by_id(most_recent_log[2])

        # Calculate progress and summarize the results.
        progress = self._get_progress_calculations(goal, routine_most_recent_workout)
        progress_summary = round(self._get_summary_progress(progress),2)
        
        # Display the overall progress percentage and a breakdown of individual exercise progress.
        print(f'Your total progress percentage is: %{progress_summary}')
        print(f'Your progression breakdown is as follows:')
        for item in progress:
            print(f'Exercise Id: {item[0]} - Sets: %{item[1][0]}, Reps: %{item[1][1]}, Rest Period: %{item[1][2]}, ')
 
    # Calculate progress for each exercise towards the fitness goal.
    def _get_progress_calculations(self, goal, routine_most_recent_workout):
        progress = []
        plans = goal[2].split()
        best_routine = routine_most_recent_workout[2].split() 
        for plan in plans:
            if plan in best_routine:
                progress.append([plan, [100, 100, 100]])
            else:
                exercise_plan_id = self.exercise_store_manager.search_exercise_plan_by_id(plan)
                result = self._find_matching_exercise(exercise_plan_id, best_routine)
                progress.append([plan, result])
        return progress

    # Calculate the average progress between sets, reps and rest periods.
    def _get_summary_progress(self, progress):
        total = 100
        for item in progress:
            total = (total + (item[1][0] + item[1][1] + item[1][2])/3)/2
        return total

    # Find exercises that match the user's goal and calculate the progress for each.
    def _find_matching_exercise(self, goal_plan, routine):
        for plan in routine:
            exercise_plan = self.exercise_store_manager.search_exercise_plan_by_id(plan)
            
            # If an exercise plan is found of the same exercise type, then calculate progress towards the goal
            # The calculation is made by the percentage ration completed for example (goal_reps/exercise_plan_reps * 100) 
            if(exercise_plan[4] == goal_plan[4]):
                sets_progress = exercise_plan[1]/goal_plan[1] * 100
                reps_progress = exercise_plan[2]/goal_plan[2] * 100
                rest_period_progress = exercise_plan[3]/goal_plan[3] * 100
                return [sets_progress, reps_progress, rest_period_progress]
            
        # No exercise plan found with of the same exercise type therefore no progress towards goal was found.            
        return [0, 0, 0]

    # Entry point for executing the command to get user's progress towards their fitness goal.
    def run(self):
        self._get_progress_towards_goal()