from crewai.tools import tool


# ============================================
# LINTER TOOL
# ============================================

@tool
def run_linter(code: str, language: str = "python") -> str:
    """
    Run static code analysis to find issues.
    """

    issues = []

    # Simulated linting
    if "print(" in code and "print(" in code.split("\n")[-1]:
        issues.append("Consider removing debug prints")

    if "TODO" in code:
        issues.append("Unresolved TODO comment found")

    if len(code.split("\n")) > 100:
        issues.append("Function/class too long, consider refactoring")

    if issues:
        return "Linter Results:\n" + "\n".join(
            f"- {issue}" for issue in issues
        )

    return "✅ No linting issues found"


# ============================================
# STYLE CHECK TOOL
# ============================================

@tool
def check_code_style(code: str) -> str:
    """
    Check code against style guidelines.
    """

    style_issues = []

    # Simulated style checks
    if "import " in code and "import *" in code:
        style_issues.append("Avoid wildcard imports (import *)")

    if "class " in code and not "self" in code:
        style_issues.append(
            "Class method may be missing self parameter"
        )

    if style_issues:
        return "Style Check:\n" + "\n".join(
            f"- {issue}" for issue in style_issues
        )

    return "✅ Code style looks good!"


# ============================================
# REFACTORING TOOL
# ============================================

@tool
def suggest_refactoring(code: str) -> str:
    """
    Suggest code improvements and refactoring opportunities.
    """

    suggestions = []

    # Simulated suggestions
    if (
        "for" in code
        and "range" in code
        and len(code.split("\n")) > 20
    ):
        suggestions.append(
            "Consider using list comprehension instead of loop"
        )

    if (
        "if" in code
        and "elif" in code
        and len(code.split("\n")) > 30
    ):
        suggestions.append(
            "Large if-elif chain, consider using dict mapping or pattern matching"
        )

    if suggestions:
        return "Refactoring Suggestions:\n" + "\n".join(
            f"- {suggestion}" for suggestion in suggestions
        )

    return "✅ Code is well-structured"


# ============================================
# SECURITY TOOL
# ============================================

@tool
def check_security(code: str) -> str:
    """
    Check for security vulnerabilities.
    """

    vulnerabilities = []

    # Simulated security checks
    if "eval(" in code or "exec(" in code:
        vulnerabilities.append(
            "🚨 CRITICAL: Use of eval/exec - security risk!"
        )

    if "subprocess." in code and "input" in code:
        vulnerabilities.append(
            "⚠️ WARNING: Subprocess with user input - command injection risk"
        )

    if (
        "password" in code.lower()
        or "secret" in code.lower()
    ):
        vulnerabilities.append(
            "⚠️ WARNING: Potential hardcoded credentials found"
        )

    if vulnerabilities:
        return "Security Audit:\n" + "\n".join(
            f"- {issue}" for issue in vulnerabilities
        )

    return "✅ No security issues found"