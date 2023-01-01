FROM python:3.7-alpine
RUN apk update && apk add --no-cache python3-dev \
                        gcc \
                        libc-dev \
    && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["flask", "run"]