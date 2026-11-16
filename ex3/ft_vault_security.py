def secure_archive(File: str, action: str, content: str) -> tuple[bool, str]:
    try:
        print("=== Cyber Archives Security ===")
        operation: bool = True
        with open(f"{File}", f"{action}") as file:
            if (action == "r"):
                return (operation, file.read())
            elif (action == "w"):
                file.write(content)
                file.write("\n")
                return (operation, content)
            else:
                operation = False
                return (operation, "Invalid action. Choose 'r' or 'w'")

    except FileNotFoundError:
        operation = False
        return (operation, "The file does not exist!")

    except PermissionError:
        operation = False
        return (operation, "You don't have permission to access this file!")

    except OSError:
        operation = False
        return (operation, "Something went wrong while accessing"
                "the file(like maybe the disk is full)!")


if (__name__ == "__main__"):
    print(secure_archive("test.txt", "w", "my name is omar"))
