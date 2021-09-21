FROM python:3

WORKDIR /usr

COPY ./requirements/dev.txt ./

RUN python3 -m ensurepip
RUN pip install -r dev.txt
# RUN \
#  apk add --no-cache postgresql-libs && \
#  apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
#  pip install -r dev.txt --no-cache-dir && \
#  apk --purge del .build-deps

ENV PYTHONPATH "${PYTHONPATH}:/usr/app"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]