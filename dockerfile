FROM python:3.8.10-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirement.txt

CMD [ "uvicorn","Source:app","--host","0.0.0.0","--port","80" ]