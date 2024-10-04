from model import load_phishing_data, train_model

if __name__ == '__main__':
    df = load_phishing_data('data/website_phishing.csv')
    model = train_model(df)
