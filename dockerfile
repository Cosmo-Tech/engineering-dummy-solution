FROM python:3.11.11-slim-bullseye

WORKDIR Solution

COPY GenericSolution/ .
COPY GenericConnector/ .

# Fix line endings in shell scripts
RUN sed -i 's/\r$//' ./run_script.sh

ENTRYPOINT ["./run_script.sh"]