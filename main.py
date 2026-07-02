from code_review_system import CodeReviewSystem


def main():

    system = CodeReviewSystem()

    sample_code = """
def process_user_data(user_data, user_id):
    # TODO: Add validation
    result = []

    for item in user_data:
        if item.get("active") == True:
            item["user_id"] = user_id
            item["processed_date"] = "today"
            result.append(item)

    if len(result) > 1000:
        print(f"Processing {len(result)} records")

    return result
"""

    result = system.review_code(
        code=sample_code,
        filename="user_processor.py",
        context="This code handles user data processing in a web application.",
    )

    print("\n" + "=" * 70)
    print("📋 FINAL REVIEW REPORT")
    print("=" * 70)

    print(result)


if __name__ == "__main__":
    main()