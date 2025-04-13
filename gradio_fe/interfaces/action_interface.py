import gradio as gr
from services.gradio_service import perform_action_on_device


text_prompt = gr.Textbox(label="Describe the desired state of devices", placeholder="e.g., Turn on the light, set fan to high, and thermostat to 25")
output_display = gr.HTML(label="Output from our LML integrated system")


action_interface = gr.Interface(
    fn=perform_action_on_device,
    inputs=text_prompt,
    outputs=output_display,
    title="Smart Home Devices Manager",
    description="Control your smart home devices by describing the desired state in plain text."
)
