import logging

# Create a custom logger
logger = logging.getLogger("MyLogger")
logger.setLevel(logging.DEBUG)  # Set logging level

# Create a file handler
handler = logging.FileHandler("custom.log")
handler.setLevel(logging.DEBUG)  # Ensure handler logs all levels

# Define log format
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(handler)

# Log messages
logger.info("This is a custom info log")
logger.error("This is a custom error log")

print("Logging complete. Check custom.log")  # To confirm script execution
