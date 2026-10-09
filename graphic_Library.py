from customtkinter import *
from CTkMessagebox import *


books = []


def add():
    root.withdraw()
    add_window = CTkToplevel(root)
    add_window.title("Add book")
    add_window.geometry("700x600")
    CTkLabel(add_window, text="Add book", font=title_font, text_color="black", fg_color="#3366FF", corner_radius=15).pack(pady=(50 ,40))

    id_ = CTkEntry(add_window, font=entry_font, placeholder_text="ID...", corner_radius=10, width=250, justify="center")
    id_.pack(pady=20)
    title_ = CTkEntry(add_window, font=entry_font, placeholder_text="Title...", corner_radius=10, width=250, justify="center")
    title_.pack(pady=20)
    author_ = CTkEntry(add_window, font=entry_font, placeholder_text="Author...", corner_radius=10, width=250, justify="center")
    author_.pack(pady=20)
    year_ = CTkEntry(add_window, font=entry_font, placeholder_text="Year...", corner_radius=10, width=250, justify="center")
    year_.pack(pady=20)

    def save():
        if not id_.get() or not title_.get() or not author_.get() or not year_.get():
            CTkMessagebox(title="Error", message="The box's of dilates are empty!", icon="warning", width=300, height=150)
            id_.delete(0, END)
            title_.delete(0, END)
            author_.delete(0, END)
            year_.delete(0, END)
            return

        try:
            int(id_.get())
        except ValueError:
            CTkMessagebox(title="Error", message="ID must be a number!", icon="warning", width=300, height=150)
            id_.delete(0, END)
            title_.delete(0, END)
            author_.delete(0, END)
            year_.delete(0, END)
            return

        try:
            int(year_.get())
        except ValueError:
            CTkMessagebox(title="Error", message="Year must be a number!", icon="warning", width=300, height=150)
            id_.delete(0, END)
            title_.delete(0, END)
            author_.delete(0, END)
            year_.delete(0, END)
            return

        for i in books:
            if id_.get() == i["ID"]:
                CTkMessagebox(title="Error", message="ID are already used!", icon="warning", width=300, height=150)
                id_.delete(0, END)
                title_.delete(0, END)
                author_.delete(0, END)
                year_.delete(0, END)
                return

        else:
            if CTkMessagebox(title="Save", message="Are you sure you want to save?", icon="question", width=300, height=150, option_1="Yes", option_2="No").get() == "Yes":
                new_dict = {
                    "ID" : id_.get().strip(),
                    "Title" : title_.get().strip(),
                    "Author" : author_.get().strip(),
                    "Year" : year_.get().strip(),
                    "Status" : "Available"
                }
                books.append(new_dict)
                root.deiconify()
                add_window.destroy()

    def cancel():
        if CTkMessagebox(title="Cancel", message="Are you sure you want to cancel?", icon="question", width=300, height=150, option_1="Yes", option_2="No").get() == "Yes":
            root.deiconify()
            add_window.destroy()

    frame_btn_ = CTkFrame(add_window, fg_color="#242424")
    done = CTkButton(frame_btn_, text="Cancel", font=label_button_font, text_color="black", fg_color="#30bdcd", corner_radius=20, command=cancel)
    done.grid(row=4, column=0, padx=20, pady=20)

    done = CTkButton(frame_btn_, text="Done", font=label_button_font, text_color="black", fg_color="#30bdcd", corner_radius=20, command=save)
    done.grid(row=4, column=1, padx=20, pady=20)
    frame_btn_.pack()

#=================================================================================================================================================================================

def show():
    if not books:
        CTkMessagebox(title="Error", message="The list of books are empty!", icon="warning", width=300, height=150)
    else:
        root.withdraw()
        show_window = CTkToplevel(root)
        show_window.title("Show book")
        show_window.geometry("1000x600")

        CTkLabel(show_window, text="Show book", font=title_font, text_color="black", fg_color="#3366FF", corner_radius=15).pack(pady=(50, 40))
        frame_scroll = CTkScrollableFrame(show_window, fg_color="#1c3273", corner_radius=20, width=800)
        r = 1
        for i in books:
            CTkLabel(frame_scroll, text="ID", font=label_button_font, text_color="black", fg_color="#3366FF", corner_radius=15).grid(row=0, column=0, padx=40, pady=(0, 30))
            CTkLabel(frame_scroll, text=f"{i['ID']}", font=label_button_font, text_color="white", fg_color="#3366FF", corner_radius=15).grid(row=r, column=0, padx=40, pady=10)

            CTkLabel(frame_scroll, text="Title", font=label_button_font, text_color="black", fg_color="#3366FF", corner_radius=15).grid(row=0, column=1, padx=40, pady=(0, 30))
            CTkLabel(frame_scroll, text=f"{i['Title']}", font=label_button_font, text_color="white", fg_color="#3366FF", corner_radius=15).grid(row=r, column=1, padx=40, pady=10)

            CTkLabel(frame_scroll, text="Author", font=label_button_font, text_color="black", fg_color="#3366FF", corner_radius=15).grid(row=0, column=2, padx=40, pady=(0, 30))
            CTkLabel(frame_scroll, text=f"{i['Author']}", font=label_button_font, text_color="white", fg_color="#3366FF", corner_radius=15).grid(row=r, column=2, padx=40, pady=10)

            CTkLabel(frame_scroll, text="Year", font=label_button_font, text_color="black", fg_color="#3366FF", corner_radius=15).grid(row=0, column=3, padx=40, pady=(0, 30))
            CTkLabel(frame_scroll, text=f"{i['Year']}", font=label_button_font, text_color="white", fg_color="#3366FF", corner_radius=15).grid(row=r, column=3, padx=40, pady=10)

            CTkLabel(frame_scroll, text="Status", font=label_button_font, text_color="black", fg_color="#3366FF", corner_radius=15).grid(row=0, column=4, padx=40, pady=(0, 30))
            CTkLabel(frame_scroll, text=f"{i['Status']}", font=label_button_font, text_color="white", fg_color="#3366FF", corner_radius=15).grid(row=r, column=4, padx=40, pady=10)

            r += 1
        frame_scroll.pack(padx=30, fill="both")

        def out():
            root.deiconify()
            show_window.destroy()

        done = CTkButton(show_window, text="Done", font=label_button_font, text_color="black", fg_color="#30bdcd", corner_radius=20, command=out)
        done.pack(pady=20)

#=================================================================================================================================================================================

def search():
    if not books:
        CTkMessagebox(title="Error", message="The list of books are empty!", icon="warning", width=300, height=150)

    else:
        root.withdraw()
        search_window = CTkToplevel(root)
        search_window.title("Search book")
        search_window.geometry("1000x600")
        CTkLabel(search_window, text="Search book", font=title_font, text_color="black", fg_color="#3366FF", corner_radius=15).pack(pady=(50, 40))

        search_ = CTkEntry(search_window, font=entry_font, placeholder_text="Search Title or Author...", corner_radius=10, width=250, justify="center")
        search_.pack()

        frame_scroll_ = CTkScrollableFrame(search_window, fg_color="#1c3273", corner_radius=20, width=800)
        def searching():

            search_get = search_.get()
            searched = []
            if not search_get:
                CTkMessagebox(title="Error", message="The box is empty!", icon="warning", width=300, height=150)
                return

            for i in books:
                if search_get.lower() in i["Title"].lower() or search_get.lower() in i["Author"].lower():
                    searched.append(i)
            if len(searched) == 0:
                CTkLabel(search_window, text="Not Founded!", font=title_font, text_color="white", fg_color="#242424").pack(pady=(50, 40))
                return
            else:
                r = 1

                for j in searched:


                    CTkLabel(frame_scroll_, text="ID", font=label_button_font, text_color="black", fg_color="#3366FF", corner_radius=15).grid(row=0, column=0, padx=40, pady=(0, 30))
                    CTkLabel(frame_scroll_, text=f"{j['ID']}", font=label_button_font, text_color="white", fg_color="#3366FF", corner_radius=15).grid(row=r, column=0, padx=40, pady=10)

                    CTkLabel(frame_scroll_, text="Title", font=label_button_font, text_color="black", fg_color="#3366FF", corner_radius=15).grid(row=0, column=1, padx=40, pady=(0, 30))
                    CTkLabel(frame_scroll_, text=f"{j['Title']}", font=label_button_font, text_color="white", fg_color="#3366FF", corner_radius=15).grid(row=r, column=1, padx=40, pady=10)

                    CTkLabel(frame_scroll_, text="Author", font=label_button_font, text_color="black", fg_color="#3366FF", corner_radius=15).grid(row=0, column=2, padx=40, pady=(0, 30))
                    CTkLabel(frame_scroll_, text=f"{j['Author']}", font=label_button_font, text_color="white", fg_color="#3366FF", corner_radius=15).grid(row=r, column=2, padx=40, pady=10)

                    CTkLabel(frame_scroll_, text="Year", font=label_button_font, text_color="black", fg_color="#3366FF", corner_radius=15).grid(row=0, column=3, padx=40, pady=(0, 30))
                    CTkLabel(frame_scroll_, text=f"{j['Year']}", font=label_button_font, text_color="white", fg_color="#3366FF", corner_radius=15).grid(row=r, column=3, padx=40, pady=10)

                    CTkLabel(frame_scroll_, text="Status", font=label_button_font, text_color="black", fg_color="#3366FF", corner_radius=15).grid(row=0, column=4, padx=40, pady=(0, 30))
                    CTkLabel(frame_scroll_, text=f"{j['Status']}", font=label_button_font, text_color="white", fg_color="#3366FF", corner_radius=15).grid(row=r, column=4, padx=40, pady=10)

                    r += 1
                    frame_scroll_.pack(padx=30, fill="both")


        def cancel():
            msg = CTkMessagebox(title="Cancel", message="Are you sure you want to cancel?", icon="question", width=300, height=150, option_1="Yes", option_2="No")
            if msg.get() == "Yes":
                root.deiconify()
                search_window.destroy()


        frame_btn__ = CTkFrame(search_window, fg_color="#242424")
        done = CTkButton(frame_btn__, text="Search", font=label_button_font, text_color="black", fg_color="#30bdcd", corner_radius=20, command=searching)
        done.grid(row=3, column=1,pady=20, padx=20)

        cancel = CTkButton(frame_btn__, text="Cancel", font=label_button_font, text_color="black", fg_color="#30bdcd", corner_radius=20, command=cancel)
        cancel.grid(row=3, column=0,pady=20, padx=20)
        frame_btn__.pack()

#=================================================================================================================================================================================

def lend():
    if not books:
        CTkMessagebox(title="Error", message="The list of books are empty!", icon="warning", width=300, height=150)
    else:
        root.withdraw()
        lend_window = CTkToplevel(root)
        lend_window.title("Lend book")
        lend_window.geometry("1000x600")

        CTkLabel(lend_window, text="Lend book", font=title_font, text_color="black", fg_color="#3366FF", corner_radius=15).pack(pady=(50, 40))

        search_id = CTkEntry(lend_window, font=entry_font, placeholder_text="Search ID to lend...", corner_radius=10, width=250, justify="center")
        search_id.pack()
        def lending():
            books_for_lend = []
            for i in books:
                if search_id.get() in i["ID"] and i["Status"] == "Available":
                    books_for_lend.append(i)

            if len(books_for_lend) == 0:
                CTkMessagebox(title="Error", message="The ID not founded or the book Borrowed! Please check in 'Show book'!!", icon="warning", width=300, height=150)
            else:
                for i in books_for_lend:
                    i["Status"] = "Borrowed"
                CTkMessagebox(title="Successful", message="The book successful Borrowed!", icon="check", width=300, height=150, sound=True)

        def done():
            if CTkMessagebox(title="Done", message="Are you sure you want to out?", icon="question", width=300, height=150, option_1="Yes", option_2="No").get() == "Yes":
                root.deiconify()
                lend_window.destroy()


        frame_lend = CTkFrame(lend_window, fg_color="#242424")
        search_btn = CTkButton(frame_lend, text="Search", font=label_button_font, text_color="black", fg_color="#30bdcd", corner_radius=20, command=lending)
        search_btn.grid(row=0, column=1, pady=20, padx=20)

        done_btn = CTkButton(frame_lend, text="Done", font=label_button_font, text_color="black", fg_color="#30bdcd", corner_radius=20, command=done)
        done_btn.grid(row=0, column=0, pady=20, padx=20)
        frame_lend.pack()

#=================================================================================================================================================================================

def return_():
    if not books:
        CTkMessagebox(title="Error", message="The list of books are empty!", icon="warning", width=300, height=150)
    else:
        root.withdraw()
        return_window = CTkToplevel(root)
        return_window.title("Return book")
        return_window.geometry("1000x600")

        CTkLabel(return_window, text="Return book", font=title_font, text_color="black", fg_color="#3366FF", corner_radius=15).pack(pady=(50, 40))

        search_id = CTkEntry(return_window, font=entry_font, placeholder_text="Search ID to return...", corner_radius=10, width=250, justify="center")
        search_id.pack()
        def returning():
            books_for_return = []
            for i in books:
                if search_id.get() in i["ID"] and i["Status"] == "Borrowed":
                    books_for_return.append(i)

            if len(books_for_return) == 0:
                CTkMessagebox(title="Error", message="The ID not founded or the book Available! Please check in 'Show book'!!", icon="warning", width=300, height=150)
            else:
                for i in books_for_return:
                    i["Status"] = "Available"
                CTkMessagebox(title="Successful", message="The book successful Available!", icon="check", width=300, height=150, sound=True)

        def done():
            if CTkMessagebox(title="Done", message="Are you sure you want to out?", icon="question", width=300, height=150, option_1="Yes", option_2="No").get() == "Yes":
                root.deiconify()
                return_window.destroy()


        frame_return = CTkFrame(return_window, fg_color="#242424")
        search_btn = CTkButton(frame_return, text="Search", font=label_button_font, text_color="black", fg_color="#30bdcd", corner_radius=20, command=returning)
        search_btn.grid(row=0, column=1, pady=20, padx=20)

        done_btn = CTkButton(frame_return, text="Done", font=label_button_font, text_color="black", fg_color="#30bdcd", corner_radius=20, command=done)
        done_btn.grid(row=0, column=0, pady=20, padx=20)
        frame_return.pack()

#=================================================================================================================================================================================

def delete():
    if not books:
        CTkMessagebox(title="Error", message="The list of books are empty!", icon="warning", width=300, height=150)
    else:
        root.withdraw()
        delete_window = CTkToplevel(root)
        delete_window.title("Delete book")
        delete_window.geometry("1000x600")

        CTkLabel(delete_window, text="Delete book", font=title_font, text_color="black", fg_color="#3366FF", corner_radius=15).pack(pady=(50, 40))

        search_id = CTkEntry(delete_window, font=entry_font, placeholder_text="Search ID to delete...", corner_radius=10, width=250, justify="center")
        search_id.pack()

        def deleting():
            for i in books:
                if search_id.get() == i["ID"]:
                    if CTkMessagebox(title="Cancel", message="Are you sure you want to delete?", icon="question", width=300, height=150, option_1="Yes", option_2="No").get() == "Yes":
                        books.remove(i)
                        CTkMessagebox(title="Successful", message="The book successful deleted!", icon="check", width=300, height=150, sound=True)
                else:
                    CTkMessagebox(title="Error", message="The ID not founded! Please check in 'Show book'!!", icon="warning", width=300, height=150)

        def done():
            if CTkMessagebox(title="Done", message="Are you sure you want to out?", icon="question", width=300, height=150, option_1="Yes", option_2="No").get() == "Yes":
                root.deiconify()
                delete_window.destroy()

        frame_del = CTkFrame(delete_window, fg_color="#242424")
        del_btn = CTkButton(frame_del, text="Delete", font=label_button_font, text_color="black", fg_color="#30bdcd", corner_radius=20, command=deleting)
        del_btn.grid(row=0, column=1, pady=20, padx=20)

        done_btn = CTkButton(frame_del, text="Done", font=label_button_font, text_color="black", fg_color="#30bdcd", corner_radius=20, command=done)
        done_btn.grid(row=0, column=0, pady=20, padx=20)
        frame_del.pack()

#=================================================================================================================================================================================

def ditals():
    if not books:
        CTkMessagebox(title="Error", message="The list of books are empty!", icon="warning", width=300, height=150)
    else:
        root.withdraw()
        ditals_window = CTkToplevel(root)
        ditals_window.title("Ditals book")
        ditals_window.geometry("1000x400")

        CTkLabel(ditals_window, text="Ditals book", font=title_font, text_color="black", fg_color="#3366FF", corner_radius=15).pack(pady=(50, 40))
        all_ = 0
        a_ = 0
        b_ = 0
        for i in books:
            if i["Status"] == "Available":
                a_ += 1
            elif i["Status"] == "Borrowed":
                b_ += 1
            all_ += 1
        frame_d = CTkFrame(ditals_window, fg_color="#1c3273", corner_radius=20, width=800)
        CTkLabel(frame_d, text="All books", font=label_button_font, text_color="black", fg_color="#3366FF", corner_radius=15, justify="left").grid(row=0, column=0, padx=40, pady=(10, 30))
        CTkLabel(frame_d, text=f"{all_}", font=label_button_font, text_color="white", fg_color="#3366FF", corner_radius=15, justify="left").grid(row=1, column=0, padx=40, pady=10)

        CTkLabel(frame_d, text="Available books", font=label_button_font, text_color="black", fg_color="#3366FF", corner_radius=15, justify="center").grid(row=0, column=1, padx=40, pady=(10, 30))
        CTkLabel(frame_d, text=f"{a_}", font=label_button_font, text_color="white", fg_color="#3366FF", corner_radius=15, justify="center").grid(row=1, column=1, padx=40, pady=10)

        CTkLabel(frame_d, text="Borrowed books", font=label_button_font, text_color="black", fg_color="#3366FF", corner_radius=15, justify="right").grid(row=0, column=2, padx=40, pady=(10, 30))
        CTkLabel(frame_d, text=f"{b_}", font=label_button_font, text_color="white", fg_color="#3366FF", corner_radius=15, justify="right").grid(row=1, column=2, padx=40, pady=10)

        frame_d.pack()

        def done():
            if CTkMessagebox(title="Done", message="Are you sure you want to out?", icon="question", width=300, height=150, option_1="Yes", option_2="No").get() == "Yes":
                root.deiconify()
                ditals_window.destroy()

        done_btn = CTkButton(ditals_window, text="Done", font=label_button_font, text_color="black", fg_color="#30bdcd", corner_radius=20, command=done)
        done_btn.pack(pady=20, padx=20)

#=================================================================================================================================================================================

def exit_():
    if CTkMessagebox(title="Exit", message="Are you sure you want to exit?", icon="question", width=300, height=150, option_1="Yes", option_2="No").get() == "Yes":
        exit()

root = CTk()
root.title("Library")
root.geometry("800x600")
set_appearance_mode("dark")
set_default_color_theme("blue")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

title_font = ("Segoe Print", 40, "bold")
label_button_font = ("Segoe Print", 20, "bold")
entry_font = ("Segoe Print", 18, "bold")

frame_btn = CTkFrame(root, fg_color="#1c3273", corner_radius=20)
frame_btn.grid_columnconfigure(0, weight=1)
frame_btn.grid_columnconfigure(1, weight=1)
frame_btn.grid_rowconfigure(0, weight=1)
frame_btn.grid_rowconfigure(1, weight=1)
frame_btn.grid_rowconfigure(2, weight=1)
frame_btn.grid_rowconfigure(3, weight=1)

CTkLabel(root, text="Library", font=title_font, text_color="black", fg_color="#3366FF", corner_radius=15).pack(pady=(50 ,30))

add_book = CTkButton(frame_btn, text="Add book", font=label_button_font, text_color="black", fg_color="#30bdcd", corner_radius=20, command=add)
add_book.grid(row=1, column=0, padx=20, pady=20)

show_book = CTkButton(frame_btn, text="Show book", font=label_button_font, text_color="black", fg_color="#30bdcd", corner_radius=20, command=show)
show_book.grid(row=1, column=1, padx=20, pady=20)

search_book = CTkButton(frame_btn, text="Search book", font=label_button_font, text_color="black", fg_color="#30bdcd", corner_radius=20, command=search)
search_book.grid(row=2, column=0, padx=20, pady=20)

lend_book = CTkButton(frame_btn, text="Lend book", font=label_button_font, text_color="black", fg_color="#30bdcd", corner_radius=20, command=lend)
lend_book.grid(row=2, column=1, padx=20, pady=20)

return_book = CTkButton(frame_btn, text="Return book", font=label_button_font, text_color="black", fg_color="#30bdcd", corner_radius=20, command=return_)
return_book.grid(row=3, column=0, padx=20, pady=20)

delete_book = CTkButton(frame_btn, text="Delete book", font=label_button_font, text_color="black", fg_color="#30bdcd", corner_radius=20, command=delete)
delete_book.grid(row=3, column=1, padx=20, pady=20)

ditals_book = CTkButton(frame_btn, text="Show ditals", font=label_button_font, text_color="black", fg_color="#30bdcd", corner_radius=20, command=ditals)
ditals_book.grid(row=4, column=0, padx=20, pady=20)

exit_btn = CTkButton(frame_btn, text="Exit", font=label_button_font, text_color="black", fg_color="#30bdcd", corner_radius=20, command=exit_)
exit_btn.grid(row=4, column=1, padx=20, pady=20)

frame_btn.pack()


root.mainloop()