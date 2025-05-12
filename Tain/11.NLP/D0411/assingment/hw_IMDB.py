from hw_강재훈_IMDB import *

word_vector_custom=torch.load('custom.pkl')
word_vector_word2vec=torch.load('word2vec.pkl')
data=pd.read_csv(r'C:\Users\Administrator\Desktop\DL\DATA\IMDb_Reviews.csv').review
target=pd.read_csv(r'C:\Users\Administrator\Desktop\DL\DATA\IMDb_Reviews.csv').iloc[:,-1]
emb=Embedded_Model(data)
emb.custom_embed()
ws2id=emb.word2vec()
# DNN,custom
normal_train(RNNModel,word_vector_custom,emb.data,target,lambda x:collate_batch_offset(x,emb.s2id))
# DNN,word2vec
normal_train(RNNModel,word_vector_word2vec,emb.data,target,lambda x:collate_batch_offset(x,ws2id))

# RNN,custom
normal_train(RNNModel,word_vector_custom,emb.data,target,lambda x:collate_batch(x,emb.s2id))
# RNN,word2vec
normal_train(RNNModel,word_vector_word2vec,emb.data,target,lambda x:collate_batch(x,ws2id))

# LSTM,custom
normal_train(RNNModel,word_vector_custom,emb.data,target,lambda x:collate_batch(x,emb.s2id))
# LSTM,word2vec
normal_train(RNNModel,word_vector_word2vec,emb.data,target,lambda x:collate_batch(x,ws2id))