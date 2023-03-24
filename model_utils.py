def get_tfidf_features(title, description, loaded_vec, selector):
    """
    Performs TF-IDF vectorization on the given text
    """
    # Boosts corpus by adding description 3 times
    corpus = [" ".join([title, description, description, description])]

    X = selector.transform(loaded_vec.transform(corpus))
    return X

def predict_bug(X, model):
    """
    Predicts whether given text is bug or not
    """
    result = model.predict(X)[0]
    if (result == 0):
        return "Not a bug"
    else:
        return "Bug"