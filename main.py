"""Исполняющий файл проекта."""
import logging


logging.basicConfig(
    filename="testovoe.log",
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
