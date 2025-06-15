# 🐳 Base image
FROM python:3.11-slim

# 📁 Set working directory
WORKDIR /app

# ⚙️ Install OS dependencies for Selenium
RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg \
    chromium chromium-driver \
    && apt-get clean

# ✅ Set Chrome driver environment variables
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# 📦 Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 📁 Copy full app
COPY . .

# 🔥 Expose port
EXPOSE 10000

# 🚀 Run Flask app with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]
