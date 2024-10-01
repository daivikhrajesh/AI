from app.main.comprehension.comprehension_agent import ComprehensionAgent
from app.main.orchestration.orchestrator import Orchestrator
from app.main.reasoning.reasoning_agent import ReasoningAgent
from app.main.evaluation.evaluator import Evaluator

def process_user_input(user_input: str) -> str:
    # Initialize system components
    comprehension_agent = ComprehensionAgent()
    orchestrator = Orchestrator()
    reasoning_agent = ReasoningAgent()
    evaluator = Evaluator()

    # Process the input through the comprehension agent
    structured_input = comprehension_agent.process_input(user_input)

    # Delegate the task using the orchestrator
    task = orchestrator.delegate_task(structured_input)

    # Solve the task with the reasoning agent
    solution = reasoning_agent.solve(task)

    # Evaluate the solution with the evaluator
    evaluation = evaluator.evaluate(solution)

    return evaluation
