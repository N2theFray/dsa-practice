from looping import iterate_with_conditions


def test_iterate_with_break_condition(capfd):
    iterate_with_conditions([1, 3, 8, 5])
    output = capfd.readouterr()[0].strip()
    assert "Found 8, break!" == output, "Output should be 'Found 8, break!'"


def test_iterate_with_continue_condition(capfd):
    iterate_with_conditions([1, 3, 5, 9])
    output = capfd.readouterr()[0].strip()
    assert "Found 5, continue!" == output, "Output should be 'Found 5, continue!'"


def test_iterate_with_both_continue_and_break(capfd):
    iterate_with_conditions([1, 3, 5, 8])
    output = capfd.readouterr()[0].strip()
    lines = output.split("\n")
    assert len(lines) == 2, "Output functions should have two lines"
    assert lines[0] == "Found 5, continue!", "First line should be continue"
    assert lines[1] == "Found 8, break!", "Second line should be break"