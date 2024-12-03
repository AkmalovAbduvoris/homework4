from mysql.connector import connect
from datetime import datetime

# # MySQL ulanish
# db = connect(
#     host="localhost",
#     user="root",
#     password="your_password",  # O'zingizning parolingizni kiriting
#     database="blog_app"
# )

# cursor = db.cursor()

# # Blog funksiyalari
# class Blog:
#     def create_post(self, title, content, author):
#         query = "INSERT INTO posts (title, content, author) VALUES (%s, %s, %s)"
#         cursor.execute(query, (title, content, author))
#         db.commit()
#         print("Post muvaffaqiyatli yaratildi!")

#     def view_posts(self):
#         query = "SELECT id, title, author, created_at FROM posts"
#         cursor.execute(query)
#         posts = cursor.fetchall()
#         print("\nBarcha postlar:")
#         for post in posts:
#             print(f"ID: {post[0]}, Title: {post[1]}, Author: {post[2]}, Created At: {post[3]}")

#     def update_post(self, post_id, new_title, new_content):
#         query = "UPDATE posts SET title = %s, content = %s WHERE id = %s"
#         cursor.execute(query, (new_title, new_content, post_id))
#         db.commit()
#         print("Post muvaffaqiyatli yangilandi!")

#     def delete_post(self, post_id):
#         query = "DELETE FROM posts WHERE id = %s"
#         cursor.execute(query, (post_id,))
#         db.commit()
#         print("Post muvaffaqiyatli o'chirildi!")

# blog = Blog()

# while True:
#     print("\n1. Post yaratish\n2. Postlarni ko'rish\n3. Postni yangilash\n4. Postni o'chirish\n5. Dasturni tugatish")
#     choice = int(input("Tanlovni kiriting: "))

#     if choice == 1:
#         title = input("Post sarlavhasi: ")
#         content = input("Post kontenti: ")
#         author = input("Muallif ismi: ")
#         blog.create_post(title, content, author)

#     elif choice == 2:
#         blog.view_posts()

#     elif choice == 3:
#         post_id = int(input("Yangilash uchun post ID: "))
#         new_title = input("Yangi sarlavha: ")
#         new_content = input("Yangi kontent: ")
#         blog.update_post(post_id, new_title, new_content)

#     elif choice == 4:
#         post_id = int(input("O'chirish uchun post ID: "))
#         blog.delete_post(post_id)

#     elif choice == 5:
#         print("Dastur tugatildi.")
#         break

#     else:
#         print("Noto'g'ri tanlov.")

class Blog:
    def __init__(self) -> None:
        self.conn = connect(user="root", password="abduvoris5005", database="blog_app", host="localhost")
        self.cursor = self.conn.cursor()
        
    def create_post(self,title,content,author):
        self.cursor.execute("INSERT INTO posts (title, content, author) VALUES (%s, %s, %s)",(title, content, author))
        self.conn.commit()
        print("Post qo'shildi")
        
    def view_posts(self):
        self.cursor.execute("SELECT * FROM posts")
        for row in self.cursor.fetchall():
            print(row)
            
    def update_post(self, post_id, new_title, new_content):
        self.cursor.execute("UPDATE posts SET title = %s, content = %s WHERE id = %s", (new_title, new_content, post_id))
        self.conn.commit()
        print("Post yangilandi")
        
    def delete_post(self, post_id):
        self.cursor.execute("DELETE FROM posts WHERE id = %s", (post_id,))
        self.conn.commit()
        print("Post o'chirildi")
        
obj = Blog()

while True:
    print("\n1. Post yaratish\n2. Postlarni ko'rish\n3. Postni yangilash\n4. Postni o'chirish\n5. Dasturni tugatish")
    choice = int(input("Tanlovni kiriting: "))
    if choice == 1:
        title = input("Post sarlavhasi: ")
        content = input("Post kontenti: ")
        author = input("Muallif ismi: ")
        obj.create_post(title, content, author)

    elif choice == 2:
        obj.view_posts()

    elif choice == 3:
        post_id = int(input("Yangilash uchun post ID: "))
        new_title = input("Yangi sarlavha: ")
        new_content = input("Yangi kontent: ")
        obj.update_post(post_id, new_title, new_content)

    elif choice == 4:
        post_id = int(input("O'chirish uchun post ID: "))
        obj.delete_post(post_id)

    elif choice == 5:
        print("Dastur tugatildi.")
        break

    else:
        print("Noto'ri raqam.")