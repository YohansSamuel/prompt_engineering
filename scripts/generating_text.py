class TextGenerator():
    def __init__(self, examples,co):
        self.examples = examples
        self.co = co

    def prepare_prompt(self, example):
        prompt = self.examples + [example]

        return ("".join([str(exam) for exam in prompt]))

    def extract(self, example):
        extraction = self.co.generate(
            model='large',
            prompt=self.prepare_prompt(example),
            max_tokens=100,
            temperature=0.5,
            stop_sequences=["----"])

        return(extraction.generations[0].text[:-1])

    def generate_score(self, example):
        self.response = self.co.generate(
        model='xlarge',
        prompt=self.prepare_prompt(example),
        max_tokens=50,
        temperature=0.9,
        k=0,
        p=0.75,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["----"],
        return_likelihoods='NONE')

    def predict_score(self):
        return self.response.generations[0].text[:-1]