
This module consists of two major components:
  • Automated Data Retrieval: The user can collect all available online data on a specific company. These will be classified depending on their relevance to Konvolut.
  • Text Sentiment Analysis: As part of the PoC, we test and compare different models for the sentiment analysis task. A simple LSTM model as well as a state-of-the-art model Xlnet are trained and evaluated. We also compare statistical and machine learning-based models in terms of classification performance versus model complexity.
  
Running the Data Retrieval Component:
To get started with the automated data retrieval model, the repository should be cloned and the dependencies have to be installed. In order to do so, follow the instructions bellow:
  1. Clone the Repository and change to the relevant branch: Run the command the
  following command in a WSL2 terminal.
  
    • git clone https://github.com/Cyr-Ch/Convolut.git
    
    • cd Convolut
    
    • git checkout cyrch/webscraping
    
    • cd automated data retrieval
    
    • pip install -r requirements.txt
    
Once the dependencies have been installed, the automated data retrieval module can be launched by running the command
  2. ./retrieve data.sh COMPANY NAME
  
The script looks up all relevant data and files to be found online on the company or entity passed as argument. This data will be then classified per relevance to convolute (if it is ESG-related or not). The results of the filtering are saved in a csv file.

Running the Text Sentiment Analysis Component:
This module is in turn composed of three sub-modules:

    • LSTM Model: A simplistic LSTM model for text sentiment analysis, trained and tested on tweets.

    • model-comparisons: We train and evaluate several models, namely, Multinomial Naive, Bayes Classifier, Logistic Regression Classifier, SVM Classifier and a RoBERTa-based pipeline.

    • xlnet: XLNet is a new unsupervised language representation learning method based on a novel generalized permutation language modeling objective. XLNet employs Transformer-XL as the backbone model, exhibiting excellent performance for language tasks involving long context.

All of the three sub-components use jupyter notebooks. Such notebooks are a powerful tool to easily run and visualize trainings and evaluations in Python. In order to run the notebooks:
  1. Open a PowerShell terminal and navigate to the automated data retrieval folder
  2. Run the command: pip install jupyter notebook
  3. A new browser window will be open
  4. Navigate to the folder of the relevant sub-component and open the jupyter notebook in the
  folder
  
Testing the LSTM Model: 
The code to train and evaluate a simple LSTM model for Test Sentiment Analysis is located under:

    • Convolut/modules/text sentiment classification/LSTM model/Sentiment Analysis.ipynb
  
Testing model-comparisons: 
In this section, the library SpaCy is used to build and train several models for Text Sentiment Analysis that are then compared to each other in terms of
performance. The code can be found under:

    • Convolut/modules/text sentiment classification/model-comparisons/compare models.ipynb.
  As some of the models have high hardware requirements, we highly recommand using the google colab platform to run the notebook. You will be prompted to upload the notebook. The required training data is under the folders:

    • Convolut/modules/text sentiment classification/model-comparisons/coronavirus tweet raw.

    • Convolut/modules/text sentiment classification/model-comparisons/spacy data.
  
These need to be uploaded to the drive of your google account (you can also use konvolut’s gmail account for that, login details are mentioned in the SolidPod section) and link the drive storage to the notebook instance. You can find details on that in the code itself.

Testing xlnet: 
XLNet is an architecture for generalized autoregressive pretraining for language understanding. It uses a permutation language modeling objective and includes the Transformer-XL architecture combined with a carefully designed two-stream attention mechanism. XLNet achieves substantial improvement over previous pretraining objectives on various tasks. It is however a highly complex module with high computational requirements. This is the reason why we recommand running the provided code in a google colab instance as well. We report the details of the training here:

    • Training Time: 1hr 11mins

    • Evaluation Time: 2.5hr

    • Accuracy: 0.92416
    
This is by far the best performing model from all of the architectures that have been tested throughout this PoC. However, it is also the most complex and has the highest requirements
