FROM python:3.6

# init
WORKDIR /root
RUN apt-get update
RUN pip install -U pip

# jupyter notebook
RUN pip install jupyter
ENV PATH $PATH:/env/bin

# nbextensions_configurator
RUN pip install jupyter_nbextensions_configurator
RUN jupyter nbextensions_configurator enable --user

# jupyter therme
RUN pip install lesscpy
RUN pip install jupyterthemes

# nbextensions
WORKDIR /notebooks
RUN pip install https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tarball/master
ENV NBEXTENSIONS_HOME /root/.local/share/jupyter/nbextensions
RUN jupyter contrib nbextension install --user
RUN jupyter nbextension enable /notebooks

# pip
RUN pip install numpy
RUN pip install scipy
RUN pip install pandas
RUN pip install matplotlib
RUN pip install networkx

WORKDIR /root