FROM python:3.10

WORKDIR /src

COPY . .

ADD requirements.txt /src

RUN pip install -r requirements.txt

# Expose 5001 as unused ports for testing purposes

EXPOSE 8000 8080

CMD ["pytest", "-m aura25 -s -v --capture=sys --html=Reports/aura26TestReport.html --self-contained-html /src/TestCases/"]