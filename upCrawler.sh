#!/bin/bash

docker build -t crawl-tesouro-direto:latest .

docker run --rm -it \
-v $(pwd)/code:/code --name crawlTesouroDireto crawl-tesouro-direto bash