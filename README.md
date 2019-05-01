# **Russian Open Speech To Text (STT/ASR) Dataset**

Arguably the largest public Russian STT dataset up to date:
- ~4.6m utterances;
- ~4000 hours;
- 431 GB;
- Additional 1,500 hours ... and more ... to be released soon!;
- And then maybe even more hours to be released!;


Prove [us](mailto:open_stt@googlegroups.com) wrong!
Open issues, collaborate, submit a PR, contribute, share your datasets!
Let's make STT in Russian (and more) as open and available as CV models.

**Table of contents**
  - [Dataset composition](https://github.com/snakers4/open_stt/#dataset-composition)
  - [Downloads](https://github.com/snakers4/open_stt/#downloads)
    - [Links](https://github.com/snakers4/open_stt/#links)
    - [Download-instructions](https://github.com/snakers4/open_stt/#download-instructions)
    - [Check md5sum](https://github.com/snakers4/open_stt/#check-md5sum)
  - [Annotation methodology](https://github.com/snakers4/open_stt/#annotation-methodology)
  - [Audio normalization](https://github.com/snakers4/open_stt/#audio-normalization)
  - [Disk db methodology](https://github.com/snakers4/open_stt/#on-disk-db-methodology)
  - [Helper functions](https://github.com/snakers4/open_stt/#helper-functions)
  - [Contacts](https://github.com/snakers4/open_stt/#contacts)
  - [FAQ](https://github.com/snakers4/open_stt/#faq)
  - [License](https://github.com/snakers4/open_stt/#license)

# **Dataset composition**

| Dataset                   | Utterances | Hours | GB  | Av s/chars | Comment          | Annotation  | Quality/noise |
|---------------------------|------------|-------|-----|------------|------------------|-------------|---------------|
| public_youtube1500 (*)    |            | 1,500 |     |            | * Coming soon    |             |               |
| audiobook_2               | 1,149,404  | 1,511 | 166 | 4.7s / 56  | Books            | Alignment (*)| 95%  / crisp  |
| public_youtube700         |   759,483  |   701 |  75 | 3.3s / 43  | Youtube videos   | Subtitles   | 95%  / ~crisp |
| tts_russian_addresses     | 1,741,838  |   754 |  81 | 1.6s / 20  | Russian addresses| TTS 4 voices| 100% / crisp  |
| asr_public_phone_calls_2  |   603,797  |   601 |  66 | 3.6s / 37  | Phone calls      | ASR         | 70%  / noisy  |
| asr_public_phone_calls_1  |   233,868  |   211 |  23 | 3.3s / 29  | Phone calls      | ASR         | 70%  / noisy  |
| asr_public_stories_2      |    78,186  |    78 |   9 | 3.5s / 43  | Books            | ASR         | 80%  / crisp  |
| asr_public_stories_1      |    46,142  |    38 |   4 | 3.0s / 30  | Books            | ASR         | 80%  / crisp  |
| public_series_1           |    20,243  |    17 |   2 | 3.1s / 38  | Youtube videos   | Subtitles   | 95%  / ~crisp |
| ru_RU                     |     5,826  |    17 |   2 | 11s  / 12  | Public dataset   | Alignment   | 99%  / crisp  |
| voxforge_ru               |     8,344  |    17 |   2 | 7.5s / 77  | Public dataset   | Reading     | 100% / crisp  |
| russian_single            |     3,357  |     9 |   1 | 9.3s / 102 | Public dataset   | Alignment   | 99%  / crisp  |
| public_lecture_1          |     6,803  |     6 |   1 | 3.4s / 47  | Lectures         | Subtitles   | 95%  / crisp  |
| Total                     | 4,657,291  | 3,961 | 431 |            |                  |             |               |

**(*) Automatic alignment**

This alignment was performed using Yuri's alignment tool.
[Contact him](mailto:open_stt@googlegroups.com) if you need alignment for your own dataset.

# **Downloads**

## **Links**

Meta data [file](https://ru-open-stt.ams3.digitaloceanspaces.com/public_meta_data_v03.csv).


| Dataset                               | GB   | GB, compressed | Audio |  Source | Manifest  |
|---------------------------------------|------|----------------|-------|  -------| ----------|
| audiobook_2                           | 166  | 131.7          |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/audiobooks_2.tar.gz_aa), [part2](https://ru-open-stt.ams3.digitaloceanspaces.com/audiobooks_2.tar.gz_ab), [part3](https://ru-open-stt.ams3.digitaloceanspaces.com/audiobooks_2.tar.gz_ac), [part4](https://ru-open-stt.ams3.digitaloceanspaces.com/audiobooks_2.tar.gz_ad), [part5](https://ru-open-stt.ams3.digitaloceanspaces.com/audiobooks_2.tar.gz_ae), [part6](https://ru-open-stt.ams3.digitaloceanspaces.com/audiobooks_2.tar.gz_af), [part7](https://ru-open-stt.ams3.digitaloceanspaces.com/audiobooks_2.tar.gz_ag)    | Sources from the Internet + alignment | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/private_buriy_audiobooks_2.csv) |
| asr_public_phone_calls_2              | 66   | 51.7          |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_phone_calls_2.tar.gz_aa), [part2](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_phone_calls_2.tar.gz_ab), [part3](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_phone_calls_2.tar.gz_ac)  | Sources from the Internet + ASR | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_phone_calls_2.csv) |
| asr_public_stories_2                           | 9  | 7.5          |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_stories_2.tar.gz)  | Sources from the Internet + alignment | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_stories_2.csv) |
| tts_russian_addresses_rhvoice_4voices | 80.9 | 67.0           |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/tts_russian_addresses_rhvoice_4voices.tar.gz_aa), [part2](https://ru-open-stt.ams3.digitaloceanspaces.com/tts_russian_addresses_rhvoice_4voices.tar.gz_ab), [part3](https://ru-open-stt.ams3.digitaloceanspaces.com/tts_russian_addresses_rhvoice_4voices.tar.gz_ac), [part4](https://ru-open-stt.ams3.digitaloceanspaces.com/tts_russian_addresses_rhvoice_4voices.tar.gz_ad)     | TTS | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/tts_russian_addresses_rhvoice_4voices.csv) |
| public_youtube700                     | 75.0 | 67.0           |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube700.tar.gz_aa), [part2](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube700.tar.gz_ab), [part3](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube700.tar.gz_ac), [part4](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube700.tar.gz_ad)    | YouTube videos | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube700.csv) |
| asr_public_phone_calls_1              | 22.7 | 19.0           |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_phone_calls_1.tar.gz)    | Sources from the Internet + ASR | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_phone_calls_1.csv) |
| asr_public_stories_1                  | 4.1  | 3.8            |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_stories_1.tar.gz)    | Public stories | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_stories_1.csv) |
| public_series_1                       | 1.9  | 1.7            |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/public_series_1.tar.gz)    | Public series | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/public_series_1.csv) |
| ru_RU                                 | 1.9  | 1.4            |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/ru_ru.tar.gz)    | Caito.de [dataset](https://www.caito.de/data/Training/stt_tts/) | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/ru_RU.csv) |
| voxforge_ru                           | 1.9  | 1.5            |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/voxforge_ru.tar.gz)    | Voxforge  [dataset](https://www.repository.voxforge1.org/downloads/) | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/voxforge_ru.csv) |
| russian_single                        | 0.9  | 0.7            |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/russian_single.tar.gz)    | Russian single speaker [dataset](https://www.kaggle.com/bryanpark/russian-single-speaker-speech-dataset) | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/russian_single.csv) |
| public_lecture_1                      | 0.7  | 0.6            |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/public_lecture_1.tar.gz)    | Sources from the Internet  | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/public_lecture_1.csv) |
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

## **Check md5sum**

`md5sum /path/to/downloaded/file`

<details>
  <summary>Click to expand</summary>
  <table>
    <tr>
      <th>type</th>
      <th>md5sum</th>
      <th>file</th>
    </tr>
    <tr>
      <td>manifest</td>
      <td>b0ce7564ba90b121aeb13aada73a6e30</td>
      <td>asr_public_phone_calls_1.csv</td>
    </tr>
    <tr>
      <td>manifest</td>
      <td>6867d14dfdec1f9e9b8ca2f1de9ceda6</td>
      <td>asr_public_phone_calls_2.csv</td>
    </tr>
    <tr>
      <td>manifest</td>
      <td>0bdd77e15172e654d9a1999a86e92c7f</td>
      <td>asr_public_stories_1.csv</td>
    </tr>
    <tr>
      <td>manifest</td>
      <td>f388013039d94dc36970547944db51c7</td>
      <td>asr_public_stories_2.csv</td>
    </tr>
    <tr>
      <td>manifest</td>
      <td>3b67e27c1429593cccbf7c516c4b582d</td>
      <td>private_buriy_audiobooks_2.csv</td>
    </tr>
    <tr>
      <td>manifest</td>
      <td>04027c20eb3aff05f6067957ecff856b</td>
      <td>public_lecture_1.csv</td>
    </tr>
    <tr>
      <td>manifest</td>
      <td>89da3f1b6afcd4d4936662ceabf3033e</td>
      <td>public_series_1.csv</td>
    </tr>
    <tr>
      <td>manifest</td>
      <td>a81dfb018c88d0ecd5194ab3d8ff6c95</td>
      <td>public_youtube700.csv</td>
    </tr>
    <tr>
      <td>manifest</td>
      <td>c858f020729c34ba0ab525bbb8950d0c</td>
      <td>ru_RU.csv</td>
    </tr>
    <tr>
      <td>manifest</td>
      <td>0275525914825dec663fd53390fdc9a0</td>
      <td>russian_single.csv</td>
    </tr>
    <tr>
      <td>manifest</td>
      <td>52f406f4e30fcc8c634f992befd91beb</td>
      <td>tts_russian_addresses_rhvoice_4voices.csv</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>a5496898ee78654bf398ec6df71540d7</td>
      <td>asr_public_phone_calls_1.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>e4df5ef50787384648b59f5a87edc0c6</td>
      <td>asr_public_phone_calls_2.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>97594127a922df8a7bcc2eecd2470805</td>
      <td>asr_public_phone_calls_2.tar.gz_aa</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>f9b6475f0f2898b16d9e6e0e648fb531</td>
      <td>asr_public_phone_calls_2.tar.gz_ab</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>b19977c889cda639f621195251e6bb6f</td>
      <td>asr_public_phone_calls_2.tar.gz_ac</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>657a31b544b10295f909ef4b2ca5c156</td>
      <td>asr_public_stories_1.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>7533581bb26975212817bcacb25546d0</td>
      <td>asr_public_stories_2.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>3955616cd89761bf2d54d0e992f7eae5</td>
      <td>audiobooks_2.tar.gz_aa</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>81b6ec147c0c43bdd56002c41e0288b8</td>
      <td>audiobooks_2.tar.gz_ab</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>15d4cf99171c2db3f375619f4bd2b6d9</td>
      <td>audiobooks_2.tar.gz_ac</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>50635b0f4bdf44fae96e5a65f4738e19</td>
      <td>audiobooks_2.tar.gz_ad</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>f1103be39ffc2da4a98d8f6ddeb50aa0</td>
      <td>audiobooks_2.tar.gz_ae</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>8b45d2bd8b1fa1d906e36b9fabd9fe4c</td>
      <td>audiobooks_2.tar.gz_af</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>5104df44933b612b3c1bfc06f6376654</td>
      <td>audiobooks_2.tar.gz_ag</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>e6b9e5f46811d33ea34ce50f6067a762</td>
      <td>public_lecture_1.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>86ebf7e30986b8ee8df11f85b35588a0</td>
      <td>public_series_1.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>dc260dd8151b4fce6cde6d80af13146d</td>
      <td>public_youtube700.tar.gz_aa</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>04706ef0f98841ec8d2f20a83aca3cf1</td>
      <td>public_youtube700.tar.gz_ab</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>e11d5b118bf71425e4915e61277a06a9</td>
      <td>public_youtube700.tar.gz_ac</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>d9a93157263eb9d8078c0e0b88c271de</td>
      <td>public_youtube700.tar.gz_ad</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>1bbba5eb2f4911c9ed20ec69cbd292cb</td>
      <td>ru_ru.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>6f79a9c514ad48a5763e3142919fc765</td>
      <td>russian_single.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>c926df1068218eb9cc8103c94003fcc6</td>
      <td>tts_russian_addresses_rhvoice_4voices.tar</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>31d515e0bdfc467c3fe63088b817c15c</td>
      <td>tts_russian_addresses_rhvoice_4voices.tar.gz_aa</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>4ca15694a8d8a638bbdc5e90832eadb4</td>
      <td>tts_russian_addresses_rhvoice_4voices.tar.gz_ab</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>447559a38cd8bf61c5de64e602f06da3</td>
      <td>tts_russian_addresses_rhvoice_4voices.tar.gz_ac</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>9131347a97c2e794d7c6d5a265083e83</td>
      <td>tts_russian_addresses_rhvoice_4voices.tar.gz_ad</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>91e2115b17b1ad08649f428d2caa643b</td>
      <td>voxforge_ru.tar.gz</td>
    </tr>
  </table>
</details>

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

**Authors in alphabetic order:**
- Anna Slizhikova;
- Alexander Veysov;
- Dmitry Voronin;
- Yuri Baburov;


# **FAQ**

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
- Blank files in Youtube dataset. Just filter them out using meta-data. Will be fixed in future;
- Some files that have low values / crash with tochaudio;
- Looks like scipy does not always write meta-data when saving wavs (or you should save (N,1) shaped file) - this can be fixed as shown above;

# **License**
Dual license, cc-by-nc and commercial usage available after agreement with dataset authors.
Except for VoxForge, its license is GNU GPL 3.0.
