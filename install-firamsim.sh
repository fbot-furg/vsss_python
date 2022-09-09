sudo apt-get update
sudo apt-get install -y build-essential g++ cmake git qt5-default libqt5opengl5-dev libgl1-mesa-dev libglu1-mesa-dev libprotobuf-dev protobuf-compiler libode-dev libboost-dev

cd /tmp
git clone https://github.com/jpfeltracco/vartypes.git
cd vartypes
mkdir build 
cd build 
cmake .. 
make 
sudo make install

cd vsss_ws
sudo git clone https://github.com/VSSSLeague/FIRASim.git
cd FIRASim
sudo mkdir build
cd build
sudo cmake ..
sudo make

cd /vsss_ws
sudo git clone https://github.com/VSSSLeague/VSSReferee.git
cd VSSReferee
sudo mkdir build 
cd build 
sudo qmake ..
sudo make

<!-- Run Firasim -->
/vsss_ws/FIRASim/bin/FIRASim

<!-- Run VSSReferee -->
/vsss_ws/VSSReferee/bin/VSSReferee --3v3 --record false