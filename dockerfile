#RUN apt update -y

#FROM python:3.10-alpine

# Install Chrome WebDriver


# Install Google Chrome

# #WORKDIR /src

# #COPY . .

# #ADD requirements.txt /src

##RUN pip install --upgrade pip

##RUN pip install -r requirements.txt


# Expose 5001 as unused ports for testing purposes

# EXPOSE 8000 8080
# ENV GROUP-["pytest","aura25"]
# CMD ["pytest", "-m aura25 -s -v --capture=sys --html=Reports/aura26TestReport.html --self-contained-html /src/TestCases/"]

##CMD [ "pytest", "-m aura25", "-vv", "-s", "--capture=sys", "--html=Reports/aura26TestReport.html", "--self-contained-html" , "/src/TestCases/" ]

# FROM ubuntu

# RUN apt update -y

WORKDIR app

COPY . /app/

ADD requirements.txt /app

RUN apt install -y wget unzip

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get install -y tzdata

CHROME_VERSION=”google-chrome-stable”
CHROME_MAJOR_VERSION=$(google-chrome --version | sed -E "s/.* ([0–9]+)(\.[0–9]+){3}.*/\1/")
#.    Please note that the steps mentioned below now can be 
#.    replaced with Web driver manager which do the the download
#.    and setup of driver
CHROME_DRIVER_VERSION=$(wget — no-verbose -O — “https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_MAJOR_VERSION}");
echo “Using chromedriver version: “$CHROME_DRIVER_VERSION
wget — no-verbose -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip
rm -rf /opt/selenium/chromedriver
unzip /tmp/chromedriver_linux64.zip -d /opt/selenium
rm /tmp/chromedriver_linux64.zip
mv /opt/selenium/chromedriver /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION
chmod 755 /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION
ln -fs /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION /usr/bin/chromedriver

CMD [ "pytest", "-m aura25", "-v", "-s", "--capture=sys", "--html=Reports/aura26TestReport.html", "--self-contained-html" , "/app/TestCases/" ]