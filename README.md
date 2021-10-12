# Quotes generator

## Usage

### Get dataset(if you need to):
TODO: remove

Write your vk api token to VK_TOKEN file. Then execute

```bash
python3 get_dataset.py > dataset
```

### Train model(if you need to):

```bash
./main.py train -d dataset.txt -m model.json
```

### Generate quotes:

```bash
./main.py generate -m model.json
```

## Datasets
Patsanskie quotes generator with N-Gram model. Dataset was collected from the following groups in vk:

- [Пацанские цитаты©](https://vk.com/public27456813)
- [Пацанские цитаты №1](https://vk.com/krutiecitati)
- [пацанские цитаты и попуги](https://vk.com/tupopopugai) (more from this)

Vanilla quotes were collected from
- [Самые ванильные цитаты (500 цитат)](https://citatnica.ru/citaty/samye-vanilnye-tsitaty-500-tsitat)

