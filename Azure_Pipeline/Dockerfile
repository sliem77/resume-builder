# syntax=docker/dockerfile:1

# Choose the Python version and OS image for your base image
ARG PYTHON_VERSION=3.9.18
FROM amd64/python:${PYTHON_VERSION}-slim-bookworm as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Create a non-privileged user that the app will run under.
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Download dependencies as a separate step to take advantage of Docker's caching.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

# Installing TeX Live
RUN apt-get update && \
    apt-get install -y texlive && \
    rm -rf /var/lib/apt/lists/*

# Install necessary LaTeX packages
RUN apt-get update && \
    apt-get install -y \
    texlive \
    texlive-lang-english \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    && rm -rf /var/lib/apt/lists/*

# Copy the local Streamlit app and Config file into the container
COPY . /app

# Install additional dependencies for Streamlit
RUN apt-get update && \
    apt-get install -y \
        build-essential \
        curl \
        software-properties-common \
        poppler-utils

# Expose the port
EXPOSE 8501

# Checking container is working
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run the application
# ENTRYPOINT ["streamlit", "run", "Azure_v1.py", "--server.port=8501", "--server.address=0.0.0.0"]
CMD streamlit run Azure_v1.py