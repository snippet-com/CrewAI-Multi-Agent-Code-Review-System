from crewai import Agent

from config import llm
from review_tools import (
    run_linter,
    check_code_style,
    check_security,
    suggest_refactoring,
)


def create_agents():
    """
    Create and return all code review agents.
    """

    # ============================================
    # LEAD REVIEWER
    # ============================================

    lead_reviewer = Agent(
        role="Lead Code Reviewer",
        goal="Coordinate code review and provide high-level feedback",
        backstory="""
        You are a seasoned software architect with over 15 years of experience.
        You specialize in software architecture, clean code, and design patterns.
        Your reviews are constructive, practical, and focused on helping
        developers improve their code quality.
        """,
        llm=llm,
        verbose=True,
    )

    # ============================================
    # BUG HUNTER
    # ============================================

    bug_hunter = Agent(
        role="Bug Detection Specialist",
        goal="Identify bugs, edge cases, and potential runtime issues",
        backstory="""
        You have an exceptional eye for finding bugs, hidden edge cases,
        and logical flaws before software reaches production.
        """,
        tools=[run_linter],
        llm=llm,
        verbose=True,
    )

    # ============================================
    # STYLE GUARDIAN
    # ============================================

    style_guardian = Agent(
        role="Code Style and Best Practices Expert",
        goal="Ensure code follows Python best practices and style guidelines",
        backstory="""
        You are passionate about writing clean, readable, maintainable code.
        You help development teams maintain consistent coding standards.
        """,
        tools=[check_code_style],
        llm=llm,
        verbose=True,
    )

    # ============================================
    # PERFORMANCE ANALYST
    # ============================================

    performance_analyst = Agent(
        role="Performance Optimization Expert",
        goal="Identify inefficient code and suggest performance improvements",
        backstory="""
        You specialize in optimizing software performance and scalability.
        You can identify inefficient algorithms, memory issues,
        and unnecessary computations.
        """,
        llm=llm,
        verbose=True,
    )

    # ============================================
    # SECURITY AUDITOR
    # ============================================

    security_auditor = Agent(
        role="Security Specialist",
        goal="Identify security vulnerabilities and unsafe coding practices",
        backstory="""
        You are a cybersecurity expert who reviews applications for
        vulnerabilities, insecure coding patterns, and data protection issues.
        """,
        tools=[check_security],
        llm=llm,
        verbose=True,
    )

    # ============================================
    # REFACTORING ADVISOR
    # ============================================

    refactoring_advisor = Agent(
        role="Refactoring Expert",
        goal="Suggest improvements that increase maintainability and readability",
        backstory="""
        You specialize in refactoring legacy software into clean,
        modular, and maintainable code while preserving functionality.
        """,
        tools=[suggest_refactoring],
        llm=llm,
        verbose=True,
    )

    return {
        "lead_reviewer": lead_reviewer,
        "bug_hunter": bug_hunter,
        "style_guardian": style_guardian,
        "performance_analyst": performance_analyst,
        "security_auditor": security_auditor,
        "refactoring_advisor": refactoring_advisor,
    }