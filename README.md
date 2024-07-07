# Intelligent Email Composition Solution

This project is a Streamlit application that generates email responses using a language model. The application allows users to input the topic of the email, the sender's and recipient's names, and the desired writing style. The language model then generates an appropriate email response based on these inputs.

## Repository Link

[GitHub Repository](https://github.com/1666sApple/Intelligent-Email-Composition-Solution.git)


## Features

- **Email Topic Input**: Users can enter the topic of the email.
- **Sender and Recipient Details**: Users can specify the names and emails of the sender and recipient.
- **Writing Style Selection**: Users can choose from various writing styles such as formal, informal, satisfied, and unsatisfied.
- **Email Generation**: The application generates an email based on the provided inputs.

## Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

- Python 3.7+
- Streamlit
- Langchain
- Langchain Community
- CTransformers

### Installation

1. Clone the repository:

```bash
git clone https://github.com/1666sApple/Intelligent-Email-Composition-Solution.git
cd Intelligent-Email-Composition-Solution
```

2. Create a virtual environment and activate it:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application:

- Ensure you have the language model file llama-2-7b-chat.ggmlv3.q8_0.bin in the appropriate directory (llm/).
- Download the language model file from the following link: `https://www.kaggle.com/datasets/rodrigostallsikora/llama-2-7b-chat-ggmlv3-q8-0-bin`
- Place the downloaded file in the llm/ directory.
- Run the Streamlit application:
```bash
streamlit run app.py
```
- The application will be accessible at http://localhost:8501 in your web browser.

### Usage

1. Enter the topic of the email in the provided text area.
2. Fill in the sender's name and email.
3. Fill in the recipient's name and email.
4. Select the writing style from the dropdown menu.
5. Click the "Generate Email" button to generate the email response.
6. The generated email will be displayed on the screen.

### Contributing

We welcome contributions to the `Intelligent Email Composition Solution` project. If you have any suggestions, bug reports, or feature requests, please create an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Make your changes.
4. Commit your changes:
    ```bash
    git commit -m 'Add some feature'
    ```
5. Push to the branch:
    ```bash
    git push origin feature/your-feature-name
    ```
6. Open a pull request.