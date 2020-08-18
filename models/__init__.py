# These 2 imports are general for any api
from models.api_errors import ApiErrors
from models.base_object import BaseObject

# These are the custom models to import
from models.TaskData import TaskData
from models.TutorialData import TutorialData
from models.TutorialQuiz import TutorialQuiz


__all__ = (
    'ApiErrors',
    'BaseObject',
    'TutorialData',
    'TutorialQuiz',
    'TaskData',
)
