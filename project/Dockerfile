FROM qasz/cubane:latest

# create app folder
RUN mkdir -p /app
WORKDIR /app
COPY . /app/

# install app python dependencies
RUN pip install -r /app/requirements.txt

# copy nginx config
RUN rm -rf /etc/nginx/conf.d/default.conf
#RUN cp -rf /app/nginx.conf /etc/nginx/conf.d/
COPY ./nginx.conf /etc/nginx/conf.d/

# make installer and deploy executable
RUN chmod 755 /app/deploy.sh
RUN chmod 755 /app/start.sh
RUN chmod 755 /app/start_prod.sh

CMD /bin/bash /app/start_prod.sh

EXPOSE 5000
EXPOSE 587
