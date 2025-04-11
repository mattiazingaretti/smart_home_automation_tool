from interfaces.devices_interface import device_interface
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info("Launching Gradio interface...")
    device_interface.launch(server_name="127.0.0.1", server_port=7860, share=False)
    logger.info("Gradio interface is running")