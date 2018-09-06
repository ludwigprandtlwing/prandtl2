# -*- coding: utf-8 -*-

place = u'J:/phD/PrandtlVlerk/CAD/'
place = ''


# Macro Begin: WingModel.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
import FreeCAD
import importAirfoilDAT
import Part

sweep = [8.3274,8.5524,8.7259,8.8441,8.903,8.8984,8.8257,8.6801,8.4565,8.1492,7.7522,
7.2592,6.6634,5.9579,5.1362,4.1927,
16	3.1253,
17	1.9394,
18	0.6589,	-0.6417, -1.6726]

b = 2.25 # Span in metres


App.newDocument("Prandtl")
App.setActiveDocument("Prandtl")
App.ActiveDocument=App.getDocument("Prandtl")

sectionstring = place + 'section_01.dat'
importAirfoilDAT.insert(sectionstring,"Prandtl")
#Gui.SendMsgToActiveView("ViewFit")
sectionstring = place + 'section_06.dat'
importAirfoilDAT.insert(sectionstring,"Prandtl")
#Gui.SendMsgToActiveView("ViewFit")
#Gui.ActiveDocument.setEdit('DWire001',0)
App.getDocument("Prandtl").DWire001.Placement=App.Placement(App.Vector(0,0,10), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
App.getDocument("Prandtl").DWire001.Placement=App.Placement(App.Vector(0,0,10), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
#Gui.ActiveDocument.setEdit('DWire001',0)
App.getDocument("Prandtl").DWire001.Placement=App.Placement(App.Vector(0,0,2), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
sectionstring = place + 'section_19.dat'
importAirfoilDAT.insert(sectionstring,"Prandtl")
#Gui.SendMsgToActiveView("ViewFit")
App.getDocument("Prandtl").DWire002.Placement=App.Placement(App.Vector(1,0,3), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
App.getDocument("Prandtl").DWire001.Placement=App.Placement(App.Vector(0,0.4,2), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
from FreeCAD import Base
App.getDocument('Prandtl').addObject('Part::Loft','Loft')
App.getDocument('Prandtl').ActiveObject.Sections=[App.getDocument('Prandtl').DWire, App.getDocument('Prandtl').DWire001, App.getDocument('Prandtl').DWire002, ]
App.getDocument('Prandtl').ActiveObject.Solid=False
App.getDocument('Prandtl').ActiveObject.Ruled=False
App.getDocument('Prandtl').ActiveObject.Closed=False

# Macro End: WingModel.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++