# Basic go commands
GOCMD=go
GOBUILD=$(GOCMD) build
GOCLEAN=$(GOCMD) clean
GOTEST=$(GOCMD) test
GOGET=$(GOCMD) get

# Binary names
BINARY_NAME=NeoAsist
BINARY_UNIX=$(BINARY_NAME)_unix
BINARY_WIN=$(BINARY_NAME)_win

nix=linux
win=windows
x64=amd64
x86=386
BUILDPATH=build

SOURCEDIR=.

all: run

build_link:
	ln -s $(shell pwd)/$(BUILDPATH)/$(BINARY_NAME) bin/$(BINARY_NAME)
	ln -s $(shell pwd)/$(BUILDPATH)/$(BINARY_NAME).exe bin/$(BINARY_NAME).exe
	ln -s $(shell pwd) $(GOPATH)/src/NeoAsist

build_linux:
	env GOOS=$(nix) GOARCH=$(x64) $(GOBUILD) -o $(BUILDPATH)/$(BINARY_NAME) $(SOURCEDIR)/htb/*.go 

build_windows:
	env GOOS=$(win) GOARCH=$(x64) $(GOBUILD) -o $(BUILDPATH)/$(BINARY_NAME).exe $(SOURCEDIR)/htb/*.go

tests:
run: build_linux build_windows
	./$(BUILDPATH)/$(BINARY_NAME)

deps:
	$(GOGET) github.com/fatih/color
	$(GOGET) github.com/oonray/godbg
	$(GOGET) https://github.com/go-yaml/yaml

dirs:
	mkdir -p build
	mkdir -p bin
	mkdir -p tests
