# **Russian Open Speech To Text (STT/ASR) Dataset**

Arguably the largest public Russian STT dataset up to date:
- ~7m utterances (1-2m with less perfect annotation);
- ~7000 hours;
- 855 GB (in `.wav` format in `int16`);
- (**new!**) A new domain - radio;
- (**new!**) A larger YouTube dataset with 1000+ additional hours;
- (**new!**) A small (300 hours) YouTube dataset downloaded in maximum quality;
- (**new!**) Small validation sets for YouTube / books / public calls manually annotated;


Prove [us](mailto:open_stt@googlegroups.com) wrong!
Open issues, collaborate, submit a PR, contribute, share your datasets!
Let's make STT in Russian (and more) as open and available as CV models.

**Planned releases:**
- 1000-10,000 additional hours of books;
- Data quality distillation and improvement / annotation improvement;
- EVEN MOAR DATA (give us your ideas where to find it!);
- ~~1000+ additional hours of YouTube~~;
- ~~Some validation / test sets~~;
- ~~Plain benchmarks, "bad files"~~;
- ~~Mp3 torrent~~;
- ~~Wav torrent~~;
- ~~Radio set~~
- ... and more!;

**Table of contents**
  - [Dataset composition](https://github.com/snakers4/open_stt/#dataset-composition)
  - [Downloads](https://github.com/snakers4/open_stt/#downloads)
    - [Via torrent](https://github.com/snakers4/open_stt/#via-torrent)
    - [Links](https://github.com/snakers4/open_stt/#links)
    - [Download-instructions](https://github.com/snakers4/open_stt/#download-instructions)
    - [Check md5sum](https://github.com/snakers4/open_stt/#check-md5sum)
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
| audiobook_2               | 1,149,404  | 1,511 | 162 | 4.7s / 56  | Books            | Alignment (*)| 95%  / crisp  |
| radio_2                   |   651,645  | 1,439 | 154 | 7.95s / 110 | Radio            | Alignment (*)|  TBC, should be high            |
| public_youtube1120        |  1,410,979 | 1,104 | 237 | 2.82s / 34 | Yutube videos    | Subtitles   | 95%  / ~crisp |
| public_youtube700         |   759,483  |   701 |  75 | 3.3s / 43  | Youtube videos   | Subtitles   | 95%  / ~crisp |
| tts_russian_addresses     | 1,741,838  |   754 |  81 | 1.6s / 20  | Russian addresses| TTS 4 voices| 100% / crisp  |
| asr_public_phone_calls_2  |   603,797  |   601 |  66 | 3.6s / 37  | Phone calls      | ASR         | 70%  / noisy  |
| public_youtube1120_hq     |   369,245  |   291 |  31 | 2.84s / 37 | YouTube videos HQ sound | Subtitles   | 95%  / ~crisp |
| asr_public_phone_calls_1  |   233,868  |   211 |  23 | 3.3s / 29  | Phone calls      | ASR         | 70%  / noisy  |
| asr_public_stories_2      |    78,186  |    78 |   9 | 3.5s / 43  | Books            | ASR         | 80%  / crisp  |
| asr_public_stories_1      |    46,142  |    38 |   4 | 3.0s / 30  | Books            | ASR         | 80%  / crisp  |
| public_series_1           |    20,243  |    17 |   2 | 3.1s / 38  | Youtube videos   | Subtitles   | 95%  / ~crisp |
| ru_RU                     |     5,826  |    17 |   2 | 11s  / 12  | Public dataset   | Alignment   | 99%  / crisp  |
| voxforge_ru               |     8,344  |    17 |   2 | 7.5s / 77  | Public dataset   | Reading     | 100% / crisp  |
| russian_single            |     3,357  |     9 |   1 | 9.3s / 102 | Public dataset   | Alignment   | 99%  / crisp  |
| asr_calls_2_val           |     12,950 |   7,7 |   2 | 2.15s / 34 | Phone calls      | Manual annotation | 99%  / crisp |
| public_lecture_1          |     6,803  |     6 |   1 | 3.4s / 47  | Lectures         | Subtitles   | 95%  / crisp  |
| buriy_audiobooks_2_val    |     7,850  |   4,9 |   1 | 2.25s / 31 | Books            | Manual annotation | 99%  / crisp |
| public_youtube700_val     |     7,311  |   4,5 |   1 | 2.2 / 35   | Youtube videos   | Manual annotation | 99%  / crisp |
| Total                     | 7,117,271‬  | 6,812 | 855 |            |                  |             |               |

**(*) Automatic alignment**

This alignment was performed using Yuri's alignment tool.
[Contact him](mailto:open_stt@googlegroups.com) if you need alignment for your own dataset.

# **Updates**



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

<details>
  <summary>Click to expand</summary>

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
- An **MP3** [version](http://academictorrents.com/details/4a2656878dc819354ba59cd29b1c01182ca0e162) of the dataset (v3), to be deprecated;
- A **WAV** [version](http://academictorrents.com/details/a12a08b39cf3626407e10e01126cf27c198446c2) of the dataset (v5);

You can download separate files via torrent.
Try several torrent clients if some do not work.

## **Links**

Meta data [file](https://ru-open-stt.ams3.digitaloceanspaces.com/public_meta_data_v04_fx.csv).

| Dataset                               | GB, wav | GB, mp3 | Wav   | Mp3 |  Source | Manifest  |
|---------------------------------------|------|----------------|-------|-----|  -------| ----------|
| audiobook_2                           | 162  | 21.0          | [torrent](http://academictorrents.com/details/a12a08b39cf3626407e10e01126cf27c198446c2)  | [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/private_buriy_audiobooks_2_mp3.tar.gz) | Sources from the Internet + alignment | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/private_buriy_audiobooks_2.csv) |
| radio_2                               | 154  | 25.7          | [torrent](http://academictorrents.com/details/a12a08b39cf3626407e10e01126cf27c198446c2)  | [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/radio_2_mp3.tar.gz) | Radio | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/radio_2.csv) |
| public_youtube1120                               | 237  | 32.4          | [torrent](http://academictorrents.com/details/a12a08b39cf3626407e10e01126cf27c198446c2)  | [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube1120_mp3.tar.gz) | YouTube videos | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube1120.csv) |
| asr_public_phone_calls_2              | 66   | 7.5           | [torrent](http://academictorrents.com/details/a12a08b39cf3626407e10e01126cf27c198446c2)  | [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_phone_calls_2_mp3.tar.gz) | Sources from the Internet + ASR | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_phone_calls_2.csv) |
| public_youtube1120_hq                               | 31  | 8.6          | [torrent](http://academictorrents.com/details/a12a08b39cf3626407e10e01126cf27c198446c2)  | [parе1](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube1120_hq_mp3.tar.gz) | YouTube videos | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube1120_hq.csv) |
| asr_public_stories_2                  | 9   | 1.1              | [torrent](http://academictorrents.com/details/a12a08b39cf3626407e10e01126cf27c198446c2)   | [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_stories_2_mp3.tar.gz)  | Sources from the Internet + alignment | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_stories_2.csv) |
| tts_russian_addresses_rhvoice_4voices | 80.9 | 9.9           | [torrent](http://academictorrents.com/details/a12a08b39cf3626407e10e01126cf27c198446c2)  | [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/tts_russian_addresses_rhvoice_4voices_mp3.tar.gz) | TTS | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/tts_russian_addresses_rhvoice_4voices.csv) |
| public_youtube700                     | 75.0 | 9.6           | [torrent](http://academictorrents.com/details/a12a08b39cf3626407e10e01126cf27c198446c2)  | [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube700_mp3.tar.gz)   | YouTube videos | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube700.csv) |
| asr_public_phone_calls_1              | 22.7 | 2.6           | [torrent](http://academictorrents.com/details/a12a08b39cf3626407e10e01126cf27c198446c2)  | [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_phone_calls_1_mp3.tar.gz)    | Sources from the Internet + ASR | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_phone_calls_1.csv) |
| asr_public_stories_1                  | 4.1  | 0.5            | [torrent](http://academictorrents.com/details/a12a08b39cf3626407e10e01126cf27c198446c2)  | [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_stories_1_mp3.tar.gz)    | Public stories | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_public_stories_1.csv) |
| public_series_1                       | 1.9  | 0.2            | [torrent](http://academictorrents.com/details/a12a08b39cf3626407e10e01126cf27c198446c2)  |  [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/public_series_1_mp3.tar.gz)    | Public series | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/public_series_1.csv) |
| ru_RU                                 | 1.9  | 0.2            | [torrent](http://academictorrents.com/details/a12a08b39cf3626407e10e01126cf27c198446c2)  |   [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/ru_ru_mp3.tar.gz)    | Caito.de [dataset](https://www.caito.de/data/Training/stt_tts/) | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/ru_RU.csv) |
| voxforge_ru                           | 1.9  | 0.2            | [torrent](http://academictorrents.com/details/a12a08b39cf3626407e10e01126cf27c198446c2)  |  [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/voxforge_ru_mp3.tar.gz)    | Voxforge  [dataset](https://www.repository.voxforge1.org/downloads/) | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/voxforge_ru.csv) |
| russian_single                        | 0.9  | 0.1            | [torrent](http://academictorrents.com/details/a12a08b39cf3626407e10e01126cf27c198446c2)  |  [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/russian_single_mp3.tar.gz)    | Russian single speaker [dataset](https://www.kaggle.com/bryanpark/russian-single-speaker-speech-dataset) | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/russian_single.csv) |
| asr_calls_2_val                      | 2  | 0.2            | [torrent](http://academictorrents.com/details/a12a08b39cf3626407e10e01126cf27c198446c2)  |  [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_calls_2_val_mp3.tar.gz)    | Sources from the Internet  | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/asr_calls_2_val.csv) |
| public_lecture_1                      | 0.7  | 0.1            | [torrent](http://academictorrents.com/details/a12a08b39cf3626407e10e01126cf27c198446c2)  |  [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/public_lecture_1_mp3.tar.gz)    | Sources from the Internet + manual  | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/public_lecture_1.csv) |
| buriy_audiobooks_2_val                      | 1  | 0.15            | [torrent](http://academictorrents.com/details/a12a08b39cf3626407e10e01126cf27c198446c2)  |  [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/buriy_audiobooks_2_val_mp3.tar.gz)    | Books + manual | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/buriy_audiobooks_2_val.csv) |
| public_youtube700_val                      | 2  | 0.13            | [torrent](http://academictorrents.com/details/a12a08b39cf3626407e10e01126cf27c198446c2)  |  [part1](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube700_val_mp3.tar.gz)    | YouTube videos + manual  | [link](https://ru-open-stt.ams3.digitaloceanspaces.com/public_youtube700_val.csv) |
| Total                                 | 855  | 87.5            |      | | | |



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

Including links to deprecated files.
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
      <td>audio</td>
      <td>f24e21c69c03062d667caf0f055244f2</td>
      <td>asr_public_stories_2_mp3.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>a6f888c53d7cbded85ab51627ef57c96</td>
      <td>asr_public_phone_calls_1_mp3.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>f707e34f488c62af2e3142085ff595ad</td>
      <td>asr_public_phone_calls_2_mp3.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>baa491ed0b526b2a989b8c4a8897429d</td>
      <td>asr_public_stories_1_mp3.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>42b9c8c2e31100d6c5b972c9ac000167</td>
      <td>private_buriy_audiobooks_2_mp3.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>7a5704721012fafa115e7316e5f6e058</td>
      <td>public_lecture_1_mp3.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>16cf820330f9f8b388395d777b2331ac</td>
      <td>public_series_1_mp3.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>dd048e7110c0c852c353759dad8fec0f</td>
      <td>public_youtube700_mp3.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>579e9d98bd159a27d3573641edee69b0</td>
      <td>ru_ru_mp3.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>177b041594684623ec7d038613e1330d</td>
      <td>russian_single_mp3.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>d7ce4c4116dcc655be2b466f82c98b6e</td>
      <td>tts_russian_addresses_rhvoice_4voices_mp3.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>25ea6d9e249a242ecc217acc28c8077b</td>
      <td>voxforge_ru_mp3.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>97cd6b56ba1eb5088bc5643dce054028</td>
      <td>asr_calls_2_val_mp3.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>69a465e218fc1f597f7b5da836952d9d</td>
      <td>radio_2_mp3.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>0cc0f50db85ec4271696b4eb03a2203c</td>
      <td>buriy_audiobooks_2_val_mp3.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>f5d2e3d13b47e1566ba0b021f00788cf</td>
      <td>public_youtube1120_hq_mp3.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>12eb78a9ab7c3d39bbe2842b8d6550ca</td>
      <td>public_youtube1120_mp3.tar.gz</td>
    </tr>
    <tr>
      <td>audio</td>
      <td>f6b6034e1e91d9a0a5069fc9ad2ed545</td>
      <td>public_youtube700_val_mp3.tar.gz</td>
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
      <td>7533581bb26975212817bcacb25546d0</td>
      <td>asr_public_stories_2.tar.gz</td>
    </tr>
    <tr>
      <td>manifest</td>
      <td>0cdbd085ffa6dab4bfdce7c3ed31fcfe</td>
      <td>asr_calls_2_val.csv</td>
    </tr>
    <tr>
      <td>manifest</td>
      <td>4e0b73e0d00374482a0f2286acf314a0</td>
      <td>buriy_audiobooks_2_val.csv</td>
    </tr>
    <tr>
      <td>manifest</td>
      <td>6b9ce6828a55d2741d51bc3503345db5</td>
      <td>public_youtube1120.csv</td>
    </tr>
    <tr>
      <td>manifest</td>
      <td>33040a25cad99e70a81e9e54ff8c758e</td>
      <td>public_youtube1120_hq.csv</td>
    </tr>
    <tr>
      <td>manifest</td>
      <td>525bd20802e529dcabf9e44345a50d0b</td>
      <td>public_youtube700_val.csv</td>
    </tr>
    <tr>
      <td>manifest</td>
      <td>2996fe938cdfb37dc6e359e4384c9bfe</td>
      <td>radio_2.csv</td>
    </tr>
  </table>
</details>


## **End to end download scripts**

You can use this [script](https://github.com/snakers4/open_stt/blob/master/download.sh) or this [script](https://github.com/snakers4/open_stt/blob/master/download.py) with this config [file](https://github.com/snakers4/open_stt/blob/master/md5sum.lst).
Please check the config first.
You can also [contribute](https://github.com/snakers4/open_stt/issues/2) a similar script in python.

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

# **Acknowledgements**

This repo would not be possible without these people:
- Many thanks for helping to encode the initial bulk of the data into mp3 to [akreal](https://nuget.pkg.github.com/akreal);
- Small validation sets are a courtesy of [activebc](https://activebc.ru/);

Kudos!

# **FAQ**

## **0. ~~Why not MP3?~~ MP3 encoding / decoding**

#### **Encoding**

Mostly we used `pydub` (via ffmpeg) to convert to MP3.
We omitted blank files (YouTube mostly).
We used the following parameters:
- 16kHz;
- 32 kbps;
- Mono;

Usually 128-192 kbps is enough for music with sr of 44 kHz, 64-96 is enough for speech.
But here we have mono, 16 kHz and usually only one speaker. So 32 kbps was a good choice.
We did not use other formats like `.ogg`, because `.mp3` is much more popular.

<details><summary>See example</summary>
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

#### **Why not OGG**

Even though OGG is considered to be better for speech with higher compression, we opted for a more conventional well known format.

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
- ~~Blank files in Youtube dataset~~. Removed in mp3 archive. Meta-data not cleaned;
- Some files that have low values / crash with tochaudio;
- Looks like scipy does not always write meta-data when saving wavs (or you should save (N,1) shaped file) - this can be fixed as shown above;

# **License**
License:
- cc-by-nc and commercial usage available after agreement with dataset authors;
- Except for radio_2, which is public domain;
- Except for VoxForge, its license is GNU GPL 3.0;
- Except for Caito.de dataset, its licence is [here](https://www.caito.de/data/Training/LICENSE.txt).

# **Donations**

[Donate](https://buymeacoff.ee/8oneCIN) (each coffee pays for several full downloads) / use our DO referral [link](https://sohabr.net/habr/post/357748/) to help.
