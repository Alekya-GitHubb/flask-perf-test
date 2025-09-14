Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"  # Ubuntu 20.04 LTS
  config.vm.network "forwarded_port", guest: 5000, host: 5000

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update -y
    sudo apt-get install -y python3 python3-pip
    cd /vagrant
    pip3 install -r requirements.txt
    nohup python3 app.py > flask.log 2>&1 &
  SHELL
end
