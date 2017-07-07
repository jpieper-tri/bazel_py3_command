# -*- python -*-

py_binary(
    name = "my_python_script",
    srcs = ["my_python_script.py"],
    # If I set these to PY2, then things work.
    srcs_version = "PY3",
    default_python_version = "PY3",
)

genrule(
    name = "thing_my_script_generates",
    srcs = ["input_file.txt"],
    outs = ["output_file.txt"],
    tools = [":my_python_script"],
    cmd = "$(location :my_python_script) $(SRCS) -o $(OUTS)",
)
