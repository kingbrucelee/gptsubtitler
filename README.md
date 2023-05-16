# Subtitler
Automatically subtitle any English-speaking video to a language of your choice.

**Please don't forget to star the repository if you find it useful or educational!**

Before:

https://github.com/extremq/subtitler/assets/45830561/49f6ecce-cfdc-4f1c-97eb-07a36ac841c9

After (in Romanian):

https://github.com/extremq/subtitler/assets/45830561/9d122965-6fc0-4cff-9dcf-a6d6c3c2f1e0

# Setup
Install the `requirements.txt` file.

```
pip install -r requirements.txt
```

# Quick guide
Example usage for adding subtitles and translating them in Romanian:
```py
from src.transcriber import Transcriber

Transcriber.transcribe("soldier.mp4", target_language="ro", model_type="medium", language_model_type="large")
```

You can also use the `Translator` class from `translator.py` if you just want to translate some text.

Example usage for translating from English to Romanian:
```py
from src.translator import Translator

print(Translator.translate("Hi!", target_language="ro", source_language="en"))
```

If you have generated a `.srt` file and just want to add subtitles:
```py
from src.video_utils import create_video_with_subtitles
create_video_with_subtitles("video.mp4", "output.srt", "video_subtitled.mp4")
```

# Options
Available options for `model_type` (the audio to text model):
- tiny
- base
- small
- medium
- large

Available options for `language_model_type` (the language translator model):
- base
- large
