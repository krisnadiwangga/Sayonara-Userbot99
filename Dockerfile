# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# GLEDEK-USERBOT
# gledek

RUN git clone -b GLEDEK-USERBOT https://github.com/gledek/GLEDEK-USERBOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/gledek/GLEDEK-USERBOT/GLEDEK-USERBOT/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
