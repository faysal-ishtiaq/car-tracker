source venv/bin/activate
python ./predictions/make_model.py car.jpeg
python ./predictions/color.py car.jpeg
python ./predictions/license.py car.jpeg

