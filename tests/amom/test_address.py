import pytest

from amom.address.address import Address
from amom.address import Anycast
from amom.address import Multicast
from amom.address import Mixed


class TestAddress:

    @pytest.mark.parametrize("address_class", [Address, Anycast, Multicast, Mixed])
    def test_address(self, address_class: Address):
        test_address = address_class(value='x')
        assert test_address.value == 'x'
