__doc__="analysis of chars, tokens, sentences and messages"

def analyseAll(texts_list):
    """Make raw text analysis of all texts and of the merged text"""
    # medidas por mensagem
    texts_measures={"each_text":[]}
    for text in texts_list:
        texts_measures["each_text"].append({})
        texts_measures["each_text"][-1]["chars"]=medidasChars(text)
        texts_measures["each_text"][-1]["tokens"]=medidasTokens(text)
        texts_measures["each_text"][-1]["sentences"]=medidasSentencas(text,texts_measures[-1]["tokens"]["known_words_unique"])
    del text
    all_texts["texts_overall"]=medidasMensagens2(texts_measures)
    all_text=" ".join(texts_list); del texts_list
    text_measures={}
    text_measures["one_string"]["chars"]=medidasChars(all_text)
    text_measures["one_string"]["tokens"]=medidasTokens(all_text); del all_text
    text_measures["one_string"]["sentences"]=medidasSentencas(all_text,text_measures["one_string"]["tokens"]["known_words_unique"])
    return locals()

def medidasMensagens2(texts_measures):
    #measure_types=("chars","tokens","sentences")
    ## tirar medias e desvios das medidas,
    # ou dos tamanhos dos seus componentes
    # parece ser a única coisa a fazer
    for each_text in texts_measures:
        for each_text_ in texts_measures[each_text]:
            for metric_group in each_text_:
                for measure_name in each_text_[metric_group]:
                    tval+=each_text_[metric_group][measure_name_]


    ## de cada variavel a media e o desvio se for numerica
    # resultando na media e desvio da media e na media e desvio do desvio
    ## e fazendo contagens com len() se for iterável
    # mandando para mediaDesvio
    



    for measure
def medidasChars(T):
    """Medidas de letras TTM formatar para passagem como dicionário"""
    nchars=len(T)
    nspaces=T.count(" ")
    nletters=sum([t.isalpha() for t in T])
    nuppercase=sum([t.isupper() for t in T])
    nvowels=sum([t in ("a","e","i","o","u") for t in T])
    npuntuations=sum([t in puncts for t in T])
    ndigits=sum([t.isdigit() for t in T]) # numerais
    frac_espaces=nspaces/nchars
    frac_letters=nletters/(nchars-nspaces)
    frac_vowels=nvowels/nletters
    frac_uppercase=nuppercase/nletters
    frac_punctuations=npunctuations/(nchars-nspaces)
    frac_digits=ndigits/(nchars-nspaces)
    del T
    return locals()

def medidasTokens(T):
    """Medidas extensas sobre os tokens TTM"""
    atime=time.time()
    tokens=k.tokenize.wordpunct_tokenize(T)
    tokens_lowercase=[t.lower() for t in tokens]
    ntokens=len(tokens) #
    ntokens_diff=len(set(tokens)) # 
    # tokens que sao pontuacoes
    ntokens_punct=sum([sum([tt in puncts for tt in t])==len(t) for t in tokens]) #
    # known and unkown words
    known_words=[] #
    unknown_words=[] #
    punctuation_tokens=[]
    stopwords=[]
    for t in tokens_lowercase:
        if t in WORDLIST_UNIQUE:
            known_words.append(t)
        elif sum([tt in puncts for tt in t])==len(t):
            punctuation_tokens.append(t)
        else:
            unknown_words.append(t)
        if t in STOPWORDS:
            stopwords.append(t)
    stopwords_unique=set(stopwords)
    known_words_unique=set(known_words)
    unknown_words_unique=set(uknown_words)
    known_words_has_wnsynset=[i for i in known_words if wn.synsets(i)]
    known_words_has_wnsynset_unique=set(known_words_has_wnsynset)
    known_words_no_wnsynset=[i for i in known_words if i not in known_words_has_wnsynset_unique]
    known_words_no_wnsynset_unique=set(known_words_without_wnsynset)
    known_words_stopwords=[i for i in known_words if i in stopwords_unique]
    known_words_stopwords_unique=set(known_words_stopwords)
    known_words_not_stopwords=[i for i in known_words if i not in stopwords_unique]
    known_words_not_stopwords_unique=set(known_words_not_stopwords)
    unknown_words_stopwords=[i for i in unknown_words if i in stopwords_unique]
    known_words_stopwords_has_wnsynset=[i for i in kwss if i in stopwords_unique]
    # known words that dont return synsets and are stopwords
    known_words_stopwords_no_wnsynset=[i for i in kwnss if i in stopwords_unique]; c("MT6:")
    # words that are known, are not stopwords and do not return synset
    foo_=known_words_no_synset_unique.difference(stopwords_unique)
    known_words_not_stopword_no_synset=[i for i in kw if i in foo_]; c("MT7:")
    # known words with synset that are not stopwords
    foo_=known_words_has_wnsynset_unique.difference(stopwords_unique) 
    known_words_not_stopword_has_synset=[i for i in kw if i in foo_] #
    known_words_not_stopword_has_synset_unique=set(known_words_not_stopword_has_synset)
    tvars=("known_words","known_words_has_wnsynset_not_stopword","known_words_stopwords","stopwords")
    frac_punctuations=len(punctuations)/len(tokens)
    frac_known_words = len(known_words)/len(tokens)
    frac_stopwords   =   len(stopwords)/len(known_words)
    lexical_diversity=len(known_words)/len(known_words_unique)
    token_sizes=mediaDesvio(tvars,medidas_tokens)
    del foo,foo_,t,tokens,tokens_lowercase,tvars,T
    return locals()

def medidasSentencasParagrafos(T,known_words_unique):
    """Medidas das sentenças TTM"""
    paragraphs=[i.strip() for i in T.split("\n")]
    sentences_paragraphs=[k.sent_tokenize(j) for j in paragraphs]
    tokens_paragraphs=[k.tokenize.wordpunct_tokenize(j) for j in paragraphs] ### Para os POS tags
    known_words_paragraphs=[[ii for ii in i if ii in known_words_unique] for i in tokens_paragraphs]
    known_words_not_stopwords_paragraphs=[[i for i in ts if (i not in STOPWORDS) and (i in WORDLIST_UNIQUE)] for ts in tokens_paragraphs]
    stopwords_paragraphs=[[i for i in ts if i in STOPWORDS] for ts in tokens_paragraphs]
    punctuations_sentences=[[i for i in ts if
         (len(i)==sum([(ii in puncts) for ii in i]))]
         for ts in tokens_paragraphs] #
 

    sentences=k.sent_tokenize(T)
    tokens_sentences=[k.tokenize.wordpunct_tokenize(i) for i in sentences] ### Para os POS tags
    known_words_sentences=[[ii for ii in i if ii in known_words_unique] for i in tokens_sentences]
    known_words_not_stopwords_sentences=[[i for i in ts if (i not in STOPWORDS) and (i in WORDLIST_UNIQUE)] for ts in tokens_sentences]
    stopwords_sentences =[[i for i in ts if i in STOPWORDS] for ts in tokens_sentences]
    punctuations_sentences=[[i for i in ts if
         (len(i)==sum([(ii in puncts) for ii in i]))]
         for ts in tokens_sentences] #
    del T
    locals_=locals()
    mvars=tuple(locals_.keys())
    medidas=mediaDesvio(mvars,locals_)
    medidas.update({nsentences:len(tokens_sentences)})
    medidas.update(locals_)
    return medidas

def medidasMensagens(texts_list):
    """Medidas das mensagens em si"""
    tokens_messages=[k.tokenize.wordpunct_tokenize(t) for t in texts_list] # tokens
    known_words_messages=[[i for i in toks if (i not in stopwords) and (i in WORDLIST_UNIQUE)] for toks in tokens_messages]
    stopwords_messages=[[i for i in toks if i in stopwords] for toks in tokens_messages]
    punctuations_messages=[[i for i in toks if
         (len(i)==sum([(ii in puncts) for ii in i]))]
         for toks in tokens_messages] #
    sentences_msgs=[k.sent_tokenize(t) for t in texts_list] # tokens
    chars_messages=texts_list[:]
    del texts_list
    locals_=locals()
    mvars=tuple(locals_.keys())
    medidas=mediaDesvio(mvars,locals())
    medidas.update({nmessages=len(texts_list)})
    medidas.update(locals_)
    return medidas
