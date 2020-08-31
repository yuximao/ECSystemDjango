FROM python:3.7
COPY .  /home
WORKDIR /home
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python3","/home/manage.py","runserver"]