import clr
import sys
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib')
import System
from System import Array
from System.Collections.Generic import *
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager 
from RevitServices.Transactions import TransactionManager 

clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")

import Autodesk 
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication 
app = uiapp.Application 
uidoc = uiapp.ActiveUIDocument

#######OK NOW YOU CAN CODE########

ArrayCurves = IN[0]
floortype = UnwrapElement(IN[1])
levels = UnwrapElement(IN[2])
structural = IN[3]

curveArray = CurveArray()
for c in ArrayCurves:
    curveArray.Append(c.ToRevitType())

TransactionManager.Instance.EnsureInTransaction(doc)
newFloor = doc.Create.NewFloor(curveArray,floortype,levels,structural )
out = newFloor.ToDSType(False)
TransactionManager.Instance.TransactionTaskDone()
OUT = out


