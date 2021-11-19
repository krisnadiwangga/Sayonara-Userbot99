# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# VEGETA-USERBOT
# HACKER
# KONTOL

RUN git clone -b VEGETA-USERBOT https://github.com/Randi356/VEGETA-USERBOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Randi356/VEGETA-USERBOT/VEGETA-USERBOT/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
