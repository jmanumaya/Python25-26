# db/schemas/article.py

def article_schema(article) -> dict:
    return {
        "id": str(article["_id"]),
        "title": article["title"],
        "body": article["body"],
        "date": article["date"],
        "idJournalist": article["idJournalist"] 
    }

def articles_schema(articles) -> list:
    return [article_schema(article) for article in articles]