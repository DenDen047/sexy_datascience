FROM python:3.6

# init
WORKDIR /root
RUN apt-get update
RUN pip install -U pip

# jupyter notebook
RUN pip install jupyter
ENV PATH $PATH:/env/bin

# pip
RUN pip install numpy
RUN pip install scipy
RUN pip install pandas
RUN pip install matplotlib
RUN pip install networkx

WORKDIR /root