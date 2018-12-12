FROM continuumio/anaconda

# jupyter-notebook
RUN /opt/conda/bin/conda install jupyter -y --quiet

# jupyter therme
RUN pip install lesscpy
RUN pip install jupyterthemes

# nbextensions_configurator
RUN pip install jupyter_nbextensions_configurator
RUN jupyter nbextensions_configurator enable --user

# nbextensions
WORKDIR /notebooks
RUN pip install https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tarball/master
ENV NBEXTENSIONS_HOME /root/.local/share/jupyter/nbextensions
RUN jupyter contrib nbextension install --user
RUN jupyter nbextension enable /notebooks

# others
RUN /opt/conda/bin/conda install networkx -y --quiet

# Open Ports for Jupyter
EXPOSE 8888

CMD /bin/bash -c "/opt/conda/bin/jupyter notebook \
    --notebook-dir=/notebooks \
     --ip='*' \
    --port=8888 \
    --no-browser \
    --allow-root"
