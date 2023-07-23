import os

def get_subdirectories(directory):
    subdirectories = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    return subdirectories

# 替换'path_to_directory'为你要读取的目录路径
directory_path = 'E:\BaiduNetdiskDownload\DSD100\Mixtures\Test'
subdirs = get_subdirectories(directory_path)
for filepath in subdirs:
    path=directory_path+'\\'+filepath+'\\'+'mixture.wav'
    with open(path,"rb") as f:
        wav=f.read()
    with open("E:\BaiduNetdiskDownload\DSD100\Mixtures\\"+filepath+'.wav',"wb") as t:
        t.write(wav)
