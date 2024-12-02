import gradio as gr
import flux


def process_txt2img(style_id, prompt, ratio, uuid_value, token):
    return flux.process_txt2img_data(prompt,ratio, style_id,
                                     uuid_value, token)


def process_img2img(style_id, ratio, uuid_value, token,
                    image):
    return flux.process_img2img_data(ratio, image, style_id, uuid_value,
                                     token)


def process_faceswap(uuid_value, token, image, style):
    return flux.process_faceswap_data(uuid_value, token, image, style)


def process_outpaint(uuid_value, token, image, canvas):
    return flux.process_outpaint_data(uuid_value, token, image, canvas)


def process_enhance(uuid_value, token, image):
    return flux.process_enhance_data(uuid_value, token, image)


def process_prompt(uuid_value, token, image):
    return flux.process_prompt_data(uuid_value, token, image)


def process_doodle(ratio, image, style_id, uuid_value, token,
                   prompt):
    return flux.process_doodle_data(ratio, image, style_id, uuid_value, token,
                   prompt)


def process_inpaint(style_id, ratio, uuid_value, token,
                    prompt, mask, image):
    return flux.process_inpaint_data(ratio, image,mask,  uuid_value,
                                     token, prompt)


def create_interface():
    with gr.Blocks() as demo:
        with gr.Tab("Text to Image"):
            # Inputs for Text-to-Image
            text_prompt = gr.Textbox(label="Prompt")
            text_ratio = gr.Textbox(label="Ratio")
            text_style = gr.Textbox(label="Style ID")
            text_uuid = gr.Textbox(label="UUID ID")  # Default UUID
            text_token = gr.Textbox(
                label="Token ID")  # Password type for token
            text_output = gr.Textbox()  # Output for text-to-image response

            # Bind the text-to-image function to the interface
            text_submit_button = gr.Button("Generate Image")
            text_submit_button.click(process_txt2img,
                                     inputs=[
                                         text_style, text_prompt, text_ratio,
                                         text_uuid, text_token
                                     ],
                                     outputs=text_output)

        with gr.Tab("Image to Image"):
            # Inputs for Image-to-Image
            img_url = gr.Textbox(label="URL")
            img_ratio = gr.Textbox(label="Ratio")
            img_style = gr.Textbox(label="Style ID")
            img_uuid = gr.Textbox(label="UUID ID")  # Default UUID
            img_token = gr.Textbox(label="Token ID")  # Password type for token

            img_output = gr.Textbox()  # Output for image-to-image response

            # Bind the image-to-image function to the interface
            img_submit_button = gr.Button("Generate Image")
            img_submit_button.click(
                process_img2img,
                inputs=[img_style, img_ratio, img_uuid, img_token, img_url],
                outputs=img_output)

        with gr.Tab("Line to Image"):
            # Inputs for Image-to-Image
            line_url = gr.Textbox(label="URL")
            line_ratio = gr.Textbox(label="Ratio")
            line_style = gr.Textbox(label="Style ID")
            line_uuid = gr.Textbox(label="UUID ID")  # Default UUID
            line_token = gr.Textbox(
                label="Token ID")  # Password type for token
            line_prompt = gr.Textbox(
                label="img_prompt ID")  # Password type for token
            line_output = gr.Textbox()  # Output for image-to-image response

            # Bind the image-to-image function to the interface
            line_submit_button = gr.Button("Generate Image")
            line_submit_button.click(process_doodle,
                                     inputs=[
                                         line_ratio,line_url, line_style, line_uuid,
                                         line_token, line_prompt, 
                                     ],
                                     outputs=line_output)

        with gr.Tab("Inpaint Image"):
            # Inputs for Inpaint-to-Image
            in_url = gr.Textbox(label="URL")
            in_mask = gr.Textbox(label="Mask URL")
            in_prompt = gr.Textbox(label="Prompt")
            in_ratio = gr.Textbox(label="Ratio")
            in_uuid = gr.Textbox(label="UUID ID")  # Default UUID
            in_token = gr.Textbox(label="Token ID")
            in_style = gr.Textbox(label="Style ID")  # Password type for token
            in_output = gr.Textbox()  # Output for image-to-image response

            # Bind the image-to-image function to the interface
            in_submit_button = gr.Button("Generate Image")
            in_submit_button.click(process_inpaint,
                                   inputs=[
                                       in_style, in_ratio, in_uuid, in_token,
                                       in_prompt, in_mask, in_url
                                   ],
                                   outputs=in_output)

        with gr.Tab("Get Enhance"):
            # Inputs for Get Upload URL
            en_url = gr.Textbox(label="URL")
            en_uuid = gr.Textbox(label="UUID ID")  # Default UUID
            en_token = gr.Textbox(label="Token ID")
            en_output = gr.Textbox()  # Output for the upload URL response

            # Bind the get_upload_url function to the interface
            en_submit_button = gr.Button("Get Upload URL")
            en_submit_button.click(process_enhance,
                                   inputs=[en_uuid, en_token, en_url],
                                   outputs=en_output)

        with gr.Tab("Get Prompt"):
            # Inputs for Get Upload URL
            gen_url = gr.Textbox(label="URL")
            gen_uuid = gr.Textbox(label="UUID ID")  # Default UUID
            gen_token = gr.Textbox(label="Token ID")
            gen_output = gr.Textbox()  # Output for the upload URL response

            # Bind the get_upload_url function to the interface
            gen_submit_button = gr.Button("Get Upload URL")
            gen_submit_button.click(process_prompt,
                                    inputs=[gen_uuid, gen_token, gen_url],
                                    outputs=gen_output)

        with gr.Tab("Get OutPaint"):
            # Inputs for Get Upload URL
            out_url = gr.Textbox(label="URL")
            out_canvas = gr.Textbox(label="Canvas")
            out_uuid = gr.Textbox(label="UUID ID")  # Default UUID
            out_token = gr.Textbox(label="Token ID")
            out_output = gr.Textbox()  # Output for the upload URL response

            # Bind the get_upload_url function to the interface
            out_submit_button = gr.Button("Get Upload URL")
            out_submit_button.click(
                process_outpaint,
                inputs=[out_uuid, out_token, out_url, out_canvas],
                outputs=out_output)

        with gr.Tab("Get Faceswap"):
            # Inputs for Get Upload URL
            fs_url = gr.Textbox(label="URL")
            fs_target = gr.Textbox(label="Target URL")
            fs_uuid = gr.Textbox(label="UUID ID")  # Default UUID
            fs_token = gr.Textbox(label="Token ID")
            fs_output = gr.Textbox()  # Output for the upload URL response

            # Bind the get_upload_url function to the interface
            fs_submit_button = gr.Button("Get Upload URL")
            fs_submit_button.click(
                process_faceswap,
                inputs=[fs_uuid, fs_token, fs_url, fs_target],
                outputs=fs_output)

        with gr.Tab("D Faceswap"):
            # Inputs for Get Upload URL
            dfs_url = gr.Textbox(label="URL")
            dfs_target = gr.Textbox(label="Target URL")
            dfs_uuid = gr.Textbox(label="UUID ID")  # Default UUID
            dfs_token = gr.Textbox(label="Token ID")
            dfs_output = gr.Textbox()  # Output for the upload URL response

            # Bind the get_upload_url function to the interface
            dfs_submit_button = gr.Button("Get Upload URL")
            dfs_submit_button.click(
                process_faceswap,
                inputs=[dfs_url, dfs_target, dfs_uuid, dfs_token],
                outputs=dfs_output)

    return demo


# Launch the Gradio interface
interface = create_interface()
interface.launch(server_name="0.0.0.0", server_port=7860)
