from pydantic import BaseModel, Field
from typing import List
from .utils import load_openai_key
from langchain.chat_models import ChatOpenAI
from abc import ABC


class BaseAgent(ABC):    
    model: ChatOpenAI = None

    def __init__(self):
        load_openai_key()
        self.model = ChatOpenAI(model_name="gpt-4", temperature=0)


## Utils classes
class CodeFile:
    filename: str
    content: str


### Pydantic classes
class Task(BaseModel):
    """A task to be performed by a software engineer, containing a description and acceptance criteria"""
    description: str = Field(description="The descrption of the task to be performed")
    acceptance_criteria: str = Field(description="The acceptance criteria to define the success of the task to be performed")

class ProjectPlan(BaseModel):
    """The project plan of a software engineer sprint, defined by the raw plain text of the initial rationale and the list of tasks to be performed"""
    plan: str = "A full copy of the original prompt used to generate the task plan"
    tasks: List[Task] = Field(description="The list of tasks to be performed")