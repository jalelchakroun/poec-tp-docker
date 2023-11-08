FROM python:3
WORKDIR /app
COPY requirement.txt ./
RUN pip install --no-cache-dir -r requirement.txt
COPY . .
CMD ["python" , "./src/main.py", "[100]","[20]"]