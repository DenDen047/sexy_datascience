#!/bin/bash

DIR=$(dirname $1)   # 親ディレクトリ名を取得
FILE=$(basename $1)
DATA_DIR=/data2/naoya/sexy_datascience
CMD="python ${FILE}"

docker run -it --rm \
    -v ${PWD}:/workdir \
    -v ${DATA_DIR}:/data \
    -w /workdir/${DIR} \
    -p 8888:8888 \
    denden047/datascience \
    /bin/bash -c "${CMD}"
