import tkinter
import tkinter.font
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from PIL import Image, ImageTk


class Window:
    def __init__(self,  master):
        self.master = master
        
        self.master.title('SYSTEM ENTRY')
        #self.master.wm_state('zoomed')
        self.master.geometry('+200+50')
        self.master.resizable(0,  0)

        top.wm_protocol("WM_DELETE_WINDOW", self.on_exit)

        curs.execute('''SELECT *
                        FROM custom''')
        cus_data = curs.fetchall()

        if cus_data == []:
                self.t = 'times'
                self.b = 'normal'
                self.i = 'roman'
                self.t2 = 'times'
                self.b2 = 'normal'
                self.i2 = 'roman'
                self.t_back = 'blue'
                self.back_color = 'khaki2'
        else:
            for i in range(len(cus_data)):
                if cus_data[i][0] == 'title':
                    self.t = cus_data[i][1]
                    self.b = cus_data[i][2]
                    self.i = cus_data[i][3]
                    self.back_color = cus_data[i][4]
                else:
                    self.t2 = cus_data[i][1]
                    self.b2 = cus_data[i][2]
                    self.i2 = cus_data[i][3]
                    self.t_back = cus_data[i][4]
                
    def formation(self):

        try:
            self.frame4.destroy()
        except:
            pass
        try:
            self.frame5.destroy()
        except:
            pass
        try:
            self.frame6.destroy()
        except:
            pass
        try:
            self.frame7.destroy()
        except:
            pass
        try:
            self.frame8.destroy()
        except:
            pass
        try:
            self.frame9.destroy()
        except:
            pass
        try:
            self.frame10.destroy()
        except:
            pass
            
        self.frame1 = tkinter.Frame(self.master, bg=self.back_color)
        self.frame1.grid(row=0, column=0, rowspan=12, columnspan=6, sticky='WENS')

        tkinter.Label(self.frame1, text="COLLEGE ROOM SEMINAR SYSTEM", bg=self.back_color, font=(self.t, 25, self.b, self.i, 'underline'), fg=self.t_back).grid(row=1, column=0, rowspan=2, columnspan=6)
        tkinter.Button(self.frame1, text='Add New Room', cursor='hand2', command=self.add).grid(row=6, column=1, ipadx=15, sticky='E')
        tkinter.Button(self.frame1, text='Remove Existing Room', cursor='hand2', command=self.remove).grid(row=6, column=3, ipadx=4, sticky='E')
        tkinter.Button(self.frame1, text='Book A Room', cursor='hand2', command=self.book).grid(row=8, column=1, ipadx=22, sticky='E')
        tkinter.Button(self.frame1, text='Check The Status', cursor='hand2', command=self.status).grid(row=8, column=3, ipadx=20, sticky='E')
        tkinter.Button(self.frame1, text='Replace rooms', cursor='hand2', command=self.replace).grid(row=10, column=1, ipadx=20, sticky='E')
        tkinter.Button(self.frame1, text='Customise window', cursor='hand2', command=self.customize).grid(row=10, column=3, ipadx=15, sticky='E')
        tkinter.Button(self.frame1, text='Reset Changes', cursor='hand2', command=self.reset).grid(row=12, column=1, ipadx=20, sticky='E')
        tkinter.Button(self.frame1, text='Exit', cursor='hand2', command=self.exit_fun).grid(row=12, column=3, ipadx=58, sticky='E')

        path = 'image001.jpg'
        image1 = ImageTk.PhotoImage(Image.open(path))
        self.li = tkinter.Label(self.frame1, image=image1, bg='black')
        self.li.image = image1
        self.li.grid(row=3, column=0, rowspan=2, columnspan=6, pady=10)
        
        tkinter.Label(self.frame1, bg=self.back_color).grid(row=5, column=0)
        tkinter.Label(self.frame1, bg=self.back_color).grid(row=7, column=0)
        tkinter.Label(self.frame1, bg=self.back_color).grid(row=9, column=0)
        tkinter.Label(self.frame1, bg=self.back_color).grid(row=11, column=0)
        tkinter.Label(self.frame1, bg=self.back_color).grid(row=13, column=0)

    def add(self):
        
        def add_func():

            try:
                v1.get() == int()
                if v1.get() == 0:
                    raise ValueError
                check1 = 0
            except tkinter.TclError as er:
                messagebox.showerror('Error', str(er)+'\n'+'\nHint:\nRoom Number must be a non zero positive integer.')
                check1 = 1

            except ValueError:
                er = ('expected a valid "Room Number" but got {}.'.format(v1.get()))
                messagebox.showerror('Error', str(er)+'\n'+'\nHint:\nRoom Number must be a non zero positive integer.')
                check1 = 1

            if check1 == 0:
                try:
                    v2.get() == int()
                    if v2.get() == 0:
                        raise ValueError
                    check2 = 0
                except tkinter.TclError as er:
                    messagebox.showerror('Error', str(er)+'\n'+'\nHint:\nNumber of Students must be a non zero positive integer.')
                    check2 = 1

                except ValueError:
                    er = ('expected a valid "Student Count" but got {}.'.format(v2.get()))
                    messagebox.showerror('Error', str(er)+'\n'+'\nHint:\nNumber of Students must be a non zero positive integer.')
                    check2 = 1
                if check2 == 0:
                    curs.execute('''SELECT room_no
                                    FROM rooms''')
                    data = curs.fetchall()
                    
                    flag = 0
                    value = [v1.get(), v2.get()]
                    
                    for i in range(len(data)):
                        
                        if data[i][0] == v1.get():
                            flag = 1
                            break
                        else:
                            flag = 0
                            
                    if flag == 0:
                        
                        curs.execute('''INSERT INTO rooms (room_no, no_stu)
                                        VALUES(?, ?)''',  value)
                        conn.commit()
                        
                        messagebox.showinfo('Info', 'Room Number {} has been successfully added !!!'.format(v1.get()))
                    else:
                        messagebox.showerror('Alert', 'Room Number {} already exists !!!'.format(v1.get()))

        
        self.frame4 = tkinter.Frame(self.master, bg=self.back_color)
        self.frame4.grid(row=0, column=0, rowspan=12, columnspan=6, sticky='EWNS')
        self.frame1.destroy()
        
        v1 = tkinter.IntVar()
        v2 = tkinter.IntVar()

        tkinter.Button(self.frame4, text='Back', cursor='hand2', command=self.formation).grid(row=0, column=0, sticky='W')
        tkinter.Label(self.frame4, bg=self.back_color, text="ROOM ADDITION", font=(self.t, 25, self.b, self.i, 'underline'), fg=self.t_back).grid(row=0, column=1, rowspan=2, columnspan=4)
        
        path = 'C:/Users/ERROR/Downloads/image001.jpg'
        image1 = ImageTk.PhotoImage(Image.open(path))
        self.li = tkinter.Label(self.frame4, image=image1, bg='black')
        self.li.image = image1
        self.li.grid(row=3, column=0, rowspan=2, columnspan=6, pady=10)
        
        tkinter.Label(self.frame4, bg=self.back_color).grid(row=5, column=0)
        tkinter.Label(self.frame4, text='New Room Number to be Added :', bg=self.back_color, font=(self.t2, 12, self.b2, self.i2)).grid(row=6, column=0, columnspan=3, sticky='WE')
        self.ea1 = tkinter.Entry(self.frame4, bg='khaki3', textvariable=v1, relief='sunken', bd=2)
        self.ea1.grid(row=6, column=3, columnspan=2, sticky='WE')
        self.ea1.bind('<Button-1>', self.on_click)
        
        tkinter.Label(self.frame4, bg=self.back_color).grid(row=7, column=0)
        tkinter.Label(self.frame4, text='Maximum Number of Students :', bg=self.back_color, font=(self.t2, 12, self.b2, self.i2)).grid(row=8, column=0, rowspan=2, columnspan=3, sticky='WE')
        self.ea2 = tkinter.Entry(self.frame4, bg='khaki3', textvariable=v2, relief='sunken', bd=2)
        self.ea2.grid(row=8, column=3, rowspan=2, columnspan=2, sticky='WE')
        self.ea2.bind('<Button-1>', self.on_click)
        
        tkinter.Label(self.frame4, bg=self.back_color).grid(row=9, column=0)
        tkinter.Label(self.frame4, bg=self.back_color).grid(row=10, column=0)
        tkinter.Button(self.frame4, text='Confirm', cursor='hand2', command=add_func).grid(row=11, column=3, pady=10, sticky='W')
        #self.ba1=tkinter.Button(self.frame4, text='Exit', command=self.exit, cursor='hand2')
        #self.ba1.grid(row=11, column=4, sticky='W')
        tkinter.Label(self.frame4, bg=self.back_color).grid(row=12, column=0)
        tkinter.Label(self.frame4, bg=self.back_color).grid(row=13, column=0)
        tkinter.Label(self.frame4, bg=self.back_color).grid(row=14, column=0)
        

    def remove(self):
        
        def del_func():
            curs.execute('''SELECT room_no
                                FROM rooms''')
            data = curs.fetchall()

            try:
                v1.get() == int()
                if data == []:
                    raise ValueError
                if v1.get() == 0:
                    raise NameError
                check1 = 0
                
            except tkinter.TclError as er:
                messagebox.showerror('Error', str(er)+'\n'+'\nHint:\nRoom Number must be a non zero positive integer.')
                check1 = 1

            except NameError:
                er = ('expected a valid "Room Number" but got {}.'.format(v1.get()))
                messagebox.showerror('Error', str(er)+'\n'+'\nHint:\nRoom Number must be a non zero positive integer.')
                check1 = 1

            except ValueError:
                messagebox.showerror('Error', 'Sorry !!! Can not remove the room.\n\nDatabase is empty')
                check1 = 1

            if check1 == 0:
                value = [v1.get()]
                flag = 2
                
                for i in range(len(data)):
                    if data[i][0] == v1.get():
                        flag = 1
                        break
                    else:
                        flag = 0
                        
                if flag == 1:
                    
                    curs.execute('''DELETE FROM rooms
                                        WHERE room_no = ?''',  value)
                    conn.commit()
                    messagebox.showinfo('Info', 'Room Number {} has been successfully removed !!!'.format(v1.get()))
                    
                elif flag == 2:
                    messagebox.showerror('Alert', 'Database is Empty !!!')
                    
                else:
                    messagebox.showerror('Alert', 'Room Number {} does not exists !!!'.format(v1.get()))
                    
            try:
                del(data, i, flag, value)
            except:
                pass
        
        self.frame5 = tkinter.Frame(self.master, bg=self.back_color)
        self.frame5.grid(row=0, column=0, rowspan=12, columnspan=6)        
        self.frame1.destroy()
        
        v1 = tkinter.IntVar()
        v2 = tkinter.IntVar()
        
        tkinter.Button(self.frame5, text='Back', cursor='hand2', command=self.formation).grid(row=0, column=0, sticky='W')
        tkinter.Label(self.frame5, bg=self.back_color, text="ROOM REMOVAL", font=(self.t, 25, self.b, self.i, 'underline'), fg=self.t_back).grid(row=0, column=1, rowspan=2, columnspan=4)

        path = 'C:/Users/ERROR/Downloads/image001.jpg'
        image1 = ImageTk.PhotoImage(Image.open(path))
        self.li = tkinter.Label(self.frame5, image=image1, bg='black')
        self.li.image = image1
        self.li.grid(row=3, column=0, rowspan=2, columnspan=6, pady=10)
        
        tkinter.Label(self.frame5, bg=self.back_color).grid(row=5, column=0)
        tkinter.Label(self.frame5, text='Room Number to be Deleted :', bg=self.back_color, font=(self.t2, 12, self.b2, self.i2)).grid(row=6, column=0, columnspan=3, sticky='WE')
        self.ea1 = tkinter.Entry(self.frame5, bg='khaki3', textvariable=v1, relief='sunken', bd=2)
        self.ea1.grid(row=6, column=3, columnspan=2, sticky='WE')
        self.ea1.bind('<Button-1>', self.on_click)
        
        tkinter.Label(self.frame5, bg=self.back_color).grid(row=7, column=0)
        tkinter.Label(self.frame5, text='Maximum Number of Students :', bg=self.back_color, font=(self.t2, 12, self.b2, self.i2)).grid(row=8, column=0, rowspan=2, columnspan=3, sticky='WE')

        self.ea2 = tkinter.Entry(self.frame5, bg='khaki3', textvariable=v2, relief='sunken', bd=2)
        self.ea2.grid(row=8, column=3, rowspan=2, columnspan=2, sticky='WE')
        tkinter.Label(self.frame5, bg=self.back_color).grid(row=9, column=0)
        self.ea2.bind('<Button-1>', self.on_click)
        
        tkinter.Label(self.frame5, bg=self.back_color, text='(*optional)', font=(self.t2, 9, self.b2, self.i2)).grid(row=10, column=3, sticky='W')
        tkinter.Label(self.frame5, bg=self.back_color).grid(row=11, column=0)
        tkinter.Button(self.frame5, text='Confirm', cursor='hand2', command=del_func).grid(row=12, column=3, pady=10, sticky='W')
        #self.ba1=tkinter.Button(self.frame5, text='Exit', command=self.exit, cursor='hand2')
        #self.ba1.grid(row=11, column=4, sticky='W')
        tkinter.Label(self.frame5, bg=self.back_color).grid(row=13, column=0)
        tkinter.Label(self.frame5, bg=self.back_color).grid(row=14, column=0)
        tkinter.Label(self.frame5, bg=self.back_color).grid(row=15, column=0)
        #tkinter.Label(self.frame5, bg=self.back_color).grid(row=7, column=0)

    def book(self):
        
        def check_func():
            
            flag1 = 1
            if data == []:
                flag1 = 0
                messagebox.showwarning('Warning', 'Sorry!!! The Database is empty.')
                
            if flag1 == 1:
                try:
                    v1.get() == int()
                    if v1.get() < 1:
                        raise ValueError
                    check1 = 0
                except tkinter.TclError as er:
                    check1 = 1
                    messagebox.showerror('Error in row 1', str(er)+'\n'+'\nHint:\nstudent count must be a non zero positive integer')

                except ValueError:
                    check1 = 1
                    er = 'Expected integer but got {}'.format(v1.get())
                    messagebox.showerror('Error in row 1', str(er)+'\n'+'\nHint:\nstudent count must be a non zero positive integer')

                if check1 == 0:
                
                    for i in range(len(data)):
                        if int(data[i][1]) >= int(v1.get()):
                            flag2 = 0
                            break
                        else:
                            flag2 = 1
                            
                    if flag2 == 1 :
                        messagebox.showwarning('Warning', 'Sorry!!! Too many students to be seated!!!')
                        
                    else:
                        try:
                            v2.get() == int()
                            v3.get() == int()
                            if v2.get() <= 0 and v3.get() <= 0:
                                raise ValueError
                            check2 = 0
                            
                        except tkinter.TclError as er:
                            messagebox.showerror('Error in row 2', str(er)+'\n'+'\nHint:\ntime duration must be a non zero positive integer.')
                            check2 = 1
                            
                        except ValueError as er:
                            er = ('expected a valid "time duration" but got {}:{} Hours.'.format(v2.get(), v3.get()))
                            messagebox.showerror('Error in row 2', str(er)+'\n'+'\nHint:\ntime duration must be a non zero positive integer.')
                            check2 = 1
                            
                        if check2 == 0:
                            if len(v4.get()) < 5:
                                messagebox.showerror('Error in row 3', 'Expected a valid Seminar Title but got '+str(self.ea4.get())+'\n'+'\nHint:\nPlease specify thr Seminae Title of max 5 characters.')
                                
                            else:
                                book_win(data)

        def click(b):
            
            if len(str(v2.get())) < 2:
                
                if len(str(v3.get())) < 2:
                    duration = '0'+str(v2.get())+':0'+str(v3.get())+':00'
                else:
                    duration = '0'+str(v2.get())+':'+str(v3.get())+':00'
                    
            else:
                
                if len(str(v3.get())) < 2:
                    duration = str(v2.get())+':0'+str(v3.get())+':00'
                else:
                    duration = str(v2.get())+':'+str(v3.get())+':00'

            r = b['text']
            value = [r, int(v1.get()), duration, str(v4.get()), 'Booked', 0]
            m = messagebox.askyesno('Confirmation', 'Are you sure ?\nDo you really want to book Room Number {} ?'.format(r))
            
            if m:
                curs.execute('''UPDATE booking
                                SET last = ?
                                WHERE last = ?''', [1, 0])
                
                curs.execute('''INSERT INTO booking (room_no, no_stu, dur, title, book, last)
                                VALUES (?, ?, ?, ?, ?, ?)''', value)
                conn.commit()
                
                messagebox.showinfo('Success', ' Room Number {} is now successfully Booked.'.format(r))
                self.book()

        def book_win( data ):
            self.frame61 = tkinter.Frame(self.master, bg=self.back_color)
            self.frame61.grid(row=0, column=0, rowspan=12, columnspan=6)
            self.frame6.destroy()
            
            tkinter.Button(self.frame61, text='Back', cursor='hand2', command=self.book).grid(row=0, column=0, sticky='W')
            tkinter.Label(self.frame61, bg=self.back_color, text="AVAILABILITY", font=(self.t, 25, self.b, self.i, 'underline'), fg=self.t_back).grid(row=0, column=0, rowspan=2, columnspan=6)
            tkinter.Label(self.frame61, bg=self.back_color).grid(row=2, column=0)
            
            path = 'C:/Users/ERROR/Downloads/image001.jpg'
            image1 = ImageTk.PhotoImage(Image.open(path))
            self.li = tkinter.Label(self.frame61, image=image1, bg='black')
            self.li.image = image1
            self.li.grid(row=3, column=0, rowspan=2, columnspan=6, pady=10)
            tkinter.Label(self.frame61, bg=self.back_color).grid(row=4, column=0)

            curs.execute('''SELECT room_no
                            FROM booking''')
            data1 = curs.fetchall()
            data3 = []
            flag = 1
            for i in range(len(data)):
                for j in range(len(data1)):
                    if data[i][0] == data1[j][0]:
                        flag = 0
                        break
                    else:
                        flag=1
                if flag == 1:
                    data3.append((data[i][0], data[i][1]))
            
            i = k = 0
            data3.sort()
            for i in range(len(data3)):
                
                if data3[i][1] >= int(v1.get()):
                    
                    if k % 3 == 0:
                        b = tkinter.Button(self.frame61, text=data3[i][0], cursor='hand2')
                        b.config(command=lambda a=b: click(a))
                        b.grid(row=5+k, column=0, ipadx=30)
                        
                    elif k % 3 == 1:
                        b = tkinter.Button(self.frame61, text=data3[i][0], cursor='hand2')
                        b.config(command=lambda a=b: click(a))
                        b.grid(row=4+k, column=2, ipadx=30)
                        
                    elif k % 3 == 2:
                        b = tkinter.Button(self.frame61, text=data3[i][0], cursor='hand2')
                        b.config(command=lambda a=b:click(a))
                        b.grid(row=3+k, column=4, ipadx=30)
                        tkinter.Label(self.frame61, bg=self.back_color).grid(row=4+k, column=0)
                    k += 1
                else:
                    pass
                    
            for k in range(10):
                tkinter.Label(self.frame61, bg=self.back_color).grid(row=i+k+5, column=6)
            try:
                del(i, k)
            except:
                pass
                
        try:
            self.frame61.destroy()
            self.b.destroy()
            self.li.destroy()
        except:
            pass

        v1 = tkinter.IntVar()
        v2 = tkinter.IntVar()
        v3 = tkinter.IntVar()
        v4 = tkinter.StringVar()
        
        curs.execute('''SELECT *
                            FROM rooms''')
        data = curs.fetchall()
        
        self.frame6 = tkinter.Frame(self.master, bg=self.back_color)
        self.frame6.grid(row=0, column=0, rowspan=12, columnspan=6)
        self.frame1.destroy()
        tkinter.Button(self.frame6, text='Back', cursor='hand2', command=self.formation).grid(row=0, column=0, sticky='W')
        tkinter.Label(self.frame6, bg=self.back_color, text="BOOKINGS", font=(self.t, 25, self.b, self.i, 'underline'), fg=self.t_back).grid(row=0, column=0, rowspan=2, columnspan=6)
        
        path = 'C:/Users/ERROR/Downloads/image001.jpg'
        image1 = ImageTk.PhotoImage(Image.open(path))
        self.li = tkinter.Label(self.frame6, image=image1, bg='black')
        self.li.image = image1
        self.li.grid(row=2, column=0, rowspan=2, columnspan=6, pady=10)
        
        tkinter.Label(self.frame6, bg=self.back_color).grid(row=4, column=0)
        tkinter.Label(self.frame6, bg=self.back_color, text='Enter Number Of Students To Be Seated :', font=(self.t2, 12, self.b2, self.i2)).grid(row=5, column=0, sticky='E')
        self.ea1 = tkinter.Entry(self.frame6, bg='khaki3', textvariable=v1, relief='sunken', bd=2)
        self.ea1.grid(row=5, column=1, columnspan=3, sticky='WE')
        self.ea1.bind('<Button-1>', self.on_click)
        
        tkinter.Label(self.frame6, bg=self.back_color).grid(row=7, column=0)
        tkinter.Label(self.frame6, bg=self.back_color, text='Enter The Duration Of The Seminar :', font=(self.t2, 12, self.b2, self.i2)).grid(row=8, column=0, sticky='E')
        tkinter.Label(self.frame6, bg=self.back_color, text='Hr.', font=(10)).grid(row=8, column=2)
        tkinter.Label(self.frame6, bg=self.back_color, text='Min.', font=(10)).grid(row=8, column=4)
        
        self.ea2 = tkinter.Entry(self.frame6, bg='khaki3', textvariable=v2, relief='sunken', bd=2)
        self.ea2.grid(row=8, column=1, columnspan=1, sticky='WE')
        self.ea2.bind('<Button-1>', self.on_click)
        
        self.ea3 = tkinter.Entry(self.frame6, bg='khaki3', textvariable=v3, relief='sunken', bd=2)
        self.ea3.grid(row=8, column=3, columnspan=1, sticky='WE')
        self.ea3.bind('<Button-1>', self.on_click)
        
        tkinter.Label(self.frame6, bg=self.back_color).grid(row=9, column=0)
        tkinter.Label(self.frame6, bg=self.back_color, text='Enter The Title Of Seminar :', font=(self.t2, 12, self.b2, self.i2)).grid(row=10, column=0, sticky='E')
        
        self.ea4 = tkinter.Entry(self.frame6, bg='khaki3', textvariable=v4, relief='sunken', bd=2)
        self.ea4.grid(row=10, column=1, columnspan=3, sticky='WE')
        self.ea4.bind('<Button-1>', self.on_click) 
        tkinter.Label(self.frame6, bg=self.back_color, text='(*minimum length of 5 characters long)', font=(self.t2, 9, self.b2, self.i2)).grid(row=11, column=1, sticky='WE')
        tkinter.Label(self.frame6, bg=self.back_color).grid(row=12, column=0)

        tkinter.Button(self.frame6, text='Confirm', cursor='hand2', command=check_func).grid(row=13, column=1, pady=10, sticky='W')
        #self.ba1=tkinter.Button(self.frame6, text='Exit', command=self.exit, cursor='hand2')
        #self.ba1.grid(row=12, column=2, sticky='W')

        for i in range(14, 15):
            tkinter.Label(self.frame6, bg=self.back_color).grid(row=i, column=0)
        del(i)

    def status(self):
        
        self.frame7 = tkinter.Frame(self.master, bg=self.back_color)
        self.frame7.grid(row=0, column=0, rowspan=12, columnspan=6)
        self.frame1.destroy()
        
        tkinter.Button(self.frame7, text='Back', cursor='hand2', command=self.formation).grid(row=0, column=0, sticky='W')
        tkinter.Label(self.frame7, bg=self.back_color, text="SYSTEM STATUS", font=(self.t, 25, self.b, self.i, 'underline'), fg=self.t_back).grid(row=0, column=0, rowspan=2, columnspan=6)

        path = 'C:/Users/ERROR/Downloads/image001.jpg'
        image1 = ImageTk.PhotoImage(Image.open(path))
        self.li = tkinter.Label(self.frame7, image=image1, bg='black')
        self.li.image = image1
        self.li.grid(row=2, column=0, rowspan=2, columnspan=6, pady=10)
        #tkinter.Label(self.frame7, bg=self.back_color).grid(row=4, column=0)
        
        #self.la1=tkinter.Label(self.frame7, text='S.No.', bg=self.back_color).grid(row=5, column=0)
        tkinter.Label(self.frame7, text='Room No.', bg=self.back_color, font=(self.t2, 12, self.b2, self.i2)).grid(row=5, column=0)
        tkinter.Label(self.frame7, text='No. Of Students', bg=self.back_color, font=(self.t2, 12, self.b2, self.i2)).grid(row=5, column=1)
        tkinter.Label(self.frame7, text='Duration', bg=self.back_color, font=(self.t2, 12, self.b2, self.i2)).grid(row=5, column=2)
        tkinter.Label(self.frame7, text='Title', bg=self.back_color, font=(self.t2, 12, self.b2, self.i2)).grid(row=5, column=3, columnspan=2)
        tkinter.Label(self.frame7, text='Availability', bg=self.back_color, font=(self.t2, 12, self.b2, self.i2)).grid(row=5, column=5)
        
        curs.execute('''SELECT *
                        FROM rooms''')
        data1 = curs.fetchall()
        data1.sort()
        
        curs.execute('''SELECT *
                        FROM booking''')
        data2 = curs.fetchall()
        data2.sort()
        
        flag1 = i = 0
        for i in range(len(data1)):
            #self.la1=tkinter.Label(self.frame7, text=i+1, bg=self.back_color).grid(row=6+i, column=0)
            for j in range(len(data2)):
                
                if data1[i][0] == data2[j][0]:
                    flag1 = 1
                    break
                
                else:
                    flag1 = 0
                    
            if flag1 == 1:
                tkinter.Label(self.frame7, text=data1[i][0], bg=self.back_color, fg='red', font=(self.t2, 9, self.b2, self.i2)).grid(row=6+i, column=0)
                tkinter.Label(self.frame7, text=data2[j][1], bg=self.back_color, fg='red', font=(self.t2, 9, self.b2, self.i2)).grid(row=6+i, column=1)
                tkinter.Label(self.frame7, text=data2[j][2], bg=self.back_color, fg='red', font=(self.t2, 9, self.b2, self.i2)).grid(row=6+i, column=2)
                ttk.Label(self.frame7, text=data2[j][3], wraplength=100, foreground='red', font=(self.t2, 9, self.b2, self.i2), background=self.back_color).grid(row=6+i, column=3, columnspan=2)
                tkinter.Label(self.frame7, text='Booked', bg=self.back_color, fg='red', font=(self.t2, 9, self.b2, self.i2)).grid(row=6+i, column=5)
                
            else:
                tkinter.Label(self.frame7, text=data1[i][0], bg=self.back_color, fg='green', font=(self.t2, 9, self.b2, self.i2)).grid(row=6+i, column=0)
                tkinter.Label(self.frame7, text=data1[i][1], bg=self.back_color, fg='green', font=(self.t2, 9, self.b2, self.i2)).grid(row=6+i, column=1)
                tkinter.Label(self.frame7, text='-', bg=self.back_color, fg='green', font=(self.t2, 9, self.b2, self.i2)).grid(row=6+i, column=2)
                tkinter.Label(self.frame7, text='-', bg=self.back_color, fg='green', font=(self.t2, 9, self.b2, self.i2)).grid(row=6+i, column=3, columnspan=2)
                tkinter.Label(self.frame7, text='Available', bg=self.back_color, fg='green', font=(self.t2, 9, self.b2, self.i2)).grid(row=6+i, column=5)

        for k in range(2):
                tkinter.Label(self.frame7, bg=self.back_color).grid(row=7+i+k, column=0)
                
        try:
            del(i, j, k, data1, data2, flag1)
        except:
            del(k, data1, data2, flag1)

    def replace(self):
        
        def rep_func():
            curs.execute('''SELECT  * FROM rooms''')
            data = curs.fetchall()

            if data == []:
                messagebox.showerror('Error','Database is Empty !!!')
            else:
                for i in range(len(data)):
                    if v1.get() == data[i][0]:
                        flag1 = 1
                        if v3.get() == data[i][1]:
                            flag2 = 1
                        else:
                            flag2 = 0
                        break
                    else:
                        flag1 = 0
                for j in range(len(data)):
                    if v2.get() == data[i][0]:
                        flag3 = 1
                        break
                    else:
                        flag3 = 0
                if flag1 == 1:
                    if flag3 == 1:
                        if v1.get() == v2.get():
                            if flag2 == 1:
                                messagebox.showerror('Error','New Room already exists !!!')
                            else:
                                if v3.get() > 0:
                                    curs.execute('''UPDATE rooms
                                                    SET no_stu = ?
                                                    WHERE room_no = ?''',[v3.get(),v1.get()])
                                    conn.commit()
                                else:
                                    curs.execute('''UPDATE rooms
                                                    SET room_no = ?
                                                    WHERE room_no = ?''',[v2.get(),v1.get()])
                                    conn.commit()
                    else:
                        curs.execute('''UPDATE rooms
                                        SET room_no = ?, no_stu = ?
                                        WHERE room_no = ?''',[v2.get(),v3.get(),v1.get()])
                        conn.commit()
                else:
                    messagebox.showerror('Error','Can not Replace !!!\n\nRoom Number {} does not exists !!!'.format(v1.get()))

        def rep_check():

            try:
                v1.get() == int()
                v2.get() == int()
                flag = 0

            except tkinter.TclError as err:
                messagebox.showerror('Alert', str(err))
                flag = 1

            if flag == 0:
                flag2 = 1
                if v1.get() < 1:
                    flag2 = 0
                if v2.get() < 1:
                    flag2 = 0
                if flag2 == 0:
                    messagebox.showerror('Error','Values must be non zero positive integer.')
                if flag2 == 1:
                    rep_func()

        v1 = tkinter.IntVar()
        v2 = tkinter.IntVar()
        v3 = tkinter.IntVar()
        
        self.frame8 = tkinter.Frame(self.master, bg=self.back_color)
        self.frame8.grid(row=0, column=0, rowspan=12, columnspan=6)
        self.frame1.destroy()
        
        tkinter.Button(self.frame8, text='Back', cursor='hand2', command=self.formation).grid(row=0, column=0, sticky='W')
        tkinter.Label(self.frame8, bg=self.back_color, text="ROOM REPLACEMENT", font=(self.t, 25, self.b, self.i, 'underline'), fg=self.t_back).grid(row=0, column=1, rowspan=2, columnspan=4)

        path = 'C:/Users/ERROR/Downloads/image001.jpg'
        image1 = ImageTk.PhotoImage(Image.open(path))
        self.li = tkinter.Label(self.frame8, image=image1, bg='black')
        self.li.image = image1
        self.li.grid(row=2, column=0, rowspan=2, columnspan=6, pady=10)

        tkinter.Label(self.frame8, bg=self.back_color).grid(row=4, column=0)
        tkinter.Label(self.frame8, text='Room Number to be Deleted :', bg=self.back_color, font=(self.t2, 12, self.b2, self.i2)).grid(row=5, column=0, columnspan=3, sticky='WE')
        self.ea1 = tkinter.Entry(self.frame8, bg='khaki3', textvariable=v1, relief='sunken', bd=2)
        self.ea1.grid(row=5, column=3, columnspan=2, sticky='WE')
        self.ea1.bind('<Button-1>', self.on_click)
        
        tkinter.Label(self.frame8, bg=self.back_color).grid(row=6, column=0)
        tkinter.Label(self.frame8, text='New Room Number to be Added :', bg=self.back_color, font=(self.t2, 12, self.b2, self.i2)).grid(row=7, column=0, rowspan=1, columnspan=3, sticky='WE')
        self.ea2 = tkinter.Entry(self.frame8, bg='khaki3', textvariable=v2, relief='sunken', bd=2)
        self.ea2.grid(row=7, column=3, rowspan=1, columnspan=2, sticky='WE')
        self.ea2.bind('<Button-1>', self.on_click)
        
        tkinter.Label(self.frame8, bg=self.back_color).grid(row=8, column=0)
        tkinter.Label(self.frame8, text='Number of Students for the new Room :', bg=self.back_color, font=(self.t2, 12, self.b2, self.i2)).grid(row=9, column=0, rowspan=1, columnspan=3, sticky='WE')
        self.ea3 = tkinter.Entry(self.frame8, bg='khaki3', textvariable=v3, relief='sunken', bd=2)
        self.ea3.grid(row=9, column=3, rowspan=1, columnspan=2, sticky='WE')
        self.ea3.bind('<Button-1>', self.on_click)
        
        tkinter.Label(self.frame8, bg=self.back_color).grid(row=10, column=0)
        tkinter.Button(self.frame8, text='Confirm', cursor='hand2', command=rep_check).grid(row=11, column=3, pady=10, sticky='W')
        #self.ba1=tkinter.Button(self.frame8, text='Exit', command=self.exit, cursor='hand2')
        #self.ba1.grid(row=10, column=4, sticky='W')
        tkinter.Label(self.frame8, bg=self.back_color).grid(row=11, column=0)
        tkinter.Label(self.frame8, bg=self.back_color).grid(row=12, column=0)
        #tkinter.Label(self.frame8, bg=self.back_color).grid(row=13, column=0)
        #tkinter.Label(self.frame8, bg=self.back_color).grid(row=14, column=0)

    def customize(self):
        def t_color():
            self.frame91 = tkinter.Frame(self.master, bg=self.back_color)
            self.frame91.grid(row=0, column=0, rowspan=12, columnspan=6, sticky='WESN')
            self.frame9.destroy()

            tkinter.Button(self.frame91, text='Back', cursor='hand2', command=self.customize).grid(row=0, column=0, sticky='W')
            tkinter.Label(self.frame91, bg=self.back_color, text="TITLE TEXT CUSTOMISATION", font=(self.t, 25, self.b, self.i, 'underline'), fg=self.t_back).grid(row=0, column=0, rowspan=2, columnspan=6)

            path = 'C:/Users/ERROR/Downloads/image001.jpg'
            image1 = ImageTk.PhotoImage(Image.open(path))
            self.li = tkinter.Label(self.frame91, image=image1, bg='black')
            self.li.image = image1
            self.li.grid(row=3, column=0, rowspan=2, columnspan=6, pady=10)

            tkinter.Label(self.frame91,  bg=self.back_color).grid(row=5, column=0)
            f = tkinter.Frame(self.frame91, width=3)
            f.grid(row=2, column=0, columnspan=8, rowspan=10, pady=30, padx=30)

            tkinter.Label(self.frame91, text='Text', font=(self.t, 50), fg=self.t_back, bg='white').grid(row=6, column=1, rowspan=3, columnspan=1, sticky='EW')
            tkinter.Label(self.frame91, text=self.t_back, font=(self.t, 10), bg='white').grid(row=7, column=1, rowspan=3, columnspan=1, sticky='EW')

            COLORS = ['snow',  'ghost white',  'white smoke',  'gainsboro',  'floral white',  'old lace', 
                      'linen',  'antique white',  'papaya whip',  'blanched almond',  'bisque',  'peach puff', 
                      'navajo white',  'lemon chiffon',  'mint cream',  'azure',  'alice blue',  'lavender', 
                      'lavender blush',  'misty rose',  'dark slate gray',  'dim gray',  'slate gray', 
                      'light slate gray',  'gray',  'light grey',  'midnight blue',  'navy',  'cornflower blue',  'dark slate blue', 
                      'slate blue',  'medium slate blue',  'light slate blue',  'medium blue',  'royal blue',   self.t_back, 
                      'dodger blue',  'deep sky blue',  'sky blue',  'light sky blue',  'steel blue',  'light steel blue', 
                      'light blue',  'powder blue',  'pale turquoise',  'dark turquoise',  'medium turquoise',  'turquoise', 
                      'cyan',  'light cyan',  'cadet blue',  'medium aquamarine',  'aquamarine',  'dark green',  'dark olive green', 
                      'dark sea green',  'sea green',  'medium sea green',  'light sea green',  'pale green',  'spring green', 
                      'lawn green',  'medium spring green',  'green yellow',  'lime green',  'yellow green', 
                      'forest green',  'olive drab',  'dark khaki',  'khaki',  'pale goldenrod',  'light goldenrod yellow', 
                      'light yellow',  'yellow',  'gold',  'light goldenrod',  'goldenrod',  'dark goldenrod',  'rosy brown', 
                      'indian red',  'saddle brown',  'sandy brown', 
                      'dark salmon',  'salmon',  'light salmon',  'orange',  'dark orange', 
                      'coral',  'light coral',  'tomato',  'orange red',  'red',  'hot pink',  'deep pink',  'pink',  'light pink', 
                      'pale violet red',  'maroon',  'medium violet red',  'violet red', 
                      'medium orchid',  'dark orchid',  'dark violet',  'blue violet',  'purple',  'medium purple', 
                      'thistle',  'snow2',  'snow3', 
                      'snow4',  'seashell2',  'seashell3',  'seashell4',  'AntiqueWhite1',  'AntiqueWhite2', 
                      'AntiqueWhite3',  'AntiqueWhite4',  'bisque2',  'bisque3',  'bisque4',  'PeachPuff2', 
                      'PeachPuff3',  'PeachPuff4',  'NavajoWhite2',  'NavajoWhite3',  'NavajoWhite4', 
                      'LemonChiffon2',  'LemonChiffon3',  'LemonChiffon4',  'cornsilk2',  'cornsilk3', 
                      'cornsilk4',  'ivory2',  'ivory3',  'ivory4',  'honeydew2',  'honeydew3',  'honeydew4', 
                      'LavenderBlush2',  'LavenderBlush3',  'LavenderBlush4',  'MistyRose2',  'MistyRose3', 
                      'MistyRose4',  'azure2',  'azure3',  'azure4',  'SlateBlue1',  'SlateBlue2',  'SlateBlue3', 
                      'SlateBlue4',  'RoyalBlue1',  'RoyalBlue2',  'RoyalBlue3',  'RoyalBlue4',  'blue2',  'blue4',
                      'DodgerBlue2',  'DodgerBlue3',  'DodgerBlue4',  'SteelBlue1',  'SteelBlue2', 
                      'SteelBlue3',  'SteelBlue4',  'DeepSkyBlue2',  'DeepSkyBlue3',  'DeepSkyBlue4', 
                      'SkyBlue1',  'SkyBlue2',  'SkyBlue3',  'SkyBlue4',  'LightSkyBlue1',  'LightSkyBlue2', 
                      'LightSkyBlue3',  'LightSkyBlue4',  'SlateGray1',  'SlateGray2',  'SlateGray3', 
                      'SlateGray4',  'LightSteelBlue1',  'LightSteelBlue2',  'LightSteelBlue3', 
                      'LightSteelBlue4',  'LightBlue1',  'LightBlue2',  'LightBlue3',  'LightBlue4', 
                      'LightCyan2',  'LightCyan3',  'LightCyan4',  'PaleTurquoise1',  'PaleTurquoise2', 
                      'PaleTurquoise3',  'PaleTurquoise4',  'CadetBlue1',  'CadetBlue2',  'CadetBlue3', 
                      'CadetBlue4',  'turquoise1',  'turquoise2',  'turquoise3',  'turquoise4',  'cyan2',  'cyan3', 
                      'cyan4',  'DarkSlateGray1',  'DarkSlateGray2',  'DarkSlateGray3',  'DarkSlateGray4', 
                      'aquamarine2',  'aquamarine4',  'DarkSeaGreen1',  'DarkSeaGreen2',  'DarkSeaGreen3', 
                      'DarkSeaGreen4',  'SeaGreen1',  'SeaGreen2',  'SeaGreen3',  'PaleGreen1',  'PaleGreen2', 
                      'PaleGreen3',  'PaleGreen4',  'SpringGreen2',  'SpringGreen3',  'SpringGreen4', 
                      'green2',  'green3',  'green4',  'chartreuse2',  'chartreuse3',  'chartreuse4', 
                      'OliveDrab1',  'OliveDrab2',  'OliveDrab4',  'DarkOliveGreen1',  'DarkOliveGreen2', 
                      'DarkOliveGreen3',  'DarkOliveGreen4',  'khaki1',  'khaki2',  'khaki3',  'khaki4', 
                      'LightGoldenrod1',  'LightGoldenrod2',  'LightGoldenrod3',  'LightGoldenrod4', 
                      'LightYellow2',  'LightYellow3',  'LightYellow4',  'yellow2',  'yellow3',  'yellow4', 
                      'gold2',  'gold3',  'gold4',  'goldenrod1',  'goldenrod2',  'goldenrod3',  'goldenrod4', 
                      'DarkGoldenrod1',  'DarkGoldenrod2',  'DarkGoldenrod3',  'DarkGoldenrod4', 
                      'RosyBrown1',  'RosyBrown2',  'RosyBrown3',  'RosyBrown4',  'IndianRed1',  'IndianRed2', 
                      'IndianRed3',  'IndianRed4',  'sienna1',  'sienna2',  'sienna3',  'sienna4',  'burlywood1', 
                      'burlywood2',  'burlywood3',  'burlywood4',  'wheat1',  'wheat2',  'wheat3',  'wheat4',  'tan1', 
                      'tan2',  'tan4',  'chocolate1',  'chocolate2',  'chocolate3',  'firebrick1',  'firebrick2', 
                      'firebrick3',  'firebrick4',  'brown1',  'brown2',  'brown3',  'brown4',  'salmon1',  'salmon2', 
                      'salmon3',  'salmon4',  'LightSalmon2',  'LightSalmon3',  'LightSalmon4',  'orange2', 
                      'orange3',  'orange4',  'DarkOrange1',  'DarkOrange2',  'DarkOrange3',  'DarkOrange4', 
                      'coral1',  'coral2',  'coral3',  'coral4',  'tomato2',  'tomato3',  'tomato4',  'OrangeRed2', 
                      'OrangeRed3',  'OrangeRed4',  'red2',  'red3',  'red4',  'DeepPink2',  'DeepPink3',  'DeepPink4', 
                      'HotPink1',  'HotPink2',  'HotPink3',  'HotPink4',  'pink1',  'pink2',  'pink3',  'pink4', 
                      'LightPink1',  'LightPink2',  'LightPink3',  'LightPink4',  'PaleVioletRed1', 
                      'PaleVioletRed2',  'PaleVioletRed3',  'PaleVioletRed4',  'maroon1',  'maroon2', 
                      'maroon3',  'maroon4',  'VioletRed1',  'VioletRed2',  'VioletRed3',  'VioletRed4', 
                      'magenta2',  'magenta3',  'magenta4',  'orchid1',  'orchid2',  'orchid3',  'orchid4',  'plum1', 
                      'plum2',  'plum3',  'plum4',  'MediumOrchid1',  'MediumOrchid2',  'MediumOrchid3', 
                      'MediumOrchid4',  'DarkOrchid1',  'DarkOrchid2',  'DarkOrchid3',  'DarkOrchid4', 
                      'purple1',  'purple2',  'purple3',  'purple4',  'MediumPurple1',  'MediumPurple2', 
                      'MediumPurple3',  'MediumPurple4',  'thistle1',  'thistle2',  'thistle3',  'thistle4', 
                      'gray1',  'gray2',  'gray3',  'gray4',  'gray5',  'gray6',  'gray7',  'gray8',  'gray9',  'gray10', 
                      'gray11',  'gray12',  'gray13',  'gray14',  'gray15',  'gray16',  'gray17',  'gray18',  'gray19', 
                      'gray20',  'gray21',  'gray22',  'gray23',  'gray24',  'gray25',  'gray26',  'gray27',  'gray28', 
                      'gray29',  'gray30',  'gray31',  'gray32',  'gray33',  'gray34',  'gray35',  'gray36',  'gray37', 
                      'gray38',  'gray39',  'gray40',  'gray42',  'gray43',  'gray44',  'gray45',  'gray46',  'gray47', 
                      'gray48',  'gray49',  'gray50',  'gray51',  'gray52',  'gray53',  'gray54',  'gray55',  'gray56', 
                      'gray57',  'gray58',  'gray59',  'gray60',  'gray61',  'gray62',  'gray63',  'gray64',  'gray65', 
                      'gray66',  'gray67',  'gray68',  'gray69',  'gray70',  'gray71',  'gray72',  'gray73',  'gray74', 
                      'gray75',  'gray76',  'gray77',  'gray78',  'gray79',  'gray80',  'gray81',  'gray82',  'gray83', 
                      'gray84',  'gray85',  'gray86',  'gray87',  'gray88',  'gray89',  'gray90',  'gray91',  'gray92', 
                      'gray93',  'gray94',  'gray95',  'gray97',  'gray98',  'gray99', 'white']

            frame911=tkinter.Frame(self.frame91, bd=5, relief='sunken')
            frame911.grid(row=6, column=3, rowspan=3)

            canvas = tkinter.Canvas(frame911, height=300, width=300, scrollregion=(0, 0, 400, 800), bg='black')
            inner_frame = tkinter.Frame(canvas, bg='black')
            canvas.create_window(0, 0, anchor="nw", window=inner_frame, tags=("frame", ))

            def confirm():
                m = messagebox.askyesno('Confirm', 'Do you want to save the changes ?')
                if m:
                    self.t_back = self.back_t

                    curs.execute('''UPDATE custom
                                    SET background = ?
                                    WHERE text_t = ?''', [self.back_color, 'title'])
                    conn.commit()
                    messagebox.showinfo('Success', 'Title Text Color is now {}'.format(self.t_back))
                    self.customize()

            r = c = 0
            max_c = 24

            def click(l):
                self.back_t = l
                tkinter.Label(self.frame91, text='Text', font=(self.t, 50), fg=l, bg='white').grid(row=6, column=1, rowspan=3, columnspan=1, sticky='EW')
                tkinter.Label(self.frame91, text=l, font=(self.t, 10), bg='white').grid(row=7, column=1, rowspan=3, columnspan=1, sticky='EW')

            for i in COLORS:
                t = tkinter.Button(inner_frame, bg=i, width=2, command=lambda i=i: click(i))
                t.grid(row=r, column=c)
                c += 1
                if c == max_c:
                    r += 1
                    c = 0

            tkinter.Label(self.frame91, bg=self.back_color).grid(row=20, column=0)
            s_hor = tkinter.Scrollbar(frame911, command=canvas.xview, orient='horizontal')
            s_ver = tkinter.Scrollbar(frame911, command=canvas.yview, orient='vertical')

            canvas['yscrollcommand'] = s_ver.set
            canvas['xscrollcommand'] = s_hor.set
            s_hor.pack(side='bottom', fill='x')
            s_ver.pack( side = 'right', fill='y')
            canvas.pack(side='left', fill='both')

            def on_configure(*args):
                canvas.itemconfigure("frame")
                canvas.configure(scrollregion=canvas.bbox("all"))

            canvas.bind("<Configure>", on_configure)
            tkinter.Button(self.frame91, text='confirm', command=confirm, cursor='hand2').grid(row=9, column=1, sticky='W')
            tkinter.Button(self.frame91, text='cancel', command=self.customize, cursor='hand2').grid(row=9, column=1, sticky='E')

        def b_color():
            self.frame91 = tkinter.Frame(self.master, bg=self.back_color)
            self.frame91.grid(row=0, column=0, rowspan=12, columnspan=6, sticky='WESN')
            self.frame9.destroy()

            tkinter.Button(self.frame91, text='Back', cursor='hand2', command=self.customize).grid(row=0, column=0, sticky='W')
            tkinter.Label(self.frame91, bg=self.back_color, text="TITLE TEXT CUSTOMISATION", font=(self.t, 25, self.b, self.i, 'underline'), fg=self.t_back).grid(row=0, column=0, rowspan=2, columnspan=6)

            path = 'C:/Users/ERROR/Downloads/image001.jpg'
            image1 = ImageTk.PhotoImage(Image.open(path))
            self.li = tkinter.Label(self.frame91, image=image1, bg='black')
            self.li.image = image1
            self.li.grid(row=3, column=0, rowspan=2, columnspan=6, pady=10)

            tkinter.Label(self.frame91, bg=self.back_color).grid(row=5, column=0)
            f = tkinter.Frame(self.frame91,  width=3)
            f.grid(row=2, column=0, columnspan=8, rowspan=10, pady=30, padx=30)

            tkinter.Label(self.frame91, text='Text', font=(self.t, 50), bg=self.back_color).grid(row=6, column=1 , rowspan=3, columnspan=1, sticky='EW')
            tkinter.Label(self.frame91, text=self.back_color, font=(self.t, 10), bg='white').grid(row=7, column=1, rowspan=3, columnspan=1, sticky='EW')

            COLORS = ['snow',  'ghost white',  'white smoke',  'gainsboro',  'floral white',  'old lace', 
                      'linen',  'antique white',  'papaya whip',  'blanched almond',  'bisque',  'peach puff', 
                      'navajo white',  'lemon chiffon',  'mint cream',  'azure',  'alice blue',  'lavender', 
                      'lavender blush',  'misty rose',  'dark slate gray',  'dim gray',  'slate gray', 
                      'light slate gray',  'gray',  'light grey',  'midnight blue',  'navy',  'cornflower blue',  'dark slate blue', 
                      'slate blue',  'medium slate blue',  'light slate blue',  'medium blue',  'royal blue',   self.t_back, 
                      'dodger blue',  'deep sky blue',  'sky blue',  'light sky blue',  'steel blue',  'light steel blue', 
                      'light blue',  'powder blue',  'pale turquoise',  'dark turquoise',  'medium turquoise',  'turquoise', 
                      'cyan',  'light cyan',  'cadet blue',  'medium aquamarine',  'aquamarine',  'dark green',  'dark olive green', 
                      'dark sea green',  'sea green',  'medium sea green',  'light sea green',  'pale green',  'spring green', 
                      'lawn green',  'medium spring green',  'green yellow',  'lime green',  'yellow green', 
                      'forest green',  'olive drab',  'dark khaki',  'khaki',  'pale goldenrod',  'light goldenrod yellow', 
                      'light yellow',  'yellow',  'gold',  'light goldenrod',  'goldenrod',  'dark goldenrod',  'rosy brown', 
                      'indian red',  'saddle brown',  'sandy brown', 
                      'dark salmon',  'salmon',  'light salmon',  'orange',  'dark orange', 
                      'coral',  'light coral',  'tomato',  'orange red',  'red',  'hot pink',  'deep pink',  'pink',  'light pink', 
                      'pale violet red',  'maroon',  'medium violet red',  'violet red', 
                      'medium orchid',  'dark orchid',  'dark violet',  'blue violet',  'purple',  'medium purple', 
                      'thistle',  'snow2',  'snow3', 
                      'snow4',  'seashell2',  'seashell3',  'seashell4',  'AntiqueWhite1',  'AntiqueWhite2', 
                      'AntiqueWhite3',  'AntiqueWhite4',  'bisque2',  'bisque3',  'bisque4',  'PeachPuff2', 
                      'PeachPuff3',  'PeachPuff4',  'NavajoWhite2',  'NavajoWhite3',  'NavajoWhite4', 
                      'LemonChiffon2',  'LemonChiffon3',  'LemonChiffon4',  'cornsilk2',  'cornsilk3', 
                      'cornsilk4',  'ivory2',  'ivory3',  'ivory4',  'honeydew2',  'honeydew3',  'honeydew4', 
                      'LavenderBlush2',  'LavenderBlush3',  'LavenderBlush4',  'MistyRose2',  'MistyRose3', 
                      'MistyRose4',  'azure2',  'azure3',  'azure4',  'SlateBlue1',  'SlateBlue2',  'SlateBlue3', 
                      'SlateBlue4',  'RoyalBlue1',  'RoyalBlue2',  'RoyalBlue3',  'RoyalBlue4',  'blue2',  'blue4', 
                      'DodgerBlue2',  'DodgerBlue3',  'DodgerBlue4',  'SteelBlue1',  'SteelBlue2', 
                      'SteelBlue3',  'SteelBlue4',  'DeepSkyBlue2',  'DeepSkyBlue3',  'DeepSkyBlue4', 
                      'SkyBlue1',  'SkyBlue2',  'SkyBlue3',  'SkyBlue4',  'LightSkyBlue1',  'LightSkyBlue2', 
                      'LightSkyBlue3',  'LightSkyBlue4',  'SlateGray1',  'SlateGray2',  'SlateGray3', 
                      'SlateGray4',  'LightSteelBlue1',  'LightSteelBlue2',  'LightSteelBlue3', 
                      'LightSteelBlue4',  'LightBlue1',  'LightBlue2',  'LightBlue3',  'LightBlue4', 
                      'LightCyan2',  'LightCyan3',  'LightCyan4',  'PaleTurquoise1',  'PaleTurquoise2', 
                      'PaleTurquoise3',  'PaleTurquoise4',  'CadetBlue1',  'CadetBlue2',  'CadetBlue3', 
                      'CadetBlue4',  'turquoise1',  'turquoise2',  'turquoise3',  'turquoise4',  'cyan2',  'cyan3', 
                      'cyan4',  'DarkSlateGray1',  'DarkSlateGray2',  'DarkSlateGray3',  'DarkSlateGray4', 
                      'aquamarine2',  'aquamarine4',  'DarkSeaGreen1',  'DarkSeaGreen2',  'DarkSeaGreen3', 
                      'DarkSeaGreen4',  'SeaGreen1',  'SeaGreen2',  'SeaGreen3',  'PaleGreen1',  'PaleGreen2', 
                      'PaleGreen3',  'PaleGreen4',  'SpringGreen2',  'SpringGreen3',  'SpringGreen4', 
                      'green2',  'green3',  'green4',  'chartreuse2',  'chartreuse3',  'chartreuse4', 
                      'OliveDrab1',  'OliveDrab2',  'OliveDrab4',  'DarkOliveGreen1',  'DarkOliveGreen2', 
                      'DarkOliveGreen3',  'DarkOliveGreen4',  'khaki1',  'khaki2',  'khaki3',  'khaki4', 
                      'LightGoldenrod1',  'LightGoldenrod2',  'LightGoldenrod3',  'LightGoldenrod4', 
                      'LightYellow2',  'LightYellow3',  'LightYellow4',  'yellow2',  'yellow3',  'yellow4', 
                      'gold2',  'gold3',  'gold4',  'goldenrod1',  'goldenrod2',  'goldenrod3',  'goldenrod4', 
                      'DarkGoldenrod1',  'DarkGoldenrod2',  'DarkGoldenrod3',  'DarkGoldenrod4', 
                      'RosyBrown1',  'RosyBrown2',  'RosyBrown3',  'RosyBrown4',  'IndianRed1',  'IndianRed2', 
                      'IndianRed3',  'IndianRed4',  'sienna1',  'sienna2',  'sienna3',  'sienna4',  'burlywood1', 
                      'burlywood2',  'burlywood3',  'burlywood4',  'wheat1',  'wheat2',  'wheat3',  'wheat4',  'tan1', 
                      'tan2',  'tan4',  'chocolate1',  'chocolate2',  'chocolate3',  'firebrick1',  'firebrick2', 
                      'firebrick3',  'firebrick4',  'brown1',  'brown2',  'brown3',  'brown4',  'salmon1',  'salmon2', 
                      'salmon3',  'salmon4',  'LightSalmon2',  'LightSalmon3',  'LightSalmon4',  'orange2', 
                      'orange3',  'orange4',  'DarkOrange1',  'DarkOrange2',  'DarkOrange3',  'DarkOrange4', 
                      'coral1',  'coral2',  'coral3',  'coral4',  'tomato2',  'tomato3',  'tomato4',  'OrangeRed2', 
                      'OrangeRed3',  'OrangeRed4',  'red2',  'red3',  'red4',  'DeepPink2',  'DeepPink3',  'DeepPink4', 
                      'HotPink1',  'HotPink2',  'HotPink3',  'HotPink4',  'pink1',  'pink2',  'pink3',  'pink4', 
                      'LightPink1',  'LightPink2',  'LightPink3',  'LightPink4',  'PaleVioletRed1', 
                      'PaleVioletRed2',  'PaleVioletRed3',  'PaleVioletRed4',  'maroon1',  'maroon2', 
                      'maroon3',  'maroon4',  'VioletRed1',  'VioletRed2',  'VioletRed3',  'VioletRed4', 
                      'magenta2',  'magenta3',  'magenta4',  'orchid1',  'orchid2',  'orchid3',  'orchid4',  'plum1', 
                      'plum2',  'plum3',  'plum4',  'MediumOrchid1',  'MediumOrchid2',  'MediumOrchid3', 
                      'MediumOrchid4',  'DarkOrchid1',  'DarkOrchid2',  'DarkOrchid3',  'DarkOrchid4', 
                      'purple1',  'purple2',  'purple3',  'purple4',  'MediumPurple1',  'MediumPurple2', 
                      'MediumPurple3',  'MediumPurple4',  'thistle1',  'thistle2',  'thistle3',  'thistle4', 
                      'gray1',  'gray2',  'gray3',  'gray4',  'gray5',  'gray6',  'gray7',  'gray8',  'gray9',  'gray10', 
                      'gray11',  'gray12',  'gray13',  'gray14',  'gray15',  'gray16',  'gray17',  'gray18',  'gray19', 
                      'gray20',  'gray21',  'gray22',  'gray23',  'gray24',  'gray25',  'gray26',  'gray27',  'gray28', 
                      'gray29',  'gray30',  'gray31',  'gray32',  'gray33',  'gray34',  'gray35',  'gray36',  'gray37', 
                      'gray38',  'gray39',  'gray40',  'gray42',  'gray43',  'gray44',  'gray45',  'gray46',  'gray47', 
                      'gray48',  'gray49',  'gray50',  'gray51',  'gray52',  'gray53',  'gray54',  'gray55',  'gray56', 
                      'gray57',  'gray58',  'gray59',  'gray60',  'gray61',  'gray62',  'gray63',  'gray64',  'gray65', 
                      'gray66',  'gray67',  'gray68',  'gray69',  'gray70',  'gray71',  'gray72',  'gray73',  'gray74', 
                      'gray75',  'gray76',  'gray77',  'gray78',  'gray79',  'gray80',  'gray81',  'gray82',  'gray83', 
                      'gray84',  'gray85',  'gray86',  'gray87',  'gray88',  'gray89',  'gray90',  'gray91',  'gray92', 
                      'gray93',  'gray94',  'gray95',  'gray97',  'gray98',  'gray99', 'white']

            frame911 = tkinter.Frame(self.frame91, bd=7, relief='sunken')
            frame911.grid(row=6, column=3, rowspan=4)

            canvas = tkinter.Canvas(frame911, height=300, width=300, scrollregion=(0, 0, 400, 800), bg='black')
            inner_frame = tkinter.Frame(canvas, bg='black')
            canvas.create_window(0, 0, anchor="nw", window=inner_frame, tags=("frame", ))

            def confirm():
                m = messagebox.askyesno('Confirm', 'Do you want to save the changes ?')
                if m:
                    self.back_color = self.back

                    curs.execute('''UPDATE custom
                                    SET background = ?
                                    WHERE text_t = ?''', [self.back_color, 'other'])
                    conn.commit()
                    messagebox.showinfo('Success', 'Application Background Color is now {}'.format(self.back_color))
                    self.customize()

            r = c = 0
            max_c = 24

            def click(l):
                self.back = l
                tkinter.Label(self.frame91, text='Text', font=(self.t, 50), bg=l).grid(row=6, column=1, rowspan=3, columnspan=1, sticky='EW')
                tkinter.Label(self.frame91, text=l, font=(self.t, 10), bg='white').grid(row=7, column=1, rowspan=3, columnspan=1, sticky='EW')

            for i in COLORS:
                t = tkinter.Button(inner_frame, bg=i, width=2, command=lambda i=i: click(i))
                t.grid(row=r, column=c)
                c += 1
                if c == max_c:
                    r += 1
                    c = 0

            tkinter.Label(self.frame91, bg=self.back_color).grid(row=20, column=0)
            s_hor = tkinter.Scrollbar(frame911, command=canvas.xview, orient='horizontal')
            s_ver = tkinter.Scrollbar(frame911, command=canvas.yview, orient='vertical')

            canvas['yscrollcommand'] = s_ver.set
            canvas['xscrollcommand'] = s_hor.set
            s_hor.pack(side='bottom', fill='x')
            s_ver.pack(side='right', fill='y')
            canvas.pack(side='left', fill='both')

            def on_configure(*args):
                canvas.itemconfigure("frame")
                canvas.configure(scrollregion=canvas.bbox("all"))

            canvas.bind("<Configure>", on_configure)
            tkinter.Button(self.frame91, text='confirm', command=confirm, cursor='hand2').grid(row=9, column=1, sticky='W')
            tkinter.Button(self.frame91, text='cancel', command=self.customize, cursor='hand2').grid(row=9, column=1, sticky='E')

        def t_font():
            self.frame91=tkinter.Frame(self.master, bg=self.back_color)
            self.frame91.grid(row=0, column=0, rowspan=12, columnspan=6)
            self.frame9.destroy()
            
            tkinter.Button(self.frame91, text='Back', cursor='hand2', command=self.customize).grid(row=0, column=0, sticky='W')
            tkinter.Label(self.frame91, bg=self.back_color, text="TITLE TEXT CUSTOMISATION", font=(self.t, 25, self.b, self.i, 'underline'), fg=self.t_back).grid(row=0, column=0, rowspan=2, columnspan=6)
            tkinter.Label(self.frame91, bg=self.back_color).grid(row=2, column=0)
            
            path = 'C:/Users/ERROR/Downloads/image001.jpg'
            image1 = ImageTk.PhotoImage(Image.open(path))
            self.li = tkinter.Label(self.frame91, image=image1, bg='black')
            self.li.image = image1
            self.li.grid(row=3, column=0, rowspan=2, columnspan=6, pady=10)
            tkinter.Label(self.frame91, bg=self.back_color).grid(row=5, column=0)
            
            fonts = list(tkinter.font.families())
            fonts.sort()
            
            v1 = tkinter.StringVar()
            v2 = tkinter.StringVar()
            v3 = tkinter.StringVar()
            
            v1.set(self.t)
            v2.set(self.b)
            v3.set(self.i)
            
            def call_back():
                tkinter.Label(self.frame91, font=(v1.get(), 50), text='Text').grid(row=6, column=1, rowspan=4, columnspan=2, sticky='EWNS')

            def confirm():
                m = messagebox.askyesno('Confirm', 'Do you want to save the changes ?')
                if m:
                    self.t = v1.get()
                    self.b = v2.get()
                    self.i = v3.get()

                    curs.execute('''UPDATE custom
                                    SET font = ? ,  bold = ? ,  italic = ?
                                    WHERE text_t = ?''', [v1.get(), v2.get(), v3.get(), 'title'])
                    conn.commit()
                    self.customize()

            def check():
                if v2.get() == 'bold':
                    if v3.get() == 'italic':
                        tkinter.Label(self.frame91, font=(v1.get(), 50, 'bold', 'italic'), text='Text').grid(row=6, column=1, rowspan=4, columnspan=2, sticky='EWNS')
                    else:
                        tkinter.Label(self.frame91, font=(v1.get(), 50, 'bold'), text='Text').grid(row=6, column=1, rowspan=4, columnspan=2, sticky='EWNS')
                else:
                    if v3.get() == 'italic':
                        tkinter.Label(self.frame91, font=(v1.get(), 50, 'italic'), text='Text').grid(row=6, column=1, rowspan=4, columnspan=2, sticky='EWNS')
                    else:
                        tkinter.Label(self.frame91, font=(v1.get(), 50), text='Text').grid(row=6, column=1, rowspan=4, columnspan=2, sticky='EWNS')
                
            
            ttk.Combobox(self.frame91, cursor='hand2', values=fonts, textvariable=v1, state='readonly').grid(row=7, column=4)
            v1.trace('w', call_back)
            tkinter.Label(self.frame91, bg=self.back_color).grid(row=10, column=0)
            tkinter.Checkbutton(self.frame91, text='Bold', onvalue='bold', offvalue='normal', bg=self.back_color, variable=v2, command=check).grid(row=8, column=4, sticky='WE')
            tkinter.Checkbutton(self.frame91, text='Italic', onvalue='italic', offvalue='roman', bg=self.back_color, variable=v3, command=check).grid(row=9, column=4, sticky='WE')
            tkinter.Label(self.frame91, bg=self.back_color).grid(row=10, column=0)
            tkinter.Label(self.frame91, font=(self.t, 50), text='Text').grid(row=6, column=1, rowspan=4, columnspan=2, sticky='EWNS')
            tkinter.Button(self.frame91, text='Confirm', cursor='hand2', command=confirm).grid(row=11, column=4, sticky='W')
            tkinter.Button(self.frame91, text='Cancel', cursor='hand2', command=self.customize).grid(row=11, column=5, sticky='W')
            tkinter.Label(self.frame91, bg=self.back_color).grid(row=12, column=0)

        def re_font():
            self.frame91 = tkinter.Frame(self.master, bg=self.back_color)
            self.frame91.grid(row=0, column=0, rowspan=12, columnspan=6)
            self.frame9.destroy()
            
            tkinter.Button(self.frame91, text='Back', cursor='hand2', command=self.customize).grid(row=0, column=0, sticky='W')
            tkinter.Label(self.frame91, bg=self.back_color, text="TITLE TEXT CUSTOMISATION", font=(self.t, 25, self.b, self.i, 'underline'), fg=self.t_back).grid(row=0, column=0, rowspan=2, columnspan=6)
            tkinter.Label(self.frame91, bg=self.back_color).grid(row=2, column=0)
            
            path = 'C:/Users/ERROR/Downloads/image001.jpg'
            image1 = ImageTk.PhotoImage(Image.open(path))
            self.li = tkinter.Label(self.frame91, image=image1, bg='black')
            self.li.image = image1
            self.li.grid(row=3, column=0, rowspan=2, columnspan=6, pady=10)
            tkinter.Label(self.frame91, bg=self.back_color).grid(row=5, column=0)
            
            fonts = list(tkinter.font.families())
            fonts.sort()
            
            v1 = tkinter.StringVar()
            v2 = tkinter.StringVar()
            v3 = tkinter.StringVar()
            
            v1.set(self.t2)
            v2.set(self.b2)
            v3.set(self.i2)
            
            def call_back():
                tkinter.Label(self.frame91, font=(v1.get(), 50), text='Text').grid(row=6, column=1, rowspan=4, columnspan=2, sticky='EWNS')

            def confirm():
                m = messagebox.askyesno('Confirm', 'Do you want to save the changes ?')
                if m:
                    self.t2 = v1.get()
                    self.b2 = v2.get()
                    self.i2 = v3.get()

                    curs.execute('''UPDATE custom
                                    SET font = ? ,  bold = ? ,  italic = ?
                                    WHERE text_t = ?''', [v1.get(), v2.get(), v3.get(), 'other'])
                    conn.commit()
                    self.customize()
                    
            def check():
                if v2.get() == 'bold':
                    if v3.get() == 'italic':
                        tkinter.Label(self.frame91, font=(v1.get(), 50, 'bold', 'italic'), text='Text').grid(row=6, column=1, rowspan=4, columnspan=2, sticky='EWNS')
                    else:
                        tkinter.Label(self.frame91, font=(v1.get(), 50, 'bold'), text='Text').grid(row=6, column=1, rowspan=4, columnspan=2, sticky='EWNS')
                else:
                    if v3.get() == 'italic':
                        tkinter.Label(self.frame91, font=(v1.get(), 50, 'italic'), text='Text').grid(row=6, column=1, rowspan=4, columnspan=2, sticky='EWNS')
                    else:
                        tkinter.Label(self.frame91, font=(v1.get(), 50), text='Text').grid(row=6, column=1, rowspan=4, columnspan=2, sticky='EWNS')

            ttk.Combobox(self.frame91, cursor='hand2', values=fonts, textvariable=v1, state='readonly').grid(row=7, column=4)
            v1.trace('w', call_back)
            tkinter.Label(self.frame91, bg=self.back_color).grid(row=10, column=0)
            tkinter.Checkbutton(self.frame91, text='Bold', onvalue='bold', offvalue='normal', bg=self.back_color, variable=v2, command=check).grid(row=8, column=4, sticky='WE')
            tkinter.Checkbutton(self.frame91, text='Italic', onvalue='italic', offvalue='roman', bg=self.back_color, variable=v3, command=check).grid(row=9, column=4, sticky='WE')
            tkinter.Label(self.frame91, bg=self.back_color).grid(row=10, column=0)
            tkinter.Label(self.frame91, font=(self.t2, 50), text='Text').grid(row=6, column=1, rowspan=4, columnspan=2, sticky='EWNS')
            tkinter.Button(self.frame91, text='Confirm', cursor='hand2', command=confirm).grid(row=11, column=4, sticky='W')
            tkinter.Button(self.frame91, text='Cancel', cursor='hand2', command=self.customize).grid(row=11, column=5, sticky='W')
            tkinter.Label(self.frame91, bg=self.back_color).grid(row=12, column=0)
        
        self.frame9=tkinter.Frame(self.master, bg=self.back_color)
        self.frame9.grid(row=0, column=0, rowspan=12, columnspan=6, sticky='WESN')
        self.frame1.destroy()
        try:
            self.frame91.destroy()
        except:
            pass
        
        tkinter.Button(self.frame9, text='Back', cursor='hand2', command=self.formation).grid(row=0, column=0, sticky='W')
        tkinter.Label(self.frame9, bg=self.back_color, text="CUSTOMISATION", font=(self.t, 25, self.b, self.i, 'underline'), fg=self.t_back).grid(row=0, column=0, rowspan=2, columnspan=6)
        
        path = 'C:/Users/ERROR/Downloads/image001.jpg'
        image1 = ImageTk.PhotoImage(Image.open(path))
        self.li = tkinter.Label(self.frame9, image=image1, bg='black')
        self.li.image = image1
        self.li.grid(row=2, column=0, rowspan=2, columnspan=6, pady=10)
        
        tkinter.Label(self.frame9, bg=self.back_color).grid(row=4, column=0)
        tkinter.Label(self.frame9, bg=self.back_color, text='Select the type of Customisation :', font=(10)).grid(row=5, column=0, columnspan=6, sticky='WE')
        tkinter.Label(self.frame9, bg=self.back_color).grid(row=6, column=0)
        tkinter.Button(self.frame9, text='Title Text Font', cursor='hand2', command=t_font).grid(row=7, column=1, ipadx=14)
        tkinter.Button(self.frame9, text='Title Text Colour', cursor='hand2', command=t_color).grid(row=7, column=3, ipadx=10)
        tkinter.Label(self.frame9, bg=self.back_color).grid(row=8, column=0)
        tkinter.Button(self.frame9, text='Background Colour', cursor='hand2',  command=b_color).grid(row=9, column=1, ipadx=1)
        tkinter.Button(self.frame9, text='Other Text Font', cursor='hand2', command=re_font).grid(row=9, column=3, ipadx=14)
        tkinter.Label(self.frame9, bg=self.back_color).grid(row=10, column=0)
        tkinter.Label(self.frame9, bg=self.back_color).grid(row=11, column=0)
        #tkinter.Label(self.frame9, bg=self.back_color).grid(row=12, column=0)
        #tkinter.Label(self.frame9, bg=self.back_color).grid(row=13, column=0)
        #tkinter.Label(self.frame9, bg=self.back_color).grid(row=14, column=0)

    def reset(self):

        def re_cus():
            m = messagebox.askyesno('Confirm', 'Are you sure ?\n\nDo you want to reset the customisation settings ?')
            if m:
                self.t = 'Arial'
                self.b = 'normal'
                self.i = 'roman'
                self.back_color = 'khaki2'
                self.t2 = 'Arial'
                self.b2 = 'normal'
                self.i2 = 'roman'
                self.t_back = 'blue2'

                curs.execute('''UPDATE custom
                                    SET font = ? ,  bold = ? ,  italic = ? ,  background = ?
                                    WHERE text_t = ?''', [self.t, self.b, self.i, self.back_color, 'title'])
                curs.execute('''UPDATE custom
                                    SET font = ? ,  bold = ? ,  italic = ? ,  background = ?
                                    WHERE text_t = ?''', [self.t2, self.b2, self.i2, self.t_back, 'other'])
                conn.commit()
                messagebox.showinfo('Success', 'All the customisation settings has been reset')
                self.formation
        
        def reset_last():
            
            curs.execute('''SELECT *
                            FROM booking''')
            data = curs.fetchall()
            
            flag = 0
            for i in range(len(data)):
                
                if data[i][5] == 0:
                    r = messagebox.askyesno('Confirm', 'Room Number {} was recently booked.\n\nDo you want free up this Room ?'.format(data[i][0]))

                    if r:
                        curs.execute('''DELETE FROM booking
                                            WHERE last = ?''', [data[i][5]])
                        conn.commit()
                        
                        messagebox.showinfo('Success', 'Room Number {} is now available.'.format(data[i][0]))
                        
                    i = len(data)
                    flag = 1
                    break
                
                else:
                    flag = 2
                    
            if flag == 0:
                messagebox.showerror('Error', 'Sorry !!!\n\nNone of the rooms are booked now !!!')
                
            if flag == 2:
                messagebox.showerror('Error', 'Sorry !!!\n\nNone of the rooms are recently booked or the recently booked room is now free.')
                

        def trunc():
            
            curs.execute('''SELECT *
                            FROM booking''')
            data = curs.fetchall()
            
            if data == []:
                messagebox.showerror('Error', 'Sorry !!!\n\nNone of the rooms are booked now !!!')
                
            else:
                r = messagebox.askyesno('Confirm', 'Do you really want to free all the booked rooms ?')

                if r:
                    curs.execute('''DELETE FROM booking''')
                    conn.commit()

                    messagebox.showinfo('Success', 'All the rooms are successfully freed.')

        def cus_free():
            
            curs.execute('''SELECT *
                            FROM booking''')
            data = curs.fetchall()
            
            if data == []:
                messagebox.showerror('Error', 'Sorry !!!\n\nNone of the rooms are booked now !!!')
                
            else:
                next_win(data)

        def click(b):
            r = b['text']
            m = messagebox.askyesno('Confirm', 'Do you really want to make Room Number {} available again ?'.format(r))

            if m:
                curs.execute('''DELETE FROM booking
                                WHERE room_no = ?''', [r])
                conn.commit()
                
                messagebox.showinfo('Info', 'Room Number {} is now available.'.format(r))
                self.reset()
                
        def next_win(data):
            
            self.frame101 = tkinter.Frame(self.master, bg=self.back_color)
            self.frame101.grid(row=0, column=0, rowspan=12, columnspan=6)
            self.frame10.destroy()
            
            tkinter.Button(self.frame101, text='Back', cursor='hand2', command=self.reset).grid(row=0, column=0, sticky='W')
            tkinter.Label(self.frame101, bg=self.back_color, text="BOOKED ROOMS", font=(self.t, 25, self.b, self.i, 'underline'), fg=self.t_back).grid(row=0, column=0, rowspan=2, columnspan=6)
            
            path = 'C:/Users/ERROR/Downloads/image001.jpg'
            image1 = ImageTk.PhotoImage(Image.open(path))
            self.li = tkinter.Label(self.frame101, image=image1, bg='black')
            self.li.image = image1
            self.li.grid(row=2, column=0, rowspan=2, columnspan=6, pady=10)
            
            tkinter.Label(self.frame101, bg=self.back_color).grid(row=4, column=0)
            tkinter.Label(self.frame101, bg=self.back_color, text='The list of all the Booked Rooms is :', font=(10)).grid(row=5, column=2)
            tkinter.Label(self.frame101, bg=self.back_color).grid(row=6, column=0)
            
            i = j = 0
            data.sort()
            for i in range(len(data)):
                
                if j % 3 == 0:
                    b = tkinter.Button(self.frame101, text=data[i][0], cursor='hand2')
                    b.grid(row=7+j, column=0, ipadx=30)
                    b.config(command=lambda a=b:click(a))
                    
                elif j % 3 == 1:
                    b = tkinter.Button(self.frame101, text=data[i][0], cursor='hand2')
                    b.grid(row=6+j, column=2, ipadx=30)
                    b.config(command=lambda a=b:click(a))
                    
                elif j % 3 == 2:
                    b = tkinter.Button(self.frame101, text=data[i][0], cursor='hand2')
                    b.grid(row=5+j, column=4, ipadx=30)
                    b.config(command=lambda a=b:click(a))
                    tkinter.Label(self.frame101, bg=self.back_color).grid(row=6+j, column=0)
                j += 1
                 
            for k in range(5):
                tkinter.Label(self.frame101, bg=self.back_color).grid(row=i+k+8, column=6)
                   
        try:
            self.frame101.destroy()
        except:
            pass
        
        self.frame10=tkinter.Frame(self.master, bg=self.back_color)
        self.frame10.grid(row=0, column=0, rowspan=12, columnspan=6)
        self.frame1.destroy()
        
        tkinter.Button(self.frame10, text='Back', cursor='hand2', command=self.formation).grid(row=0, column=0, sticky='W')
        tkinter.Label(self.frame10, bg=self.back_color, text="SYSTEM RESET", font=(self.t, 25, self.b, self.i, 'underline'), fg=self.t_back).grid(row=0, column=0, rowspan=2, columnspan=6)
        
        path = 'C:/Users/ERROR/Downloads/image001.jpg'
        image1 = ImageTk.PhotoImage(Image.open(path))
        self.li = tkinter.Label(self.frame10, image=image1, bg='black')
        self.li.image = image1
        self.li.grid(row=2, column=0, rowspan=2, columnspan=6, pady=10)
        
        tkinter.Label(self.frame10, bg=self.back_color).grid(row=4, column=0)
        tkinter.Label(self.frame10, text='What Type Of Alterations You Want To Made :', font=(10), bg=self.back_color).grid(row=5, column=0, columnspan=6, sticky='WE')
        tkinter.Label(self.frame10, bg=self.back_color).grid(row=6, column=0)
        
        tkinter.Button(self.frame10, text='Last Data Reset', padx=19, cursor='hand2', command=reset_last).grid(row=7, column=1)
        tkinter.Button(self.frame10, text='Whole Database Reset', cursor='hand2', command=trunc).grid(row=7, column=3)
        tkinter.Label(self.frame10, bg=self.back_color).grid(row=8, column=0)
        
        tkinter.Button(self.frame10, text='Custom Data Reset', padx=9, cursor='hand2', command=cus_free).grid(row=9, column=1)
        tkinter.Button(self.frame10, text='Customisation Reset', padx=6, cursor='hand2', command=re_cus).grid(row=9, column=3)
        tkinter.Label(self.frame10, bg=self.back_color).grid(row=10, column=0)
        
        tkinter.Label(self.frame10, bg=self.back_color).grid(row=11, column=0)
        #tkinter.Label(self.frame10, bg=self.back_color).grid(row=12, column=0)
        #tkinter.Label(self.frame10, bg=self.back_color).grid(row=13, column=0)
        #tkinter.Label(self.frame10, bg=self.back_color).grid(row=14, column=0)
    
    def exit_fun(self):
        
        if messagebox.askyesno("Exit",  "Do you want to quit the application?"):
            self.master.destroy()

    def about(self):
        
        win_about = tkinter.Toplevel(self.master)
        win_about.config(bg=self.back_color)
        win_about.title('About')
        win_about.geometry('335x250+100+50')
        
        win_frame = tkinter.Frame(win_about, bg=self.back_color)
        win_frame.grid()
        
        win_l = tkinter.Label(win_frame, bg=self.back_color, text='''\nAll the rights to this application are reserved by the creator.
                            \nNone of the fragments of code are copied from anywhere else
                            \nbut they are created by the long term study and hard efforts.\nNone of the actors support smocking.\nSmocking kills.
                            \nDrinking is injurious to HEALTH.
                            \n Now do whatever you want to do man.\nBut ,  don't trouble your Mother.
                            \nCREATOR  :  SHUBHAM SINGH''')
        win_l.pack()

    def on_click(self, event):
        
        event.widget.delete(0, tkinter.END)

    def on_exit(self):
        
        """When you click to exit,  this function is called"""
        
        m = messagebox.askyesno("Exit",  "Do you want to quit the application?")
        if m:
            top.destroy()

if __name__ == '__main__':

    top = tkinter.Tk()

    conn = sqlite3.connect('D:\Language\Python\save_2\seminar_entery.db')
    curs = conn.cursor()

    curs.execute('''CREATE TABLE IF NOT EXISTS rooms
                    (
                    room_no int, 
                    no_stu int
                    )
                ''')

    curs.execute('''CREATE TABLE IF NOT EXISTS booking
                    (
                    room_no int, 
                    no_stu int, 
                    dur text, 
                    title varchar(100), 
                    book text, 
                    last int
                    )
                ''')

    curs.execute('''CREATE TABLE IF NOT EXISTS custom
                    (
                    text_t text, 
                    font text, 
                    bold varchar(10), 
                    italic varchar(10), 
                    background text
                    )
                ''')

    w = Window(top)
    w.formation()

    top.mainloop()
    conn.close()
