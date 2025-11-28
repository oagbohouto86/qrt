from pathlib import Path

root = Path(__file__).resolve().parents[1]
raw_data_path = root / "data" / "raw"
models_path = root / "models" # save ml models
submission_path = root / "submission"