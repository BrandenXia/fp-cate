.PHONY: all build clean

all: build publish

build: clean
	uv build

publish: build
	uv publish

clean:
	rm -rf dist
