FROM python:3.8.1


# Application directory
WORKDIR /app
COPY . /app

SHELL ["/bin/bash", "-c"]

# Installing deps
RUN make venv
RUN make install

CMD ["til"]
