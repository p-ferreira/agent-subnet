import langchain
from loguru import logger
from agents import ProjectManagerAgent, SoftwareEngineerAgent, CodeFile, Task
from tqdm import tqdm
from rewards import calculate_reward


def get_requirements() -> str:
    requirements = """Requirements:
I need a single-page application with a header, followed by a section with a digital clock and a footer:
- The header should contain the text: "Hello from the agent-metaverse side! Here is the result of my first experiment:"
- The clock section should be centrally aligned and contain a digital clock that updates every second. The background color of the div should be black and the text color should be white.
- The footer should contain the text: "Powered by synapse labs" in font 14px, italic, and color black.
"""
    
    return requirements


def forward():
    requirements: str = get_requirements()
    
    ## TODO: create git repo

    # create agents
    project_manager: ProjectManagerAgent = ProjectManagerAgent()    
    
    # get project plan
    project_plan = project_manager.create_project_plan(requirements)

    source_code: CodeFile = None        
    developer_agent_file_history = []
    reviwer_agent_file_history = []

    for task in tqdm.tqdm(project_plan.tasks):
        # write code
        developer_agent = SoftwareEngineerAgent()

        # If source code is empty, write code from task description
        if source_code is None:
            file: CodeFile = developer_agent.write_code(task.description)                    
        # Otherwise, write code from already existing source code
        else:
            task_with_existing_code = task.description + f'\nBase code to be evolved: {source_code}'
            file: CodeFile = developer_agent.write_code(task_with_existing_code)

        # review code
        reviewer_agent = SoftwareEngineerAgent()
        reviewed_file: CodeFile = reviewer_agent.review_code(task, file)

        developer_agent_file_history.append(file)
        reviwer_agent_file_history.append(reviewed_file)
        source_code = reviewed_file

    # Writing the file to disk
    with open(source_code.filename, 'w') as file:
        file.write(source_code.content)
      
    # apply reward function
    reward = calculate_reward(source_code.filename)
    logger.info(f"Reward: {reward}")
    
    # TODO: push file to git repo


if __name__ == "__main__":
    langchain.debug = True
    forward()