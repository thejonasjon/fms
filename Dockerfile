FROM python:3.12-alpine3.18
LABEL maintainer="Jonas: Formplus"

ENV PYTHONUNBUFFERED 1

# Copy the requirements files
COPY ./requirements.txt /temp/requirements.txt
COPY ./requirements.dev.txt /temp/requirements.dev.txt
COPY ./app /app

# Set the working directory
WORKDIR /app
EXPOSE 8000

# Argument for dev mode
ARG DEV=true

# Install Python dependencies and MongoDB client, then delete temp files
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache mongodb-tools && \
    apk add --update --no-cache --virtual .temp-build-deps \
        build-base musl-dev && \
    /py/bin/pip install -r /temp/requirements.txt && \
    if [ "$DEV" = "true" ]; \
        then /py/bin/pip install -r /temp/requirements.dev.txt ; \
    fi && \
    rm -rf /temp && \
    apk del .temp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /app && chown django-user:django-user /app

# Set environment variable for Python
ENV PATH="/py/bin:$PATH"

# Switch to the non-root user
USER django-user

# Default command to run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]