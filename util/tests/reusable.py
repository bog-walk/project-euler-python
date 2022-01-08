from time import perf_counter, perf_counter_ns


def compare_speed_seconds(
        solutions: dict,
        precision: int = 4,
        repeat: int = 1
) -> dict:
    """
    :param solutions: Dict containing all solution names
    as keys and their values representing [output name,
    *arguments].
    :param precision: Number of decimal places to format
    speed output.
    :param repeat: Number of times the solution function
    should be called.
    :return: Prints the speed in seconds of each function
    ordered from fastest to slowest, before returning a
    dictionary containing all solution names as keys and
    their function output as values.
    """
    results = dict()
    times = dict()
    for name, solution in solutions.items():
        function = solution[0]
        arguments = solution[1:]
        result = None
        start = perf_counter()
        for _ in range(repeat):
            result = function(*arguments)
        stop = perf_counter()
        results[name] = result
        times[name] = stop - start
    outputs = sorted(times.items(), key=lambda kv: kv[1])
    for name, time in outputs:
        print(f"{name} solution took: {time:.{precision}f}s")
    return results


def compare_speed_nano(
        solutions: dict,
        repeat: int = 1
) -> dict:
    """
    :param solutions: Dict containing all solution names
    as keys and their values representing [output name,
    *arguments].
    :param repeat: Number of times the solution function
    should be called.
    :return: Prints the speed in nanoseconds (formatted in
    scientific notation) of each function ordered from
    fastest to slowest, before returning a dictionary containing
    all solution names as keys and their function
    output as values.
    """
    results = dict()
    times = dict()
    for name, solution in solutions.items():
        function = solution[0]
        arguments = solution[1:]
        result = None
        start = perf_counter_ns()
        for _ in range(repeat):
            result = function(*arguments)
        stop = perf_counter_ns()
        results[name] = result
        times[name] = stop - start
    outputs = sorted(times.items(), key=lambda kv: kv[1])
    for name, time in outputs:
        symbol = "ns"
        time_f = time
        if time > 1_000_000:
            symbol = "ms"
            time_f = "{:.2f}".format(time / 1_000_000)
        elif time > 100_000:
            time_f = "{:.1e}".format(time)
        print(f"{name} solution took: {time_f}{symbol}")
    return results
