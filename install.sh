git clone https://github.com/idealo/image-super-resolution
cd image-super-resolution
cat setup.py |sed "s/==/>=/g" > tmp
mv tmp setup.py
python3 setup.py install

pip install numpy PILlow
