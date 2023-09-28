from deepface import DeepFace
import matplotlib.pyplot as plt

face_1 = DeepFace.detectFace(img_path="Images/Purin1.jpg")
plt.imshow(face_1)
plt.show()

face_2 = DeepFace.detectFace(img_path="Images/Purin2.jpg")
plt.imshow(face_2)
plt.show()

result = DeepFace.verify(img1_path="Images/Purin1.jpg", img2_path="Images/Purin2.jpg", model_name = "Facenet")
print(result)

# Du doan tuoi gioi tinh etc

obj = DeepFace.analyze(img_path = "Images/Purin1.jpg", actions = ['age', 'gender', 'race', 'emotion'])
print(obj)  
