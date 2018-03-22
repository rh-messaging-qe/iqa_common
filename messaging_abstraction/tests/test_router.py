from messaging_abstraction.router import Router


class TestRouter:

    def test_router_node(self):
        router = Router()
        assert router
