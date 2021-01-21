# car-tracker
Detect and read license plate. Also predict car make and model.

### Before getting started
To get started with this program, you need to install git on your computer.

This program is tested on Ubuntu 16.04. The command to install git on Ubuntu 16.04:

```bash
$ sudo apt install git -y
```

### Get started
To get started follow open your terminal and run the commands sequentially

```bash
$ git clone https://github.com/faysal-ishtiaq/car-tracker.git
$ cd car-tracker
$ chmod +x install-dep.sh
$ chmod +x setup-venv.sh
$ sudo ./install-dep.sh
$ ./setup-venv.sh
$ source venv/bin/activate
$ python main.py ./inputs/car-a.jpg
$ python main.py ./inputs/car-b.png
```

