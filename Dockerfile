FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY get_mac_company.py .
COPY test_get_mac_company.py .


ENTRYPOINT [ "python", "get_mac_company.py" ]
