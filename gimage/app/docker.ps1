function pwd_as_linux {
  "/$((pwd).Drive.Name.ToLowerInvariant())/$((pwd).Path.Replace('\', '/').Substring(3))"
}
docker run -it --name pix --rm -v "$(pwd_as_linux)/../learning:/models/" -p 9041:9041 sleepsonthefloor/graphpipe-tf:cpu1.11.0 --model=/models/gimage_generator.pb --listen=0.0.0.0:9041
