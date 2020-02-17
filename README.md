![](https://img.shields.io/github/v/release/snakers4/open_stt?include_prereleases&style=for-the-badge)

[![Donations](https://opencollective.com/open_stt/tiers/donation/badge.svg?label=donations&color=brightgreen)](https://opencollective.com/open_stt)
[![Backers](https://opencollective.com/open_stt/tiers/backer/badge.svg?label=backers&color=brightgreen)](https://opencollective.com/open_stt)
[![Sponsors](https://opencollective.com/open_stt/tiers/sponsor/badge.svg?label=sponsors&color=brightgreen)](https://opencollective.com/open_stt)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Mailing list : test](https://img.shields.io/badge/Contact-Authors-blue.svg)](mailto:open_stt@googlegroups.com)


# **Russian Open Speech To Text (STT/ASR) Dataset**

Arguably the largest public Russian STT dataset up to date:
- ~16m utterances (1-2m with less perfect annotation, see [#7](https://github.com/snakers4/open_stt/issues/7));
- ~20 000 hours;
- 2,3 TB (in `.wav` format in `int16`);
- (**new!**) A new domain - public speech;
- (**new!**) A huge Radio dataset update with **10 000+ hours**;

Prove [us](mailto:open_stt@googlegroups.com) wrong!
Open issues, collaborate, submit a PR, contribute, share your datasets!
Let's make STT in Russian (and more) as open and available as CV models.

**Planned releases:**

- Refine and publish speaker labels, probably add speakers for old datasets;
- Improve / re-upload some of the existing datasets, refine the STT labels;
- Probably add new languages;
- Add pre-trained models;

# **Table of contents**


  - [Dataset composition](https://github.com/snakers4/open_stt/#dataset-composition)
  - [Downloads](https://github.com/snakers4/open_stt/#downloads)
    - [Via torrent](https://github.com/snakers4/open_stt/#via-torrent)
    - [Links](https://github.com/snakers4/open_stt/#links)
    - [Download-instructions](https://github.com/snakers4/open_stt/#download-instructions)
    - [End-to-end download scripts](https://github.com/snakers4/open_stt/#end-to-end-download-scripts)
  - [Annotation methodology](https://github.com/snakers4/open_stt/#annotation-methodology)
  - [Audio normalization](https://github.com/snakers4/open_stt/#audio-normalization)
  - [Disk db methodology](https://github.com/snakers4/open_stt/#on-disk-db-methodology)
  - [Helper functions](https://github.com/snakers4/open_stt/#helper-functions)
  - [Contacts](https://github.com/snakers4/open_stt/#contacts)
  - [Acknowledgements](https://github.com/snakers4/open_stt/#acknowledgements)
  - [FAQ](https://github.com/snakers4/open_stt/#faq)
  - [License](https://github.com/snakers4/open_stt/#license)
  - [Donations](https://github.com/snakers4/open_stt/#donations)

# **Dataset composition**

| Dataset                   | Utterances | Hours | GB  | Av s/chars | Comment          | Annotation  | Quality/noise |
|---------------------------|------------|-------|-----|------------|------------------|-------------|---------------|
| radio_v4                   | 7,603,192  | 10,430 | 1,195 | 4.94s / 68 | Radio            | Alignment (*)| 95%  / crisp |
| public_speech             | 1,700,060  | 2,709 | 301 | 5,73s / 79 | Public speech    | Alignment (*)| 95%  / crisp |
| audiobook_2               | 1,149,404  | 1,511 | 162 | 4.7s / 56  | Books            | Alignment (*)| 95%  / crisp  |
| radio_2                   |   651,645  | 1,439 | 154 | 7.95s / 110 | Radio            | Alignment (*)|  TBC, should be high            |
| public_youtube1120        |  1,410,979 | 1,104 | 237 | 2.82s / 34 | Youtube videos    | Subtitles   | 95%  / ~crisp |
| public_youtube700         |   759,483  |   701 |  75 | 3.3s / 43  | Youtube videos   | Subtitles   | 95%  / ~crisp |
| tts_russian_addresses     | 1,741,838  |   754 |  81 | 1.6s / 20  | Russian addresses| TTS 4 voices| 100% / crisp  |
| asr_public_phone_calls_2  |   603,797  |   601 |  66 | 3.6s / 37  | Phone calls      | ASR         | 70%  / noisy  |
| public_youtube1120_hq     |   369,245  |   291 |  31 | 2.84s / 37 | YouTube videos HQ sound | Subtitles   | 95%  / ~crisp |
| asr_public_phone_calls_1  |   233,868  |   211 |  23 | 3.3s / 29  | Phone calls      | ASR         | 70%  / noisy  |
| radio_v4_add              |    92,679  |   157 | 18  | 6.1s / 80  | Radio            | Alignment (*)| 95%  / crisp |
| asr_public_stories_2      |    78,186  |    78 |   9 | 3.5s / 43  | Books            | ASR         | 80%  / crisp  |
| asr_public_stories_1      |    46,142  |    38 |   4 | 3.0s / 30  | Books            | ASR         | 80%  / crisp  |
| public_series_1           |    20,243  |    17 |   2 | 3.1s / 38  | Youtube videos   | Subtitles   | 95%  / ~crisp |
| asr_calls_2_val           |     12,950 |   7,7 |   2 | 2.15s / 34 | Phone calls      | Manual annotation | 99%  / crisp |
| public_lecture_1          |     6,803  |     6 |   1 | 3.4s / 47  | Lectures         | Subtitles   | 95%  / crisp  |
| buriy_audiobooks_2_val    |     7,850  |   4,9 |   1 | 2.25s / 31 | Books            | Manual annotation | 99%  / crisp |
| public_youtube700_val     |     7,311  |   4,5 |   1 | 2.2 / 35   | Youtube videos   | Manual annotation | 99%  / crisp |
| Total                     | 16,513,202‬  | 20,108 | 2,369 |            |                  |             |               |

**(*) Automatic alignment**

This alignment was performed using Yuri's alignment tool.
[Contact him](mailto:open_stt@googlegroups.com) if you need alignment for your own dataset.

# **Updates**

## **_Update 2020-02-07_**

**Temporarily Deprecated Direct MP3 Links:

- Please refer here for more [information](https://github.com/snakers4/open_stt/issues/12#issuecomment-586867040)

## **_Update 2019-11-04_**

**New train datasets added:**

  - 10,430 hours radio_v4;
  - 2,709 hours public_speech;
  - 154 hours radio_v4_add;
  - 5% sample of all new datasets with annotation.
  
<details>
  <summary>Click to expand</summary>
  
  ## **_Update 2019-06-28_**

  **New train datasets added:**

    - 1,439 hours radio_2;
    - 1,104 hours public_youtube1120;
    - 291 hours public_youtube1120_hq;

  **New validation datasets added:**

    - 8 hours asr_calls_2_val;
    - 5 hours buriy_audiobooks_2_val;
    - 5 hours public_youtube700_val;

  ## **_Update 2019-05-19_**

  Also shared a wav version via torrent.

  ## **_Update 2019-05-13_**

  Added the forgotten txt files to mp3 archives.
  Updating the torrent.

  ## **_Update 2019-05-12_**

  Torrent created and uploaded to academictorrents.

  ## **_Update 2019-05-10_**

  Quickly converted the dataset to MP3 thanks to the community!
  Waiting for our account for academic torrents to be approved.
  v0.4 will boast MP3 download links.

  ## **_Update 2019-05-07_ Help needed!**

  **If you want to support the project, you can:**
  - Help us with hosting (create a mirror) / provide a reliable node for torrent;
  - Help us with writing some [helper](https://github.com/snakers4/open_stt/issues/2) functions;
  - [Donate](https://buymeacoff.ee/8oneCIN) (each coffee pays for several full downloads) / use our DO referral [link](https://sohabr.net/habr/post/357748/) to help;

  ~~We are converting the dataset to MP3 now.~~
  Please contact us using the below contacts, if you would like to help.

</details>

# **Downloads**

## **Via torrent**

Save us a couple of bucks, download via torrent:
- ~~An **MP3** [version](http://academictorrents.com/details/4a2656878dc819354ba59cd29b1c01182ca0e162) of the dataset (v3)~~ not supported anymore;
- A **WAV** [version](https://academictorrents.com/details/a7929f1d8108a2a6ba2785f67d722423f088e6ba) of the dataset (v5);

You can download separate files via torrent.
~~Try several torrent clients if some do not work.~~
Looks like that due to large chunk size, most conversional torrent clients just fail silently.
No problem (re-calculating the torrent takes much time, and some people have downloaded it already):

```
apt update
apt install aria2
# list the torrent files
aria2c --show-files ru_open_stt_wav_v10.torrent
# download only one file
aria2c --select-file=4 ru_open_stt_wav_v10.torrent
# for more options visit
# https://aria2.github.io/manual/en/html/aria2c.html#basic-options
# https://aria2.github.io/manual/en/html/aria2c.html#bittorrent-metalink-options
# https://aria2.github.io/manual/en/html/aria2c.html#bittorrent-specific-options
```
If you are using Windows, you may use Linux subsystem to run these commands.

## **Links**

All **WAV** files can be downloaded ONLY via [torrent](https://academictorrents.com/details/a7929f1d8108a2a6ba2785f67d722423f088e6ba)

| Dataset                               | GB, wav | GB, mp3 |  Mp3 |  Source | Manifest  |
|---------------------------------------|------|----------------|-----|  -------| ----------|
| radio_v4                              | 1059 | 263            | [mp3](https://ru-open-stt.ams3.digitaloceanspaces.com/radio_v4_mp3.tar.gz), [txt](https://forms.gle/nosMaNgj8MWKm99d9) | Radio | [manifest file](https://ru-open-stt.ams3.digitaloceanspaces.com/radio_v4_manifest.csv) |
| public_speech                         | 257  | 38.5            | [mp3](https://ru-open-stt.ams3.digitaloceanspaces.com/public_speech_mp3.tar.gz), [txt](https://forms.gle/nosMaNgj8MWKm99d9) | Sources from the Internet + alignment | [manifest file](https://ru-open-stt.ams3.digitaloceanspaces.com/public_speech_manifest.csv) |
| radio_v4_add                          | 15.7  | 2.2             | [mp3](https://ru-open-stt.ams3.digitaloceanspaces.com/radio_v4_add_mp3_reupload.tar.gz), [txt](https://forms.gle/nosMaNgj8MWKm99d9) | Radio | [manifest file](https://ru-open-stt.ams3.digitaloceanspaces.com/radio_v4_add_manifest.csv) |
| 5% of radio_v4 + public_speech        | -    | 15.3            | [mp3+txt](https://ru-open-stt.ams3.digitaloceanspaces.com/radio_pspeech_sample_mp3.tar.gz) | - | [manifest file](https://ru-open-stt.ams3.digitaloceanspaces.com/radio_pspeech_sample_manifest.csv) |
| audiobook_2                           | 162  | 21.0          | [mp3+txt](https://ru-open-stt.ams3.digitaloceanspaces.com/private_buriy_audiobooks_2_mp3.tar.gz) | Sources from the Internet + alignment | [manifest file](https://ru-open-stt.ams3.digitaloceanspaces.com/private_buriy_audiobooks_2.csv) |
| radio_2                               | 154  | 25.7          | [mp3+txt](https://ru-open-stt.ams3.digitaloceanspaces.com/radio_2_mp3.tar.gz) | Radio | [manifest file](https://ru-open-stt.ams3.digitaloceanspaces.com/radio_2.csv) |
| public_youtube1120                               | 237  | 32.4   | [mp3+txt](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube1120_mp3.tar.gz) | YouTube videos | [manifest file](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube1120.csv) |
| asr_public_phone_calls_2              | 66   | 7.5           | [mp3+txt](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_phone_calls_2_mp3.tar.gz) | Sources from the Internet + ASR | [manifest file](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_phone_calls_2.csv) |
| public_youtube1120_hq                               | 31  | 8.6          | [mp3+txt](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube1120_hq_mp3.tar.gz) | YouTube videos | [manifest file](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube1120_hq.csv) |
| asr_public_stories_2                  | 9   | 1.1              | [mp3+txt](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_stories_2_mp3.tar.gz)  | Sources from the Internet + alignment | [manifest file](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_stories_2.csv) |
| tts_russian_addresses_rhvoice_4voices | 80.9 | 9.9           | [mp3+txt](https://ru-open-stt.ams3.digitaloceanspaces.com/tts_russian_addresses_rhvoice_4voices_mp3.tar.gz) | TTS | [manifest file](https://ru-open-stt.ams3.digitaloceanspaces.com/tts_russian_addresses_rhvoice_4voices.csv) |
| public_youtube700                     | 75.0 | 9.6           | [mp3+txt](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube700_mp3.tar.gz)   | YouTube videos | [manifest file](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube700.csv) |
| asr_public_phone_calls_1              | 22.7 | 2.6           | [mp3+txt](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_phone_calls_1_mp3.tar.gz)    | Sources from the Internet + ASR | [manifest file](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_phone_calls_1.csv) |
| asr_public_stories_1                  | 4.1  | 0.5            | [mp3+txt](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_stories_1_mp3.tar.gz)    | Public stories | [manifest file](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_stories_1.csv) |
| public_series_1                       | 1.9  | 0.2            |  [mp3+txt](https://ru-open-stt.ams3.digitaloceanspaces.com/public_series_1_mp3.tar.gz)    | Public series | [manifest file](https://ru-open-stt.ams3.digitaloceanspaces.com/public_series_1.csv) |
| asr_calls_2_val                      | 2  | 0.2            | [mp3+txt](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_calls_2_val_mp3.tar.gz)    | Sources from the Internet  | [manifest file](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_calls_2_val.csv) |
| public_lecture_1                      | 0.7  | 0.1            | [mp3+txt](https://ru-open-stt.ams3.digitaloceanspaces.com/public_lecture_1_mp3.tar.gz)    | Sources from the Internet + manual  | [manifest file](https://ru-open-stt.ams3.digitaloceanspaces.com/public_lecture_1.csv) |
| buriy_audiobooks_2_val                      | 1  | 0.15            | [mp3+txt](https://ru-open-stt.ams3.digitaloceanspaces.com/buriy_audiobooks_2_val_mp3.tar.gz)    | Books + manual | [manifest file](https://ru-open-stt.ams3.digitaloceanspaces.com/buriy_audiobooks_2_val.csv) |
| public_youtube700_val                      | 2  | 0.13            | [mp3+txt](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube700_val_mp3.tar.gz)    | YouTube videos + manual  | [manifest file](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube700_val.csv) |
| Total                                 | 2,186  | 391            |      | | | |

## **Download instructions**

### End to end

`download.sh` 
or 
`download.py` with this config [file](https://github.com/snakers4/open_stt/blob/master/md5sum.lst). Please check the config first.

### Manually

1. Download each dataset separately:

  Via `wget`
  ```
  wget https://ru-open-stt.ams3.digitaloceanspaces.com/some_file
  ```

  For multi-threaded downloads use aria2 with `-x` flag, i.e.
  ```
  aria2c -c -x5 https://ru-open-stt.ams3.digitaloceanspaces.com/some_file
  ```

  If necessary, merge chunks like this:
  ```
  cat ru_open_stt_v01.tar.gz_* > ru_open_stt_v01.tar.gz
  ```

2. Download the meta data and manifests for each dataset:
3. Merge files (where applicable), unpack and enjoy!

# **Annotation methodology**

The dataset is compiled using open domain sources.
Some audio types are annotated automatically and verified statistically / using heuristics.

# **Audio normalization**

All files are normalized for easier / faster runtime augmentations and processing as follows:
- Converted to mono, if necessary;
- Converted to 16 kHz sampling rate, if necessary;
- Stored as 16-bit integers;

# **On disk DB methodology**

Each audio file is hashed.
Its hash is used to create a folder hierarchy for more optimal fs operation.

```
target_format = 'wav'
wavb = wav.tobytes()

f_hash = hashlib.sha1(wavb).hexdigest()

store_path = Path(root_folder,
                  f_hash[0],
                  f_hash[1:3],
                  f_hash[3:15]+'.'+target_format)
```

# **Helper functions**

Use helper functions from here for easier work with manifest files.

#### **Read manifests**

<details><summary>See example</summary>
<p>

```python
from utils.open_stt_utils import read_manifest

manifest_df = read_manifest('path/to/manifest.csv')
```

</p>
</details>

#### **Merge, check and save manifests**

<details><summary>See example</summary>
<p>

```python
from utils.open_stt_utils import (plain_merge_manifests,
                                  check_files,
                                  save_manifest)
train_manifests = [
 'path/to/manifest1.csv',
 'path/to/manifest2.csv',
]
train_manifest = plain_merge_manifests(train_manifests,
                                        MIN_DURATION=0.1,
                                        MAX_DURATION=100)
check_files(train_manifest)
save_manifest(train_manifest,
             'my_manifest.csv')
```

</p>
</details>

# **Contacts**

Please contact us [here](mailto:open_stt@googlegroups.com) or just create a GitHub issue!

**Authors (in alphabetic order):**

- Anna Slizhikova;
- Alexander Veysov;
- Diliara Nurtdinova;
- Dmitry Voronin;
- Yuri Baburov;

# **Acknowledgements**

This repo would not be possible without these people:
- Many thanks for helping to encode the initial bulk of the data into mp3 to [akreal](https://nuget.pkg.github.com/akreal);
- 18 hours of ground truth annotation datasets for validation are a courtesy of [activebc](https://activebc.ru/);

Kudos!

# **FAQ**

## **0. ~~Why not MP3?~~ MP3 encoding / decoding**

#### **Encoding**

Mostly we used `pydub` (via ffmpeg) or `sox` (much much faster way) to convert to MP3.
We omitted blank files (YouTube mostly).
We used the following parameters:
- 16kHz;
- 32 kbps;
- Mono;

Usually 128-192 kbps is enough for music with sr of 44 kHz, 64-96 is enough for speech.
But here we have mono, 16 kHz and usually only one speaker. So 32 kbps was a good choice.
We did not use other formats like `.ogg`, because `.mp3` is much more popular.

<details><summary>See example `pydub`</summary>
<p>

```python
from pydub import AudioSegment

sound = AudioSegment.from_file(temp_path,
                               format="wav")

file_handle = sound.export(store_mp3_path,
                           format="mp3",
                           parameters =["-ar", "{}".format(str(16000)),"-ac", "1"],
                           bitrate="{}k".format(str(32)))
```

</p>
</details>
<details><summary>See example `sox`</summary>
<p>

```python
import subprocess
cmd = 'sox "{}" -C 32.01 -c 1 "{}"'.format(
            wav_path,
            store_mp3_path)
    
res = subprocess.call([cmd], shell=True)

if res != 0:
    print('Problems with {}'.format(wav_path))
```

</p>
</details>


#### **Decoding**

It is up to you, but to save space and spare CPU during training, I would suggest the following pipeline to extract the files:

<details><summary>See example</summary>
<p>

```python
# you can also use pydub, torchaudio, sox or whatever
# we ended up using scipy for speed
# this example also includes hashing step which is not necessary
import librosa
import hashlib
import numpy as np
from pathlib import Path
from scipy.io import wavfile

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

root_folder = '../data/'
# save to int16, mono, 16 kHz to save space
target_dtype = np.dtype('int16')
target_sr = 16000
# librosa reads mp3
wav, sr = librosa.load(source_mp3_path,
                       mono=True,
                       sr=target_sr)

# librosa converts to float32 by default
wav = (wav * 32767).astype(target_dtype) # cast to int

wav_path = save_wav_diskdb(wav,
                           root_folder=root_folder,
                           target_sr=target_sr)
```

</p>
</details>

#### **Why not OGG/ Opus**

Even though OGG / Opus is considered to be better for speech with higher compression, we opted for a more conventional well known format.

Also LPC net codec boasts ultra-low bitrate speech compression as well. But we decided to opt for a more familiar format to avoid worry about actually losing signal in compression.

## **1. Issues with reading files**

#### **Maybe try this approach:**

<details><summary>See example</summary>
<p>

```python
from scipy.io import wavfile

sample_rate, sound = wavfile.read(path)

abs_max = np.abs(sound).max()
sound = sound.astype('float32')
if abs_max>0:
    sound *= 1/abs_max
```

</p>
</details>

## **2. Why share such dataset?**

We are not altruists,  life just is **not a zero sum game**.

Consider the progress in computer vision, that was made possible by:
- Public datasets;
- Public pre-trained models;
- Open source frameworks;
- Open research;

TTS does not enjoy the same attention by ML community because it is data hungry and public datasets are lacking, especially for languages other than English.
Ultimately it leads to worse-off situation for the general community.

## **3. Known issues with the dataset to be fixed**

- Speaker labels coming soon;
- Validation sets for new domains: Radio/Public Speech will be added in next releases.

# **License**

![сс-nc-by-license](https://static.wixstatic.com/media/342407_05e016f9f44240429203c35dfc8df63b~mv2.png/v1/fill/w_563,h_200,al_c,lg_1,q_80/342407_05e016f9f44240429203c35dfc8df63b~mv2.webp)

Сc-by-nc and commercial usage available after agreement with dataset authors.

# **Donations**

[Donate](https://buymeacoff.ee/8oneCIN) (each coffee pays for several full downloads) or via [open_collective](https://opencollective.com/open_stt) or just use our DO referral [link](https://sohabr.net/habr/post/357748/) to help.
