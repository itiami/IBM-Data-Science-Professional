# Python and R Project for IBM Data Science Professional Certificate Assignment
![IBM Data Science](https://github.com/itiami/IBM-Data-Science-Professional/blob/remoteBr/django_web_dev/django_web_dev/static/images/IBM.jpg)

## Author
**ABDULLAH AL Numan**

## Project Overview

This repository contains project work and learning resources associated with the **IBM Data Science Professional Certificate**. The project environment is built using the **Anaconda® Distribution on Cloud**, providing a powerful and flexible environment for data science and machine learning.

## 🌐 Platform

- **Environment**: Anaconda® Distribution  
- **Deployment**: Cloud-based (Jupyter Notebooks via Anaconda Cloud)

## 📚 Course Content

The professional certificate program is composed of 12 comprehensive courses:

1. **What is Data Science?**  
2. **Tools for Data Science**  
3. **Data Science Methodology**  
4. **Python for Data Science, AI & Development**  
5. **Python Project for Data Science**  
6. **Databases and SQL for Data Science with Python**  
7. **Data Analysis with Python**  
8. **Data Visualization with Python**  
9. **Machine Learning with Python**  
10. **Applied Data Science Capstone**  
11. **Generative AI: Elevate Your Data Science Career**  
12. **Data Scientist Career Guide and Interview Preparation**

## 🚀 Getting Started

To reproduce or interact with the project environment:

1. Install Anaconda or use [Anaconda Cloud](https://anaconda.org/).
2. Launch Jupyter Notebook or JupyterLab.
3. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ibm-data-science-certificate.git
   cd ibm-data-science-certificate
   ```

## Django Project Setup

This repository includes a Django web application to complement the data science projects. Below are the steps to set up and run the Django project.

### Project Structure
- **Django Project Directory**: `./django_web_dev`
- **Virtual Environment Directory**: `./venv`

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions
1. **Clone the Repository** (if not already done):
   ```bash
   git clone https://github.com/your-username/ibm-data-science-certificate.git
   cd ibm-data-science-certificate
   ```

2. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Navigate to the Django Project Directory**:
   ```bash
   cd .\django_web_dev\
   ```

4. **Install Dependencies**:
   Ensure you have the required Python packages installed by running:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Django Development Server**:
   Start the server with:
   ```bash
   py .\manage.py runserver
   ```
   - The application will be accessible at `http://127.0.0.1:8000/`.
   - Press `Ctrl+C` to stop the server.

### Requirements
The `requirements.txt` file lists all necessary Python packages for the Django project. You can generate or update it using:
```bash
pip freeze > requirements.txt
```

## License
This project is developed for educational purposes as part of a Duke University assignment. Redistribution and modification are subject to course guidelines.