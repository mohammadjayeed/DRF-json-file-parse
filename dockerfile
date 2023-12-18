FROM python:3.9
ENV PYTHONBUFFERED=1
WORKDIR /code
COPY . .
RUN pip3 install -r requirements.txt
CMD 
EXPOSE 8000