from time import perf_counter_ns
from typing import Any, Callable


def __output_speed(speeds: dict, precision: int):
    """
    Sorts measured speeds from fastest to slowest, and prints each speed in
    nanoseconds (scientific notation if large), milliseconds, or seconds (to the
    required precision), depending on the size of the speed value.

    :param speeds: Dict containing solution output name as keys and their values
        representing the calculated speed of the solution function.
    :param precision: Number of decimal places to format speed output, if in seconds.
    """
    outputs = sorted(speeds.items(), key=lambda kv: kv[1])
    for name, time in outputs:
        if time >= 1_000_000_000:
            time_f = f"{time / 1e9:.{precision}f}s"
        elif time >= 1_000_000:
            time_f = "{:.2f}ms".format(time / 1e6)
        elif time >= 10_000:
            time_f = "{:.1e}ns".format(time)
        else:
            time_f = f"{time}ns"
        print(f"{name} solution took: {time_f}")


def compare_speed(
        solutions: dict,
        precision: int = 2,
        repeat: int = 1
) -> dict:
    """ Compares the speed of multiple functions with output displayed in a unit
    appropriate to the speed, via the helper function, output_speed().

    :param solutions: Dict containing all solution output names as keys and their
        values representing [solution, *arguments].
    :param precision: Number of decimal places to format speed output.
    :param repeat: Number of times the solution function should be called.
    :returns: Prints the speed in seconds of each function ordered from fastest to
        slowest, before returning a dictionary containing all solution names as keys
        and their function output as values.
    """
    results = dict()
    times = dict()
    for name, solution in solutions.items():
        function = solution[0]
        arguments = solution[1:]
        start = perf_counter_ns()
        result = function(*arguments)
        for _ in range(repeat-1):
            function(*arguments)
        stop = perf_counter_ns()
        results[name] = result
        times[name] = (stop - start) // repeat
    __output_speed(times, precision)
    return results


def get_test_resource(
        filepath: str,
        line_strip: str = " \n",
        transformation: Callable[[str], Any] = None,
        line_split: str = " "
) -> list[str] | list[list]:
    """ Retrieves content of a test resource file, as is (default) or transformed.

    :param filepath: Relative path for test resource file.
    :param line_strip: Characters to remove from the left & right of each file line.
    :param transformation: Transformation function that takes either an entire
        line as an argument or, if split, individual elements in a line. Note that
        functions that are called on the string class, e.g. str.lower(), rather
        than taking a string as an argument, must be provided as a lambda function.
    :param line_split: Characters to use as the delimiter when splitting a line.
    :returns: List of each file line as a string, if default arguments used;
        otherwise, a list of each line as a list of transformed elements.
    """

    with open(filepath) as resourceFile:
        if transformation is None:
            resource = [line.strip(line_strip) for line in resourceFile]
        else:
            resource = [
                list(
                    map(transformation, line.strip(line_strip).split(line_split))
                )
                for line in resourceFile
            ]
    return resource
