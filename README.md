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
- Understand the algorithms and techniques that goes into building large language models
- Design a pipeline that takes a news item (e.g. title + description + body) or a job description and returns a score for the news item and list of entities (and potentially their relationship) for the job description according to stored examples. Consider the following while designing your pipeline
  * Think about in what format you want to receive the news item to be processed
  * Think about how to select the best samples for the given news item
  * Think about how to pre-process the incoming item as well as the pre-defined samples
  * Think about how to compose a prompt that gives the best result for the given item
  * Think about the post-processing step you need to do to increase the accuracy as well as return in the format required
- Write a flask or fastapi backend. The API should have at least two endpoints
        /bnewscore - for scoring breaking news that may lead to public unrest
        /jdentities - for extracting entities from job description


## Data
The 1st dataset used for this project could be found in [here](https://docs.google.com/spreadsheets/d/19N_K6SnIm0FylD2TBs-5y3WeSgdveb3J/edit?usp=sharing&ouid=108085860825615283789&rtpof=true&sd=true) , and the 2nd dataset [development and traing ](https://github.com/walidamamou/relation_extraction_transformer/blob/main/relations_dev.txt) and [testing and final reporting](https://github.com/walidamamou/relation_extraction_transformer/blob/main/relations_test.txt).

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

