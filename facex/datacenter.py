__author__ = 'Kim'

import sqlite3
import time

from facex import *

sqconn = sqlite3.connect("genD.bin")
data_hnd = sqconn.cursor()


class PersonInfo:
    def __init__(self, names, id_no, dept, pos, pic=None):
        self.names = names
        self.id_no = id_no
        self.department = dept
        self.position = pos
        self.pic = pic


def bootup():
    data_hnd.execute("CREATE TABLE IF NOT EXISTS comm("
                     "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                     "names VARCHAR(100) NOT NULL,"
                     "id_no INT(12) NOT NULL UNIQUE,"
                     "jdept VARCHAR(50) NOT NULL,"
                     "jpos VARCHAR(30) NOT NULL)")

    data_hnd.execute("CREATE TABLE IF NOT EXISTS comm_pic("
                     "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                     "pid INTEGER NOT NULL,"
                     "path VARCHAR(255) NOT NULL,"
                     "FOREIGN KEY(pid) REFERENCES comm(id))")

    data_hnd.execute("CREATE TABLE IF NOT EXISTS comm_access("
                     "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                     "id_no INT(12) NOT NULL,"
                     "granted INT(1) NOT NULL DEFAULT 0,"
                     "stamp INTEGER NOT NULL UNIQUE)")


def add_new_member(names, id_no, department, position):
    try:
        data_hnd.execute("INSERT INTO comm (names, id_no, jdept, jpos) VALUES (?, ?, ?, ?)",
                         (names, id_no, department, position,))

    except sqlite3.Error, e:
        print e.message

    sqconn.commit()

    return data_hnd.lastrowid


def get_member_by_idno(id_no):
    res = data_hnd.execute("SELECT * FROM comm WHERE id_no = ?", (id_no,))
    data = res.fetchall()
    dmap = None
    if len(data) > 0:
        dmap = dict(id=data[0][0], names=data[0][1], id_no=data[0][2], jdept=data[0][3], jpos=data[0][4])

    return len(data), dmap


def get_member_by_label(label):
    res = data_hnd.execute("SELECT * FROM comm WHERE id = ? ", (label, ))
    data = res.fetchall()
    m_info = None
    if len(data) > 0:
        m_info = PersonInfo(data[0][1], data[0][2], data[0][3], data[0][4])

    return m_info


def update_member_names(id_no, names):
    try:
        data_hnd.execute("UPDATE comm SET names = ? WHERE id_no = ?",
                         (names, id_no))
        sqconn.commit()
        return True
    except:
        sqconn.rollback()
        return False


def update_member_dept(id_no, jdept):
    try:
        data_hnd.execute("UPDATE comm SET jdept = ? WHERE id_no = ?",
                         (jdept, id_no))
        sqconn.commit()
        return True
    except:
        sqconn.rollback()
        return False


def update_member_pos(id_no, jpos):
    try:
        data_hnd.execute("UPDATE comm SET jpos = ? WHERE id_no = ?",
                         (jpos, id_no))
        sqconn.commit()
        return True
    except:
        sqconn.rollback()
        return False


def get_allmembers():
    res = sqconn.execute("SELECT comm.names, comm.id_no, comm.jdept, comm.jpos, "
                         " comm_pic.path FROM comm INNER JOIN comm_pic ON comm.id = comm_pic.pid"
                         " AND comm_pic.id = (SELECT MIN(id) FROM comm_pic WHERE pid = comm.id)"
                         " ORDER BY comm.names ASC")

    members = list()

    for row in res:
        members.append(PersonInfo(row[0], row[1], row[2], row[3], row[4]))

    return members


def delete_member(id_no):
    data_hnd.execute("DELETE FROM comm WHERE id_no = ?", (id_no,))
    sqconn.commit()


def add_face(pid, path):
    res = data_hnd.execute("INSERT INTO comm_pic (pid, path) VALUES (?, ?)", (pid, path,))
    sqconn.commit()
    return res


def get_faces(pid):
    paths = []
    res = sqconn.execute("SELECT path FROM comm_pic WHERE pid = ?", (pid,))
    data = res.fetchall()
    paths.append(x[0] for x in data)


def delete_faces(pid):
    data_hnd.execute("DELETE FROM comm_pic WHERE pid = ?", (pid,))
    sqconn.commit()


def record_access(id_no, granted):
    stamp = time.time()
    data_hnd.execute("INSERT INTO comm_access(id_no, granted,stamp) VALUES (?, ?, ?)",
                     (id_no, granted, stamp,))
    sqconn.commit()


def get_access_reports(stamp_from, stamp_to):
    reports = list()
    res = sqconn.execute("SELECT * FROM comm_access WHERE stamp >= ? AND stamp = ?",
                         (stamp_from, stamp_to,))
    res.fetchall()

    for row in res:
        data = dict()
        data["Date"] = util.stamp_to_date(row[3])
        if int(row[2]) > 0:
            data["Access"] = "Granted"
        else:
            data["Access"] = "Denied"

        data["id_no"] = row[1]
        reports.append(data)

    return reports


def shutdown():
    data_hnd.close()
