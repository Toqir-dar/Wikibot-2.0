# Wiki Bot

Wiki Bot is a Django-based web application designed to provide concise and precise responses to user queries. Unlike traditional assistants, such as ChatGPT, which often provide lengthy explanations, Wiki Bot focuses on delivering short, to-the-point information. It fetches data from Wikipedia using its API and employs regex to extract relevant information from user queries. Additionally, it offers various utility features, such as time-telling, text translation, news updates, and weather information.

## Features

- **Short and Concise Responses**: Avoids lengthy explanations and provides direct answers.
- **Wikipedia Integration**: Retrieves data from Wikipedia using its API.
- **Regex Query Matching**: Extracts key information from user input using specific regex patterns.
- **Utility Features**:
  - Time-telling
  - Text translation
  - News updates
  - Weather information (supports both Celsius and Fahrenheit)
- **Session Management**: Allows users to clear the session with a simple command.

## Supported Query Formats

- **Time Queries**: Get the current time.
  - Example Queries:
    - "Tell me the time"
    - "What's the time?"
    - "What about time?"

- **Text Translation**: Translate text between languages.
  - Example Queries:
    - "Translate it: Hello to Spanish"
    - "Can you translate: Good morning to French?"
    - "Please translate: Thank you to German."

- **Weather Queries**: Get the temperature of a specific location in Celsius or Fahrenheit.
  - Example Queries:
    - "What's the temperature in New York?"
    - "Tell me the temperature in Tokyo."
    - "Temperature in London, please."
    - "What's the temperature in New York in Fahrenheit?"

- **General Queries**: Learn about specific topics.
  - Example Queries:
    - "Tell me about Python programming."
    - "What do you know about Machine Learning?"
    - "Give me information about the Eiffel Tower."

- **News Updates**: Fetch news about a specific topic.
  - Example Queries:
    - "What's the latest news about technology?"
    - "Can you tell me news updates about climate change?"
    - "I need news about space exploration."

- **Clear Session**: Clear the current session.
  - Example Command:
    - "Clear"

## Tech Stack

- **Backend**: Django
- **Frontend**: Tailwind CSS
- **APIs**: Wikipedia API, News API (for news updates), Weather API
- **Regex**: Used for parsing and extracting relevant parts of user queries

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shk0Abdullah/Wikibot
   cd Wikibot
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows, use `env\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations and start the development server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Access the application in your web browser at `http://127.0.0.1:8000/`.

## Usage

- Enter queries using the supported formats.
- Use the specific keywords and patterns mentioned above for different features.
- Clear the session by saying "clear" when needed.

## Contributing

Contributions are welcome! Fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Author

- **Abdullah Amjad**
  - [GitHub Profile](https://github.com/shk0Abdullah)

## Feedback

If you have any feedback or suggestions, feel free to create an issue or reach out via [LinkedIn](https://www.linkedin.com/in/abdullah-amjad-a86206298/).
