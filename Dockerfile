FROM alpine:3.18.2
RUN apk update
RUN apk add py-pip
RUN apk add --no-cache python3-dev 
RUN pip install --upgrade pip
ENV CONFIGURATION_SETUP=config.ProductionConfig
WORKDIR /gptxe
COPY . /gptxe
RUN pip --no-cache-dir install -r requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
