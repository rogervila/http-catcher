FROM python:3.9-alpine

ENV FLASK_APP=web.py

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]

EXPOSE 5000
