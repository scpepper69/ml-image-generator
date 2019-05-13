docker run -d -it --name gimage --rm -v "$PWD/../learning:/models/" -p 9008:9008 sleepsonthefloor/graphpipe-tf:cpu1.11.0 --model=/models/frozen_inference_graph.pb --listen=0.0.0.0:9008 
