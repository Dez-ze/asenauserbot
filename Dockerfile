FROM fusuf/asenauserbot:latest
RUN git clone https://github.com/Dez-ze/asenauserbot /root/asenauserbot
WORKDIR /root/AsenaUserBot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"] 
