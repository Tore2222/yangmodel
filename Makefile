# Variables
DOCKER_IMAGE := xsrt-yang2cli-builder:0.1
DOCKER_CONT := xsrt-yang2cli-builder-$(SUDO_USER)
DOCKER_RUN_CMD := docker run --name=$(DOCKER_CONT) --network=host -v $(PWD):/root/yang2cli \
	-it $(DOCKER_IMAGE)  bash -c ./build.sh
BUILD_SCRIPT := build.sh
#DESTDIR := $(SRT100G_BUILD_DIR)/packages/Output

# Define the default target
.PHONY: all
all: imish-ncc-tools

# Target to build environment
.PHONY: build_env
force_build_env:
	docker build -t $(DOCKER_IMAGE) .;
build_env:
	@echo "Checking for Docker image $(DOCKER_IMAGE)..."
	@if ! docker images -q $(DOCKER_IMAGE) > /dev/null 2>&1; then \
		echo "Docker image $(DOCKER_IMAGE) not found. Building it..."; \
		docker build -t $(DOCKER_IMAGE) .; \
	fi

# Target to run imish-ncc-tools
.PHONY: imish-ncc-tools
imish-ncc-tools: build_env
	$(DOCKER_RUN_CMD)
	docker rm -f $(DOCKER_CONT)

# Target to install
.PHONY: install
install:
	@echo "Installing imish-ncc* to $(DESTDIR)..."
	cp ./dist/* $(DESTDIR)/usr/bin/.
	cp ./vht/yang/yang-library.json $(DESTDIR)/etc/.
	cp -r ./vht/yang/modules $(DESTDIR)/usr/share/yuma/modules/vht

# Target to clean up
.PHONY: clean
clean:
	@echo "Cleaning up..."
	rm -rf vht/common
	rm -rf output
	rm -rf build
	rm -rf dist
	rm -f *.spec
