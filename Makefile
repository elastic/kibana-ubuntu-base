REGISTRY=container-registry.elastic.co
IMAGE=kibana-ubuntu-base
IMAGE_TAG=$(REGISTRY)/kibana/$(IMAGE):latest

export IMAGE

test: build
	py.test --verbose

push: build test
	docker tag $(IMAGE) $(IMAGE_TAG)
	docker push $(IMAGE_TAG)

build: FORCE
	docker-compose build --pull $(IMAGE)

clean:
	find . -name '*.pyc' -delete
	rm -rf tests/__pycache__ tests/.cache

FORCE:
