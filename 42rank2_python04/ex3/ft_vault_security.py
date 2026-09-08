#!/usr/bin/env python3

def secure_archive(
        filename: str,
        action: str = "read",
        content: str = ""
        ) -> tuple[bool, str]:

    try:
        if action == "read":
            with open(filename, "r") as f:
                content = f.read()
                return (True, content)
        elif action == "write":
            with open(filename, "w") as f:
                f.write(content)
                return (True, "Content successfully written to file")
        else:
            return (False, "Invalid action parameter. Usage: secure_archive"
                           "(<filename>, <action (optional: read/write)>, "
                           "<content (optional for writing mode)>)")

    except (FileNotFoundError, PermissionError) as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(f"{secure_archive('/not/existing/file')}\n")

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(f"{secure_archive('/etc/shadow')}\n")

    print("Using 'secure_archive' to read from a regular file:")
    valid_output = secure_archive("ancient_fragment.txt")
    print(f"{valid_output}\n")

    print("Using 'secure_archive' to write previous content to a new file:")
    _, content = valid_output  # we don't care about the boolean
    new_file = "new_file.txt"
    print(f"{secure_archive(new_file, 'write', content)}")
