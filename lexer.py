from __future__ import annotations

_BF_COMMANDS: frozenset[str] = frozenset("+-<>[].,")


def tokenize(source: str) -> list[tuple[str, int]]:
    return [
        (char, pos)
        for pos, char in enumerate(source)
        if char in _BF_COMMANDS
    ]


if __name__ == "__main__":
    _tests: list[tuple[str, list[tuple[str, int]]]] = [
        ("++[->]", [('+', 0), ('+', 1), ('[', 2), ('-', 3), ('>', 4), (']', 5)]),
        ("", []),
        ("hello world!", []),
        ("+-<>[].,", [('+', 0), ('-', 1), ('<', 2), ('>', 3),
                      ('[', 4), (']', 5), ('.', 6), (',', 7)]),
        ("++++ BF is fun ++ [ > ++", [('+', 0), ('+', 1), ('+', 2), ('+', 3),
                                      ('+', 15), ('+', 16), ('[', 18),
                                      ('>', 20), ('+', 22), ('+', 23)]),
        ("a+b-c", [('+', 1), ('-', 3)]),
    ]

    all_passed = True
    for source, expected in _tests:
        result = tokenize(source)
        status = "OK  " if result == expected else "FAIL"
        if result != expected:
            all_passed = False
        print(f"[{status}] tokenize({source!r})")
        if result != expected:
            print(f"       expected: {expected}")
            print(f"       got:      {result}")

    print()
    print("All tests passed." if all_passed else "Some tests FAILED.")
