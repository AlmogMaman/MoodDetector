#Docker file for mood detector app
#Pay attention to use volume to the mood detector host directory
#Pay attention to use environment variables
FROM alpine:3.14
# Set default values for multiple environment variables
ENV MYSQL_CO_IP="mysql_co" \ #The name of the mysql container that running.
    MYSQL_USER="root" \
    MYSQL_PASSWORD="Almog" \
    MYSQL_INNER_PORT="3306" \
    MYSQL_DATABASE="mood_detector_db"
RUN apk add --no-cache python3 py3-pip && apk add --no-cache mariadb-connector-c-dev gcc musl-dev python3-dev
RUN pip install mysqlclient
WORKDIR /app
CMD ["python3","/app/main.py"]