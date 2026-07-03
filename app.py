"""
Image Generator AI - Flask Application
A web-based application for generating images using OpenAI's DALL-E API
"""

import os
import base64
import requests
from io import BytesIO
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Configuration
API_KEY = os.getenv('OPENAI_API_KEY')
if not API_KEY:
    print("WARNING: OPENAI_API_KEY not found in environment variables!")


@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_image():
    """
    Generate an image based on the prompt
    
    Expected JSON:
    {
        "prompt": "A beautiful sunset over the ocean",
        "size": "1024x1024" (optional)
    }
    """
    try:
        # Get data from request
        data = request.get_json()
        prompt = data.get('prompt', '').strip()
        size = data.get('size', '1024x1024')
        
        # Validate prompt
        if not prompt:
            return jsonify({
                'success': False,
                'error': 'Prompt cannot be empty'
            }), 400
        
        if len(prompt) > 4000:
            return jsonify({
                'success': False,
                'error': 'Prompt is too long (max 4000 characters)'
            }), 400
        
        # Check if API key is configured
        if not API_KEY:
            return jsonify({
                'success': False,
                'error': 'OpenAI API key not configured. Please set OPENAI_API_KEY in .env'
            }), 500
        
        # Call OpenAI DALL-E API
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=size,
            quality="standard",
            n=1,
        )
        
        # Get image URL from response
        image_url = response.data[0].url
        
        # Download image and convert to base64
        image_response = requests.get(image_url)
        if image_response.status_code != 200:
            return jsonify({
                'success': False,
                'error': 'Failed to download generated image'
            }), 500
        
        # Convert image to base64
        image_data = base64.b64encode(image_response.content).decode('utf-8')
        
        return jsonify({
            'success': True,
            'image': f'data:image/png;base64,{image_data}',
            'prompt': prompt,
            'message': 'Image generated successfully!'
        }), 200
    
    except Exception as e:
        print(f"Error generating image: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'Error generating image: {str(e)}'
        }), 500


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'api_configured': bool(API_KEY)
    }), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500


if __name__ == '__main__':
    # Run the Flask app
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=debug_mode
    )
