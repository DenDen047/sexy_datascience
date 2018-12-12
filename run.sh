#!/bin/bash

# DIR=$(dirname $1)   # 親ディレクトリ名を取得
# FILE=$(basename $1)
# CMD="python ${FILE}"

NOTE_DIR=${PWD}/notebooks
DATA_DIR=/data2/naoya/sexy_datascience

docker run -it --rm \
    -v ${NOTE_DIR}:/notebooks \
    -v ${DATA_DIR}:/data \
    -v ${PWD}/configs/.jupyter:/root/.jupyter \
    -w /workdir/${DIR} \
    -p 8888:8888 \
    denden047/datascience:jupyter