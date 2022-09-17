FROM python:3.9
COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . .
WORKDIR /

# Run
CMD [ "flask" , "run"]