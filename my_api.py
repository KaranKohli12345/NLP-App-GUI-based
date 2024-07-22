class API:

    def Sentiment_Analysis(self, text):

        import nlpcloud 

        client = nlpcloud.Client("distilbert-base-uncased-emotion", "7e6fe564c0baa38b214a9eb574c3242d68bbe982", gpu=False)
        response = client.sentiment(text)
        result = response['scored_labels'][0]['label']
        return result

    
    def Language_Detection(self, text):
        
        from langdetect import detect

        language = detect(text)
        return language
    
    
    def NER(self, text):

        import spacy

        # Load the pre-trained model
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        d = {}

        # Extract entities
        for ent in doc.ents:
            d[ent.text] = ent.label_
        
        return d

