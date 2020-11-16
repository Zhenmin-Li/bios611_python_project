FROM rocker/verse
MAINTAINER Zhenmin Li <zhenmin@live.unc.edu>
ARG linux_user_pwd
RUN echo Hello World
RUN apt update -y && apt install -y python3-pip
RUN pip3 install numpy pandas tweepy re matplotlib textblob datetime
RUN apt update && apt-get install -y texlive*
RUN  sudo apt install texlive-latex-extra