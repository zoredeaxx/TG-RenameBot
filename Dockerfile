FROM debian:latest

#RUN apt update && apt upgrade -y
#RUN apt install git python3-pip ffmpeg -y

RUN mkdir /app
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y ffmpeg
RUN pip3 install --upgrade pip
RUN pip3 install -U -r requirements.txt
ENV PORT = 8080 
EXPOSE 8080 
CMD python3 bot.py
