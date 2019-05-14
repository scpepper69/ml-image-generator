# Coloring Gundam Face Application

This application is created as client application.

This application colors line drawing picture.



## How to deploy

### Preparation

Please see README.md at parent directory.




### Usage
1. docker run (windows powershell)

   ```bash
   cd ml-image-generator/gimage/app/
   ./docker.ps1
   ```

1. Startup application

   ```bash
   cd ./app
   
   # coloring static picture
   python pix2pix.py <path to picture file>
   

   # coloring drawing picture
   python draw2pix.py
   ```
   
   
   
## Application Architecture

- Learned Model : TensorFlow
- Model Server : GraphPipe
- Client Application : Python



## Model Structure

The learned Model is to large to put on this GitHub Repository. So I published it to my Google Drive.

[Download Link](https://drive.google.com/open?id=1OweErMspH2l_Ao8H2XMXIziI0-AuktcA) (208 MB)



This model is built by GAN. I referred to followings. 

- [affinelayer/pix2pix-tensorflow](<https://github.com/affinelayer/pix2pix-tensorflow>)

- [GordonRen/edge2view](<https://github.com/GordonRen/edge2view>)



