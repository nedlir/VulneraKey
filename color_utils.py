from colorama import Fore, Style, init


init(autoreset=True)  # Initialize colorama with autoreset


def highlight_text(text, color=Fore.YELLOW):
    return f"{color}{text}{Style.RESET_ALL}"


def print_highlighted(message, highlight_color=Fore.YELLOW):
    print(highlight_text(message, highlight_color))


def print_malicious_pattern(description, line_number, line):
    print(highlight_text("Detected malicious pattern:", Fore.RED), description)
    print(highlight_text(f"Line {line_number}:", Fore.YELLOW), line.strip())


def print_total(total_malicious_patterns):
    if total_malicious_patterns > 0:
        result_message = f"Found {highlight_text(str(total_malicious_patterns), Fore.RED)} malicious pattern(s) in the script."
    else:
        result_message = highlight_text(
            "No malicious patterns found.", Fore.GREEN)
    print(result_message)


def print_entropy(entropy):
    entropy_message = highlight_text(
        f"High entropy detected: {entropy:.4f}. The file may be obfuscated or encrypted, potentially indicating malware.",
        Fore.MAGENTA)
    print(entropy_message)
