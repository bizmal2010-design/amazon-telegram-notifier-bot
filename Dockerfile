FROM apify/actor-python-playwright:3.11

USER root
RUN apt-get update && apt-get install -y python3-tk libtk8.6 && rm -rf /var/lib/apt/lists/*
USER apify

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m patchright install --with-deps

COPY . ./

CMD ["python3", "main.py"]
