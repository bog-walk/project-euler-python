""" Problem 79: Passcode Derivation

https://projecteuler.net/problem=79

Goal: Based on a collection of successful login attempts using 3 characters
(ASCII codes [33, 126]) in order (but not necessarily consecutive), determine the
shortest (& lexicographically smallest) original password of unknown length with
only unique characters. If a password is not possible, return None.

Constraints: 1 <= login attempts <= 3000

e.g.: attempts = {an0, n/., .#a}
     password = null
     1st attempt shows that 'n' must follow 'a'.
     2nd attempt shows that '.' must follow 'n'.
     But the last attempt has 'a' after '.' which should not be possible.
"""


def derive_passcode(logins: list[str]) -> str | None:
    """
    Solution stores all connections between each login character & characters that
    potentially precede it in the passcode, using a pseudo-graph.

    A stored character will be next in the passcode if it has degree 0 (i.e. no
    connecting edges), with multiple choices being judged based on their
    lexicographic order (as the cache is a list, the smallest will be the first
    element found that is an empty set).

    Once a character is added to the passcode, its presence in the list is
    nullified & it is removed from all characters that referenced it as an edge.

    A passcode is considered invalid/unattainable if at any point there are no
    degree 0 characters & a null value is returned.

    N.B. A dictionary could be used to cache all character nodes & references &
    would require dictionary keys to be sorted to find the smallest insert for
    every iteration.
    """

    # reduce cache size to ASCII characters between 33 and 126 inclusive
    offset = 33
    connections: list[set[int] | None] = [None]*(127 - offset)
    for login in logins:
        # normalise login character ASCII to fit in cache
        codes = [ord(ch) - offset for ch in login]
        for i in range(3):
            if i == 0:
                # create a new set if a new character
                # otherwise preceding characters unknown
                if connections[codes[0]] is None:
                    connections[codes[0]] = set()
            else:
                if connections[codes[i]] is None:
                    connections[codes[i]] = {codes[i-1]}
                else:
                    connections[codes[i]].update({codes[i - 1]})
    passcode = ""
    # break loop if no more edges exist
    while any(edges is not None for edges in connections):
        try:
            smallest = connections.index(set())
            passcode += chr(smallest + offset)
            # remove all existence of the character just added
            connections[smallest] = None
            for i in range(94):
                if connections[i] is not None:
                    # this function does nothing if the element is not present
                    # so no need to check each set for it first
                    connections[i].discard(smallest)
        except ValueError:
            # break loop if no isolated characters exist
            return None
    return passcode
