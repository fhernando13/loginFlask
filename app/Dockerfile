FROM python:3.7-alpine
RUN apk update && apk add --no-cache python3-dev \
                        gcc \
                        libc-dev \
                        libpq-dev\                    
    && pip3 install --upgrade pip 

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]