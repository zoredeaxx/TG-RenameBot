FROM python:3.10-slim-buster

RUN mkdir /app
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y ffmpeg
RUN pip3 install -r requirements.txt
ENV PORT = 8080 
EXPOSE 8080 
CMD python3 bot.py
