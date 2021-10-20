from rsa import _parse_args


def test_parse_args():
    assert isinstance(_parse_args(), tuple)
