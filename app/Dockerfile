FROM python:3.10.4-alpine3.15
RUN apk update && apk add --no-cache python3-dev \
                        gcc \
                        libc-dev \
                        libffi-dev\
                        libpq-dev\   
                        musl-dev\
                        postgresql-dev\                
    && pip3 install --upgrade pip 

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run"]