from contextlib import redirect_stdout
from io import StringIO


def execute_python(code: str):
    # TODO: a better way to parse code
    code = f"""\
    {code}
    """
    parsed_code = code.split("\n", 1)[1]
    print(parsed_code)
    if not parsed_code:
        return None

    f = StringIO()
    with redirect_stdout(f):
        exec(parsed_code)

    return f.getvalue()
