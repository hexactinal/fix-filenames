import sys


def do_args_error_checking(user_args: list[str]) -> str:
    """
    Does the error checking for the user's passed in command line arguments.
    :param user_args: The user's passed in command line arguments.
    :return: String containing the directory that the user wishes to search in.
    """
    if len(user_args) > 2:
        print("Usage: fix-filenames directory")
        # We're using a return code of 1 here to indicate that the process failed.
        sys.exit(1)
    elif len(user_args) == 1:
        # By default, we will use the current directory.
        return "."
    elif len(user_args) == 2:
        # user_args[0] is the process name.
        # user_args[1] is the directory name that the user typed in.
        return user_args[1]


user_filename = do_args_error_checking(sys.argv)

print(f"---Searching '{user_filename}'---")
