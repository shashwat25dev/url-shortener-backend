from DataBase.models import URL

def create_url(db, short_code, long_url):
    url = URL(short_code=short_code, long_url=long_url)
    db.add(url)
    db.commit()
    db.refresh(url)
    return url

def get_url(db, short_code):
    return db.query(URL).filter(URL.short_code == short_code).first()

def delete_url(db, short_code):
    url = get_url(db, short_code)
    if not url:
        return None
    db.delete(url)
    db.commit()
    return url

def get_stats(db, short_code):
    return get_url(db, short_code)

