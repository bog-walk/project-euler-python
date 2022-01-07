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
    :return: Dict containing all solution names as keys
    and their function output as values.
    """
    results = dict()
    times = []
    for solution, values in solutions.items():
        arguments = values[1:]
        result = None
        start = perf_counter()
        for _ in range(repeat):
            result = solution(*arguments)
        stop = perf_counter()
        results[solution] = result
        times.append(stop - start)
    for solution, time in zip(
            [value[0] for value in solutions.values()], times
    ):
        print(f"{solution} solution took: {time:.{precision}f}s")
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
    :return: Dict containing all solution names as keys
    and their function output as values.
    """
    results = dict()
    times = []
    for solution, values in solutions.items():
        arguments = values[1:]
        result = None
        start = perf_counter_ns()
        for _ in range(repeat):
            result = solution(*arguments)
        stop = perf_counter_ns()
        results[solution] = result
        times.append(stop - start)
    for solution, time in zip(
            [value[0] for value in solutions.values()], times
    ):
        print(f"{solution} solution took: " +
              f"{time if time <= 10_000 else '{:.2e}'.format(time)}ns")
    return results
