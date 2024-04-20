FROM python

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY python.py .
COPY random_paragraphs.txt .

CMD ["python", "python.py"]