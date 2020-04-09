#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
acciones=dict(new="Agregar",edit="Modificar",view="Ver")

def myuiext():
    return dict(buttonprint='icon print',
                buttonup='icon arrowup',
                buttondown='icon arrowdown',
                buttonright='icon arrowright',
                buttonlist='icon list',
                buttoncheck='icon check',
                buttonuncheck='icon unchek',
                buttonaccept='icon accept',
                buttoncancel='icon cancel',
                buttonappr='icon appr',
                buttondisappr='icon disappr',
                buttonsend='icon send',
                buttonsave='icon save',
                buttonconfig='icon config',
                buttondocument='icon document',
                buttonnumeration='icon numeration',
                buttonminus='icon minus',
                buttoninfo='icon info',
                buttondocmoney='icon docmoney',
                buttondoctrans='icon doctrans',
                buttonbuy='icon buy',
                buttonctrol='icon ctrol',
                buttonjob='icon job',
                buttonpath='icon path')

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

def gridbuttonext(buttonclass='buttonadd', buttontext=current.T('Add'),
                  buttonurl=URL(), title=None, callback=None,
                  delete=None, noconfirm=None, showbuttontext=False, typebutton=None):
    T= current.T
    ui=myui().copy()
    ui.update(myuiext())
    if typebutton:
        ui['button']='button btn btn-default ' + str(typebutton)
    if showbuttontext:
        return A(SPAN(_class=ui.get(buttonclass)), CAT(' '),
                 SPAN(T(buttontext), _title=title or T(buttontext),
                 _class=ui.get('buttontext')),
                 _href=buttonurl,
                 callback=callback,
                 delete=delete,
                 noconfirm=noconfirm,
                 _class=ui.get('button'))
    else:
        return A(SPAN(_class=ui.get(buttonclass)),
                 _href=buttonurl,
                 callback=callback,
                 delete=delete,
                 noconfirm=noconfirm,
                 _title=title or buttontext,
                 _class=ui.get('button'))

def gridbuttonempty():
    return A(SPAN(_class='icon empty'),
             href=URL(),
             _class='buttonempty')

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

def config_abmc_grid(grid, table, args=[],
                     backurlgrid=URL('default','index'),
                     backurlform=URL('default','index'),
                     row=None, represent=None,
                     pretitle=None,
                     presubtitle=None):
    T=current.T
    if args(-2) == "new" or args(-3) in ["edit","view"]:
        backurl = backurlform
        title = acciones['new'] if args(-2)=="new" else acciones[args(-3)]
        title += ' ' + table._singular
        modo = 'form'
    else:
        backurl = backurlgrid
        title = ((pretitle or '') + ' ').lstrip() + table._plural
        modo = 'grid'
    grid.append(gridbuttonext("buttonback", T("Back"), backurl, showbuttontext=True))
    if callable(represent) and row:
        presubtitle = presubtitle.strip() + ': ' if presubtitle else ''
        subtitle = CAT(presubtitle, represent(row))
    else:
        subtitle = None
    # busca el botón Agregar que está solo con ícono
    # y le agrega el texto
    if modo == 'grid':
        div_cons = grid.element('div.web2py_console')
        if div_cons:
            a_new = div_cons.element('a.button')
            if a_new:
                a_new.append(CAT(' '))
                a_new.append(SPAN(T('Add record'),
                              _title=T('Add record'),
                              _class='buttontext button'))
    elif modo == 'form':
        div_form = grid.element('div.form_header')
        if div_form:
            a_back = div_form.element('a.button')
            if a_back:
                a_back.append(CAT(' '))
                a_back.append(SPAN(T('Back'),
                              _title=T('Back'),
                              _class='buttontext button'))
    return title, subtitle
