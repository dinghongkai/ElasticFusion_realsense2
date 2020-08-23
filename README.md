# 编译

### 1. 安装依赖库
- 安装 apt 依赖
```bash
sudo apt-get install -y cmake-qt-gui git build-essential libusb-1.0-0-dev libudev-dev openjdk-8-jdk freeglut3-dev libglew-dev libsuitesparse-dev libeigen3-dev zlib1g-dev libjpeg-dev
```

- 安装 Pangolin
```bash
git clone https://github.com/stevenlovegrove/Pangolin.git
cd Pangolin
mkdir build
cd build
cmake ../ -DAVFORMAT_INCLUDE_DIR="" -DCPP11_NO_BOOST=ON
make -j8
```

- 安装 OpenNI2
```bash
git clone https://github.com/occipital/OpenNI2.git
cd OpenNI2
make -j8
```

### 2. 编译 Core 库
- 对于比较新的显卡，直接编译可能会报以下错误：
```
Error: invalid texture reference: /ElasticFusion/Core/src/Cuda/convenience.cuh:68
```
需将 Core/CMakeLists.txt 中的下列语句注释掉
```
set(CUDA_ARCH_BIN "30 35 50 52 61" CACHE STRING "Specify 'real' GPU arch to build binaries for, BIN(PTX) format is supported. Example: 1.3 2.1(1.3) or 13 21(13)")
```
- 编译
```bash
cd Core
mkdir build && cd build
cmake ../src
make -j8
sudo make install
```

### 3. 编译并运行 GPUTest
- 编译
```bash
cd GPUTest
mkdir build && cd build
cmake ../src
make -j8
```
- 运行
```bash
cd GPUTest/build
./GPUTest ..
```
输出结果：
```
icpStepMap["GeForce RTX 2070"] = std::pair<int, int>(96, 144);
rgbStepMap["GeForce RTX 2070"] = std::pair<int, int>(368, 32);
rgbResMap["GeForce RTX 2070"] = std::pair<int, int>(256, 384);
so3StepMap["GeForce RTX 2070"] = std::pair<int, int>(128, 64);
```
将输出结果添加到 Core/src/Utils/GPUConfig.h 中，以发挥显卡的最佳性能。

### 4. 重新编译 Core 库
```bash
cd Core/build
cmake ../src
make -j8
sudo make install
```

### 5. 编译 GUI
```bash
cd GUI
cd ../../GUI
mkdir build && cd build
cmake ../src
make -j8
```

# 制作数据集

### 1. 将 png 数据集转成 tum 数据集格式
```bash
cd png_2_klg/python_tools
python3 png_to_tum.py
```
运行之后，会生成 tum/rgb 和 tum/depth 文件夹，以及 tum/rgb.txt 和 tum/depth.txt 文件

### 2. 将 depth 和 rgb 关联

注意 depth.txt 和 rgb.txt 的先后顺序
```bash
cd png_2_klg/python_tools
python associate.py depth.txt rgb.txt > associations.txt
```

### 3. 编译 png_to_klg，生成 klg 数据集

Fork form https://github.com/HTLife/png_to_klg

- 编译
```bash
cd png_2_klg
mkdir build && cd build
cmake ..
make -j8
```

- 运行
```bash
./pngtoklg -w path_to_datasets -o path_to_save_klg/xxx.klg -s 5000 -t
```

# 参考
https://github.com/mp3guy/ElasticFusion/pull/161/files
https://github.com/HTLife/png_to_klg
