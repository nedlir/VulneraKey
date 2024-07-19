from variable_detector import replace_executed_variables_with_values
from malicious_code_detector import check_for_malicious_code
from report_exporter import print_report


def analyze_script(file_path):
    with open(file_path, 'r') as file:
        script_content = file.read()

    # script_content = decrypted_script(script_content) - to be added decryption of base64, utf, etc..
    script_content = replace_executed_variables_with_values(script_content)

    report, total_found = check_for_malicious_code(script_content)
    print_report(report, total_found)


if __name__ == "__main__":
    file_path = './tests/malicious_code.txt'
    analyze_script(file_path)
