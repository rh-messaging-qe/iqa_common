from ansible.inventory.host import Host
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.template import Templar


class AnsibleInventory(object):
    def __init__(self, inventory: str=None, extra_vars: dict=None):
        self.inventory = inventory
        self.loader = DataLoader()
        self.inv_mgr = InventoryManager(loader=self.loader, sources=self.inventory)
        self.var_mgr = VariableManager(loader=self.loader, inventory=self.inv_mgr)
        self.var_mgr.extra_vars = extra_vars

    def get_hosts_containing(self, var: str=None) -> list:
        hosts = []

        for host in self.inv_mgr.get_hosts():
            # If no specific var provided, then add it to the list
            if not var:
                hosts.append(host)
                continue

            # If var is provided and not part of host vars, ignore it
            host_vars = self.var_mgr.get_vars(host=host)
            if var not in host_vars:
                continue

            # Var has been found so adding it
            hosts.append(host)

        return hosts

    def get_host_vars(self, host: Host):
        data = self.var_mgr.get_vars(host=host)
        templar = Templar(variables=data, loader=self.loader)
        return templar.template(data, fail_on_undefined=False)
