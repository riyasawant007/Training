import logging
import os

# Ensure we write logs to a known location
log_file = os.path.abspath("app.log")

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,  # Capture all logs (DEBUG and above)
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True  # Ensure previous configurations don’t interfere
)

# Log messages
logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

print(f"Logs written to: {log_file}")  # Confirm log file location
