FROM ubuntu:20.04

# Update packages
RUN apt-get update

# Install Python 3.7 and pip
RUN apt-get install -y python3.7 python3-pip

# Install dependencies required by Playwright
RUN apt-get install -y libnss3-dev libgconf-2-4 libfontconfig1-dev libx11-dev libxkbfile-dev

# Install Playwright via pip
RUN python3.7 -m pip install playwright

# Install browser dependencies for Playwright
RUN python3.7 -m playwright install

# Set environment variables for Playwright
ENV PLAYWRIGHT_BROWSERS_PATH=/usr/local/share/playwright

# Set working directory
WORKDIR /app

# Copy project files to working directory
COPY . /app

# Set default command to run when container starts
CMD ["python3.7", "app.py"]
