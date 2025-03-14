FROM python:3.11.11-slim-bullseye

WORKDIR Solution

COPY GenericSolution/ .
COPY GenericConnector/ .

ENTRYPOINT ["./run_script.sh"]