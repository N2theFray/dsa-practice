from scope import use_local_object, use_global_object, message


def test_global():
    assert message == "This is the global object."
    assert "message" in globals()
    assert id(use_global_object()) == id(message)


def test_local():
    assert use_local_object() == "This is the local object."