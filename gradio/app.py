import gradio as gr


def greet(name):
    return f"Hello {name}!"


# text, image ,audio, video, dataframe, file, json, html, markdown, component
demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="Enter your name"),
    outputs=gr.Textbox(label="Greeting"),
)

demo.launch()
