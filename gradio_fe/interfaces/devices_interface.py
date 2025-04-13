import gradio as gr
from services.gradio_service import formatted_device_states


output_display = gr.HTML(label="Current Device States")


device_interface = gr.Interface(
    fn=formatted_device_states,
    inputs=None,
    outputs=output_display,
    title="Smart Home Devices Manager",
    description="Fetch the current state of your smart home devices."
)
