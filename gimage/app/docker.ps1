function pwd_as_linux {
  "/$((pwd).Drive.Name.ToLowerInvariant())/$((pwd).Path.Replace('\', '/').Substring(3))"
}
docker run -it --name pix --rm -v "$(pwd_as_linux)/../learning:/models/" -p 9008:9008 sleepsonthefloor/graphpipe-tf:cpu1.11.0 --model=/models/frozen_model_pix2pix_mod02.pb --listen=0.0.0.0:9008
