# 🍳 AI Recipe Generator

This is a smart web application that generates a creative, complete recipe in Persian based on an image of ingredients. This project showcases the power of combining different AI services (Computer Vision and NLP) to solve a fun and practical problem.

---

### 📸 Live Demo

[Insert a cool GIF or screenshot of the app in action here. Upload your image/GIF to the GitHub repository and link it here.]

---

### ✨ Features

*   **🖼️ Easy Image Upload:** A simple and intuitive interface to upload images in `jpg`, `jpeg`, or `png` format.
*   **🧠 Smart Ingredient Recognition:** Utilizes the powerful **AWS Rekognition** service to accurately detect food items in the uploaded image.
*   **✍️ Creative Recipe Generation:** Employs **Google's Gemini AI** to craft unique, logical, and delicious recipes from the identified ingredients.
*   **🚀 Interactive User Interface:** Built with **Streamlit** for a fast, responsive, and user-friendly experience.

---

### 🛠️ Tech Stack

*   **Languages & Frameworks:**
    *   ![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
    *   ![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-red.svg)
*   **Cloud Services & APIs:**
    *   **AWS Rekognition:** For image analysis and label detection.
    *   **Google Gemini AI:** For natural language generation.
*   **Core Libraries:**
    *   `boto3`: The official AWS SDK for Python.
    *   `google-generativeai`: The official Google library for the Gemini API.
    *   `python-dotenv`: For securely managing environment variables.

---

### 🚀 Setup and Installation

Follow these steps to run the project locally.

#### Prerequisites
*   [Python 3.8](https://www.python.org/downloads/) or higher.
*   [Git](https://git-scm.com/) installed on your machine.

#### 1. Clone the Repository
```bash
git clone [YOUR_GITHUB_REPOSITORY_URL]
cd [YOUR_PROJECT_FOLDER_NAME]
```

#### 2. Create and Activate a Virtual Environment
This isolates the project's dependencies from your main system.
*   **On Windows:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
*   **On macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

#### 3. Install Dependencies
All required packages are listed in `requirements.txt`.
```bash
pip install -r requirements.txt
```
*(Note for project owner: If you add new packages, remember to update the file by running `pip freeze > requirements.txt`)*

#### 4. Set Up API Keys (Crucial Step)
The application requires API keys from both AWS and Google to function.

1.  In the root directory of the project, create a new file named `.env`.
2.  Copy the following structure into the file and replace the placeholders with your actual keys:

    ```
    # Your IAM user access keys from AWS
    AWS_ACCESS_KEY_ID="YOUR_AWS_ACCESS_KEY_ID"
    AWS_SECRET_ACCESS_KEY="YOUR_AWS_SECRET_ACCESS_KEY"

    # Your API key from Google AI Studio
    GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
    ```
**Security Note:** The `.env` file contains sensitive credentials and should **never** be committed to Git. The `.gitignore` file is already configured to ignore it.

#### 5. Run the Application
Use the Streamlit CLI to launch the web app:
```bash
streamlit run src/app.py
```
The application will automatically open in a new tab in your web browser. Enjoy!

---

### 📈 Future Improvements
- [ ] Support for multiple image uploads.
- [ ] Allow users to manually add or remove ingredients after detection.
- [ ] Save favorite recipes to a user profile.
- [ ] Estimate nutritional information (calories, macros, etc.) for the generated recipe.