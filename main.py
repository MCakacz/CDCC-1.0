#biblioteki :>
import sys
import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def detect_academic_cheating(text1, text2):
    """
    Wykrywanie akademickiego plagiatu.
    """
    # Inicjalizacja TF-IDF Vectorizer
    tfidf_vectorizer = TfidfVectorizer()
    
    # Obliczenie TF-IDF dla tekstów
    tfidf_matrix = tfidf_vectorizer.fit_transform([text1, text2])
    
    # Obliczenie podobieństwa kosinusowego
    similarity_score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    
    threshold = 0.7
    
    if similarity_score >= threshold:
        return "Teksty są podobne (podobieństwo: {:.2f})".format(similarity_score)
    else:
        return "Teksty nie są podobne (podobieństwo: {:.2f})".format(similarity_score)

def detect_online_test_cheating(answer1, answer2):
    """
    Wykrywanie oszustw na testach online.
    """
    common_keywords = set(answer1.lower().split()) & set(answer2.lower().split())
    
    cheating_threshold = 3
    
    if len(common_keywords) >= cheating_threshold:
        return "Podejrzenie oszustwa na teście online!"
    else:
        return "Brak podejrzenia oszustwa na teście online."

def check_online_content_authenticity(url):
    """
    Sprawdzanie autentyczności treści online.
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.get_text()
        
        suspicious_keywords = ["fake news", "fałszywa informacja", "oszustwo"]
        
        for keyword in suspicious_keywords:
            if keyword in content.lower():
                return "Podejrzenie o fałszowanie informacji na stronie {}".format(url)
        
        return "Treść online jest autentyczna i nie zawiera podejrzeń o fałszowanie informacji."
    except Exception as e:
        return "Błąd podczas analizy treści: {}".format(str(e))

def main_menu():
    while True:
        print("\nWybierz tryb:")
        print("1. Akademicki Plagiat")
        print("2. Oszustwa na Testach Online")
        print("3. Podejrzenia o Fałszowanie Informacji w Treściach Online")
        print("4. Wyjście z aplikacji")
        
        wybor = input("Wybierz opcję (1/2/3/4): ")
        
        if wybor == "1":
            text1 = input("Wprowadź pierwszy tekst: ")
            text2 = input("Wprowadź drugi tekst: ")
            result = detect_academic_cheating(text1, text2)
            print(result)
        elif wybor == "2":
            answer1 = input("Wprowadź pierwszą odpowiedź: ")
            answer2 = input("Wprowadź drugą odpowiedź: ")
            result = detect_online_test_cheating(answer1, answer2)
            print(result)
        elif wybor == "3":
            url = input("Wprowadź URL treści online do analizy: ")
            result = check_online_content_authenticity(url)
            print(result)
        elif wybor == "4":
            print("Wyjście z aplikacji.")
            break
        else:
            print("Niepoprawny wybór. Wybierz opcję 1, 2, 3 lub 4.")

if __name__ == "__main__":
    main_menu()
