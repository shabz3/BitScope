
FROM python:3.12-slim


# user of "app" for security
RUN groupadd -r app && useradd -r -g app app


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY . /code/

# we use the app user instead of "root" for security reasons
USER app


EXPOSE 8000


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]