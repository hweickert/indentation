def set( string, target_level, indent_string="    ", indent_empty_lines=False ):
    """ Sets indentation of a single/multi-line string. """

    lines = string.splitlines()
    set_lines( lines, target_level, indent_string=indent_string, indent_empty_lines=indent_empty_lines )
    result = "\n".join(lines)
    return result


def set_lines( lines, target_level, indent_string="    ", indent_empty_lines=False ):
    """ Sets indentation for the given set of :lines:. """

    first_non_empty_line_index = _get_first_non_empty_line_index( lines )
    first_line_original_level =  get_line_level( lines[first_non_empty_line_index], indent_string )

    for i in range(first_non_empty_line_index, len(lines)):
        if not indent_empty_lines and lines[i] == "":
            continue

        line_i_unindented = get_line_unindented( lines[i], indent_string )
        line_i_level =      get_line_level( lines[i], indent_string )

        on_second_line_or_later = i > first_non_empty_line_index
        if on_second_line_or_later:
            first_line_final_level = get_line_level( lines[first_non_empty_line_index], indent_string )
            relative_indent_move =   first_line_final_level - first_line_original_level
            target_level =           line_i_level + relative_indent_move

        if line_i_level == target_level:
            continue

        lines[i] = indent_string * target_level + line_i_unindented


def _get_first_non_empty_line_index(lines):
    i = 0
    for i, line in enumerate(lines):
        if line.strip(" ") != "":
            break
    return i



def get_line_level( line, indent_string="    " ):
    result = 0
    while line.startswith(indent_string):
        line = line[len(indent_string):]
        result += 1
    return result


def get_line_unindented( line, indent_string="    " ):
    result = line
    while result.startswith(indent_string):
        result = result[len(indent_string):]
    return result
