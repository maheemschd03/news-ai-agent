# News AI Agent

A powerful AI-powered news aggregation and website generation system that automatically collects news from multiple sources and creates a beautiful, responsive website to display the information.

## Features

- Automated news collection from multiple reputable sources
- AI-powered content analysis and organization
- Real-time progress tracking
- Beautiful, responsive website generation
- Web interface for monitoring the process
- Background processing for long-running tasks

## News Sources

The system collects news from the following sources:
- BBC News
- The Hindu
- Times of India
- CNN
- Wired
- TechCrunch

## Prerequisites

- Python 3.x
- Google AI API key (for Gemini model)
- Internet connection for news fetching

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd news-ai-agent
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your Google AI API key:
   - Get your API key from the Google AI Studio
   - Replace the API key in `test.py` with your own key

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Click the "Start Process" button to begin news collection and website generation

4. Monitor the progress through the web interface

5. Once complete, view the generated website at:
```
http://localhost:5000/Final.html
```

## Project Structure

- `app.py`: Main Flask application with web interface
- `test.py`: Core functionality for news collection and website generation
- `templates/`: Contains HTML templates
- `static/`: Stores generated website files
- `requirements.txt`: Project dependencies

## Dependencies

- Flask 3.0.0
- Requests 2.31.0
- BeautifulSoup4 4.12.2
- Google Generative AI 0.3.2

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google AI for providing the Gemini model
- All news sources for their content 