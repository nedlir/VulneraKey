import json
import re


# Load malicious patterns from JSON file
with open('patterns.json', 'r') as file:
    MALICIOUS_PATTERNS = json.load(file)


def check_for_malicious_code(script_text):
    report = list()
    lines = script_text.splitlines()

    for line_number, line in enumerate(lines, start=1):
        for pattern, description in MALICIOUS_PATTERNS.items():
            if re.search(pattern, line):
                report.append({
                    'line_number': line_number,
                    'line_content': line,
                    'pattern_description': description
                })

    total_found = len(report)
    return report, total_found
