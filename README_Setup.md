# Environment

In the WSL/Ubuntu environment: 

```bash
python -m venv .venv

source ./.venv/bin/activate
(.venv) pip install -r requirements.txt
(.venv) pip install 'git+https://github.com/facebookresearch/detectron2.git'
```

---

## Model

```bash
(.venv) wget -O model_final.pth "https://www.dropbox.com/s/xxxxx/model_final.pth?dl=1"

-> FAILED. Cannot get model file...
```

---
