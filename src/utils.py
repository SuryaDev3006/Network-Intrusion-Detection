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

def ensure_artifacts_dir(directory):
    """
    Ensure that the artifact directory exists.
    Args:
        directory (str): Path to the directory.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        print_header(f"Created artifact directory at {directory}")