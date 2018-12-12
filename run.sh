#!/bin/bash

NOTE_DIR=${PWD}/notebooks
DATA_DIR=/data2/naoya/sexy_datascience

docker run -it --rm \
    -v ${NOTE_DIR}:/notebooks \
    -v ${DATA_DIR}:/data \
    -v ${PWD}/configs/.jupyter:/root/.jupyter:ro \
    -p 8888:8888 \
    denden047/datascience:jupyter \
    /bin/bash -c "jupyter notebook --port=8888 --allow-root"