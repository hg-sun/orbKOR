# coding=utf-8
FROM continuumio/miniconda3

# Default Settings
ENV LANG=ko_KR.UTF-8
ENV LANGUAGE ko_KR.UTF-8
ENV HOME=/root
WORKDIR /root/workspace
COPY ./ /root/workspace
RUN apt-get update
RUN apt-get install -y --allow-unauthenticated wget build-essential autotools-dev automake procps vim
RUN conda update conda -y
RUN conda create -n orbkor python=3.7.4
ENV CONDA_SHLVL 1
ENV CONDA_PROMP_MODIFIER (orbkor)
ENV CONDA_EXE /opt/conda/condabin/conda
ENV PATH /opt/conda/envs/orbkor/bin:/opt/conda/condabin:/opt/conda/envs/orbkor/bin:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV CONDA_PREFIX /opt/conda/envs/orbkor
ENV CONDA_PYTHON_EXE /opt/conda/envs/orbkor/bin/python
ENV CONDA_DEFAULT_ENV orbkor
RUN pip install -r /root/workspace/requirements.txt

# Expose Port
ARG PORT
EXPOSE $PORT
CMD ["/opt/conda/envs/orbkor/bin/python", "app.py"]

