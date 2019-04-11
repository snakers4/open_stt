# **Russian Open STT dataset**

Arguably the largest public Russian STT dataset up to date:
- 300k+ utterances;
- 300+ hours,
- 80GB;
- ~9k speaker sets;

Prove [me](https://t.me/snakers41) wrong!

## **Dataset composition**

| Type        | Utterances | Hours | GB   | Speaker sets | Characters | Mean length, seconds | Mean chars |
|-------------|------------|-------|------|--------------|------------|----------------------|------------|
| Lecture     | 6,803      | 6.3   | 1.9  | 29           | 316,953    | 3.36                 | 46.6       |
| Narration   | 67,052     | 80.3  | 27.5 | 584          | 3,075,827  | 4.31                 | 45.9       |
| Phone_calls | 233,868    | 211.2 | 45.9 | 8175         | 6,706,717  | 3.25                 | 28.7       |
| Series      | 20,243     | 17.5  | 5.2  | 51           | 759,433    | 3.10                 | 37.5       |
| Total         | 327,966    | 315   | 80   | 8,839        | 10,858,930 |                      |            |

## **Downloads**

1. Dowload the chunks:
```
wget https://ru-open-stt-v01.ams3.digitaloceanspaces.com/ru_open_stt_v01.tar.gz_aa
wget https://ru-open-stt-v01.ams3.digitaloceanspaces.com/ru_open_stt_v01.tar.gz_ab
wget https://ru-open-stt-v01.ams3.digitaloceanspaces.com/ru_open_stt_v01.tar.gz_ac
wget https://ru-open-stt-v01.ams3.digitaloceanspaces.com/ru_open_stt_v01.tar.gz_ad
wget https://ru-open-stt-v01.ams3.digitaloceanspaces.com/ru_open_stt_v01.tar.gz_ae
wget https://ru-open-stt-v01.ams3.digitaloceanspaces.com/ru_open_stt_v01.tar.gz_af
```

2. For multi-threaded downloads use aria2 with `-x` flag.

3. Put the chunks together:
`cat ru_open_stt_v01.tar.gz_* > ru_open_stt_v01.tar.gz`

4. Unpack

## **Methodology**

The dataset is compiled using open domain sources.
Some audio types are annotated automatically and verified statistically / using heuristics.


## **References**

We also used the following public datasets:
- Caito.de Russian [dataset](https://www.caito.de/data/Training/stt_tts/);
- Single speaker Kaggle [dataset](https://www.kaggle.com/bryanpark/russian-single-speaker-speech-dataset);

## **Contacts**

Please contact me [here](https://t.me/snakers41) or just create a github issue!
