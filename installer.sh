echo "install started\n"
echo "creating webui config\n"
mkdir -p ~/.config/autorip
cp index.html ~/.config/autorip/
echo "adding autorip to path"
sudo mv autorip /usr/bin/autorip
sudo chmod +x /usr/bin/autorip
echo "finished installation"
