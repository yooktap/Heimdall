from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

keywords = ["pistol", "semi-automatic rifles", "machine gun", "shotgun", "revolver"]

for kw in keywords:
    response().download(kw, 100)
