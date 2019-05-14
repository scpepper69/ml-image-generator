docker run -d -it --name gimage --rm -v "$PWD/../learning:/models/" -p 9041:9041 sleepsonthefloor/graphpipe-tf:cpu1.11.0 --model=/models/gimage_generator.pb --listen=0.0.0.0:9041 
