FROM continuumio/anaconda

# jupyter-notebook
RUN /opt/conda/bin/conda install jupyter -y --quiet
RUN mkdir /opt/notebooks

# work dir
RUN mkdir /workdir
WORKDIR /workdir

CMD [
    "/opt/conda/bin/jupyter notebook",
    "--notebook-dir=/opt/notebooks",
    " --ip='*'",
    "--port=8888",
    "--no-browser"
]
