import logging
import sys

from mcp_vision.server import mcp

logger = logging.getLogger(__name__)


def main():
    try:
        mcp.run(transport="http", host="0.0.0.0", port=8000)
    except Exception as e:
        logger.error(f"Error starting server: {e}")
        sys.exit(1)


__all__ = ["main"]
