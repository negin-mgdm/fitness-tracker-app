# Import the ConsoleWriter class for console output formatting.
from DataAccess.ExerciseStoreManager import ExerciseStoreManager
from Helpers.ConsoleWriter import ConsoleWriter

# Base class to be used as a template for capturing user commands.
class Command:
    def __init__(self, exercise_store_manager : ExerciseStoreManager) -> None:
        """
        Initialise a Command object with an ExerciseStoreManager instance and a ConsoleWriter for output.

        Args:
            exercise_store_manager (ExerciseStoreManager): An instance of ExerciseStoreManager.
        """
        self.exercise_store_manager = exercise_store_manager
        self.console_writer = ConsoleWriter()

    def run(self):
        """
        Abstract base class method to be overridden in sub-classes.
        This method defines the behavior of specific user command implementations.
        """
        pass