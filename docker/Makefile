.PHONY: build run

REPO  ?= denden047/datascience:jupyter

build:
	docker build -t $(REPO) .
	docker push $(REPO)
