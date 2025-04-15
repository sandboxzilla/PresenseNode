import os
import json
from PIL import Image
import numpy as np
import torch
from facenet_pytorch import InceptionResnetV1, MTCNN
from torchvision import transforms

# Paths
base_dir = "FaceRecognition"
output_file = "face_embeddings.json"

# Init face detector + embedding model
mtcnn = MTCNN(image_size=160, margin=14, post_process=True)
model = InceptionResnetV1(pretrained='vggface2').eval()

# Image transform
to_tensor = transforms.Compose([
    transforms.Resize((160, 160)),
    transforms.ToTensor()
])

embeddings = {}

# Walk through each person's folder
for person_name in os.listdir(base_dir):
    person_path = os.path.join(base_dir, person_name)
    if not os.path.isdir(person_path):
        continue

    embeddings[person_name] = []

    for img_file in os.listdir(person_path):
        if not img_file.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue

        img_path = os.path.join(person_path, img_file)
        img = Image.open(img_path).convert('RGB')

        # Detect + align face
        face = mtcnn(img)
        if face is None:
            print(f"❌ No face detected in {img_path}")
            continue

        # Get embedding
        with torch.no_grad():
            embedding = model(face.unsqueeze(0)).squeeze().numpy()
            embeddings[person_name].append(embedding.tolist())

        print(f"✅ Processed {img_path}")

# Save as JSON
with open(output_file, "w") as f:
    json.dump(embeddings, f, indent=2)

print(f"\n✅ Done. Saved embeddings to '{output_file}'")
