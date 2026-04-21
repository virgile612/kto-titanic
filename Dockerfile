FROM debian:bullseye

RUN apt update
RUN apt install python -y

RUN mkdir /opt/app-root
WORKDIR /opt/app-root

RUN touch my_script.py

RUN echo "import platform\nprint(\"Coucou ! On tourne sur \" + platform.platform())" > myscript.py