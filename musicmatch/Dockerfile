FROM alpine
RUN apk update
RUN apk add python3
RUN apk add py3-pip
RUN pip3 install requests
RUN mkdir /output
WORKDIR /app
COPY docker_api_query.py /app
CMD ["python3", "./docker_api_query.py"]
