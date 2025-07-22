import numpy as np
import gradio as gr


def sepia(input_img):
    input_img = input_img.astype(np.float32)

    sepia_filter = np.array(
        [[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]]
    )

    sepia_img = input_img @ sepia_filter.T
    sepia_img = np.clip(sepia_img, 0, 255).astype(np.uint8)

    return sepia_img


demo = gr.Interface(
    fn=sepia,
    inputs=gr.Image(
        type="numpy", image_mode="RGB"
    ),  # Removed `shape`, added `type` and `image_mode`
    outputs=gr.Image(type="numpy"),
)

demo.launch()
