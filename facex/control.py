__author__ = 'Kim'

import cv2
from facex import *

def add_member(names, id_no, dept, pos, paths):

    uid = datacenter.add_new_member(id_no=id_no, names=names, department=dept, position=pos)

    if uid is None:
        return

    ids = list()

    res, mm = datacenter.get_member_by_idno(id_no)

    if mm is None:
        print "System error: User is None"
        return False

    num_pics = len(paths)
    i = 0

    while i < num_pics:
        ids.append(uid)
        i += 1

    neurals.neural_update(paths, ids)

    for path in paths:
        datacenter.add_face(uid, path)

    return True

def modify_member(names, id_no, dept, pos, paths=None):

    x, mm = datacenter.get_member_by_idno(id_no)

    noop = 1

    if len(names) > 0:
        datacenter.update_member_names(id_no, names)
        noop &= 0

    if len(dept) > 0:
        datacenter.update_member_dept(id_no, dept)
        noop &= 0

    if len(pos) > 0:
        datacenter.update_member_pos(id_no, pos)
        noop &= 0

    if paths is not None:
        noop &= 0
        ids = list()
        i = 1
        while i <= len(paths):
            ids.append(mm["id"])
            i += 1

        neurals.neural_update(paths, ids)

        for path in paths:
            datacenter.add_face(mm["id"], path)

        return True

    if noop == 1:
        print "nothing to be done, sorry"


def delete_member(id_no):
    res, data = datacenter.get_member_by_idno(id_no)
    datacenter.delete_faces(data["id"])
    datacenter.delete_member(id_no)


def anonymous_checkaccess(pic):
    label, conf = neurals.neural_getlabel(pic)
    print int(label)
    print conf
    if label > 0 and conf < 200:
        uinfo = datacenter.get_member_by_label(label)
        if uinfo is not None:
            datacenter.record_access(uinfo.id_no, granted=1)
        else:
            print "label is %d, something bad happened" % label

        return True, uinfo

    datacenter.record_access(0, granted=0)
    return False, None


def access_reports(s_from, s_to):
    datalist = datacenter.get_access_reports(s_from, s_to)
    html_str = "<table><th>Index</th><th>Date</th><th>ID Number</th><th>Access</th>"
    for num, data in datalist:
        html_str += "<tr><td>%d</td><td>%s</td><td>%llu</td><td>%s</td></tr>" % \
                    (num, data["Date"], data["id_no"], data["Access"])

    html_str += "</table>"

    return html_str