INVENTORY = container-environment/inventory
ANSIBLE_ARGS = -i ($INVENTORY) -vvv

containers = client_node_1 broker_node_1 router_node_1
clean = docker rm -f $(containers) || true

all: deploy_container_env precheck_container_env

deploy_container_env:
	$(clean)
	ansible-playbook container-environment/deploy_container_env.yml $(ANSIBLE_ARGS)

precheck_container_env:
	ansible-playbook container-environment/precheck_container_env.yml $(ANSIBLE_ARGS)

clean:
    $(clean)
