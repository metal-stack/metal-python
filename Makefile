METAL_API_VERSION := $(or ${METAL_API_VERSION},$(shell python3 -c 'from version import VERSION; print(VERSION)'))
SWAGGER_VERSION := $(or ${SWAGGER_VERSION},2.4.14)

.PHONY: generate-client
generate-client:
	curl -LO https://raw.githubusercontent.com/metal-stack/metal-api/$(METAL_API_VERSION)/spec/metal-api.json
	$(MAKE) generate-client-local

.PHONY: generate-client-local
generate-client-local:
	yq e -ij ".info.version=\"${METAL_API_VERSION}\"" metal-api.json
	yq e '.info.version' metal-api.json
	rm -rf docs metal_python/api metal_python/models test
	docker run --rm \
	  -v ${PWD}:/workdir \
	  -u $$(id -u):$$(id -g) \
	  --entrypoint "java" \
	  swaggerapi/swagger-codegen-cli:$(SWAGGER_VERSION) \
	    -DsupportingFiles=configuration.py,rest.py,api_client.py,__init__.py \
	    -jar /opt/swagger-codegen-cli/swagger-codegen-cli.jar generate \
        -i /workdir/metal-api.json \
        -l python \
        -o /workdir \
        -c /workdir/config.json -Dmodels -Dapis -DpackageVersion=$(METAL_API_VERSION)
