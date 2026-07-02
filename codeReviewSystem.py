from crewai import Crew, Process

from review_agents import create_agents
from review_tasks import create_tasks
from utils import save_review


class CodeReviewSystem:
    """
    Main orchestration class for the CrewAI Code Review System.
    """

    def __init__(self):
        self.agents = create_agents()

    def review_code(
        self,
        code: str,
        filename: str = "reviewed_code.py",
        context: str = "",
    ):
        """
        Run the complete code review workflow.
        """

        print("\n" + "=" * 70)
        print("🔍 CODE REVIEW SYSTEM")
        print(f"📁 File: {filename}")
        print(f"📏 Lines: {len(code.splitlines())}")
        print("=" * 70 + "\n")

        crew_agents, crew_tasks = create_tasks(
            self.agents,
            code,
            filename,
            context,
        )

        crew = Crew(
            agents=crew_agents,
            tasks=crew_tasks,
            process=Process.sequential,
            verbose=True,
        )

        result = crew.kickoff()

        save_review(
            filename=filename,
            code=code,
            review_result=result,
        )

        return result