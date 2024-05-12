# Question & Answer System for E-Learning
 - This is an end to end LLM project based on GoogleGenAI and Langchain. In this project I built a Q&A system based on a data from an e-learning company called codebasics (website: codebasics.io). Codebasics sells data related courses and bootcamps. They have thousands of learners who uses discord server or email to ask questions. This system will provide a streamlit based user interface for students where they can ask questions and get answers.

 ![E-Learning Image](./image/e-learning-image.png)

## DEMO
- Check site [here](https://8504-01hwj8ynshjz7spkr595x77ec2.cloudspaces.litng.ai/)

## Project Highlights
- Use a real CSV file of FAQs that Codebasics company(E-Learning platform) is using right now.
- Their human staff will use this file to assist their course learners.
- We will build an LLM based question and answer system that can reduce the workload of their human staff.
- Students should be able to use this system to ask questions directly and get answers within seconds

## Libraries Used
 - FAISS
 - dotenv
 - streamlit
 - sentence-transformer
 - langchain + GoogleGenerativeAI
 - Huggingface instructor embeddings: Text embeddings

## Installation
 1. Prerequisites
    - Git
    - Command line familiarity
 2. Clone the Repository: `git clone https://github.com/NebeyouMusie/QA-System-for-E_Learning.git`
 3. Create and Activate Virtual Environment (Recommended)
    - `python -m venv venv`
    - `source venv/bin/activate`
 4. Navigate to the projects directory `cd ./QA-System-for-E_Learning` using your terminal
 5. Install Libraries: `pip install -r requirements.txt`

## Usage 
 1. run `streamlit run app.py`
 2. The web app will open in your browser.
    - To create a knowledebase of FAQs, click on Create Knolwedge Base button. It will take some time before knowledgebase is created so please wait.
    - Once knowledge base is created you will see a directory called faiss_index in your current folder
    - Now you are ready to ask questions. Type your question in Question box and hit Enter

## Sample Questions
 -Do you guys provide internship and also do you offer EMI payments?
 - Do you have javascript course?
 - Should I learn power bi or tableau?
 - I've a MAC computer. Can I use powerbi on it?
 - I don't see power pivot. how can I enable it?

## Project Structure
- app.py: The main Streamlit application script.
- langchain_utils.py: This has all the langchain code
- requirements.txt: A list of required Python packages for the project.
- notebook: jupyter notebook folder
- .env: Configuration file for storing your Google API key.

## Contributions
 - Contributions are welcomed

## Support
 - Give this project a star ⭐ if you like it

## Acknowledgements
 - I would like to thank [codebasics]() 
   
## Author
 - LinkedIn: [Nebeyou Musie](https://www.linkedin.com/in/nebeyou-musie)
 - Gmail: nebeyoumusie@gmail.com
 - Telegram: [Nebeyou Musie](https://t.me/NebeyouMusie)

