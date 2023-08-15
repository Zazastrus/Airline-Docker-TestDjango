FROM python:3
COPY . C:\Users\alsch\Desktop\Airline
WORKDIR C:\Users\alsch\Desktop\Airline>
RUN pip install -r requirements.txt
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]