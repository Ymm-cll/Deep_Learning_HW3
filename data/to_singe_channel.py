from scipy.io import wavfile
import matplotlib.pyplot as plt

# 读取16bit整数wav
fs, sig = wavfile.read('E:\\BaiduNetdiskDownload\\musika-main\data\\raw_data\\love in the dark_01.wav')
print(sig.shape)