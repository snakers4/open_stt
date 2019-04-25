import os
import shutil
import random
import librosa
import hashlib
import numpy as np
import pandas as pd
from glob import glob
from tqdm import tqdm
from pathlib import Path
from scipy.io import wavfile


def streamline_wav_encoding(source_path,
                            target_sr=16000,
                            target_dtype=np.dtype('int16')):
    
    ERROR_MSG = 'Unknown file format: channels {}, dtype {}, sr {}'
        
    sr, wav = wavfile.read(source_path)
    dims = len(wav.shape)
    dtype = wav.dtype # numpy dtype
    
    if dims==1:
        pass
    elif dims==2:
        if wav.shape[1] == 1:
            wav = wav.squeeze()
        else:
            wav = wav.mean(axis=1) # multiple channels, average   
    else:
        raise ValueError(ERROR_MSG.format(dims,
                                          str(dtype),
                                          sr))
    if sr==target_sr and dtype==target_dtype:
        pass
    elif sr==target_sr and dtype==np.dtype('float32'):
        wav = (wav * 32767).astype(target_dtype) # cast to int
    elif sr!=target_sr:
        # do no care about dtype here
        # do everything with librosa for simplicity
        wav, sr = librosa.load(source_path,
                               mono=True,
                               sr=target_sr)
        # librosa converts to float32
        wav = (wav * 32767).astype(target_dtype) # cast to int
    else:
        raise ValueError(ERROR_MSG.format(dims,
                                          str(dtype),
                                          sr))
    
    assert wav.dtype == np.dtype('int16')
    assert len(wav.shape)==1
    
    return wav


def save_wav_diskdb(wav,
                    root_folder='../data/ru_open_stt/',
                    target_sr=16000):
    assert type(wav) == np.ndarray
    assert wav.dtype == np.dtype('int16')
    assert len(wav.shape)==1    
    
    target_format = 'wav'
    wavb = wav.tobytes()

    # f_path = Path(audio_path)
    f_hash = hashlib.sha1(wavb).hexdigest()

    store_path = Path(root_folder,
                      f_hash[0],
                      f_hash[1:3],
                      f_hash[3:15]+'.'+target_format)

    store_path.parent.mkdir(parents=True,
                            exist_ok=True)
    
    wavfile.write(filename=str(store_path),
                  rate=target_sr,
                  data=wav)
    
    return str(store_path)


def reroot_manifest(manifest_path,
                    source_path,
                    target_path):
    
    manifest = read_manifest(manifest_path)
    manifest.wav_path = manifest.wav_path.apply(lambda x: x.replace(source_path,
                                                                    target_path))
    manifest.text_path = manifest.text_path.apply(lambda x: x.replace(source_path,
                                                                      target_path))
    return manifest


def save_manifest(manifest_df,
                  path):
    assert list(manifest_df.columns) == ['wav_path','text_path','duration']
    manifest_df.reset_index(drop=True).sort_values(by='duration',
                                                   ascending=True).to_csv(path,sep=',',header=False,index=False)
    return True


def read_manifest(manifest_path):
    return pd.read_csv(manifest_path,
                       names=['wav_path','text_path','duration'])


def check_files(manifest_df):
    orig_len = len(manifest_df)
    assert list(manifest_df.columns) == ['wav_path','text_path','duration']
    wav_paths = list(manifest_df.wav_path.values)
    text_path = list(manifest_df.text_path.values)
    
    omitted_wavs = []
    omitted_txts = []
    
    for wav_path,text_path in zip(wav_paths,text_path):
        if not os.path.exists(wav_path):
            print('Dropping {}'.format(wav_path))
            omitted_wavs.append(wav_path)
        if not os.path.exists(text_path):
            print('Dropping {}'.format(text_path))
            omitted_txts.append(text_path)
    manifest_df = manifest_df[~manifest_df.wav_path.isin(omitted_wavs)]
    manifest_df = manifest_df[~manifest_df.text_path.isin(omitted_txts)]
    final_len = len(manifest_df)
    if final_len!=orig_len:
        print('Removed {} lines'.format(orig_len-final_len))
    return manifest_df


def plain_merge_manifests(manifest_paths,
                          MIN_DURATION=0.1,
                          MAX_DURATION=100):
    
    manifest_df = pd.concat([read_manifest(_) 
                             for _ in manifest_paths])
    manifest_df = check_files(manifest_df)
    
    manifest_df_fit = manifest_df[(manifest_df.duration>=MIN_DURATION) &
                                  (manifest_df.duration<=MAX_DURATION)]
        
    manifest_df_non_fit = manifest_df[(manifest_df.duration<MIN_DURATION) |
                                      (manifest_df.duration>MAX_DURATION)]
    
    print(f'Good hours: {manifest_df_fit.duration.sum() / 3600:.2f}')
    print(f'Bad hours: {manifest_df_non_fit.duration.sum() / 3600:.2f}')
    
    return manifest_df_fit


def save_txt_file(wav_path, text):
    txt_path = wav_path.replace('.wav','.txt')
    with open(txt_path, "w") as text_file:
        print(text, file=text_file)
    return txt_path


def get_wav_stat(wav_path):
    # sr, wav = wavfile.read(wav_path)
    # duration = len(wav)/sr
    size_kb = os.path.getsize(wav_path)/1024
    # return duration,size_kb,sr    
    return size_kb


def create_manifest_from_df(df):
    columns = ['wav_path','text_path','duration']
    manifest = df[columns]
    return manifest


def create_txt_files(df):
    assert 'text' in df.columns
    assert 'wav_path' in df.columns
    wav_paths, texts = list(df['wav_path'].values), list(df['text'].values)
    # not using multiprocessing for simplicity
    txt_paths = [save_txt_file(*_) for _ in tqdm(zip(wav_paths, texts), total=len(wav_paths))]
    df['text_path'] = txt_paths
    return df