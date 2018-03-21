import pytest

from amom.address.address import Address
from amom.address import Anycast, Multicast, Mixed


class TestAddress:

    @pytest.mark.parametrize("address_class", [Address, Anycast, Multicast, Mixed])
    def test_address(self, address_class: Address):
        test_address = address_class(value='x')
        assert test_address.value == 'x'
