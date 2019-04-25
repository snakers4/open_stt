# **Russian Open STT Dataset**

Arguably the largest public Russian STT dataset up to date:
- ~3m utterances;
- 1,771+ hours (additional 3,000 hours ... and more ... to be released soon!);
- 190GB;

Prove [me](https://t.me/snakers41) wrong!
Open issues, collaborate, contribute, share your datasets!
Let's make STT in Russian (and more) as open and available as CV models xD

# **Dataset composition**

| Dataset                       | Utterances | Hours | GB  | Av len | Av chars | Comment            | Annotation    | Quality | Noise        |
|-------------------------------|------------|-------|-----|------- |----------|--------------------|---------------|---------|--------------|
| asr_public_phone_calls_2 (*)  |            | 1,500 |     |        |          | * Coming soon      |               |         |              |
| public_youtube1500 (*)        |            | 1,500 |     |        |          | * Coming soon      |               |         |              |
| tts_russian_addresses         | 1,741,838  | 754   | 81  | 1.6s   | 20       | Russian addresses  | TTS, 4 voices | 100%    | Crisp        |
| public_youtube700             | 759,483    | 701   | 75  | 3.3s   | 43       | Youtube videos     | Subtitles     | >95%    | Mostly crisp |
| asr_public_phone_calls_1      | 233,868    | 211   | 23  | 3.3s   | 29       | Phone calls        | ASR           | 70%     | Noisy        |
| asr_public_stories_1          | 46,142     | 38    | 4   | 3.0s   | 30       | Books              | ASR           | 70%     | Crisp        |
| public_series_1               | 20,243     | 17    | 2   | 3.1s   | 38       | Youtube videos     | Subtitles     | 95%     | Mostly crisp |
| ru_RU                         | 5,826      | 17    | 2   | 10.8s  | 12       | Public STT dataset | Alignment     | 99%     | Crisp        |
| voxforge_ru                   | 8,344      | 17    | 2   | 7.5s   | 77       | Public STT dataset | Reading       | 100%    | Crisp        |
| russian_single                | 3,357      | 9     | 1   | 9.3s   | 102      | Public STT dataset | Alignment     | 99%     | Crisp        |
| public_lecture_1              | 6,803      | 6     | 1   | 3.4s   | 47       | Lectures           | Subtitles     | >95%    | Crisp        |
| Total                         | 2,825,904  | 1,771 | 190 |        |          |                    |               |         |              |

# **Downloads**

## **Links**

Meta data file.

| Dataset                               | GB   | GB, compressed | Audio |  Source | Manifest  |
|---------------------------------------|------|----------------|-------|  -------| ----------|
| tts_russian_addresses_rhvoice_4voices | 80.9 | 67.0           |   [part1](), [part2](), [part3](), [part4]()     | TTS | [link]() |
| public_youtube700                     | 75.0 | 67.0           |   [part1](), [part2](), [part3](), [part4]()    | YouTube videos | [link]() |
| asr_public_phone_calls_1              | 22.7 | 19.0           |   [part1]()    | ASR + public phone calls | [link]() |
| asr_public_stories_1                  | 4.1  | 3.8            |   [part1]()    | Public stories | [link]() |
| public_series_1                       | 1.9  | 1.7            |   [part1]()    | Public series | [link]() |
| ru_RU                                 | 1.9  | 1.4            |   [part1]()    | Caito.de [dataset](https://www.caito.de/data/Training/stt_tts/) | [link]() |
| voxforge_ru                           | 1.9  | 1.5            |   [part1]()    | Voxforge  [dataset](www.repository.voxforge1.org/downloads/) | [link]() |
| russian_single                        | 0.9  | 0.7            |   [part1]()    | Russian single speaker [dataset](https://www.kaggle.com/bryanpark/russian-single-speaker-speech-dataset) | [link]() |
| public_lecture_1                      | 0.7  | 0.6            |   [part1]()    | Public lectures | [link]() |
| Total                                 | 190  | 163            |   [part1]()    | | | |


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
