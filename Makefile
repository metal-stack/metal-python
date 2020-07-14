METAL_API_VERSION := $(or ${METAL_API_VERSION},$(shell python3 -c 'from metal_python.version import VERSION; print(VERSION)'))
SWAGGER_VERSION := $(or ${SWAGGER_VERSION},2.4.14)

.PHONY: generate-client
generate-client:
	docker run --rm \
	  -v ${PWD}:/workdir \
	  -u $$(id -u):$$(id -g) \
	  --entrypoint "java" \
	  swaggerapi/swagger-codegen-cli:$(SWAGGER_VERSION) \
	    -DsupportingFiles=configuration.py,rest.py,api_client.py \
	    -jar /opt/swagger-codegen-cli/swagger-codegen-cli.jar generate \
        -i https://raw.githubusercontent.com/metal-stack/metal-api/$(METAL_API_VERSION)/spec/metal-api.json \
        -l python \
        -o /workdir \
        -c /workdir/config.json -Dmodels -Dapis -DpackageVersion=$(METAL_API_VERSION)

METAL_API_SPEC_LOCAL_PATH := "../metal-api/spec/metal-api.json"
.PHONY: generate-client-local
generate-client-local:
	cp $(METAL_API_SPEC_LOCAL_PATH) .
	docker run --rm \
	  -v ${PWD}:/workdir \
	  -u $$(id -u):$$(id -g) \
	  --entrypoint "java" \
	  swaggerapi/swagger-codegen-cli:$(SWAGGER_VERSION) \
	    -DsupportingFiles=configuration.py,rest.py,api_client.py \
	    -jar /opt/swagger-codegen-cli/swagger-codegen-cli.jar generate \
        -i /workdir/metal-api.json \
        -l python \
        -o /workdir \
        -c /workdir/config.json -Dmodels -Dapis -DpackageVersion=$(METAL_API_VERSION)
