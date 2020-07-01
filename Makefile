METAL_API_VERSION := $(or ${METAL_API_VERSION},v0.7.8)
SWAGGER_VERSION := $(or ${SWAGGER_VERSION},2.4.14)

.PHONY: generate-client
generate-client:
	echo "VERSION = '$(subst v,,$(METAL_API_VERSION))'" > metal_python/version.py
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
        -c /workdir/config.json -Dmodels -Dapis
