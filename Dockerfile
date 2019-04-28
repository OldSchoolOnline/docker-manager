FROM python

EXPOSE 5000
WORKDIR /root/docker-manager
COPY . .

RUN pip install -r requirements.txt && \
  echo "FLASK_APP=docker-manager.py" > .flaskenv

CMD python -m flask run --host=0.0.0.0
