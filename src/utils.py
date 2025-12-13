import os 


def print_header(message):
    """
    Print a formatted header message.
    Args:
        message (str): The message to print.
    """
    print("\n" + "=" * len(message))
    print(f"{message}")
    print("=" *len(message) + "\n")