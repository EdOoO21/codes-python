FROM python:3.12

RUN [ "pip", "install", "pytest" ]

COPY [ "test_public.py", "test_public.py" ]
COPY [ "cpython.py", "cpython.py" ]

ENTRYPOINT [ "pytest", "-vv", "test_public.py" ]
