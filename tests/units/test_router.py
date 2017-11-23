from amom.router import Router


def test_isinstance(router: Router):
    assert isinstance(router, Router)


def test_name(router: Router):
    assert router.name == 'Qpid Dispatch Router'


def test_restart(router: Router):
    assert router.service._restart().get_ecode() == 0


def test_stop(router: Router):
    assert router.service._stop().get_ecode() == 0


def test_start(router: Router):
    assert router.service._start().get_ecode() == 0