# Image Generator AI

A web-based AI image generator application that uses OpenAI's DALL-E API to generate images from text prompts.

## Features

- 🎨 Text-to-image generation powered by AI
- 🚀 Fast and responsive web interface
- 📱 Mobile-friendly design
- 💾 Download generated images
- 🔐 Secure API key handling

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **API**: OpenAI DALL-E
- **Styling**: Bootstrap 5

## Installation

### Prerequisites
- Python 3.8+
- An OpenAI API key (get one at https://platform.openai.com)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/migelmark1-bit/1st-project.git
cd 1st-project
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_api_key_here
FLASK_ENV=development
```

5. Run the application:
```bash
python app.py
```

6. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Enter a detailed text prompt describing the image you want to generate
2. Click "Generate Image"
3. Wait for the AI to generate your image
4. Download the image or generate another one

## API Configuration

The application uses:
- **Model**: DALL-E 3
- **Image Size**: 1024x1024
- **Image Quality**: Standard

## File Structure

```
1st-project/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not in repo)
├── .gitignore            # Git ignore file
├── static/
│   ├── css/
│   │   └── style.css     # Custom styles
│   └── js/
│       └── script.js     # Frontend logic
└── templates/
    └── index.html        # Main page
```

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key
- `FLASK_ENV`: Set to `development` or `production`

## Error Handling

The application includes error handling for:
- Missing API key
- Invalid prompts
- API rate limits
- Network errors

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License - feel free to use this project for personal or commercial purposes.

## Support

For issues with the OpenAI API, visit: https://platform.openai.com/docs
