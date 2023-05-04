FROM python:3.9-slim

ENV GOOGLE_USERNAME=default_username
ENV GOOGLE_PASSWORD=default_password
ENV DATE_TO_CHANGE=default_date

# Install dependencies
RUN apt-get update && apt-get install -y libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxfixes3 libxi6 libxrandr2 libasound2 libatk1.0-0 libatk-bridge2.0-0 libgtk-3-0 libnss3 libxss1 libxtst6

# Copy Autobot code
WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip3 install -r requirements.txt
RUN python3 -m playwright install
RUN python3 -m playwright install-deps 



# Set the entrypoint
ENTRYPOINT ["robot", "-d", "results","cases/case1_signin.robot"]
