# Prompt_Engineering

<!-- Table of contents -->
- [Prompt Engineering: In-context learning with GPT-3 and other Large Language Models](#Prompt-Engineering)
  - [About](#about)
  - [Objectives](#objectives)
  - [Data](#data)
  - [Repository overview](#repository-overview)
  - [Contrbutors](#contrbutors)
  - [License](#license)

## About
This week’s challenge is to systematically explore strategies that help generate prompts for LLMs to extract relevant entities from job descriptions and also to classify web pages given only a few examples of human scores. You will be also required to compare responses and accuracies of multiple LLM models for given prompts.

## Objectives


## Data
The data used for this project could be foun in [here](https://docs.google.com/spreadsheets/d/19N_K6SnIm0FylD2TBs-5y3WeSgdveb3J/edit?usp=sharing&ouid=108085860825615283789&rtpof=true&sd=true) ,[development and traing ](https://github.com/walidamamou/relation_extraction_transformer/blob/main/relations_dev.txt) and [testing and final reporting](https://github.com/walidamamou/relation_extraction_transformer/blob/main/relations_test.txt).

## Repository overview
 Structure of the repository:
 
        ├── models  (contains trained model)
        ├── .github (github workflows for CI/CD, CML)
        ├── screenshots (model versioning screenshots)
        ├── data  (contains data versioning metedata)
        ├── scripts (contains the main script)	
        │   ├── logger.py (logger for the project)
        │   ├── plot.py (handles plots)
        │   ├── preprocessing.py (dataset preprocessing)
        ├── notebooks	
        │   ├── job_description_entity_extraction.ipynb (Extraction of job description entity)
        │   ├── document_score.ipynb (score for the news item)
        ├── tests 
        │   ├── test_preprocessing.py (test for the preprocessing script)
        ├── README.md (contains the project description)
        ├── requirements.txt (contains the required packages)
        |── LICENSE (license of the project)
        └── .dvc (contains the dvc configuration)


## Contrbutor(s)
- [Yohans Samuel](https://www.linkedin.com/in/yohanssamuel/)

## License
[MIT](https://choosealicense.com/licenses/mit/)

