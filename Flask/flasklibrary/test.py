db.drop_all()
db.create_all()

au1 = Author(name='老王')
au2 = Author(name='老慧')
au3 = Author(name='老刘')

db.session.add_all([au1, au2, au3])

db.session.commit()

bk1 = Book(name='老王回忆录', author_id=au1.id)
bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
bk4 = Book(name='怎么征服美丽少女', author_id=au3.id)
bk5 = Book(name='如何征服英俊少男', author_id=au3.id)

db.session.add_all([bk1, bk2, bk3, bk4, bk5])

db.session.commit()