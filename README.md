# Quotes generator
Patsanskie quotes generator with N-Gram model

## Usage:

### Get dataset(if you need to):

Write your vk api token to VK_TOKEN file. Then execute

```bash
python3 get_dataset.py > dataset
```

### Train model(if you need to):

```bash
python3 main.py train
```

### Generate quotes:

```bash
python3 main.py generate
```
