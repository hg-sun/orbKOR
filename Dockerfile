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
RUN conda create -n orb python=3.7.3
ENV CONDA_SHLVL 1
ENV CONDA_PROMP_MODIFIER (orb)
ENV CONDA_EXE /opt/conda/condabin/conda
ENV PATH /opt/conda/envs/orb/bin:/opt/conda/condabin:/opt/conda/envs/orb/bin:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV CONDA_PREFIX /opt/conda/envs/orb
ENV CONDA_PYTHON_EXE /opt/conda/envs/orb/bin/python
ENV CONDA_DEFAULT_ENV orb
VOLUME ["/root/workspace/var/log", "/root/workspace/var/pickle"]
RUN pip install -r /root/workspace/requirements.txt
RUN python -m spacy download en_core_web_sm

# Expose Port
ARG PORT
EXPOSE $PORT
CMD ["/opt/conda/envs/orb/bin/python", "app.py"]


