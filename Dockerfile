FROM nikolaik/python-nodejs:python3.12-nodejs22

RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg aria2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app/

COPY requirements.txt .
RUN python -m pip install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir --upgrade --requirement requirements.txt

COPY . .

CMD ["bash", "start"]
