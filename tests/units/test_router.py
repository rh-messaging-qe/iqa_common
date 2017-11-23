from amom.router import Router


def test_isinstance(router: Router):
    assert isinstance(router, Router)


def test_name(router: Router):
    assert router.name == 'Qpid Dispatch Router'
