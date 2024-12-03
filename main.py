from flask import Flask, request, jsonify
import sys
import flux
import os

import json
import logging

sys.stdout = open(os.devnull, 'w')
from gradio_client import Client
sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w')
app = Flask(__name__)
txt2img_client = Client("http://216.48.185.164:7860/")
img2img_client = Client("http://216.48.185.164:7860/") 
inpaint_client = Client("http://216.48.185.164:7860/") 
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__


@app.route('/ai/art/txt2img/', methods=['POST'])
def process_txt2img_data():
    # Get form data from the request
    is_translate = request.form.get('is_translate', '')
    is_first = request.form.get('is_first', '')
    style_id = request.form.get('style_id', '')
    prompt = request.form.get('prompt', '')
    ratio = request.form.get('ratio', '')
    uuid_value = request.form.get('Uid', '')
    token = request.form.get('Token', '')

    # You can print the received form data
    print("Received form data:")
    print(f"is_translate: {is_translate}, is_first: {is_first}, style_id: {style_id}, prompt: {prompt}, ratio: {ratio}")

    # Check for required parameters
    if not prompt or not ratio:
        return jsonify({"error": "Missing required parameters: 'prompt' or 'ratio'"}), 400

    # Call Gradio client for txt2img
    result = txt2img_client.predict(
        style_id=style_id,
        prompt=prompt,
        ratio=ratio,
        uuid_value=uuid_value,
        token=token,
        api_name="/process_txt2img"
    )

    # Print the result from the Gradio client
    print("Gradio client result:", result)

    if isinstance(result, str):
        try:
            # Attempt to parse the result if it's a string
            result = json.loads(result)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON returned from the Gradio client."}), 500

    # Log the parsed result for debugging purposes
    print("Parsed result from Gradio:", result)

    # Return the parsed result as JSON
    return jsonify(result)

@app.route('/ai/art/img2img/', methods=['POST'])
def process_img2img_data():
    # Get form data from the request
    is_translate = request.form.get('is_translate', '')
    is_first = request.form.get('is_first', '')
    style_id = request.form.get('style_id', '')
    ratio = request.form.get('ratio', '')
    uuid_value = request.form.get('Uid', '')
    token = request.form.get('Token', '')
    image = request.form.get('image_name')  # Get the image file sent in the request

    # You can print the received form data
    print("Received form data for img2img:")
    print(f"is_translate: {is_translate}, is_first: {is_first}, style_id: {style_id}, ratio: {ratio}")

    # Check for required parameters
    if not ratio or not image:
        return jsonify({"error": "Missing required parameters: 'ratio' or 'image'"}), 400

    # Save the image temporarily to send to Gradio (optional, depending on your Gradio client)


    # Call Gradio client for img2img
    result = img2img_client.predict(
        style_id=style_id,
        ratio=ratio,
        uuid_value=uuid_value,
        token=token,
        image=image,
        api_name="/process_img2img"
    )

    # Print the result from the Gradio client
    print(result)

    if isinstance(result, str):
        try:
            # Attempt to parse the result if it's a string
            result = json.loads(result)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON returned from the Gradio client."}), 500

    # Log the parsed result for debugging purposes
    print(result)

    # Return the parsed result as JSON
    return jsonify(result)

@app.route('/ai/art/lineart/', methods=['POST'])
def process_doodle_data():
    # Get form data from the request
    is_translate = request.form.get('is_translate', '')
    is_first = request.form.get('is_first', '')
    style_id = request.form.get('style_id', '')
    ratio = request.form.get('ratio', '')
    uuid_value = request.form.get('Uid', '')
    token = request.form.get('Token', '')
    prompt = request.form.get('prompt', '')
    image = request.form.get('image_name')  # Get the image file sent in the request

    # You can print the received form data
    print("Received form data for img2img:")
    print(f"is_translate: {is_translate}, is_first: {is_first}, style_id: {style_id}, ratio: {ratio}")

    # Check for required parameters
    if not ratio or not image:
        return jsonify({"error": "Missing required parameters: 'ratio' or 'image'"}), 400

    # Save the image temporarily to send to Gradio (optional, depending on your Gradio client)


    # Call Gradio client for img2img
    result = img2img_client.predict(
        ratio=ratio,
        image=image,
        style_id=style_id,
        uuid_value=uuid_value,
        token=token,
        prompt=prompt,
        api_name="/process_doodle"
    )

    # Print the result from the Gradio client
    print(result)

    if isinstance(result, str):
        try:
            # Attempt to parse the result if it's a string
            result = json.loads(result)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON returned from the Gradio client."}), 500

    # Log the parsed result for debugging purposes
    print(result)

    # Return the parsed result as JSON
    return jsonify(result)

@app.route('/ai/art/enhance/', methods=['POST'])
def process_enhace_data():
    # Get form data from the request
    uuid_value = request.form.get('Uid', '')
    token = request.form.get('Token', '')
    image = request.form.get('image_name')  # Get the image file sent in the request

    # You can print the received form data
    print("Received form data for img2img:")
    print(f"uuid_value: {uuid_value}, token: {token}, image: {image}")

    # Check for required parameters
    if not uuid_value or not image:
        return jsonify({"error": "Missing required parameters: 'ratio' or 'image'"}), 400

    # Save the image temporarily to send to Gradio (optional, depending on your Gradio client)


    # Call Gradio client for img2img
    result = img2img_client.predict(
        uuid_value=uuid_value,
        token=token,
        image=image,
        api_name="/process_enhance"
    )

    # Print the result from the Gradio client
    print(result)

    if isinstance(result, str):
        try:
            # Attempt to parse the result if it's a string
            result = json.loads(result)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON returned from the Gradio client."}), 500

    # Log the parsed result for debugging purposes
    print(result)

    # Return the parsed result as JSON
    return jsonify(result)

@app.route('/ai/art/prompt/', methods=['POST'])
def process_prompt_data():
    # Get form data from the request
    uuid_value = request.form.get('Uid', '')
    token = request.form.get('Token', '')
    image = request.form.get('image_name')  # Get the image file sent in the request

    # You can print the received form data
    print("Received form data for img2img:")
    print(f"uuid_value: {uuid_value}, token: {token}, image: {image}")

    # Check for required parameters
    if not uuid_value or not image:
        return jsonify({"error": "Missing required parameters: 'ratio' or 'image'"}), 400

    # Save the image temporarily to send to Gradio (optional, depending on your Gradio client)


    # Call Gradio client for img2img
    result = img2img_client.predict(
        uuid_value=uuid_value,
        token=token,
        image=image,
        api_name="/process_prompt"
    )

    # Print the result from the Gradio client
    print(result)

    if isinstance(result, str):
        try:
            # Attempt to parse the result if it's a string
            result = json.loads(result)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON returned from the Gradio client."}), 500

    # Log the parsed result for debugging purposes
    print(result)

    # Return the parsed result as JSON
    return jsonify(result)

@app.route('/ai/art/expand/', methods=['POST'])
def process_outpaint_data():
    # Get form data from the request
    uuid_value = request.form.get('Uid', '')
    token = request.form.get('Token', '')
    image = request.form.get('image_name')

    canvas = request.form.get('canvas_info')
    
    # You can print the received form data
    print("Received form data for img2img:")
    print(f"uuid_value: {uuid_value}, token: {token}, image: {image}")

    # Check for required parameters
    if not uuid_value or not image:
        return jsonify({"error": "Missing required parameters: 'ratio' or 'image'"}), 400

    # Save the image temporarily to send to Gradio (optional, depending on your Gradio client)


    # Call Gradio client for img2img
    result = img2img_client.predict(
        uuid_value=uuid_value,
        token=token,
        image=image,
        canvas=canvas,
        api_name="/process_outpaint"
    )

    # Print the result from the Gradio client
    print(result)

    if isinstance(result, str):
        try:
            # Attempt to parse the result if it's a string
            result = json.loads(result)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON returned from the Gradio client."}), 500

    # Log the parsed result for debugging purposes
    print(result)

    # Return the parsed result as JSON
    return jsonify(result)

@app.route('/ai/art/faceswap/', methods=['POST'])
def process_faceswap_data():
    # Get form data from the request
    uuid_value = request.form.get('Uid', '')
    token = request.form.get('Token', '')
    image = request.form.get('image_name') 
    style_id = request.form.get('style')# Get the image file sent in the request

    # You can print the received form data
    print("Received form data for img2img:")
    print(f"uuid_value: {uuid_value}, token: {token}, style: {style}, image: {image}")

    # Check for required parameters
    if not uuid_value or not image:
        return jsonify({"error": "Missing required parameters: 'ratio' or 'image'"}), 400

    # Save the image temporarily to send to Gradio (optional, depending on your Gradio client)


    # Call Gradio client for img2img
    result = img2img_client.predict(
        uuid_value=uuid_value,
        token=token,
        image=image,
        target=style,
        api_name="/process_faceswap"
    )

    # Print the result from the Gradio client
    print(result)

    if isinstance(result, str):
        try:
            # Attempt to parse the result if it's a string
            result = json.loads(result)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON returned from the Gradio client."}), 500

    # Log the parsed result for debugging purposes
    print(result)

    # Return the parsed result as JSON
    return jsonify(result)

@app.route('/ai/art/inpaint/', methods=['POST'])
def process_inpaint_data():
    # Get form data from the request
    is_translate = request.form.get('is_translate', '')
    is_first = request.form.get('is_first', '')
    style_id = request.form.get('style_id', '')
    ratio = request.form.get('ratio', '')
    uuid_value = request.form.get('Uid', '')
    token = request.form.get('Token', '')
    prompt = request.form.get('prompt', '')
    mask = request.form.get('mask_name')
    image = request.form.get('image_name')  # Get the image file sent in the request

    # You can print the received form data
    print("Received form data for img2img:")
    print(f"is_translate: {is_translate}, is_first: {is_first}, style_id: {style_id}, ratio: {ratio}")

    # Check for required parameters
    if not ratio or not image:
        return jsonify({"error": "Missing required parameters: 'ratio' or 'image'"}), 400

    # Save the image temporarily to send to Gradio (optional, depending on your Gradio client)


    # Call Gradio client for img2img
    result = inpaint_client.predict(
        style_id="0",
        ratio=ratio,
        uuid_value=uuid_value,
        token=token,
        prompt=prompt,
        mask=mask,
        image=image, 
        api_name="/process_inpaint"
    )

    # Print the result from the Gradio client
    print(result)

    if isinstance(result, str):
        try:
            # Attempt to parse the result if it's a string
            result = json.loads(result)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON returned from the Gradio client."}), 500

    # Log the parsed result for debugging purposes
    print(result)

    # Return the parsed result as JSON
    return jsonify(result)

if __name__ == '__main__':
    # Bind the app to all network interfaces (0.0.0.0) and specify the port (e.g., 5000)
    app.run(host='0.0.0.0', port=3000, debug=True)
