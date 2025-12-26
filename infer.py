# infer.py
import sys
import json
import layoutparser as lp
from PIL import Image

def run_inference(image_path: str):
    image = Image.open(image_path).convert("RGB")

    model = lp.Detectron2LayoutModel(
        model_path="./model_final.pth",     # downloaded in the current directory
        config_path="lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config",
        extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.5],
        label_map={
            0: "Text",
            1: "Title",
            2: "List",
            3: "Table",
            4: "Figure",
        },
        device="cpu",
    )

    layout = model.detect(image)

    result = []
    for block in layout:
        result.append({
            "type": block.type,
            "score": float(block.score),
            "x1": int(block.block.x_1),
            "y1": int(block.block.y_1),
            "x2": int(block.block.x_2),
            "y2": int(block.block.y_2),
        })

    print(json.dumps(result, ensure_ascii=False))

if __name__ == "__main__":
    # run_inference(sys.argv[1])
    run_inference("inputs/sample01.png")
