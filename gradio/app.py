# note that to see you changes you must restart the server. that's how gradio works
import gradio as gr


def greet(name, is_morning, temperature):
    salutation = "Good morning" if is_morning else "Hello"
    greeting = (
        f"{salutation}, {name}! The temperature is {temperature} degrees Fahrenheit."
    )
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)


demo = gr.Interface(
    fn=greet,
    inputs=[
        gr.Textbox(label="Name"),
        gr.Checkbox(label="Is it morning?"),
        gr.Slider(0, 100, label="Temperature"),
    ],
    outputs=[
        gr.Textbox(label="Greeting"),
        gr.Number(label="Rounded Temp (°C)"),
    ],
)

demo.launch()
