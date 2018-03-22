import pytest

from amom.broker.address import Address, Anycast, Multicast, Mixed


class TestAddress:

    @pytest.mark.parametrize("address_class", [Address, Anycast, Multicast, Mixed])
    def test_address(self, address_class: Address):
        test_address = address_class(value='x')
        assert test_address.value == 'x'
