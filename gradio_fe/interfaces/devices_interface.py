import gradio as gr
from services.gradio_service import gradio_process_prompt


text_prompt = gr.Textbox(label="Describe the desired state of devices", placeholder="e.g., Turn on the light, set fan to high, and thermostat to 25")
output_display = gr.HTML(label="Current Device States")


device_interface = gr.Interface(
    fn=gradio_process_prompt,
    inputs=text_prompt,
    outputs=output_display,
    title="Smart Home Devices Manager",
    description="Control your smart home devices by describing the desired state in plain text."
)
