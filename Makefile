.SILENT:

run:
	pdm run python ./src/imagetoascii/main.py $(FILEPATH)

runtest:
	pdm run python ./src/imagetoascii/main.py ./testimage/test1.jpg