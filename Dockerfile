# Using Python Slim-Buster
FROM hackinguserbot/rendyprojects:buster
# credit from @FFmpegNotInstalled
# Sayonara-Userbot
# Sayonara

RUN git clone -b Sayonara-Userbot https://github.com/krisnadiwangga/Sayonara-Userbot99 /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/krisnadiwangga/Sayonara-Userbot99/Sayonara-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
