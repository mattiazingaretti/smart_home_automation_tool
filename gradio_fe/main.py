from interfaces.devices_interface import device_interface
from interfaces.action_interface import action_interface
import logging
from fastapi import FastAPI
import uvicorn
import gradio as gr

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

gradio_app = FastAPI(title="Smart home device manager")

with gr.Blocks(title="Smart home device manager") as combined_interface:
    gr.Markdown("# Smart home device manager")
    
    with gr.Tab("Fetch devices state"):
        device_interface.render()
    with gr.Tab("Perform action on devices"):
        action_interface.render()
    
gradio_app = gr.mount_gradio_app(gradio_app, combined_interface, path="/gradio")


@gradio_app.get("/")
def root():
    return {
        "message": "Welcome to Smart Home device manager API!",
        "endpoints": {
            "/": "Welcome message",
            "/devices": "Fetch Devices state",
            "/gradio": "Gradio interface"
        }
    }

if __name__ == '__main__':
    uvicorn.run(gradio_app, host='127.0.0.1', port=7860, log_level="info")