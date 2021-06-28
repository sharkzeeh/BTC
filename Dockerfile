FROM python:3.6
WORKDIR /app
COPY . .
RUN pip3 install --upgrade pip
RUN make install
    # python3 btc/manage.py migrate
EXPOSE 8001
