# Class used to manage and store exercise records in the database.
class ExerciseStoreManager:

    def __init__(self, conn):
        """
        Initialise an ExerciseStoreManager object with a database connection.

        Args:
            conn: SQLite database connection.
        """
        self.conn = conn

#region insert
    def insert_categories(self, category, startup = False):
        """
        Insert a new exercise category into the database.

        Args:
            category (tuple): A tuple containing the category's id and name.
            startup (bool): Indicates whether this is a startup operation or not.
        """
        match = self.search_category_by_name(category)

        # don't insert record if it already exists.
        if(match is not None):
            if(not startup):
                print(f"Cannot add new record for category with title \'{category[0]}\' as it has been already added to the store.")
            return

        query = ''' INSERT INTO exercise_category(name)
              VALUES(?) '''
        cur = self.conn.cursor()
        cur.execute(query, (category,))
        self.conn.commit()

    def insert_exercise(self, exercise, startup = False):
        """
        Insert a new exercise record into the database.

        Args:
            exercise (tuple): A tuple containing exercise details.
            startup (bool): Indicates whether this is a startup operation or not.
        """
        match = self.search_exercise_by_name(exercise[0])

        # don't insert record if it already exists.
        if(match is not None):
            if(not startup):
                print(f"Cannot add new record for exercise with title \'{exercise[0]}\' as it has been already added to the store.")
            return

        query = ''' INSERT INTO exercise(name, muscle_group, category_id)
              VALUES(?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(query, (exercise[0], exercise[1], exercise[2], ))
        self.conn.commit()

    def insert_exercise_plan(self, plan):
            """
            Insert a new exercise plan into the database.

            Args:
                plan (tuple): A tuple containing exercise plan details.
                startup (bool): Indicates whether this is a startup operation or not.
            """
            query = ''' INSERT INTO exercise_plan('set', rep, rest_period, exercise_id)
                VALUES(?,?,?,?)'''
            cur = self.conn.cursor()
            cur.execute(query, (plan[0], plan[1], plan[2], plan[3], ))
            self.conn.commit()
            
    def insert_exercise_plan_startup(self, plan, startup = False):
            """
            Insert the exercise plan into the database.

            Args:
                plan (tuple): A tuple containing exercise plan details.
                startup (bool): Indicates whether this is a startup operation or not.
            """
            match = self.search_exercise_plan_by_id(plan[0])

            # don't insert record if it already exists.
            if(match is not None):
                if(not startup):
                    print(f"Cannot add new record for plan with title \'{plan[0]}\' as it has been already added to the store.")
                return

            query = ''' INSERT INTO exercise_plan(id, 'set', rep, rest_period, exercise_id)
                VALUES(?,?,?,?,?)'''
            cur = self.conn.cursor()
            cur.execute(query, plan)
            self.conn.commit()

    def insert_workout_routine(self, routine, startup = False):
            """
            Insert a new workout routine into the database.

            Args:
                routine (tuple): A tuple containing workout routine details.
                startup (bool): Indicates whether this is a startup operation or not.
            """
            match = self.search_workout_routine_by_name(routine[0])

            # don't insert record if it already exists.
            if(match is not None):
                if(not startup):
                    print(f"Cannot add new record for routine with title \'{routine[0]}\' as it has been already added to the store.")
                return

            query = ''' INSERT INTO workout_routine (name, exercise_plans, goal)
                VALUES(?,?,?) '''
            cur = self.conn.cursor()
            cur.execute(query, (routine[0],routine[1],routine[2],))
            self.conn.commit()
            
            if(not startup):
                print(f'Routine \'{routine}\' has been added.')

    def insert_exercise_logs(self, log, startup = False):
            """
            Insert exercise logs into the database.

            Args:
                log (tuple): A tuple containing exercise log details.
                startup (bool): Indicates whether this is a startup operation or not.
            """
            match = self.search_exercise_logs_by_id(log[0])

            # don't insert record if it already exists.
            if(match is not None):
                if(not startup):
                    print(f"Cannot add new record for log with title \'{log[0]}\' as it has been already added to the store.")
                return

            query = ''' INSERT INTO exercise_logs(id, date, routine_id)
                VALUES(?,?,?) '''
            cur = self.conn.cursor()
            cur.execute(query, log)
            self.conn.commit()        

    def insert_logs(self, log, startup = False):
            """
            Insert exercise logs into the database.

            Args:
                log (tuple): A tuple containing exercise log details.
                startup (bool): Indicates whether this is a startup operation or not.
            """
            query = ''' INSERT INTO exercise_logs(date, routine_id)
                VALUES(?,?) '''
            cur = self.conn.cursor()
            cur.execute(query, log)
            self.conn.commit()  
#endregion

#region search
    def search_category_by_id(self, id):
        """
        Search for an exercise category by its ID.

        Args:
            id: The ID of the exercise category to search for.

        Returns:
            tuple: The exercise category record or None if not found.
        """
        sql_search_exercise = ''' SELECT * FROM exercise_category WHERE id = ? '''
        cur = self.conn.cursor()
        cur.execute(sql_search_exercise, (id,))
        self.conn.commit()
        return cur.fetchone()

    def search_category_by_name(self, name):
        """
        Search for an exercise category by its name.

        Args:
            id: The name of the exercise category to search for.

        Returns:
            tuple: The exercise category record or None if not found.
        """
        sql_search_exercise = ''' SELECT * FROM exercise_category WHERE name = ? '''
        cur = self.conn.cursor()
        cur.execute(sql_search_exercise, (name,))
        self.conn.commit()
        return cur.fetchone()

    def search_exercise_by_id(self, id):
        """
        Search for an exercise by its ID.

        Args:
            id: The ID of the exercise to search for.

        Returns:
            tuple: The exercise record or None if not found.
        """
        sql_search_exercise = ''' SELECT * FROM exercise WHERE id = ? '''
        cur = self.conn.cursor()
        cur.execute(sql_search_exercise, (id,))
        self.conn.commit()
        return cur.fetchone()
    
    def search_exercise_by_name(self, name):
        """
        Search for an exercise by its name.

        Args:
            name: The name of the exercise to search for.

        Returns:
            tuple: The exercise record or None if not found.
        """
        sql_search_exercise = ''' SELECT * FROM exercise WHERE name = ? '''
        cur = self.conn.cursor()
        cur.execute(sql_search_exercise, (name,))
        self.conn.commit()
        return cur.fetchone()
    
    def search_exercises(self):
        """
        Search and retrieve all exercises.

        Returns:
            list: A list of all exercises.
        """
        query = ''' SELECT * FROM exercise'''
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        return cur.fetchall()
        
    def search_exercise_plan_by_id(self, id):
        """
        Search for an exercise plan by its ID.

        Args:
            id: The ID of the exercise plan to search for.

        Returns:
            tuple: The exercise plan record or None if not found.
        """
        query = ''' SELECT * FROM exercise_plan WHERE id = ? '''
        cur = self.conn.cursor()
        cur.execute(query, (id,))
        self.conn.commit()
        return cur.fetchone()
    
    def search_exercise_plan_by_name(self, name):
        """
        Search for an exercise plan by its name.

        Args:
            name: The name of the exercise plan to search for.

        Returns:
            tuple: The exercise plan record or None if not found.
        """
        query = ''' SELECT * FROM exercise_plan WHERE name = ? '''
        cur = self.conn.cursor()
        cur.execute(query, (name,))
        self.conn.commit()
        return cur.fetchone()
    
    def search_exercise_plans(self):
        """
        Search and retrieve all exercise plans.

        Returns:
            list: A list of all exercise plan records.
        """
        query = ''' SELECT * FROM exercise_plan'''
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        return cur.fetchall()
    
    def search_workout_routine_by_id(self, id):
        """
        Search for a workout routine by its ID.

        Args:
            id: The ID of the workout routine to search for.

        Returns:
            tuple: The workout routine record or None if not found.
        """
        sql_search_exercise = ''' SELECT * FROM workout_routine WHERE id = ? '''
        cur = self.conn.cursor()
        cur.execute(sql_search_exercise, (id,))
        self.conn.commit()
        return cur.fetchone()
    
    def search_workout_routine_by_name(self, name):
        """
        Search for a workout routine by its name.

        Args:
            name: The name of the workout routine to search for.

        Returns:
            tuple: The workout routine record or None if not found.
        """
        sql_search_exercise = ''' SELECT * FROM workout_routine WHERE name = ? '''
        cur = self.conn.cursor()
        cur.execute(sql_search_exercise, (name,))
        self.conn.commit()
        return cur.fetchone()

    def search_workout_routines(self):
        """
        Search and retrieve all workout routines.

        Returns:
            list: A list of all workout routine records.
        """
        query = ''' SELECT * FROM workout_routine'''
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        return cur.fetchall()
    
    def search_goal(self):
        """
        Search for a workout routine with a goal set to TRUE.

        Returns:
            tuple: The workout routine record with a goal set to TRUE or None if not found.
        """
        query = ''' SELECT * FROM workout_routine WHERE goal = TRUE'''
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        return cur.fetchone()
    
    def search_exercise_logs_by_id(self, id):
        """
        Search for exercise logs by their ID.

        Args:
            id: The ID of the exercise log to search for.

        Returns:
            tuple: The exercise log record or None if not found.
        """
        sql_search_exercise = ''' SELECT * FROM exercise_logs WHERE id = ? '''
        cur = self.conn.cursor()
        cur.execute(sql_search_exercise, (id,))
        self.conn.commit()
        return cur.fetchone()
   
    def search_exercise_logs(self):
        """
        Search and retrieve all exercise logs.

        Returns:
            list: A list of all exercise log records.
        """
        query = ''' SELECT * FROM exercise_logs'''
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        return cur.fetchall()

    def search_exercises_by_category(self, category : str):
        """
        Search for exercises by their category.

        Args:
            category: The name of the exercise category to search for.

        Returns:
            list: A list of exercise records for the specified category.
        """
        query = ''' SELECT exercise.id, exercise.name, exercise.muscle_group
            FROM exercise
            JOIN exercise_category ON exercise.category_id = exercise_category.id
            WHERE exercise_category.name = ?;'''
        cur = self.conn.cursor()
        cur.execute(query, (category,))
        self.conn.commit()
        return cur.fetchall()

    def search_category(self):
        """
        Search and retrieve all categories.

        Returns:
            list: A list of all exercise categories.
        """
        query = ''' SELECT * FROM exercise_category'''
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        return cur.fetchall()
#endregion

#region update
    def update_workout_routine_goal(self, id, value):
        """
        Update the goal status of a workout routine.

        Args:
            id: The ID of the workout routine to update.
            value (bool): The new goal status (True or False).
        """
        match = self.search_workout_routine_by_id(id)
        
        # don't attempt an update if no match is found for the given record id.
        if(match is None):
            print(f"Cannot update the provided workout routine with id: {id} as it doesn't already exist in the store.")
            return

        query = '''UPDATE workout_routine
            SET goal = ?
            WHERE id = ?; '''
        cur = self.conn.cursor()
        cur.execute(query, (value, id))
        self.conn.commit()

    def update_workout_routine_set_goal(self, id):
        """
        Update the goal status of a workout routine to set one as the goal.

        Args:
            id: The ID of the workout routine to set as the goal.
        """
        match = self.search_goal()
        if(match is None):
            print(f"Cannot find a workout routine goal.")
            return
        self.update_workout_routine_goal(match[0], False)
        self.update_workout_routine_goal(id, True)
#endregion

#region delete
    def delete_exercises_by_category(self, category):
        """
        Delete exercises of a specified category from the database.

        Args:
            category: The name of the exercise category to delete exercises from.
        """

        sql_delete_ebookstore_table = '''DELETE FROM exercise
            WHERE category_id = (SELECT id FROM exercise_category WHERE name = ?);'''
        cur = self.conn.cursor()
        cur.execute(sql_delete_ebookstore_table, (category,))
        self.conn.commit()
#endregion