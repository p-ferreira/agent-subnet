import subprocess
import json

def get_linter_penalties(filepath: str) -> float:
    command = f"eslint {filepath} --format=json"
    result = subprocess.run(command, shell=True, capture_output=True)
    # if result.returncode != 0:
    #     print("Error running ESLint:", result.stderr.decode())
    #     return None
    lint_output = json.loads(result.stdout.decode())
    severity_list = [ message['severity'] for message in lint_output[0]['messages'] ]

    severity_penalty_scores = {
        1: 0.01, # 1 - Warning, gets 0.1 penalty
        2: 0.05, # 2 - Error, gets 0.5 penalty
    }

    #get accumulated penalty score
    penalty_score = sum([severity_penalty_scores[severity] for severity in severity_list])

    return penalty_score


def calculate_reward(filepath: str) -> float:
    # get linter penalties
    linter_penalty_score = get_linter_penalties(filepath)

    reward = 1 - linter_penalty_score
    return reward
