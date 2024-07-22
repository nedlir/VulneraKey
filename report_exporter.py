from color_utils import print_malicious_pattern, print_total, print_entropy


def print_report(report, total_malicious_patterns, entropy, entropy_threshold):
    for entry in report:
        print_malicious_pattern(
            entry['pattern_description'], entry['line_number'], entry['line_content'])

    if entropy is not None and entropy >= entropy_threshold:
        print_entropy(entropy)

    print_total(total_malicious_patterns)
