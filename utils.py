import json
from datetime import datetime


def save_review(filename: str, code: str, review_result):
    """
    Save the code review results to a JSON file.
    """

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    review_data = {
        "timestamp": datetime.now().isoformat(),
        "file": filename,
        "code": code,
        "review": str(review_result),
    }

    output_file = f"code_review_{timestamp}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(review_data, f, indent=4)

    print(f"\n💾 Review saved to: {output_file}")