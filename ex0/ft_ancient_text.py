import sys
import typing

if (__name__ == "__main__"):
    try:
        if (len(sys.argv) > 2 or len(sys.argv) == 1):
            print("Usage: ft_ancient_text.py <file>")
        else:
            print("=== Cyber Archives Recovery ===")
            print(f"Accessing file ’{sys.argv[1]}’")
            file: typing.IO[str] = open(f"{sys.argv[1]}", "r")
            print(file.read(), end="")
            file.close()
    except FileNotFoundError:
        print("The file does not exist!")

    except PermissionError:
        print("You don't have permission to access this file!")

    except OSError:
        print("Something went wrong while accessing"
              "the file(like maybe the disk is full)!")
