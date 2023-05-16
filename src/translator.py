from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

class Translator(object):
    model = None
    tokenizer = None

    @staticmethod
    def create_model_and_tokenizer():
        if Translator.model is None:
            try:
                Translator.model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
            except Exception as e:
                print("Couldn't load model.")
                print(e)
        
        if Translator.tokenizer is None:
            try:
                Translator.tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")
            except Exception as e:
                print("Couldn't load tokenizer.")
                print(e)

    @staticmethod
    def translate(text, source_language="en", target_language="ro"):
        Translator.create_model_and_tokenizer()

        # Set source language for tokenizer
        Translator.tokenizer.src_lang = source_language

        # Try to encode text
        try:
            encoded_text = Translator.tokenizer(text, return_tensors="pt")
        except Exception as e:
            print("Couldn't encode text.")
            print(e)
        
        # Try to generate tokens
        try:
            generated_tokens = Translator.model.generate(**encoded_text, forced_bos_token_id=Translator.tokenizer.get_lang_id(target_language))
        except Exception as e:
            print("Couldn't generate tokens. Maybe language is not supported.")
            print(e)

        target_text = None

        # Try to decode tokens
        try:
            target_text = Translator.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        except Exception as e:
            print("Couldn't decode tokens.")
            print(e)
        
        # Return translated text
        if target_text is not None:
            return target_text[0]
        else:
            return target_text
