FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install flask
RUN python setup_db.py
CMD ["python", "app.py"]

