def assert_eq_dicts(dict_a: dict, dict_b: dict, ignore_keys: set | None = None) -> None:
    """Compare two dictionaries, with the ability to ignore keys.

    :param dict_a: First dictionary to compare
    :param dict_b: Secon dictionary to comapre
    :param ignore_keys: Set of keys to ignore (optional)
    :raise AssertionError: When dictionaries don't match
    """
    ignore_keys = set() if not ignore_keys else ignore_keys
    ka = set(dict_a).difference(set(ignore_keys))
    kb = set(dict_b).difference(set(ignore_keys))
    assert ka == kb, f"Dictionaries have different sets of keys: {ka} != {kb}"
    assert [1 for k in ka if dict_a[k] != dict_b[k]] == [], "Dictionaries do not match: " + ", ".join(
        [f"{dict_a[k]} != {dict_b[k]}" for k in ka if dict_a[k] != dict_b[k]])
