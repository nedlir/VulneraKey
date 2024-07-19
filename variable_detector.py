import re


def extract_variables_and_identify_executions(script_text):
    variables = dict()
    variable_executions = dict()
    variable_assignment_pattern = re.compile(r'(\w+)\s*:=\s*"(.*?)"')
    variable_execution_pattern = re.compile(r'%\s*(.*?)\s*%')

    for line in script_text.splitlines():
        variable_match = variable_assignment_pattern.search(line)
        if variable_match:
            variable_name = variable_match.group(1)
            variable_value = variable_match.group(2)
            variables[variable_name] = variable_value

        execution_match = variable_execution_pattern.search(line)
        if execution_match:
            executed_variables = execution_match.group(1).split('.')
            executed_variables = [var.strip() for var in executed_variables]
            variable_executions[line.strip()] = executed_variables

    return variables, variable_executions


def replace_executed_variables_with_values(script_text):
    variables, variable_executions = extract_variables_and_identify_executions(
        script_text)

    # Iterate through each line where variables are executed
    for line, executed_variables in variable_executions.items():
        assigned_values = list()

        for var in executed_variables:
            # If the variable exists in our dictionary, use its value, if not then keep original value
            assigned_value = variables.get(var, var)
            assigned_values.append(assigned_value)

        full_command = ''.join(assigned_values)

        # Replace the original line with the resolved command
        script_text = script_text.replace(line, full_command)

    # Return the modified script with all variables replaced
    return script_text
