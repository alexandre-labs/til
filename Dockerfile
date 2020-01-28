FROM python:3.8.1

# Application directory
WORKDIR /app
COPY . /app

# Installing deps
RUN make install

CMD ["til"]
