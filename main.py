import re
from colorama import Fore, Style, init
from patterns import malicious_patterns

# Initialize colorama with autoreset
init(autoreset=True)

VARIABLES = dict()
VARIABLE_EXECUTIONS = dict()


def extract_variables_and_identify_executions(script_text):
    variable_assignment_pattern = re.compile(r'(\w+)\s*:=\s*"(.*?)"')
    variable_execution_pattern = re.compile(r'%\s*(.*?)\s*%')

    for line in script_text.splitlines():
        variable_match = variable_assignment_pattern.search(line)
        if variable_match:
            variable_name = variable_match.group(1)
            variable_value = variable_match.group(2)
            VARIABLES[variable_name] = variable_value

        execution_match = variable_execution_pattern.search(line)
        if execution_match:
            executed_variables = execution_match.group(1).split('.')
            executed_variables = [var.strip() for var in executed_variables]
            VARIABLE_EXECUTIONS[line.strip()] = executed_variables


def replace_executed_variables_with_values(script_text):
    for line, executed_variables in VARIABLE_EXECUTIONS.items():
        full_command = ''
        for var in executed_variables:
            full_command += VARIABLES.get(var, var)
        script_text = script_text.replace(line, full_command)
    return script_text


def highlight_pattern_in_line(line, pattern):
    match = re.search(pattern, line)
    if match:
        start_index, end_index = match.span()
        highlighted_line = (
            line[:start_index] + f"{Fore.YELLOW}" +
            line[start_index:end_index] +
            f"{Style.RESET_ALL}" + line[end_index:]
        )
        return highlighted_line
    return line


def check_for_malicious_code(script_text):
    lines = script_text.splitlines()
    total_found = 0

    for line_number, line in enumerate(lines, start=1):
        for pattern, description in malicious_patterns.items():
            pattern_found = re.search(pattern, line)
            if pattern_found:
                highlighted_line = highlight_pattern_in_line(line, pattern)
                detected_message = f"{Fore.RED}Detected malicious pattern:{Style.RESET_ALL} {description}"
                line_message = f"{Fore.YELLOW}Line {line_number}:{Style.RESET_ALL} {highlighted_line.strip()}"
                print(detected_message)
                print(line_message)
                total_found += 1

    return total_found


if __name__ == "__main__":
    file_path = './tests/malicious_code3.txt'

    with open(file_path, 'r') as file:
        script_content = file.read()

    extract_variables_and_identify_executions(script_content)
    modified_script_content = replace_executed_variables_with_values(
        script_content)
    total_malicious_patterns = check_for_malicious_code(
        modified_script_content)

    if total_malicious_patterns > 0:
        result_message = f"Found {Fore.RED}{total_malicious_patterns} malicious pattern(s){Style.RESET_ALL} in the script."
    else:
        result_message = f"{Fore.GREEN}No malicious patterns found.{Style.RESET_ALL}"

    print(result_message)
