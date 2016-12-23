# nlp-multimodal-language-models

MSc Artificial Intelligence. Natural language Processing 1: Project on Multimodal language models

### You have to have a /datasets Folder locally with the names as specified in paths.py code.


### TO RUN :
Check paths.py for the paths that the data needed to be put. We only train on a subset of them in the end. The data given for the project should be 
in the following path  : ./datasets/raw/

Afterwards start by running the pre_processing.py to pre process data given a vocabulary frequency threshold (current threshold 5 the results in the report were with 4). Now we can run the train_lstm.py with the flagged parameters. Since we are using theano/lasagne you can have GPU optimization with the given command:
$>THEANO_FLAGS=device=gpu python train_lstm.py --max_sentence 15 --seq_length 16 --batch_size 32 --embedding_size 256 --dropout 0.0 --learning_rate 1e-3

The above default setting is the vanilla one.
To use optimized setting just change optimizer in lasagne.updates by commenting 176 line and uncommenting 177.



Report:
https://www.overleaf.com/7410160xwtfvprhtxdx#/25695582/
