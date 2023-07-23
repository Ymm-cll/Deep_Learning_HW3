import os

from pydub import AudioSegment
from tqdm import tqdm


def to_double_channel(path):
    for i in tqdm(os.listdir(path)):
        audio = AudioSegment.from_wav(f'{path}/{i}')
        stereo = audio.set_channels(2)
        stereo.export(f'{path}/{i}', format='wav')

