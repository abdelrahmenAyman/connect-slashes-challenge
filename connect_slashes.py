EXAMPLE_INPUTS: list[str] = ["\\\\\\//\\/\\\\"]


class NegativeLeadingSpacesCount(Exception):
    pass


class FirstSymbolForwardSlashException(Exception):
    pass


def handle_backward_slash_case(leading_spaces_count: int) -> tuple[str, int]:
    new_line = " " * leading_spaces_count + "\\"
    return new_line, leading_spaces_count + 1


def handle_forward_slash_case(leading_spaces_count: int) -> tuple[str, int]:
    leading_spaces_count -= 1
    new_line = " " * leading_spaces_count + "/"
    return new_line, leading_spaces_count


def connect_slashes(inp: str) -> str:
    BACKWARD_SLASH = "\\"
    FORWARD_SLASH = "/"

    last_symbol = None
    output = ""
    leading_spaces_count = 0

    for symbol in inp:
        if last_symbol is None:
            if symbol == FORWARD_SLASH:
                raise FirstSymbolForwardSlashException(
                    "First symbol can not be forward slash"
                )
            output += symbol
            leading_spaces_count = 1
        elif symbol == BACKWARD_SLASH:
            new_line, leading_spaces_count = handle_backward_slash_case(
                leading_spaces_count
            )
            output += f"\n{new_line}"

        else:
            new_line, leading_spaces_count = handle_forward_slash_case(
                leading_spaces_count
            )
            if leading_spaces_count < 0:
                raise NegativeLeadingSpacesCount(
                    "Leading spaces count is not allowed to be negative"
                )
            output += f"\n{new_line}"

        last_symbol = symbol

    return output


if __name__ == "__main__":
    try:
        print("Please enter the slashes to connect:")
        print(connect_slashes(input()))
    except NegativeLeadingSpacesCount:
        print("Number of forward slashes can not be bigger than the number of back slashes")
    except FirstSymbolForwardSlashException as e:
        print(e)
