#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
from gridextgda import popoverbutton
def reprind(ent, conid=True, sep="-", cars=20):
    """ devuelve una representación general de la entidad """
    """ la representación contiene el id y con el nombre o abreviatura """
    """ ent puede ser un objeto row o una referencia """
    if ent:
        try:
            if conid:
                repre = str(ent.id) if hasattr(ent,"id") else str(ent)
                repre += " " + sep + " " if sep else " "
            else:
                repre = ""
            repre += ent.nombre if len(ent.nombre)<=20 else ent.abreviatura
        except Exception:
            repre +="ind - error en representación"
        return repre
    else:
        return ""

def reprper(per, sep=None, conid=False, sepid="-"):
    """ devuelve una representación general de una persona """
    """ la representación contiene los nombres y los apellidos """
    """ opcionalmente puede devolver el id """
    """ per puede ser un objeto row o una referencia """
    """ sep es la cadena usado como separador entre nombres y apellidos """
    if per:
        try:
            if conid:
                repre = str(per.id) if hasattr(per,"id") else str(per)
                repre += " " + sepid + " " if sepid else " "
            else:
                repre = ""
            ape = per.apellidos if hasattr(per,"apellidos") else per.apellido
            nom = per.nombres if hasattr(per,"nombres") else per.nombre
            repre += ape + " " + sep + " " + nom if sep else nom + " " + ape
        except Exception:
            repre +="error en representación"
        return repre
    else:
        return ""

def reprcam(ent, cars=20, sep=">", conid=False, sepid="-"):
    if hasattr(ent,"superior"):
        item=reprind(ent, cars=cars, conid=conid, sep=sepid)
        if ent.superior==None:
            return reprind(ent, cars=cars, conid=conid, sep=sepid)
        else:
            return reprcam(ent.superior,
                           sep=sep,
                           conid=conid,
                           sepid=sepid,
                           cars=cars) + " " + sep + " " + item
    else:
        return reprind(ent, cars=cars, conid=conid, sep=sepid)


def reprcomp(ent, corto=True, sep=">", conid=False, sepid="-"):
    ind = reprind(ent, corto=corto, conid=conid, sep=sepid)
    cam = reprcam(ent, corto=corto, sep=sep, conid=conid, sepid=sepid)
    return CAT(ind, ' ', popoverbutton(buttonid='popover1',
                                       buttonclass='buttoninfo',
                                       buttontext='Ver más...',
                                       buttontitle='Ver más datos',
                                       title='Ruta Completa',
                                       content=cam))
