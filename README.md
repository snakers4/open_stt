# **Russian Open STT Dataset**

Arguably the largest public Russian STT dataset up to date:
- ~3m utterances;
- 1,771+ hours;
- 190GB;
- Additional 3,000 hours ... and more ... to be released soon!;


Prove [me](https://t.me/snakers41) wrong!
Open issues, collaborate, submit a PR, contribute, share your datasets!
Let's make STT in Russian (and more) as open and available as CV models.


# **Dataset composition**

| Dataset                       | Utterances | Hours | GB  | Av len | Av chars | Comment            | Annotation    | Quality/noise |
|-------------------------------|------------|-------|-----|------- |----------|--------------------|---------------|---------------|
| asr_public_phone_calls_2 (*)  |            | 1,500 |     |        |          | * Coming soon      |               |               |
| public_youtube1500 (*)        |            | 1,500 |     |        |          | * Coming soon      |               |               |
| tts_russian_addresses         | 1,741,838  | 754   | 81  | 1.6s   | 20       | Russian addresses  | TTS, 4 voices | 100% / crisp  |
| public_youtube700             | 759,483    | 701   | 75  | 3.3s   | 43       | Youtube videos     | Subtitles     | >95% / ~crisp |
| asr_public_phone_calls_1      | 233,868    | 211   | 23  | 3.3s   | 29       | Phone calls        | ASR           | 70%  / noisy  |
| asr_public_stories_1          | 46,142     | 38    | 4   | 3.0s   | 30       | Books              | ASR           | 70%  / crisp  |
| public_series_1               | 20,243     | 17    | 2   | 3.1s   | 38       | Youtube videos     | Subtitles     | 95%  / ~crisp |
| ru_RU                         | 5,826      | 17    | 2   | 10.8s  | 12       | Public STT dataset | Alignment     | 99%  / crisp  |
| voxforge_ru                   | 8,344      | 17    | 2   | 7.5s   | 77       | Public STT dataset | Reading       | 100% / crisp  |
| russian_single                | 3,357      | 9     | 1   | 9.3s   | 102      | Public STT dataset | Alignment     | 99%  / crisp  |
| public_lecture_1              | 6,803      | 6     | 1   | 3.4s   | 47       | Lectures           | Subtitles     | >95% / crisp  |
| Total                         | 2,825,904  | 1,771 | 190 |        |          |                    |               |               |

# **Downloads**

## **Links**

Meta data [file](https://ru-open-stt.ams3.digitaloceanspaces.com/public_meta_data_v02.csv).

| Dataset                               | GB   | GB, compressed | Audio |  Source | Manifest  |
|---------------------------------------|------|----------------|-------|  -------| ----------|
| tts_russian_addresses_rhvoice_4voices | 80.9 | 67.0           |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/tts_russian_addresses_rhvoice_4voices.tar.gz_ab), [part2](https://ru-open-stt.ams3.digitaloceanspaces.com/tts_russian_addresses_rhvoice_4voices.tar.gz_ab), [part3](https://ru-open-stt.ams3.digitaloceanspaces.com/tts_russian_addresses_rhvoice_4voices.tar.gz_ac), [part4](https://ru-open-stt.ams3.digitaloceanspaces.com/tts_russian_addresses_rhvoice_4voices.tar.gz_ad)     | TTS | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/tts_russian_addresses_rhvoice_4voices.csv) |
| public_youtube700                     | 75.0 | 67.0           |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube700.tar.gz_aa), [part2](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube700.tar.gz_ab), [part3](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube700.tar.gz_ac), [part4](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube700.tar.gz_ad)    | YouTube videos | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube700.csv) |
| asr_public_phone_calls_1              | 22.7 | 19.0           |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_phone_calls_1.tar.gz)    | ASR + public phone calls | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_phone_calls_1.csv) |
| asr_public_stories_1                  | 4.1  | 3.8            |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_stories_1.tar.gz)    | Public stories | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_stories_1.csv) |
| public_series_1                       | 1.9  | 1.7            |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/public_series_1.tar.gz)    | Public series | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/public_series_1.csv) |
| ru_RU                                 | 1.9  | 1.4            |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/ru_ru.tar.gz)    | Caito.de [dataset](https://www.caito.de/data/Training/stt_tts/) | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/ru_RU.csv) |
| voxforge_ru                           | 1.9  | 1.5            |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/voxforge_ru.tar.gz)    | Voxforge  [dataset](www.repository.voxforge1.org/downloads/) | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/voxforge_ru.csv) |
| russian_single                        | 0.9  | 0.7            |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/russian_single.tar.gz)    | Russian single speaker [dataset](https://www.kaggle.com/bryanpark/russian-single-speaker-speech-dataset) | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/russian_single.csv) |
| public_lecture_1                      | 0.7  | 0.6            |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/public_lecture_1.tar.gz)    | Public lectures | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/public_lecture_1.csv) |
| Total                                 | 190  | 163            |      | | | |


## **Download instructions**

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

Read manifests:
```
from utils.open_stt_utils import read_manifest

manifest_df = read_manifest('path/to/manifest.csv')
```

Merge, check and save manifests:
```
from utils.open_stt_utils import (plain_merge_manifests,
                                  check_files,
                                  save_manifest)

train_manifests = [
    'path/to/manifest1.csv',
    'path/to/manifest2.csv',
]

train_manifest  = plain_merge_manifests(train_manifests,
                                        MIN_DURATION=0.1,
                                        MAX_DURATION=100)
check_files(train_manifest)

save_manifest(train_manifest,
             'my_manifest.csv')
```

# **Contacts**

Please contact me [here](https://t.me/snakers41) or just create a GitHub issue!

# **FAQ**

## **1. Issues with reading files**

Maybe try this approach:
```
from scipy.io import wavfile

sample_rate, sound = wavfile.read(path)

abs_max = np.abs(sound).max()
sound = sound.astype('float32')
if abs_max>0:
    sound *= 1/abs_max
```
## **2. Why share such dataset?**

We are not altruists,  life just is **not a zero sum game**.

Consider the progress in computer vision, that was made possible by:
- Public datasets;
- Public pre-trained models;
- Open source frameworks;
- Open research;

TTS does not enjoy the same attention by ML community because it is data hungry and public datasets are lacking, especially for languages other than English.
Ultimately it leads to worse-off situation for the general community.
