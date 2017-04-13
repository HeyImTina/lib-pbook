# coding=utf8
from flask import request, jsonify

from app.model import db
from app.model.pbook import Pbook
from . import api


@api.route("/pbook/edit", methods=['POST'])
def pbook_edit():
    ret = Pbook.query.filter_by(id=request.form.get("id")).first()
    if ret:
        ret.title = request.form.get("title")
        ret.author = request.form.get("author")
        ret.location = request.form.get("location")
        ret.category = request.form.get("category")
        ret.ibsn = request.form.get("ibsn")
        ret.publish = request.form.get("publish")
        db.session.commit()
    return jsonify({
        "code": 0,
        "msg": "ok"
    })

#添加图书
@api.route("/pbook/add", methods=['POST'])
def pbook_add():
    db.session.add(Pbook(
        title=request.form.get("title"),
        author=request.form.get("author"),
        location=request.form.get("location"),
        category=request.form.get("category"),
        ibsn=request.form.get("ibsn"),
        publish=request.form.get("publish"),
    ))
    try:
        db.session.commit()
        return jsonify({
            "code": 0,
            "msg": "ok"
        })
    except:
        import traceback
        print traceback.format_exc()
        return jsonify({
            "code": 1,
            "msg": "error"
        })


# 展示图书
@api.route("/pbook/list")
def pbook_list():
    search = request.args.get("search", None)
    page = request.args.get("page", 1)
    num = request.args.get("num", 10)
    if search:
        ret = Pbook.query.filter(Pbook.title.like("%" + search + "%")).offset((page - 1) * num).limit(num).all()
    else:
        ret = Pbook.query.offset((page - 1) * num).limit(num).all()
    data = [x.json() for x in ret]
    return jsonify({
        "code": 0,
        "data": data
    })


@api.route("/pbook/<int:book_id>")
def pbook(book_id):
    ret = Pbook.query.filter_by(id=book_id).first()
    if ret:
        return jsonify({
            "code": 0,
            "data": ret.json()
        })
    else:
        return jsonify({
            "code": 1,
            "msg": "not found!"
        })


