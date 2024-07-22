import argparse

from variable_detector import replace_executed_variables_with_values
from malicious_code_detector import check_for_malicious_code
from report_exporter import print_report
from entropy_calculator import calculate_entropy


ENTROPY_THRESHOLD = 5.1


def analyze_script(file_path, check_entropy, entropy_threshold):
    with open(file_path, 'r', encoding='utf-8') as file:
        script_content = file.read()

    entropy = calculate_entropy(script_content) if check_entropy else None

    script_content = replace_executed_variables_with_values(script_content)

    report, total_malicious_patterns = check_for_malicious_code(script_content)

    print_report(report, total_malicious_patterns, entropy, entropy_threshold)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Analyze a script for malicious code and high entropy.')
    parser.add_argument('file_path', type=str, help='Path to the script file.')
    parser.add_argument('--entropy-threshold', type=float, default=ENTROPY_THRESHOLD,
                        help='Set the threshold for entropy detection.')
    parser.add_argument('--check-entropy', action='store_true', default=True,
                        help='Enable entropy checking (default).')
    parser.add_argument('--no-check-entropy', action='store_false',
                        help='Disable entropy checking.', dest='check_entropy')

    args = parser.parse_args()

    analyze_script(args.file_path, args.check_entropy, args.entropy_threshold)
