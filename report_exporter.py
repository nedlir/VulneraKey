from color_utils import print_malicious_pattern, print_result


def print_report(report, total_found):
    for entry in report:
        print_malicious_pattern(
            entry['pattern_description'], entry['line_number'], entry['line_content'])
    print_result(total_found)

# export_to_file TBA
