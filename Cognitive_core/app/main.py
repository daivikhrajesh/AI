import importlib
import os
from api.app import app  # Importing FastAPI app from api

def load_module(module_name):
    module_path = os.path.join(os.path.dirname(__file__), f"{module_name}.py")
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

from main.comprehension.comprehension_agent import ComprehensionAgent
from main.orchestration.orchestrator import Orchestrator
from main.reasoning.reasoning_agent import ReasoningAgent
from main.evaluation.evaluator import Evaluator

print('Cognitive CORE - Initializing...')

def main():
    print('Cognitive Core - Starting...')

def process_user_input(user_input: str) -> str:
    # Initialize system components
    comprehension = ComprehensionAgent()
    orchestrator = Orchestrator()
    reasoning = ReasoningAgent()
    evaluator = Evaluator()

    structured_input = comprehension.process_input(user_input)
    task = orchestrator.delegate_task(structured_input)
    solution = reasoning.solve(task)
    evaluation = evaluator.evaluate(solution)

    return evaluation

if __name__ == "__main__":
    main()
