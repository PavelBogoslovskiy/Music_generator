import torch
import transformers
from transformers import GPT2Tokenizer
import pyttsx3
from pydub import AudioSegment

if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

tokenizer = GPT2Tokenizer.from_pretrained('sberbank-ai/rugpt3small_based_on_gpt2')

model = torch.load('krov_test_8.pt')


def text_gen(prompt):
    prompt = tokenizer.encode(prompt, return_tensors='pt').to(device)
    out = model.generate(
        input_ids=prompt,
        max_length=120,
        num_beams=5,
        do_sample=True,
        temperature=75.,
        top_k=20,
        top_p=0.40,
        no_repeat_ngram_size=2,
        num_return_sequences=1,
    ).cpu().numpy()
    text = tokenizer.decode(out[0])
    #     print(textwrap.fill(text, 120), end='\n------------------\n')
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # скорость речи
    engine.setProperty('volume', 100.0)
    voices = engine.getProperty('voices')
    # index = 0
    # for voice in voices:
    #     print(f'index-> {index} -- {voice.name}')
    #     index += 1
    engine.setProperty('voice', voices[0].id)
    engine.save_to_file(text, 'file_name.wav')
    engine.runAndWait()
    #
    # AudioSegment.ffmpeg = "C:\\FFmpeg\\bin\\ffmpeg.exe"
    sound1 = AudioSegment.from_mp3('songs\\bio.mp3')
    sound2 = AudioSegment.from_wav("file_name.wav")
    # mix sound2 with sound1, starting at 5000ms into sound1)
    output = sound1.overlay(sound2, position=5000)
    # save the result
    output.export("mixed_sounds.mp3", format="mp3")

    return text
