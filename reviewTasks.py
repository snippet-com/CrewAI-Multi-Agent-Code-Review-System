from crewai import Task


def create_tasks(agents, code: str, filename: str, context: str = ""):
    """
    Create all CrewAI review tasks.
    """

    # ============================================
    # AGENTS
    # ============================================

    lead_reviewer = agents["lead_reviewer"]
    bug_hunter = agents["bug_hunter"]
    style_guardian = agents["style_guardian"]
    performance_analyst = agents["performance_analyst"]
    security_auditor = agents["security_auditor"]
    refactoring_advisor = agents["refactoring_advisor"]

    # ============================================
    # TASK 1 - INITIAL ANALYSIS
    # ============================================

    analysis_task = Task(
        description=f"""
Perform initial analysis of the following code.

Filename:
{filename}

Code:
{code}

Context:
{context if context else "General code review"}

Provide:

1. Brief summary of what the code does.

2. Overall quality score (1-10).

3. Key strengths.

4. Main weaknesses.

5. Architectural observations.
""",
        agent=lead_reviewer,
        expected_output="Initial code analysis and quality assessment.",
    )

    # ============================================
    # TASK 2 - BUG DETECTION
    # ============================================

    bug_task = Task(
        description=f"""
Review the following code for bugs.

Code:

{code}

Focus on:

1. Logic errors

2. Runtime exceptions

3. Missing validation

4. Edge cases

5. Error handling

6. Race conditions

7. Memory leaks

8. Unexpected behaviors
""",
        agent=bug_hunter,
        expected_output="Detailed bug report with severity levels.",
        context=[analysis_task],
    )

    # ============================================
    # TASK 3 - STYLE REVIEW
    # ============================================

    style_task = Task(
        description=f"""
Review this code for style and best practices.

Code:

{code}

Check:

1. Naming conventions

2. Readability

3. Documentation

4. Pythonic code

5. Anti-patterns

6. Overall maintainability
""",
        agent=style_guardian,
        expected_output="Style review and best practices report.",
        context=[analysis_task],
    )

    # ============================================
    # TASK 4 - PERFORMANCE REVIEW
    # ============================================

    performance_task = Task(
        description=f"""
Review this code for performance issues.

Code:

{code}

Look for:

1. Algorithm efficiency

2. Time complexity

3. Memory usage

4. Resource utilization

5. Database query optimization (if applicable)

6. Caching opportunities

7. Unnecessary loops

8. Concurrency issues

Provide practical recommendations for improving performance.
""",
        agent=performance_analyst,
        expected_output="Performance analysis and optimization recommendations.",
        context=[analysis_task],
    )

    # ============================================
    # TASK 5 - SECURITY AUDIT
    # ============================================

    security_task = Task(
        description=f"""
Perform a security audit on the following code.

Code:

{code}

Check for:

1. Input validation

2. SQL Injection

3. Command Injection

4. Cross-Site Scripting (XSS)

5. Sensitive data exposure

6. Authentication issues

7. Authorization issues

8. Hardcoded credentials

9. Unsafe function usage

10. General security best practices
""",
        agent=security_auditor,
        expected_output="Security audit report with risk levels and mitigation recommendations.",
        context=[analysis_task],
    )

    # ============================================
    # TASK 6 - REFACTORING REVIEW
    # ============================================

    refactor_task = Task(
        description=f"""
Review this code and identify refactoring opportunities.

Code:

{code}

Consider:

1. Code duplication

2. Large functions

3. Large classes

4. SOLID principles

5. Design patterns

6. Readability

7. Maintainability

8. Reusability

9. Modularization opportunities

10. Overall architecture improvements
""",
        agent=refactoring_advisor,
        expected_output="Prioritized refactoring recommendations.",
        context=[
            analysis_task,
            bug_task,
            style_task,
        ],
    )

    # ============================================
    # TASK 7 - FINAL REPORT
    # ============================================

    final_task = Task(
        description=f"""
Create a comprehensive final code review report.

You have received findings from all reviewers.

Combine everything into a professional report.

Your report should include:

1. Executive Summary

2. Overall Code Quality Score (1-10)

3. Major Strengths

4. Critical Issues (Must Fix)

5. Medium Priority Improvements

6. Low Priority Improvements

7. Security Recommendations

8. Performance Recommendations

9. Refactoring Suggestions

10. Final Recommendation

Keep the report professional, structured, and actionable.
""",
        agent=lead_reviewer,
        expected_output="Comprehensive code review report.",
        context=[
            analysis_task,
            bug_task,
            style_task,
            performance_task,
            security_task,
            refactor_task,
        ],
    )

    # ============================================
    # CREATE CREW LISTS
    # ============================================

    crew_agents = [
        lead_reviewer,
        bug_hunter,
        style_guardian,
        performance_analyst,
        security_auditor,
        refactoring_advisor,
    ]

    crew_tasks = [
        analysis_task,
        bug_task,
        style_task,
        performance_task,
        security_task,
        refactor_task,
        final_task,
    ]

    return crew_agents, crew_tasks