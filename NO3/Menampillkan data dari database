# Menampilkan Data dari Database
def Tampil(self):
    firstname = self.FirstName.text()
    db = pymysql.connect(db='aplikasi', user='root', passwd='', 
    	 host='localhost', port=3306, autocommit=True)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM data WHERE first_name='"+str(firstname)+"'")
    data = cursor.fetchall()
    if (data):
        for tp in data:
            self.LastName.setText("" + tp[1])
            self.Address.setText("" + tp[2])
            self.Phone.setText("" + tp[3])
            self.messagebox("INFO","Data Ada")
    else:
        self.messagebox("INFO", "Data belum ada")
