# Subtitler
Automatically subtitle any English-speaking video to a language of your choice.
**Please don't forget to star the repository if you find it useful or educational!**

# Setup
Install the `requirements.txt` file.

```
pip install -r requirements.txt
```

# Quick guide
Example usage for adding subtitles and translating them in Romanian:
```py
from src.transcriber import Transcriber

Transcriber.transcribe("video.mp4", target_language="ro", model_type="base")
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