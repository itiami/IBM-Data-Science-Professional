from flask import current_app
import os
import pandas as pd

def load_data(csv):
    assets_dir = current_app.config['ASSETS_DIR']
    csv_path = os.path.join(assets_dir, csv)
    df = pd.read_csv(csv_path)
    return df
