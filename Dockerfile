FROM python:3.6
WORKDIR /app
COPY . .
RUN make install
EXPOSE 8001
