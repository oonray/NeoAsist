# Basic go commands
GOCMD=go
GOBUILD=$(GOCMD) build
GOCLEAN=$(GOCMD) clean
GOTEST=$(GOCMD) test
GOGET=$(GOCMD) get

# Binary names
BINARY_NAME=HTBManager
BINARY_UNIX=$(BINARY_NAME)_unix
BINARY_WIN=$(BINARY_NAME)_win
nix=linux
win=windows
x64=amd64
x86=386
BUILDPATH="build"


build:

tests:
run: build
	./$(BUILDPATH)/$(BINARY_NAME)

deps:
	go get github.com/fatih/color

dirs:
	mkdir -p build
	mkdir -p bin
	mkdir -p tests
