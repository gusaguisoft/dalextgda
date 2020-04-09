#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *

def myuiext():
    return dict(buttonprint='icon print', \
                buttonup='icon arrowup', \
                buttondown='icon arrowdown', \
                buttonright='icon arrowright', \
                buttonlist='icon list', \
                buttoncheck='icon check', \
                buttonuncheck='icon unchek', \
                buttonaccept='icon accept', \
                buttoncancel='icon cancel', \
                buttonappr='icon appr', \
                buttondisappr='icon disappr', \
                buttonsend='icon send', \
                buttonsave='icon save', \
                buttonconfig='icon config', \
                buttondocument='icon document', \
                buttonnumeration='icon numeration', \
                buttonminus='icon minus')

def myui():
    return dict(widget='',
                header='',
                content='',
                default='',
                cornerall='',
                cornertop='',
                cornerbottom='',
                button='button btn btn-default btn-secondary',
                buttontext='buttontext button',
                buttonadd='icon plus icon-plus glyphicon glyphicon-plus',
                buttonback='icon arrowleft icon-arrow-left glyphicon glyphicon-arrow-left',
                buttonexport='icon export icon-download glyphicon glyphicon-download',
                buttondelete='icon trash icon-trash glyphicon glyphicon-trash',
                buttonedit='icon pen icon-pencil glyphicon glyphicon-pencil',
                buttontable='icon table icon-table glyphicon glyphicon-arrow-right',
                buttonview='icon magnifier icon-zoom-in glyphicon glyphicon-zoom-in')

def gridbuttonext(buttonclass='buttonadd', buttontext=current.T('Add'), buttonurl=URL(), title=None, \
                  callback=None, delete=None, trap=True, noconfirm=None, showtext=True):
    ui=myui().copy()
    ui.update(myuiext())
    return A(SPAN(_class=ui.get(buttonclass), _title=title or current.T(buttontext)), CAT(' '), \
         SPAN(current.T(buttontext), _title=title or current.T(buttontext), _class=ui.get('buttontext')),\
             _href=buttonurl, \
             callback=callback, \
             delete=delete, \
             noconfirm=noconfirm, \
             _class=ui.get('button'))

def gridbuttonbas(buttonclass='buttonadd', buttontext=current.T('Add'), title=None):
    ui=myui().copy()
    ui.update(myuiext())
    return CAT(SPAN(_class=ui.get(buttonclass), _title=title or current.T(buttontext)), ' ', \
             SPAN(current.T(buttontext), _title=title or current.T(buttontext), _class=ui.get('buttontext')))

def gridbuttonmult(buttonid='btnGroupDrop1', buttonclass='buttonadd', buttontext=current.T('Add'), title=None, **links):
    openbtn="<button id='" + buttonid + "' type='Button' class='btn btn-secondary dropdown-toggle' " + \
    "data-toggle='dropdown' aria-haspopup='true' aria-expanded='false'>"
    closebtn="</button>"
    buttontag=CAT(XML(openbtn), gridbuttonbas(buttonclass=buttonclass, buttontext=buttontext, title=title), XML(closebtn))
    atags=CAT('')
    for link in links:
         atags=CAT(atags, A(link, _class="dropdown-item", _href=links[link]))
    divtag=CAT(XML("<div class='dropdown-menu' aria-labelledby='" + buttonid + "'>"), atags, XML('</div>'))
    return DIV(buttontag, divtag, _class="btn-group", role="group")

def popoverbutton(buttonid='popover1',
                  buttonclass='buttoninfo',
                  buttontext='Ver más...',
                  buttontitle='Ver más datos',
                  title='Título',
                  content='Contenido'):
    openbtn="<button id='" + buttonid + "' type='Button' class='btn btn-secondary' " + \
    "data-container='body' data-toggle='popover' data-placement='bottom' " + \
    "title='" + (title or 'Titulo') + "' data-content='" + (content or 'Contenido') + "'>"
    closebtn="</button>"
    buttontag=CAT(XML(openbtn),
                  gridbuttonbas(buttonclass=buttonclass,
                                buttontext=buttontext,
                                title=buttontitle),
                  XML(closebtn))
    return buttontag
