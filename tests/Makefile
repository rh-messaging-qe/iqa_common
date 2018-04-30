.PHONY: deploy_container_env precheck_container_env clean

INVENTORY = container-environment/inventory
ANSIBLE_ARGS = -i $(INVENTORY) -vvv

containers = client1 broker1 router1
clean = docker rm -f $(containers) || true

all: deploy_container_env

deploy_container_env:
	$(clean)
	#ansible-playbook container-environment/deploy_container_env.yml $(ANSIBLE_ARGS)
	ansible-playbook -i containers/1router_1brouker_1client/inventory.yaml containers/1router_1brouker_1client/main.yaml

# precheck_container_env:
#	 ansible-playbook container-environment/precheck_container_env.yml $(ANSIBLE_ARGS)

#test:
#	$(clean)
#	ROUTER1=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' router1)
#  	BROKER1=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' broker1)

clean:
	$(clean)
