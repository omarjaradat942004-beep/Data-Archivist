import sys
import typing

if (__name__ == "__main__"):
    try:
        if (len(sys.argv) > 2 or len(sys.argv) == 1):
            print("Usage: ft_ancient_text.py <file>")
        else:
            print("=== Cyber Archives Recovery ===")
            print(f"Accessing file ’{sys.argv[1]}’\n---\n")
            file: typing.IO[str] = open(f"{sys.argv[1]}", "r")
            print(file.read(), end="")
            print("\n---")
            file.close()
            print("Transform data:\n---\n")
            file2: typing.IO[str] = open(f"{sys.argv[1]}", "r")
            original: str = file2.read()
            Transform: str = ""
            for ch in original:
                if (ch == "\n"):
                    Transform += "#\n"
                else:
                    Transform += ch
            file2.close()
            file2 = open(f"{sys.argv[1]}", "w")
            file2.write(Transform)
            file2.close()
            file2 = open(f"{sys.argv[1]}", "r")
            print(file2.read())
            file2.close()
            sys.stdout.write("Enter new file name (or empty): ")
            sys.stdout.flush()
            file_input = sys.stdin.readline().strip()
            if (file_input):
                print(f"Saving data to ’{file_input}’")
                file3: typing.IO[str] = open(f"{file_input}", "w")
                print(f"Data saved in file ’{file_input}’.")
                file3.write(Transform)
                file3.close()
            else:
                print("Not saving data.")

    except FileNotFoundError:
        print("[STDERR] Error The file does not exist!", file=sys.stderr)
        if (file_input):
            print(f"denied: ’{file_input}’,", file=sys.stderr)
            print("Data not saved.", file=sys.stderr)

    except PermissionError:
        print("[STDERR] Error You don't have permission"
              "to access this file!", file=sys.stderr)
        if (file_input):
            print(f"denied: ’{file_input}’,", file=sys.stderr)
            print("Data not saved.", file=sys.stderr)

    except OSError:
        print("[STDERR] Error Something went wrong while accessing"
              "the file(like maybe the disk is full)!")
        if (file_input):
            print(f"denied: ’{file_input}’,", file=sys.stderr)
            print("Data not saved.", file=sys.stderr)
