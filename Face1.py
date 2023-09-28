# Su dung deepface

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from deepface import DeepFace

obj = DeepFace.analyze(img_path="Images/Purin3.jpg", actions=["age", "gender", "emotion", "race"])

print(obj)