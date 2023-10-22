#!/bin/bash

# Run first script
python unzipStep1.py

# Run second script
python tsvToCsvStep2.py

# Run third script
python splitDataStep3.py

# Run fourth script
python cleanPreprocessStep4.py

# Run fifth script
python sendToArangoStep5.py
